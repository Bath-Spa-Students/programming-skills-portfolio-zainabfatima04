#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
#Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
#Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['ham and cheese', 'chicken salad', 'pastrami', 'BLT', 'pastrami', 'turkey club', 'pastrami']
finished_sandwiches = []

#Print a message about running out of pastrami
print("Sorry, we've run out of pastrami.")

#Remove all occurrences of 'pastrami' from sandwich_orders using a while loop
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

#Loop through the list of sandwich orders
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    
    #Move the sandwich to the list of finished sandwiches
    finished_sandwiches.append(sandwich)

#Print a message listing each sandwich that was made
print("\nList of finished sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)   