# Day 12 ------------------->>>>>>>>>>

# ------------------ Sets -----------------

info = {"Carla", 19, False, 5.9, 19}
print(info)

# accesing element
info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)

# joining set 

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)     # union methods
print(cities3)

cities4 = cities.intersection(cities2)   # intersection methods

cities5 = cities.symmetric_difference(cities2)  # symetric diffrence metgods 

cities6  = cities.difference(cities2)    # diffrence methods

print(cities.isdisjoint(cities2))    # check it is is disjoint
print(cities.issuperset(cities2))    # check it is superset
print(cities.issubset(cities2))      # check it is subset

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")    # add methods
print(cities)    

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)     # updates methods
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")   # remove methods
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()     # pop methods
print(cities)
print(item)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()    # clera methods
print(cities)
