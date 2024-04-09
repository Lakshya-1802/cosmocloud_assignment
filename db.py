import pymongo

mongoURI='mongodb+srv://Lakshya1802:Lakshya1802@cluster0.24irp7x.mongodb.net'

client = pymongo.MongoClient(mongoURI)

db=client['Cosmo']
collection=db['Students']