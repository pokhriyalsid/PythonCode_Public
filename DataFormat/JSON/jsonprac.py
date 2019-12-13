import json

data1 = {'name': 'Sid', 'No': 56417, 'Age' : 'Stone Age'}
data2 = '{"name": "Sid", "No": 56417, "Age" : "Stone Age"}'

print (type(data1))  # This is Dictionary
print (type(data2)) # This is String

### json.loads() converts json data to take dictionary form
data2_1 = json.loads(data2)
print (data2_1)
print (type(data2_1))   ## This is dictionary

with open('jsonex.json') as file:
    jsonfile = file.read()
print (type(jsonfile))  ## Obiviuosly this would be a string
#print (jsonfile[Student1])## this will give error since jsonfile is a string and not a dict
jsondict = json.loads(jsonfile)
print (type(jsondict))  ## This is now a dict as you can note now double quotes are converted to single quotes
print (jsondict["Student1"]) ### This is the use of loads() fn as now we can access json elements like dictionary

## Below I will try to convert the dict back to json

with open('converteddict.json', 'w+') as cjson:
    cjson.write(str(jsondict))
with open('convertedjson.json', 'w+') as cjson1:
    x = json.dumps(jsondict)
    print(jsondict)  ### Since this is dictionary you will see single quotes around the elements
    print(x)    ### since this is json string , now you will see double quotes
    cjson1.write(x) ## here we can use write() since x is string representation of json
                    ## we could not use cjson1.write(jsondict) because write() is a func for string and not dict
