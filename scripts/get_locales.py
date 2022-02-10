from country_list import available_languages
from country_list import countries_for_language

import untangle

import lxml

# importing struct module
import struct
# packing 3 integers, so 'iii' is required
variable = struct.pack('iii', 1, 2, 3)
# printing the type of packed variable
print(type(variable))
# printing
print(variable)
# python strucn unpack() method
numeric_values = struct.unpack('iii', variable)
# printing
print(numeric_values)
#for language in available_languages():
#    print(language)

'''
for lang in available_languages():
    countries = dict(countries_for_language(lang))
    #print(countries['GB'])
    if lang == 'fi':
        #print('\n')
        for count in countries:
            print(countries[count])
print("*****************")
print("*****************")
for lang in available_languages():
    countries = dict(countries_for_language(lang))
    if lang == 'es_ES':
        #print('\n')
        for country in countries:
            print(countries[country])

'''

xml = '''
<resources>
    <stringarray name="country_codes">
        <item>AR</item><item>AU</item> <item>AT</item> <item>BE</item> <item>CA</item> <item>CN</item> <item>CZ</item> <item>DK</item> <item>EE</item> <item>FI</item> <item>FR</item> <item>DE</item> <item>HK</item><item>HU</item> <item>IS</item> <item>IE</item> <item>IL</item> <item>IT</item>
        <item>JP</item> <item>LV</item> <item>LT</item> <item>LU</item> <item>MY</item> <item>NL</item> <item>NZ</item> <item>NO</item> <item>PL</item> <item>RU</item> <item>SG</item> <item>SK</item> <item>ES</item> <item>SE</item> <item>CH</item> <item>TW</item> <item>TH</item> <item>GB</item>
        <item>US</item> <item>VN</item> <item>BG</item> <item>HR</item> <item>PT</item> <item>RO</item> <item>GT</item> <item>PA</item> <item>CO</item>
    </stringarray>
</resources>
'''






obj = untangle.parse('C:/Users/fitim/IdeaProjects/PythonProject/PythonProject/scripts/localizations.xml')
print(obj.resources.stringarray.item)

l = []

for item in range (len(obj.resources.stringarray.item)):
    #print(obj.resources.stringarray.item[item])
    txt = obj.resources.stringarray.item[item]
    #print(txt)
    y = str(txt).split(' ',9)
    l.append(y[9])

#print(l)

countries_from_yaml = {"Dutch": "nl", "English": "en", "French": "fr", "German": "de", "Italian": "it", "Spanish": "es", "Japanese": "ja"}

#print(countries_from_yaml.get("Dutch"))

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

a = 0
country = []
list_of_lists = [[]]   #* 44
#print(list_of_lists)
list = []
cnt = 0

#print("Value : %s "+countries_from_yaml.get('Dutch'))

for z in countries_from_yaml:
    a = 0
    countries = dict(countries_for_language(countries_from_yaml.get(z)))
    #print(countries)
    print("**********************************************************************")
    print(countries_from_yaml.get(z))
    #print(len(countries))
    #print("**********"+countries_from_yaml.get(z)+"**********")
    #for c in range (len(countries)):
    for c in range (len(l)-1):
        #country.append(countries[l[a]])
        #print(country)
        #list_of_lists[43].insert(1,countries[l[a]])
        #print(countries[l[a]])
        if a <= 44:
            list.append(countries[l[a]])
            a = a + 1
        if a == 44:
            a = 0
            list_of_lists.insert(cnt, list)
            list = []
            list_of_lists = [x for x in list_of_lists if x != []]
            print(list_of_lists[cnt])
            print("**********************************************************************")
            cnt = cnt + 1


print(list_of_lists[1])
#print(len(list_of_lists))
#print(set(country))
'''
lang = 'fr'
for lang in available_languages():
    if lang == 'fr':
        print(lang)
        for maa in l:
            print(maa)
            print(dict(countries_for_language(maa)))
            #a = a + 1

'''


'''
countries = dict(countries_for_language('fi'))
print(countries['GB'])

countries = dict(countries_for_language('sv'))
print(countries['GB'])

countries = dict(countries_for_language('fr'))
print(countries['GB'])
'''