import json
import string
import random
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists() :
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("there is no such file present")
    except Exception as err:
        print(f"exception occured: {err}")

    @classmethod    
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __generateAccNo(cls):
        digit = random.choices(string.digits, k=3)
        char = random.choices(string.ascii_letters, k=2)
        spchar = random.choices('!@#$&', k=1)
        id = digit + char + spchar
        random.shuffle(id)   
        return "".join(id)       

    def createAccount(self):
        info = {
            "name" : input("enter your name: "),
            "age" : int(input("enter your age: ")),
            "email" : input("enter your email id "),
            "pin" : int(input("enter your 4 digit pin no. ")),
            "account_no" : Bank.__generateAccNo(),
            "balance" : 0
        }

        if info['age']<=18 and len(info['pin']) != 4:
            print("sorry we can't create this account")
        else:
            print("your account is created succesfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("note down account no.")

            Bank.data.append(info)

            Bank.__update()

    def depositMoney(self):
        accNo = input("Enter your acc no. ")
        pin = input("Enter your pin no. ")

        userData = [i for i in Bank.data if i['account_no'] == accNo and str(i['pin']) == pin]

        if not userData:
            print("Account no or pin is invalid")
        else:
            amount = int(input("Enter money to deposit"))
            if(amount <= 0):
                print("Amount value is invalid")
            else:
                userData[0]['balance'] += amount
                Bank.__update()
                print("Amount is deposited successfully")

    def withdraw(self):
        accNo = input("Enter your acc no ")
        pin = input("Enter yout pin no ")

        userData = [i for i in Bank.data if i['account_no'] == accNo and str(i['pin']) == pin]

        if not userData:
            print("Account no. or pin is invalid")
        else:
            amount = int(input("Enter amount to withdraw"))
            if(amount > userData[0]['balance'] and amount <= 0):
                print("invalid amount")
            else:
                userData[0]['balance'] -= amount
                Bank.__update()
                print(f'{amount} is withdraw successfully')

    def details(self):
        accNo = input("Enter your acc no ")
        pin = input("Enter yout pin no ")

        userData = [i for i in Bank.data if i['account_no'] == accNo and str(i['pin']) == pin]

        for i in userData[0]:
            print(f"{i}: {userData[0][i]}")

    def updatedetails(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin aswell "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("no such user found ")
        
        else:
            print("you cannot change the age, account number, balance")

            print("Fill the details for change or leave it empty if no change")

            newdata = {
                "name": input("please tell new name or press enter : "),
                "email":input("please tell your new Email or press enter to skip :"),
                "pin": input("enter new Pin or press enter to skip: ")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']
            
            newdata['age'] = userdata[0]['age']

            newdata['accountNo.'] = userdata[0]['accountNo.']
            newdata['balance'] = userdata[0]['balance']
            
            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])
            

            for i in newdata:
                 if newdata[i] == userdata[0][i]:
                     continue
                 else:
                     userdata[0][i] = newdata[i]

            Bank.__update()
            print("details updated successfully")

    def delete(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin aswell "))

        userData = [i for i in Bank.data if i['account_no'] == accnumber and i['pin'] == pin]

        if not userData:
            print("no such usser found")
        else:
            check = input("press y if you actually want to delete the account or press n")
            if check == 'n' or check == "N":
                print("bypassed")
            else:
                index = Bank.data.index(userData[0])
                Bank.data.pop(index)
                print("account deleted successfully ")
                Bank.__update()



user = Bank()


print("Press 1 for creating an account")
print("Press 2 for Depositing money")
print("Press 3 for withdraw money")
print("Press 4 for details")
print("Press 5 for updating details")
print("Press 6 for deleting an account")


option = int(input("enter your choice "))

if option == 1:
    user.createAccount()

if option == 2:
    user.depositMoney()

if option == 3:
    user.withdraw()

if option == 4:
    user.details()

if option == 5:
    user.updatedetails()

if option == 6:
    user.delete()