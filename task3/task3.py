import json


path1 = input()
path2 = input()
path3 = input()

with open(path1, 'r') as f:
    data = json.load(f)
    id_value = {}

    for i in data['values']:
        id_value[i['id']] = i['value']

with open(path2, 'r') as f:
    data = json.load(f)


def check_values(x):
    for elem in x:
        if 'value' in elem.keys():
            elem['value'] = id_value[elem['id']]

        if elem.get('values'):
            check_values(elem['values'])


with open(path3, 'w') as f:
    for j in data['tests']:
        if 'value' in j.keys():
            j['value'] = id_value[j['id']]

        if j.get('values'):
            check_values(j['values'])

    json.dump(data, f, indent=2)
