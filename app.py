from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps

app = Flask(__name__)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'feinschneiden4'
#Collection Names
COLLECTION_NAME_SOUNDSENSOR = 'Soundsensor'
FIELDS_SOUNDSENSOR = {'Values': True, 'Datetime': True, '_id': False}

#COLLECTION_NAME_USTR = 'Ultrasonic_top_right'
#FIELDS_USTR = {'Values': True, 'Datetime': True, '_id': False}


@app.route("/")
def index():
    return render_template("index.html")

'''@app.route("/feinschneiden4_0/Ultrasonic_top_right")

def fs40_sens_Ultrasonic_top_right():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME_USTR]
    Sensors = collection.find(projection=FIELDS_USTR, limit=50)
    json_Sensors = []
    for Sensor in Sensors:
        json_Sensors.append(Sensor)
    json_Sensors = json.dumps(json_Sensors, default=json_util.default)
    connection.close()
    return json_Sensors'''


@app.route("/feinschneiden4_0/soundsensor")

def fs40_sens_soundsensor():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME_SOUNDSENSOR]
    Sensors = collection.find(projection=FIELDS_SOUNDSENSOR, limit=100)
    json_Sensors = []
    for Sensor in Sensors:
        json_Sensors.append(Sensor)
    json_Sensors = json.dumps(json_Sensors, default=json_util.default)
    connection.close()
    return json_Sensors



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
