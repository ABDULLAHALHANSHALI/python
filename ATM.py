import time

print("please insert ypur card")

password=1234

 Pin = int(input("enter your atm pin"))
 balance = 5000
 if pin==password:
   print("""
   1 == balance
   2 == withdrow
   3 == deposite
   4 == exit
   """
         )
   try:
       option=int(input("enter your option"))
 except:
print("enter valid option")

if option==1:
    print(f"current balance {balance}")
    if option == 2:
        withdraw_amount = int(input("please enter your withdrow_amount"))
   balance=balance=withdrow_amount

   print("{withdrow_amount} debited from your account")

   print("your uptated balance {balance}")

   if option==3:
  deposite_amount=int(input("please enter deposite_amount"))

balance=balance+deposite_amount

  print("{withdrow_amount} is  credited to your account")

print(f"your uodated balance is {balance}")
if option==4:
    break





 else:
     print("wrong pin Please try again")
