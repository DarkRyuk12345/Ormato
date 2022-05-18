from dataclasses import dataclass
from typing import Union
import random
import random, string
import requests

# file imports 


class Helpers:

    def random_pass(x):
        length = 12
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        signs = ["$", "[", "%", "*", "@", "!", "=", "-", "(", "}"]
        password = result_str + f"{random.randint(873, 81849)}" + random.choice(signs)
        return password

    def get_location(x):
        location = requests.get("http://ipinfo.io")
        return location.json() 