# #maximum dictonary ethods
# d = {
#     'clear': 'Removes all items from the dictionary.',
#     'copy': 'Returns a shallow copy of the dictionary.',
#     'fromkeys': 'Creates a new dictionary from given keys and a value.',
#     'get': 'Returns the value for a specified key if the key is in the dictionary.',
#     'items': 'Returns a view object that displays a list of dictionary\'s key-value pairs.',
#     'keys': 'Returns a view object that displays a list of all the keys in the dictionary.',
#     'pop': 'Removes the item with the specified key and returns its value.',
#     'popitem': 'Removes and returns a random (key, value) pair from the dictionary.',
#     'setdefault': 'Returns the value of a specified key. If the key does not exist, inserts the key with a specified value.',
#     'update': 'Updates the dictionary with the key-value pairs from another dictionary or from an iterable of key-value pairs.',
#     'values': 'Returns a view object that displays a list of all the values in the dictionary.'
# }

d = {
    'name':'Your name is Anuj kumar thakur.',
    'age': 'Your age is 20 years old',
    'city': 'you live in lalitpur, nepal',
    'country': 'you are from nepal',
    'permanent_address': 'your permanent address is sarlahi, nepal',
    'current_studying':'you are currently studing in Lord buddha education foundation',
    'university': 'you are enrolled in Asian pacific university',
    'course': 'you are studying bachelor in computer application',
    'hobby': 'your hobby is playing football and coding',
    'goal': 'your goal is to become a successful data scientist'
        
}

#copy command or method makes a shallow copy of the dictionary
my_dict = d.copy()
print("Copied Dictionary:\n", my_dict)
print('\nkeys from dictionary d:\n', d.keys())
print('\nValues from dictionary d:\n ', d.values())
print('\n items from dictionary d : \n ', d.items())


#using method called fromkeys()

k = {'1', '2', '3'}
v = {'one', 'two', 'three'}

new_dict = dict.fromkeys(k , v)
print('\nNew dictionary using fromkeys method:\n', new_dict)
'''
Output:  {'2': {'two', 'one', 'three'}, '3': {'two', 'one', 'three'}, '1': {'two', 'one', 'three'}}

'''
v1 = 'number'
new_dict1 = dict.fromkeys(k, v1)
print('\nNew dictionary using fromkeys method:\n', new_dict1)
'''output:
 {'2': 'number', '3': 'number', '1': 'number'}'''
 
 #using get method
print('\n Using get method to access value of key:\n')
print('name: ', d.get('name'))
print('age: ', d.get('age'))
print('city:', d.get('city'))
print('country:', d.get('country'))
print('permanent_address:', d.get('permanent_address'))
print('current studying:', d.get('current_studying'))
print('University:', d.get('university'))
print('course:', d.get('course'))
print('hobby: ', d.get('hobby'))
print('goal:', d.get('goal'))

#using set default method
#--> if the key is not present in the dictionary it will add a default value and call it when the unknown key is getiing callled
print('\nUsing setdefault method:\n')
if 'favorite_color' not in d:
    s = d.setdefault('favorite_color', input('enter your favorite color: '))
    d.update({'favorite_color': s})

print('favorite_color:', d.get('favorite_color'))
print(d.keys())