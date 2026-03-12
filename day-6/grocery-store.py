
"""
# Grocery Store Billing System

products = ["Rice","Wheat Flour","Sugar","Milk","Eggs (12 pcs)",
            "Cooking Oil","Tea Powder","Salt","Bread","Soap"]

prices = [60,45,40,25,70,130,90,20,30,25]

print("------ Welcome to Grocery Store ------")
print("Here are the available products:\n")

print("Index   Product        Price(Rs.)")

for i in range(len(products)):
    print(i+1,"     ",products[i],"       ",prices[i])

print("\nEnter the product indexes you want to buy (you can repeat indexes)")
indexes = list(map(int,input("Enter indexes (e.g. 1 2 2 5): ").split()))

print("\n------- Your Bill -------")
print("Product\t\tQty\tPrice\tTotal")

for i in set(indexes):
    qty = indexes.count(i)
    price = prices[i-1]
    total = qty * price
    print(products[i-1],"\t",qty,"\t",price,"\t",total)
    """
"""
 # Grocery Store Billing System

products = ["Rice","Wheat Flour","Sugar","Milk","Eggs (12 pcs)",
            "Cooking Oil","Tea Powder","Salt","Bread","Soap"]

prices = [60,45,40,25,70,130,90,20,30,25]

print("------ Welcome to Grocery Store ------")
print("Here are the available products:\n")

print("Index   Product        Price(Rs.)")

for i in range(len(products)):
    print(i+1,"     ",products[i],"       ",prices[i])

print("\nEnter the product indexes you want to buy (you can repeat indexes)")
indexes = list(map(int,input("Enter indexes (e.g. 1 2 2 5): ").split()))

print("\n------- Your Bill -------")
print("Product\t\tQty\tPrice\tTotal")

for i in set(indexes):
    qty = indexes.count(i)
    price = prices[i-1]
    total = qty * price
    print(products[i-1],"\t",qty,"\t",price,"\t",total)
    """

def display(username,email,password):
    print("username:",username)
    print("email:",email)
    print("password:",password)
display("praveen","pra@4",1234)