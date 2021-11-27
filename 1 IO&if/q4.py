numbers = eval(input("How many guests are coming to the party? "))
if numbers <= 20:
    price = 95 * numbers
elif numbers <= 40:
    price = 95 * 20 + (numbers - 20) * 75
elif numbers <= 50:
    price = 95 * 20 + 75 * 20 + (numbers - 40) * 65
else:
    price = 95 * 20 + 75 * 20 + 10 * 65 + (numbers - 50) * 60
print("{0} guests will cost {1}.".format(numbers, price))
