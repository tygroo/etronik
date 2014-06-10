from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.epsi
documents = db.documentsTest

#Ligne a supprimer (utilisee seulement pour les tests d'insertion)
documents.remove()

def insererDocument( titre, auteur, annee, sommaire, body ):
	documents.save({ "titre" : titre, "auteur" : auteur, "annee" : annee, "sommaire" : sommaire, "body" : body },);
	return;

def chercherDocument( recherche ):
	return documents.find({ '$text': { '$search': recherche, '$language': "fr" } })


insererDocument(titre="premier", auteur="moi", annee="2014", sommaire="first", body="Le texte du premier")

#A faire a la main dans mongodb
#documents.ensureIndex({ "titre" : "text", "sommaire" : "text", "body" : "text" },{ "default_language": "french" } )


test = chercherDocument("premier")

for e in test:
	print e



