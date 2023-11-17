#Make several dictionaries, where each dictionary represents a different pet. 
#In each dictionary, include the kind of animal and the owner’s name. 
#Store these dictionaries in a list called pets. 
#Next, loop through your list and as you do, print everything you know about each pet.

#Create a list of dictionaries representing different pets
pets = [
    {'animal': 'dog', 'owner': 'Aisha'},
    {'animal': 'cat', 'owner': 'Fatima'},
    {'animal': 'parrot', 'owner': 'Mahnoor'},
    {'animal': 'fish', 'owner': 'Sarah'},
    {'animal': 'rabbit', 'owner': 'Sahiba'}
]

#Loop through the list and print information about each pet
for pet in pets:
    animal = pet['animal']
    owner = pet['owner']
    print(f"{owner}'s pet is a {animal}.")