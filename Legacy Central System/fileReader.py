import csv
import random
from xml.dom import minidom
import os
#from nemID_ESB import nemId
from csv import reader
from csv import writer
from datetime import datetime
import requests


csv.register_dialect('myDialect',
                     delimiter='|',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_ALL)

csv_file = "people.csv"

def read_CSV():
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)

    #for row in reader:
        #print(row)
    return file


def update_CSV():
    # Open the input_file in read mode and output_file in write mode
    with open(csv_file, 'r') as file, \
            open('output_people.csv', 'w', newline='') as write_obj:
        reader = csv.reader(file)

        for row in reader:
            cpr = random_cpr_generator()
            #print(CPR)
            csv_writer = writer(write_obj)
            row.append(cpr)
            csv_writer.writerow(row)


def creat_XML():
    # find file and open it
    file = read_CSV()

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]
            lName = row[1]
            mail = row[2]
            cpr = random_cpr_generator()

            # XML stuff
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
            cprnumber.setAttribute('CPRNumber', cpr)
            xml.appendChild(cprnumber)

            email = root.createElement('Email')
            email.setAttribute('Email', mail)
            xml.appendChild(email)

            xml_str = root.toprettyxml(indent ="\t")

            save_path_file = "body.xml"

            with open(save_path_file, "w") as f:
                f.write(xml_str)

            postRequestNemID(xml_str)


    #return print("nothing yet")


def create_msgpack():
    return print("nothing yet")

def postRequestNemID(xmlBody):

    url = 'http://localhost:8080/nemID'

    myobj = {xmlBody}

    x = requests.post(url, data=myobj)

    date = x.json()

    #return print("nothing yet")

def random_cpr_generator():
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            date = row[3]
            #print(date)
            number = random.randint(1000, 9999)
            my_date = (date[0] + date[1] + date[3] + date[4] + date[6] + date[7] + date[8] + date[9])
            #print(my_date)
            CPR = str(my_date) + str(number)
            #print(CPR)
    return CPR

#update_CSV()


creat_XML()
