import time, os, sys
def typingPrint (text):
    for character in text: 
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.09)




typingPrint('Hello my name is Alex, your virtual assistant. I will help you order a pizza!\n')
typingPrint('I am going to ask you a few questions. After typing a response, please press enter.')

print("\n")

userName=input('Enter your name:  ')
while(len(userName) == 0):
    userName = input("Please enter your name: ")


if userName.lower() == "brianna carlisle": 
    typingPrint("I love that name!")
else:
    typingPrint("Nice to meet you!")

print("\n")

typingPrint("I know you're hungry, so let's get started! ")

print("\n")

size=input("What size pizza would you like? Please enter small, medium, or large.  ").lower()
while size!= "small" and size != "medium" and size != "large":
    size = input("Invalid value. Please enter small, medium, or large: ").lower()

print("\n")

flavor = input('Please enter the type of pizza you would like :  ')
while(len(flavor) == 0):
    flavor = input("Please enter a pizza flavor: ")

print("\n")

crustType = input('Please enter the type of crust you would like:  ')
while(len(crustType) == 0):
    crustType = input("Please enter pizza crust type: ")

print("\n")

quantity = input('Please enter the quantity of pizzas you would like. Please enter a numeric value:  ')
while(len(quantity) == 0):
   quantity = input("Please enter how many pizzas you would like:  ")
quantity=int(quantity)

print("\n")

method = input('Great! Will this be for carryout or delivery?  ')
while(len(method) == 0):
    method = input("Please choose carryout or delivery: ")


print("\n")


salesTax= 1.1
if size.lower()== "small":
    pizzaCost= 8.99
elif size.lower()== "medium":
    pizzaCost= 14.99
elif size.lower()== "large":
    pizzaCost= 17.99

if method.lower()== "delivery":
    deliveryFee= 5
else:
    deliveryFee= 0


total=( pizzaCost * quantity ) * salesTax + deliveryFee


print('\n-------------------------')

typingPrint('Thank you, ' + userName + ' for your order!') 
typingPrint(" The total for your ")
typingPrint (str(quantity))
typingPrint(" ")
typingPrint (str(size))
typingPrint(", ")
typingPrint (str(flavor))
typingPrint(" ")

if quantity >= 2:
   typingPrint("pizzas with ")
else:
    typingPrint("pizza with ")

typingPrint (str(crustType))
typingPrint(" comes: ")
typingPrint("${:,.2f}" .format (total) + ".")

print("\n")

typingPrint("We are currently preparing your order. It will be ready for " + method + " soon!")

print("\n")

if total >= 50 :
    print("Congratulations, you've earned a $10 coupon for you next order! ")

print("\n")

print("Your order has been received. ETA: 3 mins!")

for min in range (3, 1, -1):
   print(min, "minutes remaining")
   for seconds in range (60, 0, -1):
       print(seconds, end = " \r")
       import time 

print('\n')

typingPrint('Thank you for using Max, the virtual assistant. See you next time!')

print('\n')

print('-------------------------')

print("\n")

