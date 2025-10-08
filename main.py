from pyscript import display
#Restaurant Order System (Pyton Data Types)


#string
restaurant_name = "PRNDL"
owner_name = "Kleiser Fermocil"

#integer
year_since = 2025

#float
tax_rate = 0.08

#boolean
has_delivery = True
is_dine_in = True
is_takeaway = False

#list
product_name = ["Burger", "Pizza", "Pasta", "Salad", "Soup"]
beverages = ["Coke", "Sprite", "Water", "Juice", "Tea"]

#tuple
business_hours = ("Monday to Friday", "10:00 AM to 10:00 PM")

#dictionary
menu = { 
    "Burger": 9.00,
    "Pizza": 11.00,
    "Pasta": 9.50,
    "Salad": 7.00,
    "Soup": 5.50,
    "Coke": 2.00,
    "Sprite": 2.00,
    "Water": 1.00,
    "Juice": 2.50,
    "Tea": 1.50
}

#Set
common_allergens = {"Nuts", "Dairy", "Gluten", "Soy", "Shellfish"}

# Displaying the restaurant information
display(f"{restaurant_name}", target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_since}", target="since")
display("Menu Pricelist", target="heading1")

#Display Menu Items
display(product_name[0], target="prod1")
display(f"${menu['Burger']:.2f}", target="price1")
display(product_name[1], target="prod2")
display(f"${menu['Pizza']:.2f}", target="price2")
display(product_name[2], target="prod3")
display(f"${menu['Pasta']:.2f}", target="price3")
display(product_name[3], target="prod4")
display(f"${menu['Salad']:.2f}", target="price4")
display(product_name[4], target="prod5")
display(f"${menu['Soup']:.2f}", target="price5")

display(beverages[0], target="prod6")
display(f"${menu['Coke']:.2f}", target="price6")
display(beverages[1], target="prod7")
display(f"${menu['Sprite']:.2f}", target="price7")
display(beverages[2], target="prod8")
display(f"${menu['Water']:.2f}", target="price8")
display(beverages[3], target="prod9")
display(f"${menu['Juice']:.2f}", target="price9")
display(beverages[4], target="prod10")
display(f"${menu['Tea']:.2f}", target="price10")

#Display Additional Information
display(f"Open: {business_hours[0]} {business_hours[1]}", target="openingHours")

#Display Order Type
display(f"Dine-in Available", target="orderType")
   