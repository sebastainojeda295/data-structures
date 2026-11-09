planets = ['Mercury','Venus','Eath','Murs','Jupiter','Saturn','Uranus','Neptuno']
gravity = [ 3.7, 8.8, 9.8, 3.7, 24.7, 10.4, 8.6, 11.1]
#print (type(gravity)) #Class List

print (planets)
print (gravity)

print ('-'*31)
print (f"| {'planet name' :<15} | {'gravity' :<9} | ")
print ('-'*31)

i=0
while i <= len(planets)-1:
    print (f'| {planets[i] :<15} | {planets[i] :<9} | ')
    print ('-'*31)
    i += 1
