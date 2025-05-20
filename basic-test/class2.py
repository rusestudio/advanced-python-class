class Microwave:
    def __init__(self, brand:str, power_rating:str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turn_onn: bool = False

    def turn_on(self) -> None:
        if self.turn_onn:
            print(f'Microwave ({self.brand}) is already turned on.')
        else:
            self.turn_onn = True
            print(f'Microwave ({self.brand}) is now turned on.')

    def turn_off(self) -> None:
        if self.turn_onn:
            self.turn_onn = False
            print(f'Microwave ({self.brand}) is now off.')
        else:
            print(f'Microwave ({self.brand}) is already off.')

    def run(self, seconds: int) ->None:
        if self.turn_onn:
            print(f'Running ({self.brand}) for {seconds} seconds')
        else:
            print(f'turn on the microwave first')

    #dunder method
    def __add__(self,other):
        return f'{self.brand} + {other.brand}'
    
     #dunder method
    def __mul__(self,other):
        return f'{self.brand} * {other.brand}'
    
    def __str__(self) -> str:  #return in string
        return f'{self.brand} (Rating: {self.power_rating})'
    
    def __repr__(self) -> str:
        return f'Microwave(brand="{self.brand}", power_rating="{self.power_rating}")'


panasonic: Microwave = Microwave(brand='Panasonic', power_rating='A')
print(panasonic)
print(panasonic.brand)
print(panasonic.power_rating)

panasonic.turn_on()
panasonic.turn_on()
panasonic.run(30)
panasonic.turn_off()
panasonic.run(10)

samsung: Microwave = Microwave(brand='Samsung', power_rating='B')

print(panasonic+ samsung)
print(panasonic* samsung)

print(panasonic) # in string, to get the name instead code
print(samsung)

print(repr(panasonic)) # return string in represantation(more specific)
print(repr(samsung))

