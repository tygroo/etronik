from pymongo import MongoClient
import pymongo
client = MongoClient('localhost', 27017)

db = client.epsi
db.command( { "dropDatabase" : 1 } ) 

db = client.epsi

index1 = db.index1
index2 = db.index2
index3 = db.index3
notice = db.notice

#Ligne a supprimer (utilisee seulement pour les tests d'insertion)
#documents.remove()

def insererIndex1( titre, body ):
	index1.save({ "titre" : titre, "body" : body })
	return

def insererIndex2( titre, body ):
	index2.save({ "titre" : titre, "body" : body })
	return

def insererIndex3( titre, body ):
	index3.save({ "titre" : titre, "body" : body })
	return

def insererNotice( titre, body ):
	notice.save({ "titre" : titre, "body" : body })
	return

def createIndexes():
	index1.ensure_index([("titre" , pymongo.TEXT),("body",pymongo.TEXT)], default_language="french")
	index2.ensure_index([("titre" , pymongo.TEXT),("body",pymongo.TEXT)], default_language="french")
	index3.ensure_index([("titre" , pymongo.TEXT),("body",pymongo.TEXT)], default_language="french")
	notice.ensure_index([("titre" , pymongo.TEXT),("body",pymongo.TEXT)], default_language="french")
	return