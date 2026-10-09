#Example 01
>>> tea_varities
['Black', 'Green', 'Oolong', 'White']
>>> tea_varities[1:2]
['Green' ]
>>> tea_varities[1:2] = ["Lemon"]
>>> tea_varities
['Black', 'Lemon', 'Oolong', 'White']
>>> tea_varities[1:3]
['Lemon', 'Oolong']
>>> tea_varities[1:3] = ["green", "Masala"]
>>> tea_varities
['Black', 'green', 'Masala', 'White']


#Example 02
>>> tea_varities
['Black', 'green', 'Masala', 'White']
>>> tea_varities[1:1]
[]
>>> tea_varities[1:1] = ["test", "test"]
>>> tea_varities
['Black', 'test', 'test', 'green', 'Masala', 'White']
>>> tea_varities[1:2]
['test' ]
>>> tea_varities[1:3]
['test', 'test']
>>> tea_varities[1:3] = []
>>> tea_varities
['Black', 'green', 'Masala', 'White']

#Example 03
>>> for tea in tea_varities:
print(tea, end="-")

Black-green-Masala-White->>>
...
>>> tea_varities
['Black', 'green', 'Masala', 'White']
>>> if "Oolong" in tea_varities:
print("I have Oolong tea")
<!-- Append --> 
<!-- last may add kar deta h  -->
>>> tea_varities.append("Oolong")
>>> tea_varities
['Black', 'green', 'Masala', 'White', 'Oolong']
>>> if "Oolong" in tea_varities:
print("I have Oolong Tea")

I have Oolong Tea
<!-- pop sy last value remove arry/list may sy -->
>>> tea_varities.pop()
'Oolong'
>>> tea_varities
['Black', 'green', 'Masala', 'White']

#Example 04
>>> tea_varities_copy = tea_varities.copy()
>>> tea_varities_copy
['Black', 'green', 'Masala', 'White']



#example 05
>>> tea_varities
['Black', 'Masala', 'White']
<!-- insert sy value add karna h list may -->
>>> tea_varities.insert(1, "green")
>>> tea_varities
['Black', 'green', 'Masala', 'White']
>>> tea_varities_copy - tea_varities.copy()
>>> tea_varities_copy
['Black', 'green', 'Masala', 'White']
>>> tea_varities_copy.append("Lemon")
>>> tea_varities
['Black', 'green', 'Masala', 'White']
>>> tea_varities_copy
['Black', 'green', 'Masala', 'White', 'Lemon']

#Example 06
>>> range(10)
range(0, 10)
>>> print(range(10))
range(0, 10)

#Example 07
>>> squared_num = [x**2 for x in range(10)]
>>> squared_num
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#Example 08
>>> cube_num = [y**3 for y in range(5)]
>>> cube_num
[0, 1, 8, 27, 64]

#Example 09
Dictonary
>>> chai_type = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
>>> chai_type["Masala"]
'Spicy'
>>> chai_type["Ginger"]
'Zesty'
>>> chai_type["Green"]
'Mild'
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types["Green"] = "Fresh"
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}

#Example 10
..

..
Masala
Ginger
Green
>>> for chai in chai_types:
print(chai, chai_types[chail)

Masala Spicy
Ginger Zesty
Green Fresh

>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> for chai in chai_types:
print (chai)

>>> for key, value in chai_types.items():
print(key, value)

Masala Spicy
Ginger Zesty
Green Fresh

#Example 11
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> chai_types["Earl Grey"] = "Citrus"
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus
itrus'}
>>> chai_types.pop("Ginger")
'Zesty'
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Fresh', 'Earl Grey': 'citrus'}
>>> chai_types.popitem()
('Earl Grey', 'Citrus')
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Fresh'}

#Example 12
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Fresh'}
>>> del chai_types["Green"]
>>> chai_types
{'Masala': 'Spicy'}
>>> chai_types_copy = chai_types.copy()

#Example 13
.

>>> tea_shop = {
"chai": {"Masala" : "Spicy", "Ginger": "Zesty"},
"Tea" : {"Green": "Mild", "Black": "Strong"}
.. }
>>> tea_shop
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild'
'Black': 'Strong'}}
>>> print(tea_shop)
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild'
, 'Black': 'Strong'}}
>>> tea_shop["chai"]
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
>>> tea_shop["chai"]["Ginger"]:
'Zesty'

#Example 14
>>> squared_num = {x:x ** 2 for x in range(6)}
>>> squared_num
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> squared_num.clear()
>>> squared_num
{}


#Example 15
Tuples
>>> tea_types = ("Black", "Green", "Oolong")
>>> tea_types
('Black', 'Green', 'Oolong')
>>> tea_types[0]
'Black'
>>> tea_types[-1]
'Oolong'
>>> tea_types [1: ]
('Green', 'Oolong')
>>> tea_types [0]
'Black'

>>> len(tea_types)
3
>>> more_tea = ("Herbal", "Earl Grey")
>>> all_tea = more_tea + tea_types
>>> all_tea
('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')
>>>
>>> if "Green" in all_tea:
print("I have green tea")

I have green tea
>>> more_tea = ("Herbal", "Earl Grey", "Herbal")
>>> more_tea
('Herbal', 'Earl Grey', 'Herbal')
>>> more_tea.count("Herbal")
2
>>> more_tea.count("Herb")
0
>>> tea_types
('Black', 'Green', 'Oolong')
>>> (black, green, Oolong) = tea_types
>>> black
'Black'
>>> type(tea_types)
<class 'tuple'>

...












