
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from models.data.beanie import Cart, Order, Receipt

async def db_connect():
    global client
    client = AsyncIOMotorClient(f"mongodb+srv://Reginaldo:Mng0101&&@cluster0.ctnyk.mongodb.net/")
    print ("Beanie db_connect")
    await init_beanie(client.obrs, document_models=[Cart, Order, Receipt])
    
async def db_disconnect():
     client.close()