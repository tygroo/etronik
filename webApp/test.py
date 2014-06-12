import moteurInsersion
import parser2
import os
from pymongo import MongoClient
import pdf2txt
import dumppdf
import subprocess
import sys

client = MongoClient('localhost', 27017)
db = client.epsi
documents = db.documentsTest
#test = moteurV2.chercherDocument( "bidon1" )

#for e in test:
#	print e
#out = parser.inputDocsToBody("docs/M13_CAMPAGNE.pdf")
#documents.save({ "titre" : "bidon2", "body" : out })
dirs = os.listdir('docs/')
dir = ('docs/')
for file in dirs:
	print 'docs/'+file
	print "Creation des index"
	subprocess.call(['bash','createIndexes.sh','docs/'+file]);
	# Ouverture du fichier index1 en *lecture*
	fichier = open("index1", "r")
	temp = fichier.readlines()
	moteurInsersion.insererIndex1( file, temp )
	fichier.close()
	print 'index1 fait!'

	# Ouverture du fichier index2 en *lecture*
	fichier = open("index2", "r")
	temp = fichier.readlines()
	moteurInsersion.insererIndex2( file, temp )
	fichier.close()
	print 'index2 fait!'

	# Ouverture du fichier index3 en *lecture*
	fichier = open("index3", "r")
	temp = fichier.readlines()
	moteurInsersion.insererIndex3( file, temp )
	fichier.close()
	print 'index3 fait!'

#parser2.obtainTable("docs/M13_CAMPAGNE.pdf")
#parser2.getPageInPdf("docs/M13_CAMPAGNE.pdf", 1)
#subprocess.call(['java', '-jar', 'tika-app-1.5.jar', '-j', document])
a = '"'
#out = pdf2txt.main([a,'-m','2','docs/M13_TALEC.pdf'])
#pdf2txt.main([a,'-p','1','-o','toto','docs/M13_TALEC.pdf'])
#-m 1 -o toto ~/IdeaProjects/etronik/webApp/docs/M13_TALEC.pdf
#dumppdf.main([a,'-p','1','-t','docs/M13_TALEC.pdf']) >> toto.pdf


def extractpages(pageDebut, pageFin):
	result = ""
	print "toto"
	for i in range(pageDebut, pageFin):
		print "toto"
		#temp = pdf2txt.main([a,'-p',str(i),'docs/M13_TALEC.pdf'])
		temp = parser2.getPageInPdf('docs/M13_TALEC.pdf')
		result = result + str(temp)
	return result

#extractpages(1,5)
#print parser2._parse_pages('docs/M13_TALEC.pdf')


