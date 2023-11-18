#A girl heads to a computer shop to buy some USB sticks. 
#She loves USB sticks and wants as many as she can get for £50. 
#They are £6 each.
#Write a program that calculates how many USB sticks she can buy and how many pounds she will have left.

#Cost of each USB stick
usb_stick_price = 6

#Total budget in pounds
total_budget = 50

#Calculate the number of USB sticks she can buy
num_usb_sticks = total_budget // usb_stick_price

#Calculate the amount of money left after buying USB sticks
remaining_money = total_budget % usb_stick_price

#Display the results
print(f"With £{total_budget}, she can buy {num_usb_sticks} USB sticks.")
print(f"She will have £{remaining_money} left.")