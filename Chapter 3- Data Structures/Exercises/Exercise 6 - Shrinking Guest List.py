#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#•Start with your program from Exercise 3-5. 
#Add a new line that prints a message saying that you can invite only two people for dinner.
#•Use pop() to remove guests from your list one at a time until only two names remain in your list. 
#Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#•Print a message to each of the two people still on your list, letting them know they’re still invited.
#•Use del to remove the last two names from your list, so you have an empty list. 
#Print your list to make sure you actually have an empty list at the end of your program.    

#Initialize a list of people to invite to dinner
guests = ["Audrey Hepburn", "Coco Chanel", "Marie Curie"]

#Print invitation messages to each person
for person in guests:
    print(f"Dear {person},\n\tYou are cordially invited to join me for dinner. It would be an honor to have your company.\nSincerely, Zainab Fatima\n")

#Print the guest who can't make it
cannot_make_it = "Audrey Hepburn"
print(f"Unfortunately, {cannot_make_it} can't make it to dinner.\n")

#Replace the guest who can't make it with a new person
new_guest = "Marilyn Monroe"
guests[guests.index(cannot_make_it)] = new_guest

#Print invitation messages to each person after the update
for person in guests:
    print(f"Dear {person},\n\tYou are cordially invited to join me for dinner. It would be an honor to have your company.\nSincerely, Zainab Fatima\n")

#Print a message that you can invite only two people for dinner
print("Due to a delay, I can only invite two people for dinner.\n")

#Use pop() to remove guests until only two names remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner due to unforeseen circumstances.\n")

#Print invitation messages to the two remaining guests
for person in guests:
    print(f"Dear {person},\n\tYou are still invited to join me for dinner. It would be an honor to have your company.\nSincerely, Zainab Fatima\n")

#Use del to remove the last two names from the list
del guests[:]
print("Guest list:", guests)

