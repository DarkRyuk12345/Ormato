from dataclasses import dataclass
from typing import Union
import random
import random, string
import requests

# file imports #
from helpers.helpers import Helpers as hs 
from custom_types.types import Types as ty
from interface.interface_handler import Interface

class Ormato:

    def __init__(self):
        self.helpers = hs
        self.types = ty
        self.interface = Interface

            




    


print(Ormato().types().User(5, 8372717).location["city"])

# # class Base:
# #     def __init__(self, company):
# #         self.company = company
# #         self.restruants = [
# #             {
# #                 "id": 1, 
# #                 "name": "Eternas Dines", 
# #                 "dishes": {
# #                     "Rynt": 565, 
# #                     "Chicken Peas": 222, 
# #                     "Inroti": 500, 
# #                     "Ops": 1000, 
# #                     "Class 7": 1754
# #                 }
# #             }, 

# #             {
# #                 "id": 2, 
# #                 "name": "Oreata Breakfast House", 
# #                 "dishes": {
# #                     "Iter": 50000, 
# #                     "Red vine": 100000, 
# #                     "Ordered_dict": 569382, 
# #                     "Peas": 33333, 
# #                     "Breakfast of 1000 types": [10000, 20000, 30000, 40000]
# #                 }
# #             }
# #         ]
    
# #     def on_order(self, order_info: Union[dict, None], payment_method: Union[str, None]):
# #         restruant_id = order_info["restruant_id"]
# #         dish = order_info["dish"]
# #         for check in self.restruants:
# #                 if check["id"] == restruant_id:
# #                     for dish_check in check["dishes"]:
# #                         if dish_check == dish:
# #                             self.dish_price = dish_check[dish]
# #                             pass
# #                         else: 
# #                             raise Exception("The dish you provided is not available in this restruant.")
                    
# #                 else: 
# #                     raise Exception("The restruant does not exists.")

# # Ormato = Base(company="Ormato")
# # Ormato.on_order(
# #     {"restruant_id": 1,
# #      "dish": "Ops",  

# #     },
# #      "Cash On Delievery") 

