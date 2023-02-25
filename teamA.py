num_of_toys = int(input())
total_amount = int(input())
amount_left = int(input())
each_toy_price = total_amount // num_of_toys
remaining_amount = total_amount + amount_left
print("Cost of each toy is", each_toy_price , "and the Amount he had is" , remaining_amount)
