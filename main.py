7import json

with open('boxes.json', 'r') as boxes: 
    box_data = json.load(boxes)

with open('orders.json', 'r') as orders: 
    order_data = json.load(orders)

# def calculate_size(box_data, order_data):
#     print(box_data)

def calculate_box_volume(box_data): 
    for box in box_data: 
         box['volume'] = box['dimensions']['widthMm'] * box['dimensions']['heightMm'] * box['dimensions']['depthMm']
    return box_data


def calculate_order_ingredience_volume(order_data): 
    for order in order_data: 
        order['volume'] = 0 
        for ingredient in order['ingredients']: 
            order['volume'] += ingredient['volumeCm3']
    return order_data

# def assign_box(box_data, order_data): 
#     for order in order_data: 
