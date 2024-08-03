# movie ticket discount
ticket_price = 0
discount = 0

age = int(input("Enter your age :"))
if age>=10 and age<=12:
    ticket_price = 5
elif age>=12 and age<=18:
    ticket_price = 7
elif age>=18 and age<=64:
    ticket_price = 12
elif age>=65:
    ticket_price = 7

day= input("Enter the day =")
if day == "saturday" or day == "sunday":
    discount = 10
else:
    print(ticket_price)

sum = ticket_price*discount/100
bp=ticket_price-sum

print(f"Base price = ${bp}")

