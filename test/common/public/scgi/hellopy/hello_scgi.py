#!/usr/bin/env python2

import random, sys, os, cgi
from flup.server.scgi import WSGIServer

current = 0

def simple_app(environ, start_response):
    global current
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    ret = []
    ret.append('<title>Hello from Python</title>')
    for i in range(1, random.randint(2, 11)):
	ret.append('<h3>Hello, World No <span style="color: #008800;">%0.2d</span></h3>' % i)
    
    current += 1
    ret.append('<p>&nbsp;</p><p>Current request: <strong>%s</strong></p>' % (current,))
    form = cgi.FieldStorage(fp = environ['wsgi.input'], environ = environ, keep_blank_values = 1)
 
    ret.append('<ul>')
    for key in form.keys():
        ret.append('<li>%s: <strong>%s</strong></li>' % (key, form[key].value))

    ret.append('</ul>')
    return ret

print "Serving scgi content..."
os.umask(0o111)
#WSGIServer(simple_app, bindAddress=('', 9500)).run()
WSGIServer(simple_app, bindAddress='/tmp/hello_scgi_py.sk').run()




