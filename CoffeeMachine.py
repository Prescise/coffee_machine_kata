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
        print(f" Water: {self.water}ml \n Milk: {self.milk}ml \n Coffee: {self.coffee}g \n Money: ${self.money}")

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
    
    def updateProfit(self, price_order):
        setattr(self, 'money', self.money + price_order)
    
    def refundUser(self, refund):
        print (f"Here is ${refund} dollars in change.")
    
    def paymentProcess(self, order):
        price_order = list_recipes[order]['money']
        coins_inserted = 0
        while coins_inserted < price_order:
            coins = input(f"{money_reminder_message}, current coins: {format(coins_inserted, '.2f')}, drink price: {price_order}     ")

            if coins in coins_available:
                coins_inserted =  round(coins_inserted + float(coins), 2)
        refund = format(coins_inserted - price_order, '.2f')
        self.updateProfit(price_order)
        self.refundUser(refund)
        print(f"... Here is your {order}. Enjoy!")

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
