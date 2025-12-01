🧾 Account Class – Debit & Credit Operations

This Python program defines a simple Account Management System using Object-Oriented Programming (OOP).
It allows you to debit, credit, and check balance for a bank account.

🔍 Features

Create an account with:

Initial balance

Account number

Debit an amount from the account
→ Automatically updates balance and prints transaction details

Credit an amount into the account
→ Updates balance and shows remaining balance

Get current balance anytime using a method

📌 How It Works

An Account class is created with:

__init__() for initializing balance and account number

debit() method to subtract money

credit() method to add money

get_balance() method to retrieve the updated balance

An object emp1 is created:

emp1 = Account(10000, 1245698)


A debit operation is performed:

emp1.debit(6000)


A credit operation is performed:

emp1.credit(8000)

📤 Sample Output
rs. 6000 was debited
balance left: 4000
rs. 8000 was credited
balance left: 12000

✅ Use Case

Useful for beginners learning:

Python OOP

Classes and objects

Methods and data handling

Simple banking logic simulation
