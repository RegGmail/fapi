from odmantic import Model
#from bson import datetime
#from datetime import datetime
import bson, datetime

print ("..> Model/Purchase")
class Purchase(Model):
    purchase_id: int
    buyer_id: int 
    book_id: int 
    items: int 
    price: float 
    date_purchased: datetime.datetime
    
    model_config = {
        "collection" : "purchase"
    }
