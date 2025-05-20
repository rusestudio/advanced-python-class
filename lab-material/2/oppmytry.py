from random import randint


class Bos:
    name =""
    num_vending = []
    total_property =0

    def __init__(self, name:str, num_vending,total_property ):
        self.name = name
        self.num_vending= num_vending
        self.total_property =0

    def add_vending(self):
        if self.total_property >= Vending.machine_price:
            self.total_property -= Vending.machine_price
            machine = Vending(0,0,0)
            self.num_vending.append(machine)

    def collect_money_vending(self):
        for machine in self.num_vending:
            money = machine.return_money()

class Vending:
    vending_id =""
    drink_price ={
        "coffee":500,
        "cola":1000,
        "vitamin":800,
    }
    machine_price =10000

    def __init__(self, num_coffee, num_cola, num_vitamin):
        self.money =0
        self.num_drink ={
            "coffee": num_coffee,
            "cola": num_cola,
            "vitamin": num_vitamin,
        }
    

    def sell_drink(self):
        price = self.drink_price[drink_type]
        price= self.money > vending.drink_price[drink_type]
        if customer.money > price:
            customer.money 
            print

    def return_money(self):
        pass

    def balance(self):
        pass

class Customer:
    def __init__(self,name,c_money):
        self.name=name
        self.c_money = c_money

    def buy_drink(self, drink_type, vending:Vending):
        vending.sell_drink(drink_type)

