#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable()

from templates import login_page, secret_page

import os
import secret
from http.cookies import SimpleCookie


# access entered data
s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")


# create cookie
cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None
if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value

# check cookie
cookie_ok = cookie_username == secret.username and cookie_password == secret.password

if cookie_ok:
    username = cookie_username
    password = cookie_password

# if user data is correct
correct = username == secret.username and password == secret.password


# set cookie
print("Content-Type: text/html")
if correct:
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")


print()
# choose page
if correct:
    print(secret_page(username, password))
else:
    print(login_page())

# display entered data
if username:
    print("You entered:", username)
    print("<br>")
if password:
    print("You entered:", password)
