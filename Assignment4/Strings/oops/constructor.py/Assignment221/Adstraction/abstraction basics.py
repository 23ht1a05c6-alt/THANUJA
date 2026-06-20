#abstraction
#the fuctionalilty is same
#show in the esstional features
#definiton:
#we will never know how oeartion will work internal 
#what opeartion is done
#its hidis internal application
#why use abstracion?
#it reduse the complexity
#improves the security
#better maintances
#claer code
#standorization
#how to implement?
#python supports abstraction usess abstraction class, abstraction method
#module is calss is aclld as 'ABC' method means:
#abstraction base class
#abstraction class means bule of the class
#w cannot create object in this class
#use of abstraction class?
#basic commom structure
#it can have abstraction method common method
#what is abstrction method
#we can declare method but implemention is not providing 
#example;
#yechile:
#start botton same for  methods


from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def Sound(self):
        pass
class Dog (Animal):
    def sound(self):
        print("Bark")
d = Dog()
d.sound()              
