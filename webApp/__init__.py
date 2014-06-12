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

import json
import moteur
import execjs
from pymongo import *

def toDisplay(title,obj):
    table = "<table><th>"+title+"</th>"    
    for e in obj:
        table = table+"<tr><td>"+e+"</td><td></tr>"
    table = table + "</table>"
    return table
    
class Root:

    @cherrypy.expose
    def index(self):
        template_index=env.get_template('base.html')
        return template_index.render()

    @cherrypy.expose
    def base(self):
        template_index=env.get_template('index.html')
        return template_index.render()

    @cherrypy.expose
    def about(self):
        template_index=env.get_template('about.html')
        return template_index.render()

    @cherrypy.expose
    def response(self, titre, auteur, annee, query):
        template_index=env.get_template('response.html')
        
        return template_index.render(_titres = "titres",_auteurs = "auteurs",_annees = "annees",_contents = "contents",
        _title = titre, _author= auteur, _annee = annee, _query = query )

        
        #titres = toDisplay('titres',moteur.afficher('titre',titre))
        #auteurs = toDisplay('auteurs',moteur.afficher('auteur',auteur))
        #annees = toDisplay('annees',moteur.afficher('annee',annee))
        #contents = toDisplay("contents",moteur.afficher('content',query))
        #return template_index.render(_titres = titres,_auteurs = auteurs,_annees = annees,_contents = contents,
        #    _title = titre, _author= auteur, _annee = annee, _query = query )



