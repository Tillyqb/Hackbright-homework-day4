melon_cost = 1.00

the_file = open('customer-orders.txt')

for line in the_file:
    order = line.split('|')
    order_number = order[0]
    customer_name = order[1]
    quantity = order[2]
    total_paid = float(order[3])
    expected_paid = float(order[2]) * melon_cost
    if not float(quantity) == float(total_paid):
        print(f"order no.: {order[0]}: {customer_name} paid ${total_paid:.2f}, expected ${expected_paid:.2f}"
          )
