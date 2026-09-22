
print ("Hello. velcome to data structures class !!!")

# Numeric Data Types 
number1 = 10
print(f"var number1 is:{type(number1)}")

gravity = 9.8
print(f"var gravity is:{type(gravity)}")

numberx = 8j
print(f"var numberx is:{type(numberx)}")

#string Data Types
my_name = "juan"
fullname = 'peter McDonal'
description = '''
    hello, how's it going?
    thisw is amazing !!!
'''      
print(f"var my_name is:{type(my_name)}")
print(f"var fullname is:{type(fullname)}")
print(f"var description is:{type(description)}")

#list
week_days = []
print (week_days)
print(type(week_days)) # es mutable
                       # multi data type

#dictionary
fruits={}
print (fruits)
print(type(fruits)) # si es mutable --- es como un  JSON formato particular para progrmar la web
                    # multi data type

#duple                    
months=()
print (months)
print(type(months)) # no mutable



#list
personal_info=[
    'juan',
    'ojeda',
    18,
    True,
    '34567891',
    'pasto',
    ['juli', 9]
]
print(personal_info)

#show father age and city
print (f"Father age: {personal_info[2]}")
print ("Father city:", personal_info[5] )

#show daugther name and age
print (f"Daugther Name: {personal_info[6][0]}")
print (f"Daugther age: {personal_info[6][1]}")

#Update father age
new_age = input ("please, type the new father age: ")
personal_info[2]= new_age
print (f"Father age: {personal_info[2]}")

#Add new informaation
personal_info.append('malala') 
print(personal_info)


#tuple
user_data = ('Benazir', 'Butto', 35, False)
print (user_data)
print (user_data[0])

#user_data[2] = new_age


#dictionaries
countries_info = {
    'country_name': 'colombia'
    'capital': 'Bogota'
    'abbrev': 'CO'
    'copde': 123456

}
print (countries_info)





