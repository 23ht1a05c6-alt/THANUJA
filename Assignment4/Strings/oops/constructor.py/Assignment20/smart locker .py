class   SmartLocker:
    def __init__(self,locker_id, owner_name, pin):
        self.lockr_id = locker_id
        self.owner_name = owner_name
        self.__pin = pin
        self.__access_count = 0
    def access_locker(self, entered_pin):
        if entered_pin == self.__pin:
            self.__access_count +=1
            print("Access granted")
        else:
            print("Invalid PIN") 
    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            print("PIN change successfully") 
        else:
            print("incorrect old PIN") 
    def show_details(self):
        print(f"lockerID: {self.locker_id}") 
        print(f"owner:{self.owner_name}")  
        print(f"accesscount:{self.__access_count}")
    locker_id, owner_name, pin = input().split()
    locker = SmartLocker(locker_id, owner_name,pin)
    q = int(input())  
    for _ in range(q):
        operation = input().split()
        
    if operation[0] == "ACCESS":
        locker.access_locker(operation[1]) 
    elif operation[0] == "CHANGE":
        locker.changr_pin(operation[1],operation[2]) 
    elif operation[0] == "DEtAIlS": 
        locker.show_details()                             
        


