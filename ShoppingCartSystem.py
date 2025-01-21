Product = {
    'Boys' : {
        'Shirt'     : '1500',
        'Pent'      : '1450',
        'Jacket'    : '1350',
        'Coat'      : '1990',
        'Jeans'     : '1270',
        'Lower'     : '1650',
        'Underwear' : '1540',
    },
    'Girls' : {
        'Shirt'     : '1500',
        'Pent'      : '1450',
        'Jacket'    : '1350',
        'Nighty'    : '1990',
        'Jeans'     : '1270',
        'Lower'     : '1650',
        'Shadi'     : '1650',
        'Suit'      : '1650',
        'Underwear' : '1540',
    }
}

Cart = []
Tamount = 0




print("====$-$----------WECOME SHOPPING CART SYSTEM------------$-$========")
print("\n")
print("\n_______________|  We have two department  |__________\n")


def depart():
    for i in Product.keys():
        print("\t\t|\t",i,"\t\t|")
    print("_________________________________________________________")
depart()


def Show_System(**kwargs):
    for keys,values in kwargs.items():
        print(f"\t\t{keys}\t\t:{values}")
# # Show_System(**Product)

def Amount(product_name, department):
    global Tamount
    Tamount += int(Product[department][product_name])  # Update Tamount globally
    print(f"\n\tAdded {product_name} (₹{Product[department][product_name]}) to your cart.")
    print(f"\tCurrent Total Price   : ₹{Tamount}\n")


def Total_price():
    print(f"\nFinal Total Price of items in the cart\t: {Tamount}")

def remove_Section(): 
    global Tamount
    product_name = input("Enter the product name to remove from your cart: ").capitalize()
    if product_name in Cart:
        Cart.remove(product_name)
        for dept in Product:
            if product_name in Product[dept]:
                Tamount -= int(Product[dept][product_name])  # Subtract the price
                break
        print(f"\n\tRemoved {product_name} from your cart.")
        print(f"\tCurrent Cart          : {Cart}")
        print(f"\tUpdated Total Price   : ₹{Tamount}\n")
    else:
        print("\tProduct not found in your cart.")


def greet():
    print('\nThankyou you came in "Akash Enterprices" Shop\n')
    print("====$-$----------CLOSED SHOPPING CART SYSTEM------------$-$========")

def Exit_Section():
    print("\n\tFinal Cart       :", Cart)
    if not Cart:
        print("\tYour cart is empty.")
    else:
        print(f"\tFinal Total Price : ₹{Tamount}")
    greet()




def View_Section():
        while True:
            department = input("\nEnter your Department ('Boys'/'Girls'): ").strip().title()
            if not department:
                pass
            elif department not in Product.keys():
                print("wrong input!!")
            else:    
                print(f"\n____________________|  {department}  |________________\n")
                if department in Product.keys():
                    Show_System(**Product[department])
                    
                else:
                    print("Invalid department. Please enter 'Boys' or 'Girls'.")
                    break
                print(f"\n______________________________________________________\n")
                break

# Updated AddCart_Section function
def AddCart_Section(): 
    global Tamount
    Rproduct_name = input("Enter the product name to add to your cart: ").capitalize()
    
    # Check if the product is in Boys' or Girls' section
    if Rproduct_name in Product["Boys"]:
        Cart.append(Rproduct_name)
        Tamount += int(Product['Boys'][Rproduct_name])  # Add the price of the product to Tamount
        print(f"\n\tAdded {Rproduct_name} from Boys' section to the cart.")
        print(f"\tCurrent cart  : {Cart}")
        print(f"\tTotal price   : {Tamount}\n")
        
    elif Rproduct_name in Product["Girls"]:
        Cart.append(Rproduct_name)
        Amount(Rproduct_name)  # Call the Amount function to update the price
        print(f"\n\tAdded {Rproduct_name} from Girls' section to the cart.")
        print(f"\tCurrent cart  : {Cart}\n")
        
    else: 
        print("\tProduct not found in the inventory. Please try again.")



def option():    
    print("\n")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Check and Exit")
    print("6. Total Amount")
    print("\n")
option()



def Choice_option():
    while True:
        try:
            user = int(input("Enter your choice '0' or (1-6):"))
            if user == 1:
                View_Section()
            elif user == 2:
                AddCart_Section()
            elif user == 3:
                remove_Section()
            elif user == 4:
                print(f"\n\tCurrent Cart    : {Cart}")
                print(f"\tTotal Price       : ₹{Tamount}\n")
            elif user == 5:
                if user == 'exit' or user == 'Exit':
                    Exit_Section()
                else:
                    Exit_Section()
                break
            elif user == 6:
                Total_price()
            elif user == 0:
                option()
            else:
                print("Invalid option! Please choose a number between 1 and 6.")
        except ValueError:
            print("Invalid input! Please enter number between 1 and 6.")      
Choice_option()
































