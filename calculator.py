def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

while True:
     print("please press the keys")
     print("\t1. ADD\n\t2. SUB\n\t3. MUL\n\t4. DIV")
     choice = input("enter the choice :")
      
     num1 = int(input("enter the number: "))
     num2 = int(input("enter the number: "))
      
     if choice == '1':
      a = add(num1, num2)
      print(f"Addition of {num1} and {num2} is {a}")
         
     elif choice == '2':
      a = sub(num1 , num2)
      print(f"Substraction of {num1} and {num2} is {a}")
      if a > 0:
          print("Your answer is Positive")
      elif a == 0:
          print("Your answer number is Zero")
      else :
          print("Your answer number is Negative")

     elif choice == '3':
      a = mul(num1, num2)
      print(f"Multiplication of {num1} and {num2} is {a}")
      
     elif choice == '4':
       if num2 == 0:
        print("\tDIVIDE BY 0 NOT ALLOWED...")
        print("\t\tTRY AGAIN....THANK YOU")
       else:
         d = div(num1, num2)
         print(f"Division of {num1} and {num2} is {d}")
         
         if d > 0:
            print("Your answer is Positive")
         elif d == 0:
            print("Your answer is Zero")
         else :
            print("Your answer is Negative")

     else:
       print("\t\tINVALID CHOICE")


 
     ch = input("do you wish to continue? ==> Y/N :")
     if ch in ('Y','y','yes','YES','Yes'):
         continue
     else:
        print("Thanks for using our calculator")
        break
         
      
     
