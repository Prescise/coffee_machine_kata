from list_resources import *
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
        return list_drinks

    def setMachineOff(self):
        self.machine_on = False
        print("...machine shut down ... ")
        return

    def isResourceAvailable(self, order):
        for key, value in list_recipes[order].items():
            resource_quantity = getattr(self, key)
            if resource_quantity < value:
                print(f"Sorry there is not enough {key}")
                return False
                
    def decreaseResourceQuantity(self, order):
        if self.isResourceAvailable(order):
            for key, value in list_recipes[order].items():
                resource_item_quantity = getattr(self, key)
                setattr(self, key, resource_item_quantity - value)
    
    def displayMessage(self):
        return money_reminder_message

    def getOrder(self):  
        while self.machine_on == True:
            order = input("What would you like ?")
            if order == "report":
                return self.getReport()
            
            elif order == "off":
                return self.setMachineOff()
            
            elif order == "espresso" or order == "latte" or order == "cappuccino" :
                self.isResourceAvailable(order)
                self.buyDrink()
                self.decreaseResourceQuantity(order)
            