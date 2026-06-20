def find_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

print(find_sum(10, 20, 30))




#print should display
#canot reuse
#return statements
#define values
#can  reuse
#muliple return values


3calculate return a=b a-b a/b a*b
tuple formate 




#create a function bank transaction abbount hoder name transcation type
#deposite or withdraw  howmuch money
#t#hings useing golbal balance default  return ststements by useing this




balance = 10000   # Global balance

def bank_transaction(account_holder, transaction_type="deposit", amount=0):
    global balance

    if transaction_type.lower() == "deposit":
        balance += amount
        return f"{account_holder} deposited ₹{amount}. New Balance = ₹{balance}"

    elif transaction_type.lower() == "withdraw":
        if amount <= balance:
            balance -= amount
            return f"{account_holder} withdrew ₹{amount}. New Balance = ₹{balance}"
        else:
            return "Insufficient Balance"

    else:
        return "Invalid Transaction Type"


print(bank_transaction("Tanu", "deposit", 5000))
print(bank_transaction("Tanu", "withdraw", 3000))
print(bank_transaction("Tanu", "withdraw", 15000))