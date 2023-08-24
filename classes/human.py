class Human:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = 27

    def __repr__(self):
        return f"Person (name= {self.first_name}, last name= {self.last_name}, age= {self._age})"
    
    def say_full_name(self):
        return f"Thank you for calling Verizon my name is {self.first_name} {self.last_name}, how can I help you?"

    def happy_birthday(self):
        self._age +=1
        return f"Today I became {self._age}!"

    @property
    def age(self):
        return f"{self.first_name} is {self._age} don't tell anybody"
    
    @age.setter
    def age(self, new_age):
        if new_age < self._age or new_age > self._age :
            print("I know your address, blood type, skin color and age. Do yourself a favor and quit lying about your age.")