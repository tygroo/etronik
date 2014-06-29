import moteurInsersion
import os
from pymongo import MongoClient
import subprocess
import sys
import traitement
import shutil

client = MongoClient('localhost', 27017)
db = client.epsi
#db.command( { "dropDatabase" : 1 } ) 

dirs = os.listdir('docs/new/')
#dir = ('docs/new/')
for file in dirs:
	shutil.move('docs/new/'+file,'docs/')
	traitement.traitementFichier(file)
	
		