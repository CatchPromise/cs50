pupils = [
    {"name": "Hermione", "house": "Harvard"},
    {"name": "Ruth", "house": "Harvard"},
    {"name": "Eliora", "house": "Harvard"},
    {"name": "Chidera", "house": "Stanford"},
    {"name": "Khari", "house": "MIT"},
]

houses = set()
for pupil in pupils:
    houses.add(pupil["house"])

for house in sorted(houses):
    print(house)