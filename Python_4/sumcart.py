def calculate_total_amount(products):
    total_amount = 0
    discounted_amount = 0
    discount = float(input("Enter the discount : "))
    
    for product in products:
        product_name, unit_price, quantity = product
        product_total = unit_price * quantity
        total_amount += product_total
        
    discounted_amount = total_amount -((total_amount * discount)/100)
        
    print("The Total Amount in Cart is {}. ".format(total_amount))
    print("The Total Amount in Cart after discount is  {}. ".format(discounted_amount))
    
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
        # print(cart)
        product = get_product_details()
        cart.append(product)
    # print("The final cart is : ",cart)

    if None not in cart:
        calculate_total_amount(cart)    
    else:
        print("Some of the details in the cart are invalid. Please enter correct details")

if __name__ == "__main__":
    main()