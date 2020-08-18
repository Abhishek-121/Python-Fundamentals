 
#  Method 1 : By Using Simple functions and if-else conditions
   
# water = 400
# milk = 540
# coffee_beans = 120
# cups = 9
# cash = 550


# def status():
#     print("The coffee machine has:")
#     print(water, "of water")
#     print(milk, "of milk")
#     print(coffee_beans, "of coffee beans")
#     print(cups, "of disposable cups")
#     print(cash, "of money")


# def buy():
#     coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
#     if coffee_type == '1':
#         espresso()
#     elif coffee_type == '2':
#         latte()
#     elif coffee_type == '3':
#         cappuccino()
#     else:
#         return


# def espresso():
#     global water
#     global coffee_beans
#     global cash
#     global cups
#     if water - 250 >= 0 and coffee_beans - 16 >= 0 and cups - 1 >= 0:
#         water -= 250
#         coffee_beans -= 16
#         cups -= 1
#         cash += 4
#         print("I have enough resources, making you a coffee!")
#     else:
#         print("Sorry, not enough water!")


# def latte():
#     global water
#     global milk
#     global coffee_beans
#     global cash
#     global cups
#     if water - 350 >= 0 and milk - 75 >= 0 and coffee_beans - 20 >= 0 and cups - 1 >= 0:
#         water -= 350
#         milk -= 75
#         coffee_beans -= 20
#         cups -= 1
#         cash += 7
#         print("I have enough resources, making you a coffee!")
#     else:
#         print("Sorry, not enough water!")


# def cappuccino():
#     global water
#     global milk
#     global coffee_beans
#     global cash
#     global cups
#     if water - 200 >= 0 and milk - 100 >= 0 and coffee_beans - 12 >= 0 and cups - 1 >= 0:
#         water -= 200
#         milk -= 100
#         coffee_beans -= 12
#         cups -= 1
#         cash += 6
#         print("I have enough resources, making you a coffee!")
#     else:
#         print("Sorry, not enough water!")


# def take():
#     global cash
#     print("I gave you $" + str(cash))
#     cash = 0


# def fill():
#     global water
#     global milk
#     global coffee_beans
#     global cups
#     water += int(input("Write how many ml of water do you want to add:"))
#     milk += int(input("Write how many ml of milk do you want to add:"))
#     coffee_beans += int(input("Write how many grams of coffee beans do you want to add:"))
#     cups += int(input("Write how many disposable cups of coffee do you want to add:"))


# option = input(Write action (buy, fill, take, remaining, exit):)
# while option != "exit":
#     if option == "buy":
#         buy()
#     elif option == "fill":
#         fill()
#     elif option == "take":
#         take()
#     elif option == "remaining":
#         status()
#     option = input("Please choose the suitable action")



# Method 2 : Using Classes and Oops Concepts


class CoffeeMachine:
    
    def __init__(self, water=0, milk=0, beans=0, cups=0, money=0):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        
    def status(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money')
        
    def update_quantites(self, water=0, milk=0, beans=0, cups=0, money=0):
        self.water += water
        self.milk += milk
        self.beans += beans
        self.cups += cups
        self.money += money
        
    def make_espresso(self):
        if self.water>=250 and self.beans>=16 and self.cups>=1:
            self.update_quantites(water=-250, beans=-16, cups=-1, money=4)
            print("I have enough resources, making you a espresso!")
        else:
            print("Sorry, we do not have the ingredients for a espresso")

        
    def make_latte(self):
        if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups > 0:
            self.update_quantites(water=-350, milk=-75, beans=-20, cups=-1, money=7)
            print("I have enough resources, making you a latte!")
        else:
            print("Sorry, we do not have the ingredients for a latte")

    def make_cappuccino(self):
        if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups > 0:
            self.update_quantites(water=-200, milk=-100, beans=-12, cups=-1, money=6)
            print("I have enough resources, making you a cappuccino!")
        else:
            print("Sorry, we do not have the ingredients for a cappuccino")
      
            
    def withdrawnMoney(self):
        print(f'I gave you ${self.money}.')
        self.money = 0
        
    
    
def get_action():
    query = ["buy", "fill", "take", "remaining", "exit"]
    action = ""
    while action not in query:
        print("Write action (buy, fill, take, remaining, exit):")
        action = input().lower()
    return action
        
def make_purchase():
    selections = ['1', '2', '3', 'back']
    selection = ""
    
    while selection not in selections:
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back")
        selection = input().lower()
        
    # Espresso
    if selection == '1':
        coffeeMachine.make_espresso()
    
    # Latte
    if selection == '2':
        coffeeMachine.make_latte()
   
    # Cappuccino
    if selection == '3':
        coffeeMachine.make_cappuccino()
   
    # Go back
    if selection == 'back':
        print("Redirecting you back to the main menu...")
      
        
def fill_requirements():
    
    water = int(input("Write how many ml of water do you want to add:"))
    milk = int(input("Write how many ml of milk do you want to add:"))
    beans = int(input("Write how many grams of coffee beans do you want to add:"))
    cups = int(input("Write how many disposable cups do you want to add:"))
    
    coffeeMachine.update_quantites(water=water, milk=milk, beans=beans, cups=cups)



# Execution of the code start from here

coffeeMachine = CoffeeMachine(water=400, milk=540, beans=120, cups=9, money=550)

is_right = False

print('Welcome to the Coffee Cafe !')

while is_right==False:
    print()
    action = get_action() 
    print()
    if action == "buy":
        make_purchase()
    elif action == "fill":
        fill_requirements()
    elif action == "take":
        coffeeMachine.withdrawnMoney()
    elif action == "remaining":
        coffeeMachine.status()
    elif action == "exit":
        print("Bye !")
        is_right = True
    else:
        print("Invalid Input...Try with diffrent one !")

