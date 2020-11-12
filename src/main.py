"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Photo
import base64
import codecs
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200


@app.route('/userphoto', methods=['POST'])
def photo_post():
   file = request.files['archivo'].read()
   encoded_string = base64.b64encode(request.files['archivo'].read())
   b = bytearray(file)
   txt_b64 = base64.b64encode(b)
   c = base64.encodestring(txt_b64)
   txt_b64_string = c.decode('utf-8')
   #print(txt_b64)
   new_photo=Photo(data = txt_b64_string)
   db.session.add(new_photo)  
   db.session.commit()   

   return "save "  + " to the DB"

@app.route('/imagen', methods=['GET'])
def get_photo():
    photos = Photo.query.all()
    photo=photos[1].data
    b1 = photo.decode("utf-8")
    d = base64.b64decode(b1)
    s2 = d.decode("utf-8")
    print(type(photo))
    print(s2)
    #print(d)
    return jsonify({"data":s2})
    

  

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
