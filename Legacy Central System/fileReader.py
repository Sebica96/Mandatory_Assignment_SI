import csv
import random
from xml.dom import minidom
import os
# from nemID_ESB import nemId
from csv import reader
from csv import writer
from msgpack import packb
from datetime import datetime
import requests

csv.register_dialect('myDialect',
                     delimiter='|',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_ALL)

csv_file = "people.csv"


def Legacy_Central_System():
    # find file and open it

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            name = row[0]
            lName = row[1]
            mail = row[2]

        # Generate a CPR
            mydate = row[3]
            # print(date)
            number = random.randint(1000, 9999)
            my_date = (mydate[0] + mydate[1] + mydate[3] + mydate[4] + mydate[6] + mydate[7] + mydate[8] + mydate[9])
            # print(my_date)
            CPR = str(my_date) + str(number)
            # print(CPR)

        # Build an XML body
            root = minidom.Document()

            xml = root.createElement('person')
            root.appendChild(xml)

            firstname = root.createElement('FirstName')
            firstname.setAttribute('FirstName', name)
            xml.appendChild(firstname)

            lastname = root.createElement('LastName')
            lastname.setAttribute('LastName', lName)
            xml.appendChild(lastname)

            cprnumber = root.createElement('CPRNumber')
            cprnumber.setAttribute('CPRNumber', CPR)
            xml.appendChild(cprnumber)

            email = root.createElement('Email')
            email.setAttribute('Email', mail)
            xml.appendChild(email)

            xml_str = root.toprettyxml(indent="\t")

            save_path_file = "body.xml"

            with open(save_path_file, "w") as f:
                f.write(xml_str)

        # Send a POST request
            url = 'http://localhost:8080/nemID'

            myobj = {xml_str}

            x = requests.post(url, data=myobj)
            response = requests.get('http://localhost:8080/nemID')

            #date = x.json()
            print(x.status_code)

        # Write msgpack file

            data = "f_name: " + row[0] + "," + "l_name: " + row[1] + "," + "birth_date: " \
                   + row[3] + "," + "email: " + row[2] + "," + "country: " + row[6] + "," + "phone: " \
                   + row[4] + "," + "address: " + row[5] + "," + "CPR: " + str(CPR) + "," + "NemID: " + nemid

            if os.path.exists("../" + str(CPR) + ".msgpack"):
                return print("nothing")
            else:
                with open("../msgpack/" + str(CPR) + ".msgpack", "wb") as outfile:
                    packed = packb(data)
                    outfile.write(packed)


def postRequestNemID(xmlBody):
    url = 'http://localhost:8080/nemID'

    myobj = {xmlBody}

    x = requests.post(url, data=myobj)

    date = x.json()

    # return print("nothing yet")


Legacy_Central_System()

