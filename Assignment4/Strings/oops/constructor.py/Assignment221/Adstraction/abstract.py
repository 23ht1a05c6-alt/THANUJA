
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog (Animal):
    def sound(self):
        print("Bark")
d = Dog()
d.sound()





#problem4
#create an abstract claas payment gateway
#create an abstraction payment gate way
#pay refond amount parameter
#know create child class credit class payment
#and second class upi payment




from abc import ABC, abstractmethod
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    def refund(self,amount):
        pass
class creditCard(PaymentGateway):
    def pay(self,amount) :
        print("Credit Card Payment")
        print("Amount Refunded")
    def refund(self, amount): 
        print("Credit card refund") 
        print("Amount Refunded")

class UpIPay(creditCard):
    def  pay(self, amount):
        print("UPI Payment")
        print("Amount Paid")
    def refund(self, amount):
        print("UPI Refund")
        print("amount Refunded")
c = creditCard() 
c.pay(1000) 
c.refund(500)
u = UpIPay()
u.ppay()
u.refund(1000)     
 

       
#create abstract class restarent prepare food in online delivery 
#than create child class pizza, brgur shop
#food preparation time delivery time



