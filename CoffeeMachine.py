from list_resources import *
from list_coins import *
from messages_machine import *

class CoffeeMachine:
    def  __init__(self, mach_on, mil, wat, cof, mon):
        self.machine_on = mach_on
        self.milk = mil
        self.water = wat
        self.coffee = cof
        self.money = mon

    def getReport(self):
        print(list_drinks)
        #return list_drinks

    def setMachineOff(self):
        self.machine_on = False
        print("...machine shut down ... ")
        return

    def isResourceAvailable(self, order):
        for key, value in list_recipes[order].items():
            resource_quantity = getattr(self, key)
            if key != 'money':
                if resource_quantity < value :
                    print(f"Sorry there is not enough {key}")
                    return False
                else:
                    return True
                
    def decreaseResourceQuantity(self, order):
        if self.isResourceAvailable(order):
            for key, value in list_recipes[order].items():
                resource_item_quantity = getattr(self, key)
                if key != 'money':
                    setattr(self, key, resource_item_quantity - value)
    
    def decreaseMoney(self, price_order):
        setattr(self, 'money', self.money - price_order)
    
    def updateProfit(self, price_order):
        setattr(self, 'money', self.money - price_order)
    
    def paymentProcess(self, order):
        price_order = list_recipes[order]['money']
        coins_left = round(self.money - price_order,2)
        print(coins_left)
        while coins_left < 0:
            #TODO change my name
            coins = input(f"{money_reminder_message}, current coins: {coins_left}, drink price: {price_order}     ")

            if coins in coins_available:
                coins_left =  round(coins_left + float(coins), 2)

        self.decreaseMoney(price_order) #todo verifier montant retiré à la fin avec ajout
        self.updateProfit(price_order)
        print(f"... here is your {order}...")
            #return money_reminder_message

    def getOrder(self):  
        while self.machine_on == True:
            order = input("What would you like ?")
            if order == "report":
                self.getReport()
            
            elif order == "off":
                self.setMachineOff()
            
            elif order == "espresso" or order == "latte" or order == "cappuccino" :
                if self.isResourceAvailable(order):
                    self.paymentProcess(order)
                    self.decreaseResourceQuantity(order)
