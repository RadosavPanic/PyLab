from utils import enterProducts, makeAndPrintBill

shoppingCart = enterProducts()
membershipType = input("Enter your customer membership type: ")
makeAndPrintBill(shoppingCart, membershipType)