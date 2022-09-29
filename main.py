#Exercise 6 - Combo Meal
burger = int(input("Enter burger selling price:"))
soda = int(input("Enter soda selling price:"))
combo = int(input("Enter combo meal selling price:"))

f = soda + burger
g = f - combo

print("\nThe fixed profit is $%.2f"%g)