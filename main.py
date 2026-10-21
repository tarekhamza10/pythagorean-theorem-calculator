print("Hello, " + input("Enter your name: ") + " welcome")


adjacent_side = input("Adjacent side: ")
opposite_side = input("Opposite side: ")
hypotenuse = input("Hypotenuse: ")

if hypotenuse == "x":
    result = (float(adjacent_side)**2 + float(opposite_side)**2)**0.5

elif adjacent_side == "x":
    result = (float(hypotenuse)**2 - float(opposite_side)**2)**0.5

elif opposite_side == "x":
    result = (float(hypotenuse)**2 - float(adjacent_side)**2)**0.5

print("The result is:", result)
