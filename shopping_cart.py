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
            #Tried to use a break instead of count but the break didn't seem to be working
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