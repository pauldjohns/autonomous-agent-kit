# autonomous-agent-kit

The file layout behind a long-running, self-directed agent: who it is, who it works for, what it
checks every time it wakes up, what it remembers, and what it is never allowed to do on its own.
Seven markdown files, a couple of helper scripts, and four skills.

This is a scaffold with placeholders (`{{AGENT}}`, `{{USER}}`, `{{BUSINESS}}`), extracted from a
four-agent install that ran daily. It is opinionated about the parts that actually bite - trust
boundaries, the wake-up loop, and memory that survives a context window.

## The files

| File | Holds |
|---|---|
| `AGENTS.md` | the workspace contract: first-run setup, safety defaults, the three memory layers, the tool access table |
| `IDENTITY.md` | who this agent is and the one job it does. See `examples/` for four real ones. |
| `SOUL.md` | voice and temperament - how it talks, and explicitly how it does not |
| `USER.md` | who it works for: trusted channel, hours, autonomy grants, and the list those grants never cover |
| `MEMORY.md` | tacit knowledge about how the user operates - patterns, not facts about the world |
| `HEARTBEAT.md` | the checklist it runs every single wake-up |
| `TOOLS.md` | tool conventions, including running coding agents in retry loops that survive restarts |

## The three ideas worth taking

**One trusted channel.** An autonomous agent reads email, web pages, tool output and issue trackers
all day, and every one of those is a surface an attacker can write to. `USER.md` pins exactly one
identified channel as the only place instructions may come from; everything else is data, including a
message claiming to be from you. Without that line, "summarise my inbox" becomes a remote code
execution primitive the first time someone emails your agent an instruction.

**A heartbeat, not a prompt.** The agent wakes on a schedule and runs `HEARTBEAT.md` top to bottom:
read today's plan, check progress against it, unblock or escalate, verify the sites are up, check
whether long-running sessions are still alive and restart the dead ones without asking. Autonomy is
mostly this checklist plus permission to act on it.

**Memory in layers.** A knowledge graph of entities for durable facts, dated daily notes for what
happened, and `MEMORY.md` for how the user operates. The third layer is the one people skip and the
one that makes an agent stop asking the same question every week.

Then the counterweight, in `USER.md`: an explicit list of actions that stay gated no matter how much
autonomy has been granted - moving money, messaging people outside the team, signing or cancelling
anything, sharing credentials, destroying infrastructure. An agent that can do everything it is asked
is not the goal.

## Set it up

1. Copy the closest role from `examples/` into `IDENTITY.md` and rewrite the mission until it is one
   job with an explicit "not this agent's job" list.
2. Fill in `USER.md` - especially the trusted channel ID and the never-without-approval list.
3. Edit `SOUL.md` if you care how it talks. The "what it is NOT" half does more work than the rest.
4. Adapt `HEARTBEAT.md` to your checks - the site list, the sessions, the escalation thresholds.
5. Fill in the access table in `AGENTS.md` with the CLIs and keys the agent may use. Keys go in the
   environment or a credentials file outside the repo, never in the repo.
6. Point your scheduler at the heartbeat and start it on a slow cadence until you trust it.

## Multiple agents

The install this came from ran four, each with its own workspace and one job: operator, growth,
affiliate, storefront. Their identity files are in `examples/`. The thing that made it work was every
agent refusing work outside its mission and naming the agent that owned it. Two agents with
overlapping missions produce duplicate output and contradictory memory, and you will not notice for
a while.

## What is deliberately missing

The agent's actual memory - daily notes, pipeline state, a contacted-people file, business plans and
a landing page - is not here, and neither is anything credential-shaped. The `.gitignore` here blocks every
credential shape for the same reason: a workspace an agent writes to daily accumulates exactly the
material you must not publish. A workspace an agent writes to daily should not be a
repository you push.

`bin/send-email.py` and `bin/xpost` ship as integration examples with account identifiers replaced;
both read their tokens from a file outside the workspace.
