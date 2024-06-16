def main():
    foods={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    total=0
    while True:
        try:
            items=input("Item: ")
            for food in foods:
                if food==items.lower().title():
                    total=total+foods[food]
                    print(f"Total: ${total}")
                else:
                    pass
        except EOFError:
            break











main()
