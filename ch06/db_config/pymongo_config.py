from pymongo import MongoClient

def create_db_collections():
    client = MongoClient('ongodb+srv://Reginaldo:Mng0101&&@cluster0.ctnyk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    try:
        db = client.obrs
        buyers = db.buyer
        users = db.login
        yield {"users": users, "buyers": buyers}
    finally:
        client.close()

    
    

