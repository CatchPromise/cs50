import random



class Hat:
        
        houses = ["Red House", "Blue House", "Green House", "White House"]

        @classmethod
        def sort(cls, name):
         print(name, "is in", random.choice(cls.houses))

Hat.sort("Promise")