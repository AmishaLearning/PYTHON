
# def calculate_total(cart_items):
#     total_amount = 0.0

#     for item in cart_items:
#         product_name = item['name']
#         unit_price = item['unit_price']
#         quantity = item['quantity']

#         total_amount += unit_price * quantity

#     return total_amount


# cart_items = [
#     {'name': input("Enter the Product Name : "), 'unit_price': int(input("Enter the amount : ")), 'quantity': int(input("Enter the quantity : "))}
#     # {'name': 'Gadget', 'unit_price': 5.49, 'quantity': 2},
#     # {'name': 'Doodad', 'unit_price': 2.99, 'quantity': 4},
# ]
  
# total_amount = calculate_total(cart_items)
# print("The total amount is {}.".format(total_amount))






def calculate_total_amount(products):
    total_amount = 0

    for product in products:
        product_name, unit_price, quantity = product
        product_total = unit_price * quantity
        total_amount += product_total
   
    print("The Total Amount in Cart is {}. ".format(total_amount))
    return total_amount

def get_product_details():
    try:
        product_name = input("Enter product name: ")
        unit_price = float(input("Enter unit price: "))
        quantity = int(input("Enter quantity: "))
        return product_name, unit_price, quantity
    
    except Exception as e:
        print("Getting Product details failed due to :: ", e)   
        return     

def main():
    cart = []
    num_rows = int(input("Enter the Number of Products in cart :"))

    for x in range(num_rows):
        product = get_product_details()
        cart.append(product)

    if None not in cart:
        calculate_total_amount(cart)
    else:
        print("Some of the details in the cart are invalid. Please enter correct details")

if __name__ == "__main__":
    main()