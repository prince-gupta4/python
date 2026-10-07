class Phone:
    def call(self):
        print("Making a voice call...")

class Camera:
    def take_photo(self):
        print("Clicking a picture...")

## Single Inheritance
class SmartPhone(Phone):
    def browse_internet(self):
        print("Browsing the web")

# Multiple + Multilevel Inheritance
class AIPhone(SmartPhone, Camera):
    def use_ai(self):
        print("AI Smartphone")

my_device = AIPhone()
my_device.call()              
my_device.browse_internet()   
my_device.take_photo()        
my_device.use_ai()            