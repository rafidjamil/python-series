#Example 01
import random
>>> random.randint(1, 10)
8
>>> random.randint(1, 10)
6
>>> random.randint(1, 10)
7
>>> random.randint(1, 10)
8
>>> random.randint(1, 10)
7
#Example 02
>>> 11 = ['lemon', 'masala', 'ginger', 'mint']
>>> random.choice(11)
'lemon'
>>> random.choice(l1)
'ginger'
>>> random.choice(11)
'ginger'
>>> random.choice(l1)
'masala'
>>> random.shuffle(11)
>>> 11
['mint', 'masala', 'ginger', 'lemon']
>>> random.shuffle(11)
>>> 11
['mint', 'ginger', 'lemon', 'masala']

#Example 03
>>> 0.1 +0.1 +0.1
0.30000000000000004
>>> 0.1 + 0.1 + 0.1 - 0.3
5.551115123125783e-17
>>> (0.1 + 0.1 + 0.1) - 0.3
5.551115123125783e-17
>>> from decimal import Decimal
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
Decimal('0.3')
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
Decimal('0.0')

#Example 04
>>> from fractions import Fraction
>>> myFra = Fraction(2, 7)
>>> myFra
Fraction(2, 7)

#Example 05
>>> setone = {1, 2, 3, 4}
>>> setone & {1, 3}
{1, 3}
>>> setone | {1, 3}
{1, 2, 3, 4}
>>> setone | {1, 3, 7}
{1, 2, 3, 4, 7}
>>> setone
{1, 2, 3, 4}
>>> setone - {1, 2, 3, 4}
set()
>>> type({})
<!-- <class 'dict'> -->

#Example 06
>>> num_list = "0123456789"
>>> num_list[:]
'0123456789'
>>> num_list[3:]
'3456789'
>>> num_list[ :7]
'0123456'
>>> num_list[0:7:2]
'0246'
>>> num_list[0:7:3]
'036'

#Example 07
>>> chai_type = "Masala"
>>> quantity = 2
>>> order = "I ordered {} cups of {} chai"
>>> order
'I ordered {} cups of {} chai'
>>> print (order.format (quantity, chai_type))
I ordered 2 cups of Masala chai

#Example 08
>>> chai_variety = ["Lemon", "Masala", "Ginger"]
>>> chai_variety
['Lemon', 'Masala', 'Ginger']
>>> print("".join(chai_variety))
LemonMasalaGinger
>>> print(" ".join(chai_variety) )
Lemon Masala Ginger
>>> print("-".join(chai_variety))
Lemon-Masala-Ginger
>>> print(", ".join(chai_variety) )
Lemon, Masala, Ginger