class Smartphone:
    def __init__(self, brand, model, colour):
        self.brand = brand
        self.model = model
        self.colour = colour

        self.battery_level = 100
    def make_call(self, number):
        print(f"calling {number}")

    def send_message(self, number, message):
        print(f"Sending {message} to {number}")

    def check_battery(self):
        print(f"Battery level is {self.battery_level}")

# creating a smartphone instance
Phone = Smartphone('Samsung', 'S8+', 'black')
print(Phone.brand)
print(Phone.model)
print(Phone.colour)
Phone.make_call('+2347039493584')
Phone.send_message('+2347039493584', 'Hello World')
Phone.check_battery()

#  inheritance example
class SmartPhonePro(Smartphone):
    def __init__(self, brand, model, colour, storage):
        super().__init__(brand, model, colour)
        self.storage = storage

    def check_storage(self):
        print(f'My phone has a storage of {self.storage}')

phonePro = SmartPhonePro('Samsung', 'S8+', 'Black', '68GB')  
phonePro.check_storage() 