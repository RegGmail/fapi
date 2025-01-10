#from __future__ import annotations
from odmantic import Model

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
        "collection":"purchase"
    }

