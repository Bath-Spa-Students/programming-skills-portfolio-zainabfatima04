#Start with the list you used in Exercise 1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.

#Define a list of friends' names
names = ["Aisha", "Sahiba", "Suriya", "Urooj"]

#Iterate through the list and print a personalized message for each friend
for name in names:
    message = f"Hi, {name}! I'm glad to see you."
    print(message)