# x = [100420, 204820, 938902, 290482, 295082, 84702782, 477302, 4840082, 583558, 84755527]
# current_cost = 0
# for y in x:
    # current_cost =+ y 

# print(current_cost)
# if (current_cost / 10 ) > 25000:
    # print("this restruant is for rich class")
# elif (current_cost / 10) > 10000:
    # print("this restruant is for upper-middle class")
 #   elif (current_cost/ 10) > 5000:
  #   print("this restruant is for the middle class")
# else:
#     print("this restruant is for the poor class and lower")

# print(current_cost / 10)

from __future__ import print_function, unicode_literals

from pprint import pprint

from PyInquirer import prompt, Separator

from examples import custom_style_2


            
        
            


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
        "choices": ["Macroni: $5.2", "Double Cheese: 9,2$", "Chicken TIkka: 7.88$"], 
        "when": lambda answers: answers["Order Something"] == "Pizza"

    }, 
    {
        "type": "list", 
        "name": "Favorite Momo", 
        "message": "Oh My Momarazi, Lets select which Momo you like then, shall we?",
        "choices": ["Veg Momo(Boiled): 2.11$", "Chicken Momo(Boiled): 3.1", "Veg Momo(Freid): 3$", "Chicken Momo(Fried): 4.2$"],
        "when": lambda answers: answers["Order Something"] == "Momo"
    },
    {
        "type": "list", 
        "name": "Favorite Chaat", 
        "message": "Chaat or Chai, Sabke dil jit jaye. Well, which chaat has won your heart?",
        "choices": ["Papri Chaat: 1.9$", "Samosa Chaat(Full Plate): 4$", "Paneer Chaat: 3.25$"],
        "when": lambda answers: answers["Order Something"] == "Chaat"
    }
]

answers = prompt(questions, style=custom_style_2)
pprint(answers)