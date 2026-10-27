A = input("Enter condition of Room A (dirty/clean): ").lower()
B = input("Enter condition of Room B (dirty/clean): ").lower()

location = input("Enter vacuum location (A/B): ").upper()

if location == "A":
    if A == "dirty":
        print("Room A is dirty")
        print("Action: Suck")
        A = "clean"
    else:
        print("Room A is clean")
        print("Action: Move Right")

else:
    if B == "dirty":
        print("Room B is dirty")
        print("Action: Suck")
        B = "clean"
    else:
        print("Room B is clean")
        print("Action: Move Left")

print("Final Room A:", A)
print("Final Room B:", B)
