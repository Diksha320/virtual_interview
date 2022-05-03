from flask import Flask, jsonify, request, json
from flask_cors import CORS
from os import path
import random


app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "videos"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

gesture = ['Confident', 'Not-confident', 'Shy', 'Bold', 'Blunt']

@app.route('/')
def home():
    return {"msg": "Home Page"}


@app.route('/login-user', methods=["POST"])
def login_user():
    data = request.form
    f = open("users.txt", 'a')
    f.writelines("Name: "+ data['name']+"\t")
    f.writelines("Email: "+ data['email']+ '\n')
    print(data['name'])

    return jsonify({"msg": "Logged in successfully"})


@app.route('/upload-video', methods=["POST"])
def upload_video():
    
    # if 'video' not in request.files:
    #     resp = jsonify({"msg": "Video file not found"})
    #     resp.status_code = 400
    #     return resp

    file = request.files['video']


    errors = {}
    success = True
    
    if file:
        filename = file.filename
        file.save(path.join(app.config['UPLOAD_FOLDER'], filename))
        success = True

    else:
        errors[file.filename] = "File contains some error"


        
    if success: 
        resp = jsonify({"msg": "Video uploaded successfully", "gesture": gesture[random.randint(0, len(gesture))]})
        resp.status_code = 201
        return resp

    else:
        resp = jsonify({"msg": "Error occured while uploading video"})
        resp.status_code = 500
        return resp

    

if __name__ == '__main__':
    app.run(debug=True)




