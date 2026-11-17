import csv, sys, re
csv.field_size_limit(10**9)
def host(w):
    w=(w or '').strip()
    return re.sub(r'^https?://','',w).replace('www.','').split('/')[0].lower() if w else ''
ap={host(a.get('Website')):a for a in csv.DictReader(open(sys.argv[1],encoding='utf-8-sig',newline=''))}
ours=list(csv.DictReader(open(sys.argv[2],encoding='utf-8-sig',newline='')))
removed=list(csv.DictReader(open(sys.argv[3],encoding='utf-8-sig',newline='')))

def emp(a):
    try: return int(a.get('# Employees') or 0)
    except: return 0
groups={'KEEP - correct Utah company':[], 'CAUTION - Apollo holds the national parent':[],
        'NO ADDRESS - verify before dialling':[]}
for r in ours:
    d=r['Domain'].lower(); a=ap.get(d)
    if not a: continue
    s=r['Apollo status']
    k=('KEEP - correct Utah company' if s=='Apollo confirms Utah'
       else 'CAUTION - Apollo holds the national parent' if s.startswith('KEEP - Apollo')
       else 'NO ADDRESS - verify before dialling')
    groups[k].append((d, r['Name'], a.get('Company Name',''), emp(a), a.get('Company City','')+', '+a.get('Company State','')))

ourdoms={r['Domain'].lower() for r in ours}|{r['Domain'].lower() for r in removed}
notours=[(d,a.get('Company Name',''),a.get('Company City','')+', '+a.get('Company State','')) for d,a in ap.items() if d not in ourdoms]
remd=[(r['Domain'].lower(), r['Name'], r['Apollo note']) for r in removed if r['Domain'].lower() in ap]

out=[]
for k,v in groups.items():
    print(f"\n{'='*70}\n{k}  ({len(v)})\n{'='*70}")
    for d,name,apname,e,loc in sorted(v, key=lambda x:-x[3]):
        extra='' if apname.lower().replace(' ','')==name.lower().replace(' ','') else f"  [Apollo: {apname}]"
        print(f"   {d:<36} {e:>4} emp  {name[:30]}{extra}")
        out.append({'Apollo action':k,'Domain':d,'Our company':name,'Apollo company':apname,
                    'Employees':e,'Apollo location':loc})
print(f"\n{'='*70}\nDELETE FROM APOLLO - not our companies  ({len(notours)})\n{'='*70}")
for d,n2,loc in notours:
    print(f"   {d:<36} {n2[:34]:<36} {loc}")
    out.append({'Apollo action':'DELETE - not our company','Domain':d,'Our company':'',
                'Apollo company':n2,'Employees':'','Apollo location':loc})
print(f"\n{'='*70}\nDELETE FROM APOLLO - cut from our list  ({len(remd)})\n{'='*70}")
for d,n2,why in remd:
    print(f"   {d:<36} {n2[:30]:<32} {why[:40]}")
    out.append({'Apollo action':'DELETE - cut from our list','Domain':d,'Our company':n2,
                'Apollo company':'','Employees':'','Apollo location':why})
with open(sys.argv[4],'w',encoding='utf-8',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=['Apollo action','Domain','Our company','Apollo company','Employees','Apollo location'])
    w.writeheader(); w.writerows(out)
