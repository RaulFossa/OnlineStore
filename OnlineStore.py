# Online Store!
# raul_andres 12/12/2015
# This is a simple program using arrays, loops and more!
# Welcome to the OnlineStore

def thankyou():
    print("Thank you for shopping with us")
def main():
    thankyou()

item_name = []
quantity = []
cost_per_item = []
sub_totals = []
total_purchase = []

print(" ")
print("Welcome to the Online Store!")
print(" ")

x = 0
item_name.append(input("Please enter the name of your item: "))

while item_name[x].upper() != "NONE" :
    quantity.append(int(input("How many of this " + item_name[x] + " are you buying? ")))
    cost_per_item.append(float(input("Please enter the price per item: $")))
    x += 1
    print(" ")
    item_name.append(input("Please enter the name of your item: "))
    
y = 0
while y < x:
    sub_totals.append(quantity[y] * cost_per_item[y])
    y += 1

print(" ")
print("Item\tCost\tQty.\tSubTotal")
x = 0
while x < y:
    print(item_name[x],'\t',cost_per_item[x],'\t', quantity[x],'\t', sub_totals[x])
    x += 1

print(" ")
total_purchase = sum(sub_totals)
print("The total amount for this purchase is: $", total_purchase, "\n")

cost_w_ship = 0
location = input("Are you shipping to the USA or CANADA? ")

if location.upper() == "USA" :
    if total_purchase > 0 and total_purchase <= 50 :
       cost_w_ship = total_purchase + 10.95
       print("Your total with delivery right to your door is: $", cost_w_ship, "Dollars")

    elif total_purchase > 50 and total_purchase <= 100 :
        cost_w_ship = total_purchase + 14.95
        print("Your total with delivery right to your door is: $", cost_w_ship, "Dollars")

    elif total_purchase > 100 :
        cost_w_ship = total_purchase + 0
        print("CONGRATULATIONS! Enjoy Free Shipping.")


if location.upper() == "CANADA" :
    if total_purchase > 0 and total_purchase <= 50 :
       cost_w_ship = total_purchase + 10.95
       print("Your total with delivery right to your door is: $", cost_w_ship, "Dollars")

    elif total_purchase > 50 and total_purchase <= 100 :
        cost_w_ship = total_purchase + 14.95
        print("Your total with delivery right to your door is: $", cost_w_ship, "Dollars")

    elif total_purchase > 100 :
        cost_w_ship = total_purchase + 0
        print("CONGRATULATIONS! Enjoy Free Shipping.")




print(" ")

main()

















