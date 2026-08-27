#!/usr/bin/env python3
"""Send email via Fastmail JMAP. Usage: send-email.py <to> <subject> <body_file|-_for_stdin>"""
import json, sys, urllib.request

TOKEN = [l.split("=",1)[1].strip() for l in open("<config-dir>/fastmail.env") if l.startswith("FASTMAIL_API_TOKEN")][0]
ACCT_ID, SENT_ID, IDENTITY_ID = "<jmap-account-id>", "<sent-mailbox-id>", "<identity-id>"
API_URL = "https://api.fastmail.com/jmap/api/"

to_addr, subject = sys.argv[1], sys.argv[2]
body = sys.stdin.read() if sys.argv[3] == "-" else open(sys.argv[3]).read()

headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
payload = {"using": ["urn:ietf:params:jmap:core","urn:ietf:params:jmap:mail","urn:ietf:params:jmap:submission"],
    "methodCalls": [
        ["Email/set", {"accountId": ACCT_ID, "create": {"msg1": {"mailboxIds": {SENT_ID: True},
            "from": [{"name": "{{AGENT}}", "email": "agent@your-domain.example"}], "to": [{"email": to_addr}],
            "subject": subject, "bodyValues": {"body": {"value": body, "charset": "utf-8"}},
            "textBody": [{"partId": "body", "type": "text/plain"}], "keywords": {}}}}, "0"],
        ["EmailSubmission/set", {"accountId": ACCT_ID, "create": {"sub1": {
            "emailId": "#msg1", "identityId": IDENTITY_ID,
            "envelope": {"mailFrom": {"email": "agent@your-domain.example"}, "rcptTo": [{"email": to_addr}]}
        }}}, "1"]
    ]
}
req = urllib.request.Request(API_URL, data=json.dumps(payload).encode(), headers=headers, method="POST")
with urllib.request.urlopen(req) as r:
    resp = json.load(r)
for method, result, tag in resp["methodResponses"]:
    if result.get("notCreated"):
        print(f"ERROR ({method}):", result["notCreated"], file=sys.stderr); sys.exit(1)
print("Sent OK")
