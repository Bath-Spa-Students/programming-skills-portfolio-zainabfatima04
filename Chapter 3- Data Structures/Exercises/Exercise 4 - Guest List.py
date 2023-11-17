#If you could invite anyone, living or deceased, to dinner, who would you invite? 
#Make a list that includes at least three people you’d like to invite to dinner. 
#Then use your list to print a message to each person, inviting them to dinner.

#Define a list of people to invite to dinner
guests = ["Audrey Hepburn", "Coco Chanel", "Marie Curie"]

#Print invitation messages to each person
for person in guests:
    invitation = f"Dear {person},\n\tYou are cordially invited to join me for dinner. It would be an honor to have your company.\nSincerely, Zainab Fatima"
    print(invitation)
    print("\n")