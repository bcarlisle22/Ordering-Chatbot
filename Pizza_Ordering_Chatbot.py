print('Hello my name is Alex, your virtual assistant. I will help you order a pizza!')
print('I am going to ask you a few questions. After typing an answer, please press enter.')
username=input('\n Enter your name:  ')
if username.lower() == "brianna carlisle": 
    print("\n That name sounds familiar.")
else:
    print("\n Nice to meet you!")

print("\n Well, I know you're hungry, so let's get started! ")
size=input("\n What size pizza would you like? Please enter small, medium, or large.  ")
flavor = input('\n Please enter the type of pizza you would like :  ')
crustType = input('\n Please enter the type of crust you would like :  ')
quantity = input('\n Please enter the quantity of pizzas you would like. Please enter a numeric value:   ')
quantity=int(quantity)
method = input('\n Great! Would this be for carryout or delivery?  ')

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
total=(pizzaCost * quantity ) * salesTax + deliveryFee
print('\n ------------------------')
print('\n Thank you, ' + username + ' for your order!') 
print("\n Your ", quantity, size, flavor + ' pizza with',  crustType, "crust costs:", "${:,.2f}" .format (total) + ".")
print("\n We are currently preparing your order. It will be ready for " + method + " soon!")
print('\n')
print('\n Thank you for using Max, the virtual assistant. See you next time!')
print('\n ------------------------')
