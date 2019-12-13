import xml.etree.ElementTree as ET

with open('xmlfile.xml') as file:
    xmltree = ET.parse(file)

root = xmltree.getroot()

print(root.tag)

for elem in root.iter('country1'):
    print (elem.tag, elem.attrib)
    for subelem in elem.iter('gdppc'):
        for subsubelem in subelem.iter():
            print(type(subsubelem))
