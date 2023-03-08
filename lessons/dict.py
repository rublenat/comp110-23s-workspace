"""Practice with dictionaries"""

# creating an empty dict
ice_cream: dict[str, int] = dict()

# not empty
ice_cream2: dict[str, int] = {'chocolate': 12, 'vanilla': 8, 'strawberry': 5}

#adding elements
ice_cream2['mint'] = 3

#removing elements
ice_cream2.pop('mint')

#accessing elemtns
print(ice_cream2['vanilla'])

#f string: use single quotes
print(f"Number of vanilla orders: {ice_cream2['vanilla']}")

#modify values
ice_cream2['vanilla'] = 9
#or
ice_cream2['vanilla'] += 100
print(ice_cream2)

#check if key in dictionary
print("mint" in ice_cream2)
print("chocolate" in ice_cream2)

