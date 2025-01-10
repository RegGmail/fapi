from odmantic import AIOEngine
from motor.motor_asyncio import AsyncIOMotorClient

def create_db_connection():
   global client_od
   print (">>> [db_config - CreateDBConnection] 2 ---> FastAPI")
   #client_od = AsyncIOMotorClient(f"mongodb://localhost:27017/")
   client_od = AsyncIOMotorClient(f"mongodb+srv://Reginaldo:Mng0101&&@cluster0.ctnyk.mongodb.net/")

   print (">>> [db_config - CreateDBConnection] 2a) cliente_od -->", client_od)

   #cluster0.ctnyk.mongodb.net
   #mongodb+srv://Reginaldo:Mng0101&&@cluster0.ctnyk.mongodb.net/

def create_db_engine():
   engine = AIOEngine(client=client_od, database="obrs")
   return engine

def close_db_connection():
    client_od.close()
