#!/usr/bin/env python3

import os
import json

# print("Content-Type: application/json")
print("Content-Type: text/html")

print()

# environment variables
# print(os.environ)

# environment variables as JSON
# print(json.dumps(dict(os.environ), indent=2))

# get the query string
# q = os.environ.get("QUERY_STRING")

# include query string in html
# print(f"<!doctype html><title>Hello</title><h2>{q}</h2>")

# get the user's browser
a = os.environ.get("HTTP_USER_AGENT")

# include user's browser in html
print(f"<!doctype html><title>Hello</title><h2>{a}</h2>")
