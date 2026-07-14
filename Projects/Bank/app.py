# main
if __name__ == "__main__":
    
    print("Welcome to the small scale bank")
    print("1. Register \n 2. Login")
    choice = int(input("Select Your choice:"))

    # calling register function
    if choice == 1:
        print("Registation Page Under Development Process....")

    # calling Login Function
    elif choice == 2:
        account = int(input("Enter Your Account Number:"))
        password = input("Enter Your Password:")
        login_val = login(account = account, password = password)

        while login_val:
            print("The small scale Bank Providing services")
            print("1. Balance \n 2. Withdraw \n 3. Deposite \n \
                   4. Transfer \n 5. Ministatement \n 6. Logout")
            choice = int(input("Enter your choice(1-6):"))

            if choice == 1:
                # call Balance Function
                current_balance = balance(account = account)
                print(f"Current Balance is:{current_balance}")

            elif choice == 2:
                amount = int (input("Enter your withdraw amount:"))
                # call withdraw function
                res = withdraw(account = account, withdraw_amount = amount)
                print(res)

            elif choice == 3:
                amount = int (input("Enter your deposite amount:"))
                # call deposite function
                res = deposite(account = account, deposite_amount = amount)
                print(res)

            elif choice == 4:
                reciever_amount = int(input("Enter your Reciever account number:"))
                amount = int(input("Enter Your Transfer amount:"))
                # call transfer function
                res = transfer(sender = account, reciever = reciever_amount, transfer_amount = amount)
                print(res)

            elif choice == 5:
                # call ministatement function 
                res = ministatement(account = account)
                print(res)
            elif choice == 6:
                # call logout function
                print(logout())
                exit()
            else:
                print("Invalid choice, select in between 1-6")
        print("Invaild Login Credentials")
    else:
        print("Invaild choice, select in between 1-2")


