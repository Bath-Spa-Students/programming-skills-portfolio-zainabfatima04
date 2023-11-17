#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
#As they enter each topping, print a message saying you’ll add that topping to their pizza.

while True:
    topping = input("Enter a pizza topping (type 'quit' to finish): ")

    if topping.lower() == 'quit':
        print("Quitting the pizza topping selection. Enjoy your pizza!")
        break

    print(f"We'll add {topping} to your pizza.")

#The program will reach this point after the user enters 'quit' and breaks out of the loop.