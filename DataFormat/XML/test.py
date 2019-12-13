import xmltodict
import pprint
import json

with open('xmlfile.xml') as xmlfile:
    my_xml = xmlfile.read()
dict1 = {'a': 1, 'b': 2}
pprint.pprint(my_xml)
"""
The output of above is below:
('\n'
 '    <audience>\n'
 '      <id what="attribute">123</id>\n'
 '      <name>Shubham</name>\n'
 '    </audience>\n')
 """


pp = pprint.PrettyPrinter(indent=50, width = 80, depth = 1)
pp.pprint(my_xml)
pp.pprint(dict1)
#print(my_xml)
 #pp.pprint(json.dumps(xmltodict.parse(my_xml), indent=5))
