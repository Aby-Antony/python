# Using string
from codecs import utf_16_be_encode


country_name = 'I Love My India'
country_name1 = '01\t012\t0123\t01234'
print(country_name)
print(country_name.capitalize())
print(country_name.casefold())
print(country_name.center(80))
print(country_name.count('n'))
print(country_name.encode())
print(country_name.endswith('a'))
print(country_name.endswith('y'))
print(country_name1)
print(country_name1.expandtabs(10))
print(country_name.find('o'))
print(country_name.strip('I'))
print(country_name.split(" "))
print(country_name.removesuffix(''))