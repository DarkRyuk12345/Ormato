from dataclasses import dataclass, field
from typing import Union
import random
import random, string
import requests
from helpers.helpers import Helpers

# file imports

class Types:

    @dataclass(init=True)
    class User:
        id: int 
        phone_number: int
        location: dict = field(default_factory=Helpers().get_location)
        password: str =  field(default_factory=Helpers().random_pass)

    @dataclass(init=True)
    class Order:
        id: int
        order_info: dict
        valet_info: dict
        restruant_info: dict
        payment_method: str