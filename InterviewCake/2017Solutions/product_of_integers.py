arr = [0, 0, 0]
products = []
product = 1

for number in arr:
    for number2 in arr:
        if number2 != number:
            if number2 != 0:
                product *= number2
            else:
                product = 0
    products.append(product)
    if product != 0:
        product = 1
print(products)