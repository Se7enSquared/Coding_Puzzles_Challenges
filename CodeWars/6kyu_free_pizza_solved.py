# Name: Heather Gray
# Date: 8/9/2018
# Source: Codewars 6kyu: Free Pizza
# Notes: came back to this one, which is something I couldn't solve 2 years ago. Today, it was easy.

# ===================Description=========================================================================================
# In an attempt to boost sales, the manager of the pizzeria you work at has devised a pizza rewards system: if you
# already made at least 5 orders of at least 20 dollars, you get a free 12 inch pizza with 3 toppings of your choice.
#
# However, the rewards system may change in the future. Your manager wants you to implement a function that, given a
# dictionary of customers, a minimum number of orders and a minimum order value, returns a set of the customers who are
# eligible for a reward.
#
# Customers in the dictionary are represented as:
#
# { 'customerName' : [list_of_order_values_as_integers] }
# =======================================================================================================================

# ===================Solution=======================
def pizza_rewards(customers, min_orders, min_price):
    eligible_customers = []

    for key, value in customers.items():
        count = 0
        if len(value) < min_orders:
            continue
        else:
            for i in range(len(value)):
                if value[i] >= min_price:
                    count += 1
            if count >= min_orders:
                eligible_customers.append(key)
    return eligible_customers


# ===================Basic Test=====================
customers = {'annie_elig': [45, 38, 23, 90, 38], 'ben_notelig': ['28, 30, 44'], 'casey_elig': [25, 25, 25, 25],
             'derek_notelig': [22, 23, 24, 19, 40]}

print('original list: ', customers)
print('eligible list: ', pizza_rewards(customers, 4, 25))
