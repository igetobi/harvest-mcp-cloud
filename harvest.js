import express from "express";
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { SSEServerTransport } from "@modelcontextprotocol/sdk/server/sse.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const app = express();
app.use(express.json());

const TOKEN = process.env.HARVEST_ACCESS_TOKEN;
const ACCOUNT_ID = process.env.HARVEST_ACCOUNT_ID;
const HEADERS = {
  "Authorization": `Bearer ${TOKEN}`,
  "Harvest-Account-Id": ACCOUNT_ID,
  "Content-Type": "application/json",
  "User-Agent": "Harvest-MCP/1.0"
};

async function harvestGet(path) {
  const r = await fetch(`https://api.harvestapp.com/v2${path}`, { headers: HEADERS });
  return r.json();
}
async function harvestPost(path, body) {
  const r = await fetch(`https://api.harvestapp.com/v2${path}`, {
    method: "POST", headers: HEADERS, body: JSON.stringify(body)
  });
  return r.json();
}
async function harvestPatch(path, body) {
  const r = await fetch(`https://api.harvestapp.com/v2${path}`, {
    method: "PATCH", headers: HEADERS, body: JSON.stringify(body)
  });
  return r.json();
}
async function harvestDelete(path) {
  const r = await fetch(`https://api.harvestapp.com/v2${path}`, {
    method: "DELETE", headers: HEADERS
  });
  return r.status === 204 ? { success: true } : r.json();
}

