from __future__ import print_function, unicode_literals
from custom_types.types import Types as ty
from typing import Union
from pprint import pprint
from PyInquirer import prompt, Separator
from examples import custom_style_2
import pyfiglet


class Interface:
    def startup(self, user: Union[ty.User, None]):
        print(pyfiglet.figlet_format("Ormato", font="starwars"))
        questions = [
        {
            "type": "list", 
            "name": "Order Something",
            "message": "Are your Hungry? Lets Order Something",
            'choices': [
                "Pizza", 
                "Momo", 
                "Chaat",
                "Vine", 
                "Ice cream",
                Separator(),
                "Cant Think Of What to Order? Check our Suggestions, Now!"

            ]
        },
        {
            "type": "list",
            "name": "Favorite Pizza",
            "message": "Oh Perfect, Which Pizaa do you Like?",
            "choices": ["Veggie Pizza", "Double Cheese", "Chicken Tikka", "Margherita Pizza", "Pepperoni Pizza"], 
            "when": lambda answers: answers["Order Something"] == "Pizza"

        }, 
        {
            "type": "list", 
            "name": "Favorite Momo", 
            "message": "Oh My Momarazi, Lets select which Momo you like then, shall we?",
            "choices": ["Veg Momo(Boiled)", "Chicken Momo(Boiled)", "Veg Momo(Fried)", "Chicken Momo(Fried)"],
            "when": lambda answers: answers["Order Something"] == "Momo"
        },
        {
            "type": "list", 
            "name": "Favorite Chaat", 
            "message": "Chaat or Chai, Sabke dil jit jaye. Well, which chaat has won your heart?",
            "choices": ["Papri Chaat", "Samosa Chaat", "Paneer Chaat"],
            "when": lambda answers: answers["Order Something"] == "Chaat"
        }
        ]


        answers = prompt(questions, style=custom_style_2)
        pprint(answers)
