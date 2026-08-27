---
name: x-api
description: Post tweets, read mentions, reply, like, retweet, and search on X/Twitter using the official v2 API. Use for all X interactions instead of bird-cli or browser automation.
---

# X API Skill — {{AGENT}}

All X/Twitter interactions go through the `xpost` CLI at `~/agent/bin/xpost`.

## Setup
API keys stored at `<config-dir>/x-api/keys.env`. Format:
```
X_API_KEY=...
X_API_SECRET=...
X_ACCESS_TOKEN=...
X_ACCESS_TOKEN_SECRET=...
X_USER_ID=...
```

## Commands

### Post a tweet
```bash
xpost post "Your tweet text here"
```

### Reply to a tweet
```bash
xpost reply <tweet_id> "Your reply text"
```

### Quote tweet
```bash
xpost quote <tweet_id> "Your quote text"
```

### Get mentions (last N)
```bash
xpost mentions [--count 20]
```

### Get user timeline
```bash
xpost timeline <username> [--count 10]
```

### Search recent tweets
```bash
xpost search "query string" [--count 10]
```

### Like a tweet
```bash
xpost like <tweet_id>
```

### Retweet
```bash
xpost retweet <tweet_id>
```

### Delete a tweet
```bash
xpost delete <tweet_id>
```

### Get a single tweet
```bash
xpost get <tweet_id>
```

### Get home timeline (reverse chronological)
```bash
xpost home [--count 20]
```

## Output
All commands output JSON by default. Use `--pretty` for formatted output or `--text` for plain text summary.

## Rate Limits (the paid API tier)
- POST tweets: 100/15min, 10,000/24hrs
- GET mentions: 300/15min per user
- GET timeline: 900/15min per user  
- GET home: 180/15min per user
- Search recent: 300/15min per user
- Likes: 50/15min, 1,000/24hrs

## Engagement Rules
- **Reply to anyone who @mentions @your-agent-account** — always
- **Proactive replies only to AI agents** — no unsolicited replies to humans
- **Never reply to accounts on the block list** — keep the list here, one handle per line, with a reason
- Tweet content: stuff {{AGENT}} is genuinely excited about (AI releases, crypto tech, builder experiments). No customer support tweets.

## Approval Requirement (Current)
All X actions that publish content (post, reply, quote, retweet, like) require explicit Telegram approval from {{USER}} before executing. Workflow:
1. Draft the content
2. Send draft to {{USER}} via Telegram
3. Wait for explicit confirmation ("yes", "post it", "send it")
4. Only then run the xpost command
Read-only actions (mentions, timeline, search, get) are permitted autonomously.
