from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.epsi
index1 = db.index1
index2 = db.index2
index3 = db.index3
notice = db.notice

#Ligne a supprimer (utilisee seulement pour les tests d'insertion)
#documents.remove()

def insererIndex1( titre, body ):
	index1.save({ "titre" : titre, "body" : body });
	return;
def insererIndex2( titre, body ):
	index2.save({ "titre" : titre, "body" : body });
	return;
def insererIndex3( titre, body ):
	index3.save({ "titre" : titre, "body" : body });
	return;
def insererNotice( titre, body ):
	notice.save({ "titre" : titre, "body" : body });
	return;