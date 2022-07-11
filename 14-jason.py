# JSON - Javascript Object Notation Best for pulling out of the data
import json
data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''
info = json.loads(data) #loads : load from string
print(info[1]['name'])

# Service Oriented Approach
# Service publish the "rules" applications must follow to make use of the service(API)
# With a services oriented approach to developing web apps, where is the data located?
# : Spread across many computer systems connected via the internet or internal network.
