"""Zero-cost pre-filter: classify companies from name + Google review text alone.

Splits a list into AUTO_YES / AUTO_NO / AMBIGUOUS so that paid web verification is
spent only on the ambiguous middle. Tuned and measured against companies whose
verdicts are already known from a prior verified run.
"""
import re

def norm(s):
    return re.sub(r'\s+', ' ', (s or '').lower())

# --- vehicle / not-a-building ------------------------------------------------
AUTO = re.compile(r'\b(auto ?glass|windshield|windscreen|auto body|collision|car audio|'
                  r'car stereo|auto sound|paint protection|ppf|vinyl wrap|car wrap|'
                  r'auto detail|car detail|mobile auto|automotive|dealership|tire|'
                  r'muffler|transmission|oil change|body shop)\b')

# --- services that are NOT window installation/repair ------------------------
CLEANING = re.compile(r'\b(window cleaning|window washing|windowcleaning|squeegee|'
                      r'pressure wash|power wash|gutter clean|soft wash|christmas light)\b')
TREATMENT = re.compile(r'\b(blind|blinds|shade|shades|shutter|shutters|drapery|draperies|'
                       r'curtain|window treatment|window covering|window fashion)\b')
TINT = re.compile(r'\b(window tint|window film|tinting|solar screen|security film)\b')

# --- trades with no window scope --------------------------------------------
OTHER_TRADE = re.compile(r'\b(plumb|hvac|air conditioning|heating|electric|pest|termite|'
                         r'lawn|landscap|tree service|arborist|pool|spa|junk removal|moving|'
                         r'mover|carpet|upholstery|maid|janitor|dog|pet|grooming|veterinar|'
                         r'dental|dentist|salon|barber|spa|restaurant|coffee|bakery|pizza|'
                         r'insurance|mortgage|realt|law firm|attorney|accounting|'
                         r'locksmith|garage door|fence|fencing|septic|chimney|sweep|'
                         r'appliance|computer|phone repair|sign|banner|printing|'
                         r'solar panel|pergola|deck|concrete|asphalt|paving|tow|storage)\b')

# --- positive window signals -------------------------------------------------
WIN_STRONG = re.compile(r'\b(window (replacement|installation|install|repair|replace)|'
                        r'replacement window|window and door|windows and doors|windows & doors|'
                        r'window & door|glazing|glazier|window company|window world|'
                        r'window depot|window source|renewal by andersen|window pro)\b')
WIN_NAME = re.compile(r'\bwindow')
GLASS = re.compile(r'\b(glass|mirror|glazing)\b')
BUILDER = re.compile(r'\b(exterior|remodel|renovat|construction|contractor|home improvement|'
                     r'siding|roofing|restoration|builder|design build|handyman)\b')

# review text describing real window work
REV_WIN = re.compile(r'\b(new windows|replaced (my |our |the )?windows?|window (install|replacement|'
                     r'repair)|installed (my |our |the )?windows?|window glass|foggy window|'
                     r'broken window|double pane|low-?e window)\b')
REV_CLEAN = re.compile(r'\b(clean(ed|ing)? (my |our |the )?windows?|window (clean|wash)|'
                       r'washed (my |our |the )?windows?)\b')


def classify(name, review):
    """Return (tier, reason). tier in AUTO_YES / AUTO_NO / AMBIGUOUS."""
    n, rv = norm(name), norm(review)
    both = n + ' || ' + rv

    # 1. vehicles. Measured against known labels, auto-rejecting these is the single
    # biggest source of false negatives: DFW shops routinely do windshields AND
    # residential/commercial glass. Never auto-reject — route to human/web check.
    if AUTO.search(n):
        if GLASS.search(n) or WIN_NAME.search(n):
            return 'AMBIGUOUS', 'auto-glass name, but may also do building glass — must verify'
        return 'AUTO_NO', 'vehicle/automotive business, no glass or window signal'

    # 2. name-level exclusions that are reliably not installation
    if CLEANING.search(n) or (REV_CLEAN.search(rv) and not WIN_STRONG.search(n)):
        if not WIN_STRONG.search(n):
            return 'AUTO_NO', 'window cleaning/washing'
    if TREATMENT.search(n) and not WIN_STRONG.search(n):
        return 'AUTO_NO', 'blinds/shades/shutters/drapery (window treatments)'
    # tint shops that also carry glass are the same trap as auto — verify, don't reject
    if TINT.search(n) and not WIN_STRONG.search(n):
        if GLASS.search(n):
            return 'AMBIGUOUS', 'tint/film name, but carries glass — must verify'
        return 'AUTO_NO', 'window tint/film only'

    # 3. clearly unrelated trades, with no window signal anywhere
    if OTHER_TRADE.search(n) and not WIN_NAME.search(n) and not REV_WIN.search(rv):
        return 'AUTO_NO', 'unrelated trade, no window signal'

    # 4. strong positives
    if WIN_STRONG.search(n):
        return 'AUTO_YES', 'name states window installation/replacement/doors'
    if WIN_NAME.search(n) and not (CLEANING.search(both) or TREATMENT.search(n) or TINT.search(n)):
        if REV_WIN.search(rv):
            return 'AUTO_YES', 'window in name + review describes window work'
        return 'AMBIGUOUS', 'window in name but service type unconfirmed'
    if REV_WIN.search(rv) and not REV_CLEAN.search(rv):
        return 'AUTO_YES', 'review explicitly describes window install/replacement'

    # 5. plausible but unproven — glass shops, builders, exteriors
    if GLASS.search(n) or BUILDER.search(n):
        return 'AMBIGUOUS', 'glass shop or building contractor, window scope unknown'

    return 'AMBIGUOUS', 'insufficient signal'
