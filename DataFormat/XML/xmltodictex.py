import xmltodict
import pprint
import json

with open('xmlfile.xml') as xmlfile1:
    xmlcontent = xmlfile1.read()

print (type(xmlcontent))    # This would be string
xmltodictf = xmltodict.parse(xmlcontent)
print(type(xmltodictf))                     ## output is <class 'collections.OrderedDict'> and if we print xmltodictf
                                            ## output is very weird
obj_json = json.dumps(xmltodictf)
print (type(obj_json))                      ### its string type, string representation of json data in double quotes

obj_dict = json.loads(obj_json)             ## This is now a dictionary
print (obj_dict)

## So basically in this example we have converted xml to collections.orderedDict using xmltodict
## Then we have converted tht orderedDict to json using json.dumps
## then we converted that json string to Dict so that we can access elements of dict

print(obj_dict['audience'])
print(obj_dict['audience']['Age'])  ## Check the xml file, the root is shown as the only xml key and the value
                                    ## assign to it are other dictionary hence obj_dict['audience'] key value is
                                    ## also an dictionary. Note the text's, attributes assigned to any xml element
                                    ## will also come here as an dictionary.


print("*****************************************")
print("\n")

print(obj_json)
abc = {"x":obj_json}     ### Here we are modifying the Dictionary. What this actually does is add a root element
                           ### for the xml else below line will throw error that there are multiple roots.
jsontoxml = xmltodict.unparse(abc)
pp = pprint.PrettyPrinter(indent=10)
pp.pprint(jsontoxml)
