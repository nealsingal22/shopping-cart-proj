# Shopping Cart Project

## Installation
Use the GitHub.com online interface to create a new remote project repository called something like "shopping-cart-proj". Also add a "README.md" file during the repo creation process. After this process is complete, you should be able to view the repo on GitHub.com at an address like https://github.com/YOUR_USERNAME/shopping-cart-proj.

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

```sh
cd ~/Desktop/shopping-cart-proj
```
Use your text editor or the command-line to create a file in that repo called "shopping_cart.py", and then place the following contents inside:

```sh
import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#Used screencast to develop the structure of the code

total_price = 0
selected_ids = []

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

#Handles Invalid Inputs
def check_valid_input(product_id):
    count = 0
    for num in range(1, len(products)+1):
        if (str(num) == str(product_id)):
            selected_ids.append(product_id)
            count += 1
    if count == 0:
        new_id = input("Hey, are you sure that product identifier is correct? Please try again: ") 
        check_valid_input(new_id)

while True:
    product_id = input("Please input a product identifier or DONE when you are finished: ")
    if product_id == "DONE":
        break
    else:
        check_valid_input(product_id)

print("                      ")
print("----------------------------------")
print("NEALS GROCERY EMPORIUM")
print("WWW.NEALS-GROCERY-EMPORIUM.COM")

# Source Code: https://stackoverflow.com/questions/1759455/how-can-i-account-for-period-am-pm-using-strftime
now = datetime.datetime.now()
time = now.strftime("%I:%M %p")
day = datetime.date.today()

print("----------------------------------")
print("CHECK OUT AT: " +str(day) + " " + time)
print("----------------------------------")
print("SELECTED PRODUCTS: ")

for product_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(product_id)]
    matching_product = matching_products[0]
    total_price += matching_product["price"]
    print ("... " + matching_product["name"] + " " + "(" + to_usd(matching_product["price"]) + ")" )

print("----------------------------------")
print("SUBTOTAL: " +to_usd(total_price))
#DC Tax Rate from Internet: http://www.tax-rates.org/district_of_columbia/sales-tax
tax_rate = .0575
tax = total_price*tax_rate
print("TAX: "+ to_usd(tax))

#total payment due
final_price = to_usd(tax + total_price)
print("TOTAL: " + final_price)
print("----------------------------------")
print("THANKS FOR SHOPPING, SEE YOU AGAIN SOON!")
print("----------------------------------")
```

## Setup
Create and activate a new Anaconda virtual environment:

```sh
conda create -n shopping-env python=3.7 # (first time only)
conda activate shopping-env
```

## Usage
In order to run the program and successfully use it please enter the 
follwing in your command line promopt:

```sh
python shopping_cart.py
```
At this point your code should be running and the program should be working.
The code can be broken down into the following sections to make it easier to understand:
1) Products dictionary contains all the items available at the grocery store
2) to_usd coverts a price to the proper format with a $ sign
3) chech_valid_input makes sure the product id exists in the products dictionary
and if it doesn't asks the user to try again
4) Print the header of the receipt along with a time using the datetime function
5) Loop through all the selected ids and print their name and price
6) Print subtotal, tax, total, and a friendly message to come shop again

