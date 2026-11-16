# Connect EvoLink MCP

Use a shell-capable agent that can read local images and run FFmpeg. The agent handles inspection, planning, and edits on disk. EvoLink MCP handles model selection, uploads, estimates, generation, and task retrieval. You can run the main workflow with the hosted MCP connection, browser OAuth, and local FFmpeg.

## Codex

```sh
codex mcp add evolink --url https://mcp.evolink.ai/mcp
```

Approve in the browser. If Codex asks for manual login, run `codex mcp login evolink`. Resume or reopen the chat if the tools have not appeared.

## Claude Code

```sh
claude mcp add --transport http --scope user evolink https://mcp.evolink.ai/mcp
claude mcp login evolink
```

Approve in the browser, then reopen Claude Code if needed. If the client expects interactive authentication, use `/mcp`, choose `evolink`, and authenticate there.

For other clients, add `https://mcp.evolink.ai/mcp` as a Streamable HTTP server and sign in with OAuth. Check that the client also has the local capabilities this workflow uses. [Official client setup](https://github.com/Evolink-AI/mcp-plugin#install).

## Check the connection

Ask the agent to call `check_balance` and `search_models` for an image-to-video model with first-frame control. Both are read-only checks. A verified connection lets you paste the [agent brief](agent-brief.md) and start the reference analysis.

## Move assets between the agent and MCP

Use an authorized HTTPS URL or the hosted upload flow. For local files, ask MCP for a `prepare_upload` ticket, let the agent upload the file from disk with the returned PUT command, and call `get_upload` with the original upload ID. Use the returned `file_url` after the upload shows `done`. Check the selected model's size, duration, and format limits separately. Keep result URLs and upload tokens out of case writeups.

Use `get_model` to check the current input fields and `estimate_cost` for the exact request. Review the quote before generation. Poll the original task ID with `get_task` and download the result while its link is valid. [Official tool reference](https://evolink.ai/docs/en/mcp/tools).
