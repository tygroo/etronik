from pymongo import MongoClient
import json
client = MongoClient('localhost', 27017)
db = client.epsi

#Ligne a supprimer (utilisee seulement pour les tests d'insertion)
#documents.remove()

def getList():
	res = db.index1.find({},{"_id":0,"body":0})
	return res

def insererDocument( titre, auteur, annee, sommaire, body ):
	documents.save({ "titre" : titre, "auteur" : auteur, "annee" : annee, "sommaire" : sommaire, "body" : body });
	return;

def chercheDansIndex1(query):
	result = db.index1.find({ '$text': { '$search': query, '$language': "fr" } },{"_id":0,"titre":1})
	array = []
	for item in result:
		for key, value in item.items():
			res = db.notice.find({"titre":value},{"_id":0,"titre":0})
			for elem in res:
				for key2,value2 in elem.items():
					array.append(value2)
	return array

def chercheDansIndex2(query):
	result = db.index2.find({ '$text': { '$search': query, '$language': "fr" } },{"_id":0,"titre":1})
	array = []
	for item in result:
		for key, value in item.items():
			res = db.notice.find({"titre":value},{"_id":0,"titre":0})
			for elem in res:
				for key2,value2 in elem.items():
					array.append(value2)
	return array

def chercheDansIndex3(query):
	result = db.index3.find({ '$text': { '$search': query, '$language': "fr" } },{"_id":0,"titre":1})
	array = []
	for item in result:
		for key, value in item.items():
			res = db.notice.find({"titre":value},{"_id":0,"titre":0})
			for elem in res:
				for key2,value2 in elem.items():
					array.append(value2)
	return array

def chercherDocument( field,recherche ):
	result = documents.find({ '$text': { '$search': recherche, '$language': "fr" } },{"_id":0,field:1})
	array = []
	for item in result:
		for key, value in item.items():
			array.append(value)
	return array

#insererDocument(titre="premier", auteur="moi", annee="2014", sommaire="first", body="Le texte du premier")
#insererDocument(titre="second", auteur="toi", annee="2015", sommaire="second", body="nlapute")

#A faire a la main dans mongodb
#documents.ensureIndex({ "titre" : "text", "body" : "text" },{ "default_language": "french" } )

def afficher(field,query):
	test = chercherDocument(field,query)
	return test







