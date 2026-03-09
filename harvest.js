import express from "express";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { isInitializeRequest } from "@modelcontextprotocol/sdk/types.js";
import { z } from "zod";
import { randomUUID } from "crypto";

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
  const server = new McpServer({ name: "harvest", version: "3.0.0" });

  server.registerTool("get_current_user", { description: "Get the current logged-in Harvest user", inputSchema: {} }, async () => {
    const data = await harvestGet("/users/me");
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
  });

  server.registerTool("list_projects", { description: "List all projects", inputSchema: { client_id: z.string().optional().describe("Filter by client ID") } }, async ({ client_id }) => {
    let path = "/projects?per_page=100";
    if (client_id) path += `&client_id=${client_id}`;
    const data = await harvestGet(path);
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
  });

  server.registerTool("list_clients", { description: "List all clients", inputSchema: {} }, async () => {
    const data = await harvestGet("/clients?per_page=100");
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
  });

  server.registerTool("list_time_entries", { description: "List time entries, optionally filtered by date or project", inputSchema: { from: z.string().optional().describe("Start date YYYY-MM-DD"), to: z.string().optional().describe("End date YYYY-MM-DD"), project_id: z.string().optional().describe("Filter by project ID") } }, async ({ from, to, project_id }) => {
    let path = "/time_entries?per_page=100";
    if (from) path += `&from=${from}`;
    if (to) path += `&to=${to}`;
    if (project_id) path += `&project_id=${project_id}`;
    const data = await harvestGet(path);
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
  });

  server.registerTool("list_tasks", { description: "List tasks for a specific project", inputSchema: { project_id: z.string().describe("The project ID") } }, async ({ project_id }) => {
    const data = await harvestGet(`/projects/${project_id}/task_assignments?per_page=100`);
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
  });

  server.registerTool("list_users", { description: "List all team members", inputSchema: {} }, async () => {
    const data = await harvestGet("/users?per_page=100");
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
  });

  server.registerTool("list_invoices", { description: "List invoices, optionally filtered by status", inputSchema: { status: z.string().optional().describe("draft, open, paid, or closed") } }, async ({ status }) => {
    let path = "/invoices?per_page=100";
    if (status) path += `&status=${status}`;
    const data = await harvestGet(path);
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
  });

  server.registerTool("list_expenses", { description: "List expense reports", inputSchema: { from: z.string().optional().describe("Start date YYYY-MM-DD"), to: z.string().optional().describe("End date YYYY-MM-DD") } }, async ({ from, to }) => {
    let path = "/expenses?per_page=100";
    if (from) path += `&from=${from}`;
    if (to) path += `&to=${to}`;
    const data = await harvestGet(path);
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
  });

  server.registerTool("list_estimates", { description: "List all estimates/quotes", inputSchema: { client_id: z.string().optional(), state: z.string().optional().describe("draft, sent, accepted, or declined"), from: z.string().optional(), to: z.string().optional() } }, async ({ client_id, state, from, to }) => {
    let path = "/estimates?per_page=100";
    if (client_id) path += `&client_id=${client_id}`;
    if (state) path += `&state=${state}`;
    if (from) path += `&from=${from}`;
    if (to) path += `&to=${to}`;
    const data = await harvestGet(path);
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
  });

  server.registerTool("get_estimate", { description: "Get a single estimate by ID", inputSchema: { estimate_id: z.string() } }, async ({ estimate_id }) => {
    const data = await harvestGet(`/estimates/${estimate_id}`);
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
  });

  server.registerTool("create_estimate", { description: "Create a new estimate/quote", inputSchema: { client_id: z.string(), subject: z.string().optional(), notes: z.string().optional(), issue_date: z.string().optional(), tax: z.number().optional(), discount: z.number().optional(), currency: z.string().optional() } }, async (args) => {
    const body = { client_id: args.client_id };
    if (args.subject) body.subject = args.subject;
    if (args.notes) body.notes = args.notes;
    if (args.issue_date) body.issue_date = args.issue_date;
    if (args.tax !== undefined) body.tax = args.tax;
    if (args.discount !== undefined) body.discount = args.discount;
    if (args.currency) body.currency = args.currency;
    const data = await harvestPost("/estimates", body);
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
  });

  server.registerTool("update_estimate", { description: "Update an existing estimate/quote", inputSchema: { estimate_id: z.string(), subject: z.string().optional(), notes: z.string().optional(), tax: z.number().optional(), discount: z.number().optional(), issue_date: z.string().optional() } }, async (args) => {
    const body = {};
    if (args.subject !== undefined) body.subject = args.subject;
    if (args.notes !== undefined) body.notes = args.notes;
    if (args.tax !== undefined) body.tax = args.tax;
    if (args.discount !== undefined) body.discount = args.discount;
    if (args.issue_date !== undefined) body.issue_date = args.issue_date;
    const data = await harvestPatch(`/estimates/${args.estimate_id}`, body);
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
  });

  server.registerTool("delete_estimate", { description: "Delete an estimate permanently", inputSchema: { estimate_id: z.string() } }, async ({ estimate_id }) => {
    const data = await harvestDelete(`/estimates/${estimate_id}`);
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
  });

  server.registerTool("create_project", { description: "Create a new project", inputSchema: { name: z.string(), client_id: z.string(), is_billable: z.boolean(), bill_by: z.string(), budget_by: z.string() } }, async (args) => {
    const data = await harvestPost("/projects", args);
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
  });

  server.registerTool("update_project", { description: "Rename or update a project", inputSchema: { project_id: z.string(), name: z.string().optional(), is_active: z.boolean().optional(), notes: z.string().optional() } }, async (args) => {
    const body = {};
    if (args.name !== undefined) body.name = args.name;
    if (args.is_active !== undefined) body.is_active = args.is_active;
    if (args.notes !== undefined) body.notes = args.notes;
    const data = await harvestPatch(`/projects/${args.project_id}`, body);
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
  });

  server.registerTool("create_time_entry", { description: "Log hours or start a timer", inputSchema: { project_id: z.string(), task_id: z.string(), spent_date: z.string(), hours: z.number().optional(), notes: z.string().optional() } }, async (args) => {
    const body = { project_id: args.project_id, task_id: args.task_id, spent_date: args.spent_date };
    if (args.hours !== undefined) body.hours = args.hours;
    if (args.notes) body.notes = args.notes;
    const data = await harvestPost("/time_entries", body);
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
  });

  server.registerTool("update_time_entry", { description: "Update hours or notes on a time entry", inputSchema: { time_entry_id: z.string(), hours: z.number().optional(), notes: z.string().optional() } }, async (args) => {
    const body = {};
    if (args.hours !== undefined) body.hours = args.hours;
    if (args.notes !== undefined) body.notes = args.notes;
    const data = await harvestPatch(`/time_entries/${args.time_entry_id}`, body);
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
  });

  server.registerTool("stop_timer", { description: "Stop a running timer", inputSchema: { time_entry_id: z.string() } }, async ({ time_entry_id }) => {
    const data = await harvestPatch(`/time_entries/${time_entry_id}/stop`, {});
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
  });

  server.registerTool("delete_time_entry", { description: "Delete a time entry", inputSchema: { time_entry_id: z.string() } }, async ({ time_entry_id }) => {
    const data = await harvestDelete(`/time_entries/${time_entry_id}`);
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
  });

  return server;
}

