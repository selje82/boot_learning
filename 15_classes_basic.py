class Cat:
    # Simple attempt to model a cat
    def __init__(self, name: str, age: int):
        # Initialize name and age attributes
        self.name = name
        self.age = age

    def sleep(self):
        # Simulate a cat is going to sleep. 
        print(f"{self.name} is sleeping")

    def eat(self):
        # Simulate a cat is eating.
        print(f"{self.name} is now eating again...")

    def cuddle(self):
        # Simulate a cat that want's to cuddle. 
        print(f"{self.name} want to cuddle...")

    def age_check(self):
        if self.age < 0:
            raise ValueError(f"{self.name} can not be negative years.")
        elif self.age < 5:
            print(f"{self.name} is a young cat")
        elif self.age < 10:
            print(f"{self.name} is an adult cat")
        else:
            print(f"{self.name} is a senior cat")

def main():
    kassy = Cat("Kassy", -15)
    kassy.sleep()
    try:
        kassy.age_check()
    except ValueError as e:
       print(f"{e}") 

main()