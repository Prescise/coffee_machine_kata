from CoffeeMachine import *

coffee_machine = CoffeeMachine(True, 100, 50, 76, 2.5)

class TestCoffeeMachine:
    """def test_get_quantity_items(self):
        assert coffee_machine.getOrder() == list_drinks

    def test_turn_machine_off(self):
        coffee_machine.getOrder()
        assert coffee_machine.machine_on == False
    
    def test_milk_empty(self):
        coffee_machine_2 = CoffeeMachine(True, 0, 100, 76, 2.5)
        assert coffee_machine_2.getOrder() == "Sorry there is not enough milk"

    def test_water_empty(self):
        coffee_machine_3 = CoffeeMachine(True, 100, 0, 2, 2.5)
        assert coffee_machine_3.getOrder() == "Sorry there is not enough water"

    def test_coffee_empty(self):
        coffee_machine_4 = CoffeeMachine(True, 100, 100, 0, 2.5)
        assert coffee_machine_4.getOrder() == "Sorry there is not enough coffee"
    
    def test_check_machine_resources_used(self):
        coffee_machine_5 = CoffeeMachine(True, 100, 50, 76, 2.5)
        coffee_machine_5.getOrder()
        assert coffee_machine_5.milk == 98
        assert coffee_machine_5.water == 45
        assert coffee_machine_5.coffee == 76

    def test_check_resources_available(self):
        coffee_machine_6 = CoffeeMachine(True, 100, 50, 0, 2.5)
        coffee_machine_6.getOrder()"""
    
    def test_get_value_money(self):
        coffee_machine.getOrder()
        assert coffee_machine.getOrder() == '''Please pay your drink, you can pay with coins of:
        quarter: $0.25,
        dimes: $0.10,
        nickles: $0.05,
        pennies: $0.01'''


        