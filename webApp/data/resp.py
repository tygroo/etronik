#!/usr/bin/env python

import cgi
import cgitb

cgitb.enable()

print "Content-type: text/html\n\n"

form=cgi.FieldStorage()
    text=form["data"].value
    print "<h1>Text from text input box:</h1>"
    print cgi.escape(text)