import hashlib
import random


class BankingUpdate:
    def __init__(self, name, age, balance, account_number, phone_number, gender, category, login_name, hashed_password):
        self.name = name
        self.age = age
        self.balance = balance
        self.account_number = account_number
        self.phone_number = phone_number
        self.gender = gender
        self.category = category
        self.login_name = login_name
        self.hashed_password = hashed_password


MAX_NAME = 100
banking_updates = []


def generate_random():
    num1 = random.randint(1000000, 9999999)
    num2 = random.randint(10000000, 99999999)
    return num1 * 10000000 + num2


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def add_account():
    if len(banking_updates) >= MAX_NAME:
        print("SIZE NOT SUPPORTED!")
        return

    name = input("ENTER YOUR NAME: ")
    gender = input("ENTER YOUR GENDER (M/F): ")
    category = input("ENTER YOUR CATEGORY: ")

    try:
        age = int(input("ENTER YOUR AGE: "))
    except ValueError:
        print("Invalid age input.")
        return

    if age < 18:
        print("AGE MUST BE AT LEAST 18 YEARS!\nCANNOT ADD USER")
        return

    try:
        phone_number = int(input("ENTER YOUR PHONE NUMBER: "))
    except ValueError:
        print("Invalid phone number input.")
        return

    if len(str(phone_number)) != 10:
        print("Invalid phone number. Please enter a 10-digit number.")
        return

    login_name = input("ENTER USERNAME: ")
    password = input("ENTER A PASSWORD: ")
    hashed_password = hash_password(password)

    try:
        balance = int(input("ENTER THE AMOUNT YOU WANT TO DEPOSIT: "))
    except ValueError:
        print("Invalid deposit amount.")
        return

    account_number = generate_random()

    new_account = BankingUpdate(name, age, balance, account_number, phone_number, gender, category, login_name,
                                hashed_password)
    banking_updates.append(new_account)

    print(f"ACCOUNT NUMBER: {account_number}")
    print("ACCOUNT CREATED SUCCESSFULLY!")


def fetch_data():
    user_name = input("ENTER USERNAME: ")
    password = input("ENTER YOUR PASSWORD: ")
    hashed_password_input = hash_password(password)

    for account in banking_updates:
        if account.login_name == user_name and account.hashed_password == hashed_password_input:
            print("ACCOUNT FOUND!")
            print(f"NAME: {account.name}")
            print(f"GENDER: {account.gender}")
            print(f"CATEGORY: {account.category}")
            print(f"AGE: {account.age}")
            print(f"PHONE NUMBER: {account.phone_number}")
            print(f"BALANCE: {account.balance}")
            if account.balance < 1500:
                print("Sufficient balance is not maintained!")
            return

    print("WRONG USERNAME OR PASSWORD. TRY AGAIN!")


def update_balance():
    user_name = input("ENTER USERNAME: ")
    password = input("ENTER YOUR PASSWORD: ")
    hashed_password_input = hash_password(password)

    for account in banking_updates:
        if account.login_name == user_name and account.hashed_password == hashed_password_input:
            try:
                deposit_amount = int(input("ENTER THE DEPOSIT AMOUNT: "))
            except ValueError:
                print("Invalid deposit amount.")
                return

            account.balance += deposit_amount
            print("AMOUNT CREDITED SUCCESSFULLY!")
            print(f"NEW BALANCE: {account.balance}")
            return

    print("ACCOUNT NOT FOUND. PLEASE TRY AGAIN.")


def withdrawal():
    user_name = input("ENTER USERNAME: ")
    password = input("ENTER YOUR PASSWORD: ")
    hashed_password_input = hash_password(password)

    for account in banking_updates:
        if account.login_name == user_name and account.hashed_password == hashed_password_input:
            try:
                withdrawal_amount = int(input("ENTER THE WITHDRAWAL AMOUNT: "))
            except ValueError:
                print("Invalid withdrawal amount.")
                return

            if account.balance >= withdrawal_amount:
                account.balance -= withdrawal_amount
                print("AMOUNT DEBITED SUCCESSFULLY!")
                print(f"NEW BALANCE: {account.balance}")
            else:
                print("INSUFFICIENT BALANCE!")
            return

    print("ACCOUNT NOT FOUND. PLEASE TRY AGAIN.")


def main():
    while True:
        print("\nWELCOME")
        print("1) ADD USER")
        print("2) CHECK BALANCE")
        print("3) DEPOSIT")
        print("4) WITHDRAWAL")
        print("5) EXIT!")

        try:
            choice = int(input("ENTER YOUR CHOICE: "))
        except ValueError:
            print("INVALID INPUT!")
            continue

        if choice == 1:
            add_account()
        elif choice == 2:
            fetch_data()
        elif choice == 3:
            update_balance()
        elif choice == 4:
            withdrawal()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("INVALID INPUT!")


if __name__ == "__main__":
    main()
