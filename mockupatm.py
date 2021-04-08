
import random
database = {}
def init():
    print(' WELCOME TO PAY QUICK ATM CENTER ')
    from datetime import datetime
    now = datetime.now()
    date_String = now.strftime('%d/%m/%y %H:%M:%S')
    print(date_String)
    selectedOption = int(input('What would you like to do? (1) Login (2) Register (3) Exit  \n'))
    if selectedOption == 1:
        login()
    elif selectedOption == 2:
        register()
    elif selectedOption == 3:
        exit()
    else:
        print('Invalid option selected.')
        init()



def login():
    print('***** LOGIN *****')
    accountNumberFromUser = int(input('Enter Your Account Number:  \n'))
    userPassword = input('Enter Your Password: \n')

    for accountNumber, userDetails in database.items():
        if accountNumber == accountNumberFromUser:
            if userDetails == userPassword:
                print('Logged in successfully')
        else:
            print('Incorrect account number or password')
            login()
    print('Select an Option:')
    selectedOption2 = int(input('(1) Withdrawal (2) Cash Deposit (3) Complaint (4) Logout \n'))
    if selectedOption2 == 1:
         withdrawal()
    elif selectedOption2 == 2:
        cashDeposit()
    elif selectedOption2 == 3:
        complaint()
    elif selectedOption2 == 4:
        logout()
    else:
        print('Invalid Option Selected.')
        login()


def register():
    print('***** REGISTER *****')
    phoneNumber = int(input('Enter Your Phone Number: \n'))
    first_name = input('First Name: \n')
    last_name = input('Last Name: \n')
    password = input('Create Your Password: \n')

    newAccountNumber = accountNumberGenerator()
    print('***************************')
    print('Dear', first_name, last_name,', your account has been succesfully created')
    print('Your account number is', newAccountNumber)
    login()


def withdrawal():
    withdraw = input('How much would you like to withdraw?: \n')
    print('Take your cash')

def cashDeposit():
    makeADeposit = input('How much would you like to deposit?: \n')
    print('Your current balance is %s' %makeADeposit)

def complaint():
    report = input('What issue will you like to report?: ')
    print('Thank you for contacting us.')

def accountNumberGenerator():
    return random.randrange(1111111111,9999999999)

def logout():
    init()

init()
