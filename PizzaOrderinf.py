print("Thank you for choosing Python Pizza Deliveries!")
size = input(
    " What size pizza do you want? S, M, or L\n"
)  # What size pizza do you want? S, M, or L
add_pepperoni = input(
    "Do you want pepperoni? Y or N\n"
)  # Do you want pepperoni? Y or N
extra_cheese = input(
    "Do you want extra cheese? Y or N \n"
)  # Do you want extra cheese? Y or N
total_bill = 0
# Small pizza (S): $15

# Medium pizza (M): $20S
# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2

# Add pepperoni for medium or large pizza (Y or N): +$3

# Add extra cheese for any size pizza (Y or N): +$1

if size == "S" or size == "s":
    total_bill += 15
elif size == "M" or size == "m":
    total_bill += 20
elif size == "L" or size == "l":
    total_bill += 25
else:
    print(f"Please enter the correct input")

if add_pepperoni == "Y" or add_pepperoni == "y":
    total_bill += 3


if extra_cheese == "Y" or extra_cheese == "y":
    total_bill += 1
    print(
        f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${total_bill}."
    )
else:
    print(
        f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${total_bill}."
    )
