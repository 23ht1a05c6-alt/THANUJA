class InvalidAddressError(Exception):
    pass

class EcommerceAddress:

    def __init__(self, customer, delivery, payment):
        self.customer = customer
        self.delivery = delivery
        self.payment = payment

    def validate(self):
        if len(self.customer.strip()) < 5:
            raise InvalidAddressError("Invalid Customer Address")

        if len(self.delivery.strip()) < 5:
            raise InvalidAddressError("Invalid Delivery Address")

        if len(self.payment.strip()) < 5:
            raise InvalidAddressError("Invalid Payment Address")

        print("All addresses are valid")
        print("Customer Address :", self.customer)
        print("Delivery Address :", self.delivery)
        print("Payment Address :", self.payment)

try:
    customer = input("Enter Customer Address: ")
    delivery = input("Enter Delivery Address: ")
    payment = input("Enter Payment Address: ")

    obj = EcommerceAddress(customer, delivery, payment)
    obj.validate()

except InvalidAddressError as e:
    print("Error:", e)





'''
Student Result Processing

Exceptions:

Marks < 0 → NegativeMarksError
Marks > 100 → MarksExceedError
Non-numeric input → ValueError
2. Bank Account Withdrawal

Exceptions:

Withdrawal amount > balance → InsufficientBalanceError
Negative withdrawal amount → InvalidAmountError
3. ATM System

Exceptions:

Wrong PIN → InvalidPinError
Withdrawal exceeds balance → InsufficientFundsError
4. Login System

Exceptions:

Username contains digits/special characters → InvalidUsernameError
Username not found → UserNotFoundError
5. Product Inventory Management

Exceptions:

Invalid product index → InvalidProductIndexError
Requested quantity exceeds stock → OutOfStockError
6. Employee Salary Management

Exceptions:

Salary < 0 → InvalidSalaryError
Employee ID not found → EmployeeNotFoundError
7. E-commerce Order Processing

Exceptions:

Empty delivery address → InvalidAddressError
Payment amount ≤ 0 → InvalidPaymentError
8. Library Management System

Exceptions:

Book not available → BookNotAvailableError
Invalid member ID → InvalidMemberError
9. Online Exam System

Exceptions:

Marks out of range (0–100) → InvalidMarksError
Student absent → StudentAbsentError
10. Parking Management System

Exceptions:

Invalid vehicle number → InvalidVehicleError
Parking hours ≤ 0 → InvalidParkingHoursError
11. Electricity Bill Calculator

Exceptions:

Units < 0 → InvalidUnitsError
Non-numeric units → ValueError
12. Ticket Booking System

Exceptions:

Seats not available → SeatNotAvailableError
Invalid seat number → InvalidSeatError
Generic Exception Handling Structure
class CustomError(Exception):
    pass

try:
    # input and logic
    if condition:
        raise CustomError("Error Message")

except ValueError:
    print("Invalid Input")

except CustomError as e:
    print(e)

finally:
    print("Program Ended")

These are the most frequently asked Exception Handling + OOP interview/exam problems.

'''



