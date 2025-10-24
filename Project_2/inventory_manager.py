def add_item(name, qnty, price):
    # qnty is quantity, this function adds items to our dict
    # takes parameters, name (of item) how much (qnty) and price
    if name in inventory:
        inventory[name]["qnty"] =+qnty
    else:
        inventory[name] = {"qnty": qnty, "price": price}

def sell(name, qnty):
    # sell, reduce items from inventory
    # check if name is present and reduce quantity
    # if there is non or not enough raise error
    if name not in inventory:
        print("Item not found")
    if qnty > inventory[name]["qnty"]:
        print("Not enough in stock")
    if qnty == inventory[name]["qnty"]:
        print("This is all we got")
    if qnty < inventory[name]["qnty"]:
        inventory[name]["qnty"] -+ qnty
        print(f"sold {qnty} {name}")

def value():
    total = 0
    for item, data in inventory.items():
        total += data["qnty"] * data["price"]
    return total

if __name__ == "__main__":
    inventory = {}
    add_item("apple", 10, 3.1)
    add_item("oranges", 41, 2.0)
    add_item("banana", 3, 5.2)
    add_item("ananas", 5, 8.9)

    sell("banana", 2)
    sell("apple", 10)
    sell("ananas", 6)

    print("total inventory value: ", value())
