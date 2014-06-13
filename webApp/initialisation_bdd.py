import moteurInsersion
import os
from pymongo import MongoClient
import subprocess
import sys

#test = moteurV2.chercherDocument( "bidon1" )

#for e in test:
#	print e
#out = parser.inputDocsToBody("docs/M13_CAMPAGNE.pdf")
#documents.save({ "titre" : "bidon2", "body" : out })
dirs = os.listdir('docs/')
dir = ('docs/')
for file in dirs:
	print 'Traitement du fichier : '+file
	print "Decoupage du fichier..."
	subprocess.call(['bash','createIndexes.sh','docs/'+file]);


	print "Insertion du fichier dans la collection 'index1'"
	# Ouverture du fichier index1 en *lecture*
	fichier = open("index1", "r")
	temp = fichier.readlines()
	moteurInsersion.insererIndex1( file, temp )
	fichier.close()

	print "Insertion du fichier dans la collection 'index2'"
	# Ouverture du fichier index2 en *lecture*
	fichier = open("index2", "r")
	temp = fichier.readlines()
	moteurInsersion.insererIndex2( file, temp )
	fichier.close()

	print "Insertion du fichier dans la collection 'index3'"
	# Ouverture du fichier index3 en *lecture*
	fichier = open("index3", "r")
	temp = fichier.readlines()
	moteurInsersion.insererIndex3( file, temp )
	fichier.close()

	print "Insertion du fichier dans la collection 'notice'"
	# Ouverture du fichier notice en *lecture*
	fichier = open("notice", "r")
	temp = fichier.readlines()
	moteurInsersion.insererNotice( file, temp )
	fichier.close()
	
	print "Traitement du fichier "+file+" termine\n"

# creation des Index
print 'Indexation des collections'
moteurInsersion.createIndexes()
print 'Indexation terminee'