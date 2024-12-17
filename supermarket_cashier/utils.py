productsPrices = {
        "Biscuit": 3,
        "Chicken": 5,
        "Egg": 1,
        "Fish": 3,
        "Coke": 2,
        "Bread": 2,
        "Apple": 3,
        "Onion": 3
}


def enterProducts():
    shoppingCart = {}
    enterDetails = True
    while enterDetails:
        details = input("Press A to add product and Q to quit selection: ").capitalize()
        if details == "A":
            product = input("Enter product: ")
            quantity = input("Enter quantity: ")
            shoppingCart.update({product: quantity})
        elif details == "Q":
            enterDetails = False
        else:
            print("Please select a correct option. Try again.")
    return shoppingCart


def getPrice(product, quantity):
    """Function returns subtotal price of a given product based on price and quantity. Currency is USD."""
    product = product.capitalize()
    subtotal = productsPrices[product] * int(quantity)
    print(f"{product}: ${productsPrices[product]} x {quantity} = ${subtotal}")
    return subtotal


def getDiscount(billAmount, membershipType):
    discount = 0
    billAmountBeforeDiscount = billAmount
    if billAmount > 25:
        if membershipType == "Gold":
            billAmount *= 0.8
            discount = 20
        elif membershipType == "Silver":
            billAmount *= 0.9
            discount = 10
        elif membershipType == "Bronze":
            billAmount *= 0.95
            discount = 5
        print(f"{discount}% off for {membershipType} membership on total amount: ${billAmountBeforeDiscount}")
    else:
        print("No discount on amount less than $25")
    return round(billAmount, 1)


def makeAndPrintBill(shoppingCart, membershipType):
    # Helper function for creating bill text borders
    createAndPrintBorder = lambda length: print("-" * length)

    billTitleText = "Shopping information"
    membershipType = membershipType.capitalize()
    billAmount = 0

    createAndPrintBorder(len(billTitleText))
    print(billTitleText)
    createAndPrintBorder(len(billTitleText))

    for product, quantity in shoppingCart.items():
        billAmount += getPrice(product, quantity)
    billAmount = getDiscount(billAmount, membershipType)

    billPriceText = f"Your total bill price is: ${billAmount}"
    print(billPriceText)
    createAndPrintBorder(len(billPriceText))
