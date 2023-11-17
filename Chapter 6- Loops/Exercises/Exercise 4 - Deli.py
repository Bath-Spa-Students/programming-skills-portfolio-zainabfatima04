#Make a list called sandwich_orders and fill it with the names of various sandwiches. 
#Then make an empty list called finished_sandwiches.
#Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. 
#As each sandwich is made, move it to the list of finished sandwiches. 
#After all the sandwiches have been made, print a message listing each sandwich that was made.

#Make a list called sandwich_orders and fill it with the names of various sandwiches
sandwich_orders = ['ham and cheese', 'turkey club', 'BLT', 'chicken salad']

#Make an empty list called finished_sandwiches
finished_sandwiches = []

#Loop through the list of sandwich orders
while sandwich_orders:
    #Get the next sandwich order
    current_order = sandwich_orders.pop(0)

    #Print a message for each order
    print(f"I made your {current_order} sandwich.")

    #As each sandwich is made, move it to the list of finished sandwiches
    finished_sandwiches.append(current_order)

#After all the sandwiches have been made, print a message listing each sandwich that was made
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)  