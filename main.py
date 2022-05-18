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
print(Ormato().interface().startup(Ormato().types.User(22, 55)))

