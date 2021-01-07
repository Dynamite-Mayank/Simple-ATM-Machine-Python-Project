import time
m=-1
while m<=-1:
    name=input("Enter Your Name: ")
    print("Hi,",name,"Welcome to SBI Bank Atm")
    m=2
    count=0
    while m>=0:
        pin=int(input("Enter your Pin Number: "))
        if(pin<1000 or pin>9999):
            print("""Invaild Pin Try again....
            You have""",m,"""more chances left to Enter your correct Pin""")
            m-=1
            count+=1
            if m==0:
                print("You have Enter wrong Pin",count,"times")
                print("Your have been blocked for 25 seconds...Please Wait")
                time.sleep(25)
                
            elif m==-1:
                time.sleep(5)
                print("""Request Fail Try after some time
            Please wait for 10 sec...We are redirected to Start Window""")
                time.sleep(10)
        else:
            break
    m=m
balance=10000.00
while True:
    print("""
Welcome to SBI ATM
1. CASH WITHDRAWAL
2. BALANCE CHECK
3. DEPOSIT
4. Exit""") 
    c=int(input("Please Enter your choice: "))
    if(c==1):
        while True:
            print("""
1. CURRENT ACCOUNT
2. SAVING ACCOUNT
3. GO BACK""")
            c1=int(input("Please choose your Account type: "))
        #while True:
            if(c1==1):
                while True:
                    print("")
                    amt=float(input("Enter amount(Should be multiple of 100): "))
                    if amt<=0:
                        print("Your transaction is in process...Please wait")
                        time.sleep(2)
                        print("Invalid Amount...Please Enter Amount again")
                        time.sleep(2)
                    elif amt>balance:
                        print("Your transaction is in process...Please wait")
                        time.sleep(5)
                        print("Sorry Insufficient Balance in your Account...Transaction Failed")
                        time.sleep(2)
                        break
                    elif amt>0 and amt<=balance and amt%100==0:
                        balance=balance-amt
                        print("Your transaction is in process...Please wait")
                        time.sleep(5)
                        print("Hi,",name,"You have succesfully withdrawal Rs.",amt)
                        time.sleep(2)
                        break
                    else:
                        print("Your transaction is in process...Please wait")
                        time.sleep(2)
                        print("Entered amount is not a Multiple of 100")
                        time.sleep(2)
                break
            elif c1==2:
                while True:
                    print("")
                    amt=float(input("Enter amount(Should be multiple of 100): "))
                    if amt<=0:
                        print("Your transaction is in process...Please wait")
                        time.sleep(2)
                        print("Invalid Amount...Please Enter Amount again")
                        time.sleep(2)
                    elif amt>balance:
                        print("Your transaction is in process...Please wait")
                        time.sleep(5)
                        print("Sorry Insufficient Balance in your Account...Transaction Failed")
                        time.sleep(2)
                        break
                    elif amt>0 and amt<=balance and amt%100==0:
                        balance=balance-amt
                        print("Your transaction is in process...Please wait")
                        time.sleep(5)
                        print("Hi,",name,"You have succesfully withdrawal Rs.",amt)
                        time.sleep(2)
                        break
                    else:
                        print("Your transaction is in process...Please wait")
                        time.sleep(2)
                        print("Entered amount is not a Multiple of 100")
                        time.sleep(2)
                break
            elif c1==3:
                print()
                break
            else:
                print("Invaild Input")
    elif c==2:
        print("")
        print("We are fetching Your Balance...Please Wait")
        time.sleep(5)
        print("Hi,",name,"Your current Balance is Rs.",balance)
    elif c==3:
        while True:
            print("")
            amt=int(input("Enter amount(should be multiple of 100): "))
            if amt<=0:
                print("Invalid Amount...Please Enter Amount again")
                time.sleep(2)
            elif amt>0 and amt%100==0:    
                balance=balance+amt
                print("Please wait...We are depositing Your amount")
                time.sleep(5)
                print("Hi,",name,"Your amount has been succesfully Deposited")
                break
            else:
                print("Please wait...")
                time.sleep(2)
                print("Entered amount is not a Multiple of 100")
                time.sleep(2)
    elif c==4:
        print()
        print(name,",Thanks for using SBI Bank ATM")
        break
                
    else:
        print("Invaild Input")

    
    
    
    
    

