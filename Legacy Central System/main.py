import csv
from dicttoxml import dicttoxml
import requests
import random
import string
import json
import msgpack


with open('people.csv', 'r') as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')
    for row in readCSV:
        firstname = row[0]
        lastname = row[1]
        email = row[2]
        birthday = row[3]

        print(firstname, lastname, birthday)
        chars = string.digits
        cprnumber = '{}-{}'.format(birthday.replace('-', ''), ''.join(random.choice(chars) for _ in range(4)))
        print(cprnumber)

        person_dict = {'FirstName': firstname, 'LastName': lastname, 'CPRNumber': cprnumber, 'Email': email}

        print(person_dict)

        xmlbody = dicttoxml(person_dict, custom_root='Person')

        r = requests.post(
            'http://localhost:8080/nemID',
            data=xmlbody,
            headers={
                'Content-Type': 'application/xml'
            }
        )

        person_dict['NemID'] = json.loads(
            r.content.decode('utf-8')).get('nemID', None)

        print(person_dict['NemID'])

        with open(person_dict['CPRNumber'] + '.msgpack', 'wb') as out:
            out.write(msgpack.packb(person_dict))
