print('Hello my name is Alex, your virtual assistant. I will help you order a pizza!')
print('I am going to ask you a few questions. After typing an answer, please press enter.')

userName=input('Enter your name:  ')
while(len(userName) == 0):
    userName = input("Please enter your name: ")


if userName.lower() == "brianna carlisle": 
    print("I love that name!")
else:
    print("Nice to meet you!")

print("\n")

print("I know you're hungry, so let's get started! ")

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


print('\n ------------------------')

print('Thank you, ' + userName + ' for your order!') 
print("Your ", quantity, size, flavor + ' pizza with',  crustType, "crust costs:", "${:,.2f}" .format (total) + ".")
print("We are currently preparing your order. It will be ready for " + method + " soon!")

print('\n')

print('Thank you for using Max, the virtual assistant. See you next time!')
print('------------------------')
