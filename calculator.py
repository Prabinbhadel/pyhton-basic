def add(x,y):
    return x+y;
def subtract(x,y):
    return x-y;
def multipy(x,y):
    return x*y;
def division(x,y):
    return x/y;
while True:
    try:
      choice=int(input(" 1:addition \n 2:subtraction \n 3:multiplication \n 4:division \n 5: quit \n enter the operation you want to perform(1/2/3/4/5)"))
      if choice==1:
        a=int(input("enter the first number: "))
        b=int(input("enter the second number: "))
        sum=add(a,b)
        print(f"the sum of {a} and {b} is {sum}")
      elif choice==2:
        a=int(input("enter the minuend: "))
        b=int(input("enter the subtrahend: "))
        difference=subtract(a,b)
        print(f"the difference of {a} and {b} is {difference}")
      elif choice==3:
        a=int(input("enter the first number: "))
        b=int(input("enter the second number: "))
        product=multipy(a,b)
      elif choice==4:
        a=int(input("enter the dividend: "))
        b=int(input("enter the divisor: "))
        try:
          quotient=division(a,b)
          print(f"the quotient of{a} and {b} is {quotient}")
        except ZeroDivisionError as e:
          print(f"the divisor cannot be zero")
      elif choice==5:
         break
    
      else:
       print("enter the valid option")
    except Exception as e:
     print("enter the valid option")




