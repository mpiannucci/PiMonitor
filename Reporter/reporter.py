#!/usr/bin/python
# Copyright 2015 Matthew Iannucci
# 
# reporter.py 
# The main collector script. The front end web page. Recieves the 
# data from the collector and displays it for the user in meaningful 
# way
import web
import json
import model
import config
from google.appengine.api import users

# Map out the URLs
urls = (
    '/', 'Index',
    '/report/(.+)', 'Report'
)

# Set the debugging messages
web.config.debug = True

# Define the globals
t_globals = {
    'datestr': web.datestr,
    'getAllReports': model.getAllReports,
    'len': len
}
render = web.template.render('Templates', base='base', globals=t_globals)

# Create the web application
app = web.application(urls, globals())

# ------------------------------------------------------------------------
# Web Page Class Definitions

class Index:
    '''Main index page'''
    def GET(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin(): 
            return render.index()
        else:
            raise web.redirect(users.create_login_url('/'))

class Report:
    ''' Report URL to receive POST calls full with data '''
    def POST(self, api_key):
        if api_key in config.KEYS:
            newReport = json.loads(web.data())
            model.newReport(newReport["temp"], newReport["humidity"])
            return web.data()
        else:
            return web.internalerror('The server says: No soup for you!')

def notfound():
    ''' Create the not found page '''
    return web.notfound('Sorry, the page you were looking for was not found.')
    # You can use template result like below, either is ok:
    # return web.notfound(render.notfound())
    # return web.notfound(str(render.notfound()))

def internalerror():
    ''' Create the internal error page '''
    return web.internalerror('The server says: No soup for you!')

# Create the not found app
app.notfound = notfound
app.internalerror = internalerror

main = app.cgirun()