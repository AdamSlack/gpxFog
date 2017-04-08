#!/usr/anaconda3/bin/env python
import cgi
import cgitb
cgitb.enable(display=0, logdir="..")

print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

print("<TITLE>CGI script output</TITLE>")
print("<H1>This is my first CGI script</H1>")
print("Hello, world!")