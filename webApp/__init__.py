# coding=UTF-8
# -*- coding: UTF-8 -*-
import os
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import moteur
import cherrypy
import json
import subprocess
#import execjs
from pymongo import *
from cherrypy.lib.static import serve_file
from jinja2 import Template, Environment, FileSystemLoader

#class level variables
localDir=os.path.dirname(__file__)
absDir=os.path.join(os.getcwd(), localDir)
current_dir=os.path.dirname(os.path.abspath(__file__))

#setup some rendering templates
env=Environment(loader=FileSystemLoader(current_dir), trim_blocks=True)
    
def addtoRes(array,data):
    for item in data:
        array.append(item)
    return array


def delDuplicate(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]


class Root:

    @cherrypy.expose
    def index(self):
        template_index=env.get_template('base.html')
        return template_index.render()

    @cherrypy.expose
    def pdf(self,name):
        stream = open(os.getcwd()+'/webApp/docs/'+name,'rb').read()
        cherrypy.response.headers['Content-Type'] = "application/pdf"
        cherrypy.response.headers['Content-Length'] = len(stream)
        cherrypy.response.headers['Expires'] = 0
        return stream
        

    @cherrypy.expose
    def base(self):
        liste=""
        data = moteur.getList()
        for item in data:
            for key,value in item.items():
                liste=liste+"<a href='/pdf?name="+value+"'>"+value+"</a><br/>"
        template_index=env.get_template('index.html')
        return template_index.render(_liste= liste)

    @cherrypy.expose
    def about(self,p):
        template_index=env.get_template('about.html')
        return template_index.render()

    @cherrypy.expose
    def response(self, titre, auteur, annee, sommaire, query):

        res = []

        # Recherche dans l'index 1
        titres = moteur.chercheDansIndex1(titre)
        res = addtoRes(res,titres)
        auteurs = moteur.chercheDansIndex1(auteur)
        res = addtoRes(res,auteurs)
        annees = moteur.chercheDansIndex1(annee)
        res = addtoRes(res,annees)

        # Recherche dans l'index 2
        sommaires = moteur.chercheDansIndex1(sommaire)
        res = addtoRes(res,titres)
        sommaires = moteur.chercheDansIndex2(sommaire)
        res = addtoRes(res,titres)

        # Recherche dans l'index 3
        contents = moteur.chercheDansIndex1(query)
        res = addtoRes(res,contents)
        contents = moteur.chercheDansIndex2(query)
        res = addtoRes(res,contents)
        contents = moteur.chercheDansIndex3(query)
        res = addtoRes(res,contents)

        resultsArray = []
        results = ""
        strTmp = ""
        resTmp = []
        for data in res:
            if isinstance(data, list):
                strTmp = ""
                for data2 in data:
                    strTmp = strTmp + data2
                resultsArray.append(strTmp) 

        resTmp = delDuplicate(resultsArray)

        for dataTmp in resTmp:
            print dataTmp
            results=results+dataTmp


        template_index=env.get_template('response.html')
        return template_index.render(_results= results,
        _title = titre, _author= auteur, _annee = annee, _query = query )

        
        #titres = toDisplay('titres',moteur.afficher('titre',titre))
        #auteurs = toDisplay('auteurs',moteur.afficher('auteur',auteur))
        #annees = toDisplay('annees',moteur.afficher('annee',annee))
        #contents = toDisplay("contents",moteur.afficher('content',query))
        #return template_index.render(_titres = titres,_auteurs = auteurs,_annees = annees,_contents = contents,
        #    _title = titre, _author= auteur, _annee = annee, _query = query )

    @cherrypy.expose
    def upload(self, myFile=None):
        out = """<html>
        <body>
        myFile length: %s<br />
        myFile filename: %s<br />
        myFile mime-type: %s
        </body>
        </html>"""


        direction = 'webApp/'
        size = 0
        allData=''
        while True:
                data = myFile.file.read(8192)
                allData+=data
                if not data:
                        break
                size += len(data)
        savedFile=open(direction+'docs/new/'+myFile.filename, 'wb')
        savedFile.write(allData)
        savedFile.close()
        file = myFile.filename

        ##############################################
        #on peut optimiser en cherchant le chemin absolu
        
        #traitement.traitementFichier(direction+'docs/'+myFile.filename)
        #subprocess.call(['python','traitement.py',myFile.filename],cwd = direction);
        subprocess.call(['python','updateIndex.py'],cwd = direction);
        #initBase.initByDir(direction+'docs/')
        ##############################################

        template_index=env.get_template('index.html')
        return template_index.render()
        

        