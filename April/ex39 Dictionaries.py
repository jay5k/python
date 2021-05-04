things = ['a', 'b', 'c', 'd']
print(things[1])
things[1] = 'z'
print(things[1])

stuff = {'name': 'Zed', 'age': 39, 'height': 6* 12 + 2}
print(stuff['name'])
print(stuff['age'])
print(stuff['height'])
stuff['city'] = "SF"
print(stuff['city'])

stuff[1] = 'Wow'
stuff[2] = 'Neato'
print(stuff[1])
print(stuff[2])

del stuff['city']
del stuff[1]
del stuff[2]
print(stuff)

#########################################################################

#create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Micigan': 'MI'
}

#create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-' * 10)
print('NY State has: ', cities['NY'])
print('OR State has: ', cities['OR'])

