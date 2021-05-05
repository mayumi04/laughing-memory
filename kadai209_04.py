import json

with open('text.json', 'r', encoding = 'utf_8') as f:
    data = json.load(f)

    for program_list in data['program_list']:
        l = list(program_list.values())
        print(' '.join(l))