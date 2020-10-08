import requests
import sqlite3

def postRequests():
    db = sqlite3.connect('NemId_CodeGenerator/nem_id_database.sqlite')
    response = requests.post('http://localhost:8090/nemid-auth')
    # Check people in db 
    db_cursor = db.cursor()
    query = """SELECT * FROM user"""

    for row in db_cursor.execute(query):
        if f'NemIdCode: {row[2][-4:]}, NemId: {row[2]}' == response.json():
            json_response={"status":200}
            print(json_response)
        else:
            json_response={"status":403}
            print(json_response)

postRequests()