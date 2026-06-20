balance = 10000   

def bank_transaction(account_holder, transaction_type="deposit", amount=0):
    global balance

    if transaction_type) == "deposit":
        balance += amount
        return f"{account_holder} deposited ₹{amount}. New Balance = ₹{balance}"

    elif transaction_type == "withdraw":
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




