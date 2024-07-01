import json

data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email": {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print(type(info))
print(f'Name: {info['name']}')
print(f'Hide: {info['email']['hide']}')