import csv
import json
from random import randint  

with open('data.json', 'r') as f:  # assume json is in the current directory
    pws = json.load(f)

vaults = pws['vaults']
export = []  # blank list used later to store all the passwords getting exported
export_filename = f'export_{randint(0,10000)}.csv'  # generate a random number for the output csv filename
print(export_filename)

for vault in vaults.keys():
    print(vaults[vault]['name'], '\t', vault,)

    for item in vaults[vault]['items']:
        data = item['data']
        content = data['content']
        metadata = data['metadata']
        # print(content)
        # print(metadata)

        pw = {}

        if content == {}:
            print(metadata['name'], 'HAS NO CONTENT')
            continue

        pw['name'] = metadata['name']                  # Name

        try:
            pw['login_uri'] = content['urls'][0]       # URL
        except IndexError:
            print(metadata['name'], 'HAS NO URLS')
            pw['login_uri'] = ''

        pw['login_username'] = content['username']     # Username
        pw['login_password'] = content['password']     # Password

        pw['folder'] = vaults[vault]['name']          # Folder (uses PP vault name)
        pw['notes'] = metadata['note']                # Notes

        # assume everything is a login - i only had logins.
        pw['type'] = 'login'  
        pw['favorite'] = 0
        pw['reprompt'] = 0

        # stop extra fields exporting as '[]'
        if data['extraFields']:  
            pw['fields'] = data['extraFields']
        else:
            pw['fields'] = ''

        if content['totpUri']:
            totp = content['totpUri'].split('?')[1].split('&')
            # spliting on 0 leaves url and then the rest, split on & splits up the rest. then grab the one that has the secret
            for item in totp:
                if item[0:7] == 'secret=':
                    pw['login_totp'] = item[7:]
        else:
            pw['login_totp'] = ''

        export.append(pw)

# Export to CSV
headers = ['name', 'login_uri', 'login_username', 'login_password', 'folder', 'notes', 'type', 'favorite', 'reprompt', 'fields', 'login_totp']


with open(export_filename, 'x', newline='') as expfile:
    csvw = csv.writer(expfile)
    csvw.writerow(headers)

    for item in export:
        x = []
        for value in item.values():
            x.append(value)
        csvw.writerow(x)

input('\n\nprogram finished, file saved', export_filename)
