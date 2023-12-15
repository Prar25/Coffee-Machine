MENU = {
    "espresso": { "ingredients": { "water": 50, "milk": 0 ,"coffee": 18, },
                   "cost": 80,
                },
    "latte": { "ingredients": { "water": 200,"milk": 150,"coffee": 24,},
               "cost": 110,
             },
    "cappuccino": { "ingredients": { "water": 250, "milk": 100, "coffee": 24,},
                     "cost": 150,
                  }
        }


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit=0

#Function to update the resources
def update_resources(drink):
        for key in resources:
            resources[key]=resources[key] - drink["ingredients"][key]

#Function to check if resources are enough
def check_resources(drink_ingredients):
        '''Function checks if the machine has enough resources to make the drink required'''
        for key in resources:
          if drink_ingredients[key]>=resources[key]:
               print("Sorry we currently do not have enough resources")
               return False
          else:
              return True
          
#Function to process money ( to check if its enough and to calculate the change)
def process_money(cash,drink):
    if cash<drink["cost"]:
        print("The amount is not sufficient, money is being refunded.")             
    elif cash==drink["cost"]:
        return True
    elif cash>drink["cost"]:
        change=cash-drink["cost"]
        print(f"Here is the change ₹{change}")
        return True

new_drink=True

# Prompt user, ask what drink they want
while new_drink:
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if drink=="off":
        pass
    elif drink=="report":
        for key in resources:
            print(key,':',resources[key])
    elif drink=='espresso' or drink=='latte' or drink=='cappuccino':
        drink=MENU[drink]
        if check_resources(drink["ingredients"]):
            print("The cost of the drink is :₹", drink["cost"])
            cash=int(input("Please enter the amount:" ))
            if process_money(cash,drink):
                profit+=cash
                update_resources(drink)
                print("Here is your drink ☕ ")
            choice=input("Do you want another drink? Y/N").lower()
            if choice=="no" or choice=="n":
                new_drink=False
    else:
        print("Please choose an item from the menu only.")
 
             