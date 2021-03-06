from flask import Flask, render_template, jsonify
import pymongo
from bson.json_util import loads, dumps
import uv_melanoma_ETL

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.uv_melanoma_db
collection_incidence = db.melanoma_incidence
collection_mortality = db.melanoma_mortality
collection_uv = db.uv

@app.route("/")
def index():
    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html")

@app.route("/api/get_all_data")
def get_all_data():
    incidences_clean = []
    mortalities_clean = []
    uvs_clean = []

    incidences = collection_incidence.find()
    mortalities = collection_mortality.find()
    uvs = collection_uv.find()
    
    for incidence in incidences:
        incidence["_id"] = str(incidence["_id"])
        incidences_clean.append(incidence)

    for mortality in mortalities:
        mortality["_id"] = str(mortality["_id"])
        mortalities_clean.append(mortality)  

    for uv in uvs:
        uv["_id"] = str(uv["_id"])
        uvs_clean.append(uv)

    all_data = {
        "incidences": incidences_clean,
        "mortalities": mortalities_clean,
        "uvs": uvs_clean
    }
    return jsonify(all_data)

@app.route("/api/upload_to_db")
def upload_to_db():
    # Drops collection if available to remove duplicates
    db.melanoma_incidence.drop()
    db.melanoma_mortality.drop()
    db.uv.drop()

    # Run the get_data function
    incidence_dict, mortality_dict, UV_dict = uv_melanoma_ETL.get_data()

    # Update the Mongo database using update and upsert=True
    for incidence_data in incidence_dict:
        collection_incidence.insert_one(incidence_data)

    for mortality_data in mortality_dict:
        collection_mortality.insert_one(mortality_data)

    for UV_data in UV_dict:
        collection_uv.insert_one(UV_data)

    return "Data uploaded!"

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'msg': 'This is a Test'})

if __name__ == "__main__":
    app.run(debug=True)