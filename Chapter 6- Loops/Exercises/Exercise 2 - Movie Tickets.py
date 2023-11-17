#A movie theater charges different ticket prices depending on a person’s age. 
#If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 
#Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

while True:
    #Get user's age
    age_str = input("Please enter your age (enter 'quit' to exit): ")

    #Check if the user wants to quit
    if age_str.lower() == 'quit':
        break

    #Convert age input to an integer
    try:
        age = int(age_str)
    except ValueError:
        print("Please enter a valid age.")
        continue

    #Determine ticket price based on age
    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

    #Display the ticket price
    print(f"The cost of your movie ticket is ${ticket_price}\n")
