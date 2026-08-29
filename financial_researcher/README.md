# financial_researcher

A small crewAI project that researches a company and writes up a report.

Two agents work in sequence:

1. **Senior Financial Researcher** — digs up recent news, filings, and background
   using a Serper-backed web search tool.
2. **Market Analyst & Report Writer** — turns that research into a clean,
   readable report with an executive summary and a market outlook.

The final report lands in `output/report.md`.

## Running

```bash
crewai run
```

You'll be prompted for the `company` (and `current_date`) inputs.

## Setup

You need a `.env` with at least:

```
OPENAI_API_KEY=...
SERPER_API_KEY=...   # free key at https://serper.dev
```

## Layout

- `crew.jsonc` — crew, tasks, and run config
- `agents/` — the two agent definitions
- `tools/mytools.py` — the tuned web search tool (`custom:mytools`)
- `knowledge/` — knowledge files for the agents
- `output/` — generated reports

> Heads up: `custom:<name>` runs `tools/<name>.py` as local Python when the crew
> loads. Only run crews you trust.
