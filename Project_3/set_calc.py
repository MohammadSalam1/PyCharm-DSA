a = set()
b = set()

while True:
    print("\n commands: add_a, add_b, union, inter, diff_ab, diff_ba, quit")
    user_choice = input("Enter a command: \n").lower()

    if user_choice == "add_a":
        a_val = int(input("Enter a number for a: "))
        a.add(a_val)
    elif user_choice == "add_b":
        b_val = int(input("Enter a number for b: "))
        b.add(b_val)
    elif user_choice == "union":
        print("a U b = ", a | b)
    elif user_choice == "inter":
        print("a ∩ b = ", a & b)
    elif user_choice == "diff_ab":
        print("a - b = ", a - b)
    elif user_choice == "diff_ba":
        print("b - a = ", b - a)
    elif user_choice == "quit":
        break
    else:
        print("Invalid Command")