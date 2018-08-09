def pizza_rewards(customers, min_orders, min_price):
    eligible_customers = []
    count = 0
    for key, value in customers.items():
        for i in range(0, len(value)):
            if value[i] >= min_price:
                count += 1
        if count >= min_orders:
            eligible_customers.append(key)
    print(eligible_customers)

customers = {'cust1': [21, 39, 40, 52, 88, 19, 22], 'cust2': [9, 5, 19, 22, 25], 'cust3': [1, 2, 3]}
pizza_rewards(customers, 5, 20)
