# coding=UTF-8
# -*- coding: UTF-8 -*-
import os
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

import cherrypy
from cherrypy.lib.static import serve_file

from jinja2 import Template, Environment, FileSystemLoader

#class level variables
localDir=os.path.dirname(__file__)
absDir=os.path.join(os.getcwd(), localDir)
current_dir=os.path.dirname(os.path.abspath(__file__))

#setup some rendering templates
env=Environment(loader=FileSystemLoader(current_dir), trim_blocks=True)

class Root:

    @cherrypy.expose
    def index(self):
        template_index=env.get_template('index.html')
        return template_index.render()

    @cherrypy.expose
    def response(self, title, author, annee, query):
        template_index=env.get_template('response.html')
        return template_index.render(_title = title, _author= author, _annee = annee, _query = query )

    @cherrypy.expose
    def test(self, title, author, annee, query):
    	a=title+" "+author+" "+annee+" "+query
    	return a