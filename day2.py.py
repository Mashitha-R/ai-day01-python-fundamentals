#CONDITIONAL STATEMENT

####    IF ELSE  


#example 1
a=13
#if a>10:
    #print('I Will do task A')
#else:
   # print('I Will do task B')

#b=6
#if b>10:
    #print('I Will do task A')
#else:
    #print('I Will do task B')

#example 2
#money=int(input(("PLEASE PROVIDE MONEY:- ")))
#if money==2000:
    #print("I WILL LEARN JAVA")
#else:
    #print("I will learn ML")




####       if-elif-ese


#money=int(input(("PLEASE PROVIDE MONEY:- ")))
#if money==10:
    #print("I WILL BUY chocobar")
#elif money==20:
   # print("I will buy Mango dolly")
#elif money==1000:
   # print("I WILL BUY STOCK")
#else:
   # print("I will buy cone")



###            
# REVISION

#          Accept two numbers and print the greatest b/w them
#num1=int(input("PLEASE TELL YOUR NUMBER "))
#num2=int(input("PLEASE TELL YOUR NUMBER "))
#if num1>num2:
 #   print(f"{num1} is greater than {num2}")

#elif num2>num1:
 #   print(f"{num2} is greater than {num1}"
  #        )
#else:
 #   print("both are equal")



#revision 2
""" accept the gender from the user as chart and 
   print the respective greeting message
   ex:- Good morning sir(on the basis of gender)"""


#g=input("PLEASE PROVIDE GENDER:(Male or Female) :-  ")
#if g=="female":
 #   print("Good morning Mam")
#elif g=="Male":
 #   print("Good morning Sir")
#else:
 #   print("wrong input")


#revision
"""Accept an integer and check whether it is an even number or odd  """
#a=int(input("provide a number "))
#if a%2==0:
 #   print("it is an even number")
#else:
 #   print("it is an odd number")


#revision
"""Accept name and age from the use.
Check if the user is a valid voter or not """
#name=input("please provide name: ")
#age=int(input("please provide age:  "))
#if age>=18:
 #   print(f"{name} your eligible")
#else:
 #   print(f"{name} you are not elligible")

#
""" Accept a year and check if it is a leap year or not"""
#y=int(input("PLEASE PROVIDE YEAR:- "))
#if y%100==0 and y%400==0:
 #   print("its leap year")
#elif y%100!=0 and y%4==0:
 #   print("its leap year")
#else:
 #   print("its not leaap year")


""" take the input of temperature in celsius"""
temp=int(input("PROVIDE TEMPERATURE"))
if temp<0:
    print("FREEZING COLD")
elif temp>=0 and temp<10:
    print("VERY COLD")
elif temp>=10 and temp<20:
    print("COLD")
elif temp>=20 and temp<30:
    print("PLEASANT")
elif temp>=30 and temp<40:
    print("HOT")
else:
    print("VERY HOT")