const sessions = {};

app.use((req, res, next) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, POST, DELETE, OPTIONS, HEAD");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization, Mcp-Session-Id, Accept");
  if (req.method === "OPTIONS") return res.sendStatus(200);
  next();
});

app.post("/mcp", async (req, res) => {
  const sessionId = req.headers["mcp-session-id"];
  let transport;
  if (sessionId && sessions[sessionId]) {
    transport = sessions[sessionId];
  } else if (!sessionId && isInitializeRequest(req.body)) {
    transport = new StreamableHTTPServerTransport({ sessionIdGenerator: () => randomUUID() });
    const server = buildServer();
    await server.connect(transport);
    transport.onclose = () => {
      if (transport.sessionId) delete sessions[transport.sessionId];
    };
    sessions[transport.sessionId] = transport;
  } else {
    res.status(400).json({ error: "Bad request" });
    return;
  }
  await transport.handleRequest(req, res, req.body);
});

app.get("/mcp", async (req, res) => {
  const sessionId = req.headers["mcp-session-id"];
  if (!sessionId || !sessions[sessionId]) {
    res.status(400).json({ error: "Session not found" });
    return;
  }
  await sessions[sessionId].handleRequest(req, res);
});

app.delete("/mcp", async (req, res) => {
  const sessionId = req.headers["mcp-session-id"];
  if (sessionId && sessions[sessionId]) {
    await sessions[sessionId].close();
    delete sessions[sessionId];
  }
  res.status(200).end();
});

app.get("/", (req, res) => res.send("Harvest MCP Server running ✅"));

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
