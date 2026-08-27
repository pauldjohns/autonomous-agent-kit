# memory/

Dated daily notes live here: `YYYY-MM-DD.md`, one per day the agent ran.

Each day's file carries the plan for the day, what actually happened, active long-running sessions,
and anything that needs to survive into tomorrow. `HEARTBEAT.md` reads today's file at the top of
every wake-up and writes progress back to it, which is what makes a fresh context window able to
continue yesterday's work.

The directory is gitignored on purpose. These notes accumulate real operational detail - who was
contacted, what a site was doing at 3am, what the user said to do - and none of it belongs in a
repository.
