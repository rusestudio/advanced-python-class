#inheritance

class Phone:    #parent class
    def __init__(self, brand, year, storage):
        self.brand= brand
        self.year = year
        self.storage = storage

    def operate(self):
        return True
    
    def call(self):   #polymorphism
        return 'Dialing...'
    
class Iphone(Phone):    #child class. child(parent)
    def __init__(self, brand, year, storage):
        super().__init__(brand, year, storage)

    def camera(self):
        return 18
    
    def call(self):   #polymorphism
        return 'Siri Dialing...'

class Oppo(Phone):
    def __init__(self, brand, year, storage):
        super().__init__(brand, year, storage)

    def battery(self):
        if self.year < 2020:
           return 90
        else:
            return 100
        
    def call(self):   #polymorphism
        return 'Oppo Dialing...'
        

class Huwawei(Phone):
    def __init__(self, brand, year, storage):
        super().__init__(brand, year, storage)

#multiple inheritance
class Asus(Oppo,Iphone):
    def __init__(self, brand, year, storage):
        super().__init__(brand, year, storage)

    def call(self):   #polymorphism
        return 'Connecting...'


phone1 = Iphone('Iphone12', 2021, 128)
print(phone1.brand, phone1.year, phone1.storage)
print(phone1.operate())

laptop1 = Asus('Asus Tuf', 2020, 564)
print(laptop1.brand, laptop1.year, laptop1.storage)
print(laptop1.operate())
print(laptop1.camera())
print(laptop1.battery())

#polymorphism
print(phone1.call())
print(laptop1.call())

phone2 = Phone('Rog', 2024, 265)
print(phone2.call())