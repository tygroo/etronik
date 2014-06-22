import moteurInsersion
import os
from pymongo import MongoClient
import subprocess
import sys
import traitement

client = MongoClient('localhost', 27017)
db = client.epsi
db.command( { "dropDatabase" : 1 } ) 
#test = moteurV2.chercherDocument( "bidon1" )

#for e in test:
#	print e
#out = parser.inputDocsToBody("docs/M13_CAMPAGNE.pdf")
#documents.save({ "titre" : "bidon2", "body" : out })

dirs = os.listdir('docs/')
dir = ('docs/')
for file in dirs:
	traitement.traitementFichier(file)
