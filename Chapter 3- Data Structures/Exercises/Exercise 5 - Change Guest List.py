#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
#•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
#•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#•Print a second set of invitation messages, one for each person who is still in your list.

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