function buildServer() {
  const server = new Server(
    { name: "harvest", version: "3.0.0" },
    { capabilities: { tools: {} } }
  );

  server.setRequestHandler(ListToolsRequestSchema, async () => ({
    tools: [
      { name: "get_current_user", description: "Get the current logged-in Harvest user",
        inputSchema: { type: "object", properties: {} } },
      { name: "list_projects", description: "List all projects",
        inputSchema: { type: "object", properties: {
          client_id: { type: "string", description: "Filter by client ID (optional)" }
        }}},
      { name: "list_clients", description: "List all clients",
        inputSchema: { type: "object", properties: {} } },
      { name: "list_time_entries", description: "List time entries, optionally filtered by date or project",
        inputSchema: { type: "object", properties: {
          from: { type: "string", description: "Start date YYYY-MM-DD" },
          to: { type: "string", description: "End date YYYY-MM-DD" },
          project_id: { type: "string", description: "Filter by project ID (optional)" }
        }}},
      { name: "list_tasks", description: "List tasks for a specific project",
        inputSchema: { type: "object", properties: {
          project_id: { type: "string", description: "The project ID" }
        }, required: ["project_id"] }},
      { name: "list_users", description: "List all team members",
        inputSchema: { type: "object", properties: {} } },
      { name: "list_invoices", description: "List invoices, optionally filtered by status",
        inputSchema: { type: "object", properties: {
          status: { type: "string", description: "draft, open, paid, or closed (optional)" }
        }}},
      { name: "list_expenses", description: "List expense reports",
        inputSchema: { type: "object", properties: {
          from: { type: "string", description: "Start date YYYY-MM-DD (optional)" },
          to: { type: "string", description: "End date YYYY-MM-DD (optional)" }
        }}},
      { name: "list_estimates", description: "List all estimates/quotes",
        inputSchema: { type: "object", properties: {
          client_id: { type: "string", description: "Filter by client ID (optional)" },
          state: { type: "string", description: "draft, sent, accepted, or declined (optional)" },
          from: { type: "string", description: "Start date YYYY-MM-DD (optional)" },
          to: { type: "string", description: "End date YYYY-MM-DD (optional)" }
        }}},
      { name: "get_estimate", description: "Get a single estimate by ID",
        inputSchema: { type: "object", properties: {
          estimate_id: { type: "string", description: "The estimate ID" }
        }, required: ["estimate_id"] }},
      { name: "create_estimate", description: "Create a new estimate/quote",
        inputSchema: { type: "object", properties: {
          client_id: { type: "string", description: "The client ID" },
          subject: { type: "string", description: "Estimate subject/title (optional)" },
          notes: { type: "string", description: "Additional notes (optional)" },
          issue_date: { type: "string", description: "Issue date YYYY-MM-DD (optional)" },
          tax: { type: "number", description: "Tax percentage (optional)" },
          discount: { type: "number", description: "Discount percentage (optional)" },
          currency: { type: "string", description: "Currency code e.g. USD (optional)" },
          line_items: { type: "array", description: "Array of line items",
            items: { type: "object", properties: {
              kind: { type: "string", description: "Category e.g. Service" },
              description: { type: "string", description: "Line item description" },
              quantity: { type: "number", description: "Quantity (defaults to 1)" },
              unit_price: { type: "number", description: "Price per unit" },
              taxed: { type: "boolean" },
              taxed2: { type: "boolean" }
            }, required: ["kind", "unit_price"] }}
        }, required: ["client_id"] }},
      { name: "update_estimate", description: "Update an existing estimate/quote",
        inputSchema: { type: "object", properties: {
          estimate_id: { type: "string", description: "The estimate ID" },
          subject: { type: "string", description: "New subject (optional)" },
          notes: { type: "string", description: "Updated notes (optional)" },
          tax: { type: "number", description: "Updated tax % (optional)" },
          discount: { type: "number", description: "Updated discount % (optional)" },
          issue_date: { type: "string", description: "Updated issue date (optional)" },
          line_items: { type: "array", description: "Line items to add/update/delete",
            items: { type: "object", properties: {
              id: { type: "number", description: "Include to update existing item" },
              kind: { type: "string" },
              description: { type: "string" },
              quantity: { type: "number" },
              unit_price: { type: "number" },
              _destroy: { type: "boolean", description: "Set true to delete this line item" }
            }}}
        }, required: ["estimate_id"] }},
      { name: "delete_estimate", description: "Delete an estimate permanently",
        inputSchema: { type: "object", properties: {
          estimate_id: { type: "string", description: "The estimate ID" }
        }, required: ["estimate_id"] }},
      { name: "create_project", description: "Create a new project",
        inputSchema: { type: "object", properties: {
          name: { type: "string" }, client_id: { type: "string" },
          is_billable: { type: "boolean" }, bill_by: { type: "string" }, budget_by: { type: "string" }
        }, required: ["name", "client_id", "is_billable", "bill_by", "budget_by"] }},
      { name: "update_project", description: "Rename or update a project",
        inputSchema: { type: "object", properties: {
          project_id: { type: "string" }, name: { type: "string" },
          is_active: { type: "boolean" }, notes: { type: "string" }
        }, required: ["project_id"] }},
      { name: "create_time_entry", description: "Log hours or start a timer",
        inputSchema: { type: "object", properties: {
          project_id: { type: "string" }, task_id: { type: "string" },
          spent_date: { type: "string" }, hours: { type: "number" }, notes: { type: "string" }
        }, required: ["project_id", "task_id", "spent_date"] }},
      { name: "update_time_entry", description: "Update hours or notes on a time entry",
        inputSchema: { type: "object", properties: {
          time_entry_id: { type: "string" }, hours: { type: "number" }, notes: { type: "string" }
        }, required: ["time_entry_id"] }},
      { name: "stop_timer", description: "Stop a running timer",
        inputSchema: { type: "object", properties: {
          time_entry_id: { type: "string" }
        }, required: ["time_entry_id"] }},
      { name: "delete_time_entry", description: "Delete a time entry",
        inputSchema: { type: "object", properties: {
          time_entry_id: { type: "string" }
        }, required: ["time_entry_id"] }}
    ]
  }));

  server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;
    let data;
    switch (name) {
      case "get_current_user": data = await harvestGet("/users/me"); break;
      case "list_projects": {
        let path = "/projects?per_page=100";
        if (args.client_id) path += `&client_id=${args.client_id}`;
        data = await harvestGet(path); break;
      }
      case "list_clients": data = await harvestGet("/clients?per_page=100"); break;
      case "list_time_entries": {
        let path = "/time_entries?per_page=100";
        if (args.from) path += `&from=${args.from}`;
        if (args.to) path += `&to=${args.to}`;
        if (args.project_id) path += `&project_id=${args.project_id}`;
        data = await harvestGet(path); break;
      }
      case "list_tasks": data = await harvestGet(`/projects/${args.project_id}/task_assignments?per_page=100`); break;
      case "list_users": data = await harvestGet("/users?per_page=100"); break;
      case "list_invoices": {
        let path = "/invoices?per_page=100";
        if (args.status) path += `&status=${args.status}`;
        data = await harvestGet(path); break;
      }
      case "list_expenses": {
        let path = "/expenses?per_page=100";
        if (args.from) path += `&from=${args.from}`;
        if (args.to) path += `&to=${args.to}`;
        data = await harvestGet(path); break;
      }
      case "list_estimates": {
        let path = "/estimates?per_page=100";
        if (args.client_id) path += `&client_id=${args.client_id}`;
        if (args.state) path += `&state=${args.state}`;
        if (args.from) path += `&from=${args.from}`;
        if (args.to) path += `&to=${args.to}`;
        data = await harvestGet(path); break;
      }
      case "get_estimate": data = await harvestGet(`/estimates/${args.estimate_id}`); break;
      case "create_estimate": {
        const body = { client_id: args.client_id };
        if (args.subject) body.subject = args.subject;
        if (args.notes) body.notes = args.notes;
        if (args.issue_date) body.issue_date = args.issue_date;
        if (args.tax !== undefined) body.tax = args.tax;
        if (args.discount !== undefined) body.discount = args.discount;
        if (args.currency) body.currency = args.currency;
        if (args.line_items) body.line_items = args.line_items;
        data = await harvestPost("/estimates", body); break;
      }
      case "update_estimate": {
        const body = {};
        if (args.subject !== undefined) body.subject = args.subject;
        if (args.notes !== undefined) body.notes = args.notes;
        if (args.tax !== undefined) body.tax = args.tax;
        if (args.discount !== undefined) body.discount = args.discount;
        if (args.issue_date !== undefined) body.issue_date = args.issue_date;
        if (args.line_items !== undefined) body.line_items = args.line_items;
        data = await harvestPatch(`/estimates/${args.estimate_id}`, body); break;
      }
      case "delete_estimate": data = await harvestDelete(`/estimates/${args.estimate_id}`); break;
      case "create_project":
        data = await harvestPost("/projects", {
          name: args.name, client_id: args.client_id,
          is_billable: args.is_billable, bill_by: args.bill_by, budget_by: args.budget_by
        }); break;
      case "update_project": {
        const body = {};
        if (args.name !== undefined) body.name = args.name;
        if (args.is_active !== undefined) body.is_active = args.is_active;
        if (args.notes !== undefined) body.notes = args.notes;
        data = await harvestPatch(`/projects/${args.project_id}`, body); break;
      }
      case "create_time_entry": {
        const body = { project_id: args.project_id, task_id: args.task_id, spent_date: args.spent_date };
        if (args.hours !== undefined) body.hours = args.hours;
        if (args.notes) body.notes = args.notes;
        data = await harvestPost("/time_entries", body); break;
      }
      case "update_time_entry": {
        const body = {};
        if (args.hours !== undefined) body.hours = args.hours;
        if (args.notes !== undefined) body.notes = args.notes;
        data = await harvestPatch(`/time_entries/${args.time_entry_id}`, body); break;
      }
      case "stop_timer": data = await harvestPatch(`/time_entries/${args.time_entry_id}/stop`, {}); break;
      case "delete_time_entry": data = await harvestDelete(`/time_entries/${args.time_entry_id}`); break;
      default: data = { error: `Unknown tool: ${name}` };
    }
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
  });

  return server;
}

const transports = {};

// CORS middleware for all routes
app.use((req, res, next) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, POST, OPTIONS, DELETE");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization, Accept, Cache-Control");
  if (req.method === "OPTIONS") return res.sendStatus(200);
  next();
});

app.get("/sse", async (req, res) => {
  res.setHeader("Content-Type", "text/event-stream");
  res.setHeader("Cache-Control", "no-cache");
  res.setHeader("Connection", "keep-alive");
  const transport = new SSEServerTransport("/messages", res);
  transports[transport.sessionId] = transport;
  res.on("close", () => delete transports[transport.sessionId]);
  const server = buildServer();
  await server.connect(transport);
});

app.post("/messages", async (req, res) => {
  const sessionId = req.query.sessionId;
  const transport = transports[sessionId];
  if (transport) {
    await transport.handlePostMessage(req, res);
  } else {
    res.status(400).json({ error: "Session not found" });
  }
});

app.get("/", (req, res) => res.send("Harvest MCP Server running ✅"));

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
