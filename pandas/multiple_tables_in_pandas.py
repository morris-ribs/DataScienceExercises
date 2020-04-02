import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head(5))
print(cart.head(5))
print(checkout.head(5))
print(purchase.head(5))

visits_cart = pd.merge(visits, cart, how='left')
total_visits_cart = len(visits_cart)
print(total_visits_cart)

visits_cart_null = visits_cart[visits_cart.cart_time.isnull()]
total_not_cart_visits = len(visits_cart_null)
print(total_not_cart_visits)
print(float(total_not_cart_visits)/total_visits_cart)

cart_checkout = pd.merge(cart, checkout, how='left')
total_cart_checkout = len(cart_checkout)
cart_checkout_null = cart_checkout[cart_checkout.checkout_time.isnull()]
total_not_cart_checkout = len(cart_checkout_null)

print(total_cart_checkout)
print(total_not_cart_checkout)
print(float(total_not_cart_checkout)/total_cart_checkout)

all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
print(all_data.head(5))

checkout_purchase = pd.merge(checkout, purchase, how='left')
total_checkout_purchase = len(checkout_purchase)
checkout_purchase_null = checkout_purchase[checkout_purchase.purchase_time.isnull()]
total_not_checkout_purchase = len(checkout_purchase_null)

print(total_checkout_purchase)
print(total_not_checkout_purchase)
print(float(total_not_checkout_purchase)/total_checkout_purchase)

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time
print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())