from models.item import Item
from models.alert import Alert
from models.stores import Stores
from models.user import User

import re


#Stores("headphoneszone","https://www.headphonezone.in/","span",{'class':"bold_option_price_display current_price"},2).savetodb()
"""try:

    u=User.getByName('shva')
except Exception as e:
    print(e.message)
"""
#print(u.json())
"""sto=Alert.getById("74254b0c65a0484284c41a44f9755503")
sto.updatePriceLimit(20)
print(sto.json())"""
"""a= Alert.all()
for i in a:
    i.load_item_price()
    print(i.notify_if_pdrop())"""

"""
add all alerts"""
"""print(Item.getById("32af153202ce4d599ca5b24357999828").load_price())"""
