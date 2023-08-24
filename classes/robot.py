class Robot:
    def __init__ (self, name, age, model_num, battery_type="A"):
        self.name = name
        self.age = 0
        self.model_num = model_num
        self.battery_type = battery_type

    def eat_corn(self):
        return "Delicious"

    def swim(self):
        return f"Hey someone need help {self.name} the robot is going to save you"