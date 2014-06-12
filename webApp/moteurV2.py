from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.epsi
documents = db.documentsTest

#Ligne a supprimer (utilisee seulement pour les tests d'insertion)
#documents.remove()

def insererDocument():
	documents.save({ "titre" : "bidon1", "body" : "body1" })
	return
def chercherDocument( recherche ):
	return documents.find({ '$text': { '$search': {"titre": recherche }, '$language': "fr" } })
def chercherUnDocParTitre( title ):
	return documents.find_one({"titre": title})
#A faire a la main dans mongodb
#documents.ensureIndex({ "titre" : "text", "sommaire" : "text", "body" : "text" },{ "default_language": "french" } )




