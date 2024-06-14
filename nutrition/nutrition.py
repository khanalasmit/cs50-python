calories=dict(apple=130,avocado=50,banana=110,cantaloupe=50,grapefruit=60,grapes=90,honewdew_melon=50,kiwifruit=90,lemon=15,lime=20,nectrine=60,orange=80,peach=60,pear=100,pineapple=50,plums=70,strawberries=50,sweet_cherries=100,tangerine=50,watermelon=80)
fruit=input("Item: ").lower()
fruit=fruit.strip().replace(" ","_")
for fr in calories:
    if fr==fruit:
        print("Calories:",calories[fr])
