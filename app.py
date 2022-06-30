#!/usr/bin/python3

from flask import Flask, render_template, request, make_response

app = Flask(__name__, static_url_path="", static_folder="templates")

@app.route("/")
def index():
    response = make_response(render_template('index.html'))
    req_cookie = request.cookies.get('SESSION')
    if req_cookie is None:
        response.set_cookie('SESSION', '0')
        
    return response

@app.route("/flag-auth/", methods=['POST'])
def authenticate_flag():
    flags_dictionary = {
        "front-left-motor": "front-left{placeholder_flag_1}",
        "front-right-motor": "front-right{placeholder_flag_2}",
        "rear-left-motor": "rear-left{placeholder_flag_3}",
        "rear-right-motor": "rear-right{placeholder_flag_3}"
    }
    
    data = request.json;
    
    motor = data['motor']
    flag = data['flag']
    if flag == flags_dictionary[motor]:
        return "flag_correct"
    else:
        return "flag_incorrect"
    
@app.route("/post-demo/", methods=['POST', 'GET'])
def post_demo():
    if request.method != 'POST':
        return render_template('bad-request.html')
    else:
        content = request.form['message']
        print(content)
        return content
        
@app.route("/driver")
def driver_challenge():
    return render_template('driver-challenge.html')
    
@app.route('/movement/', methods=['POST'])
def move_input():
    content = request.json

    if content['zoom'] == "forward":
        #forward()
        print("User requested forward movement...")
        return "Forward movement request successful!"

    elif content['zoom'] == "left":
        #left()
        print("User requested left movement...")
        return "Left movement request successful!"

    elif content['zoom'] == "right":
        #right()
        print("User requested right movement...")
        return "Right movement request successful!"

    elif content['zoom'] == "backward":
        #backward()
        print("User requested backward movement...")
        return "Backward movement request successful!"

    elif content['zoom'] == "stop":
        #stop()
        print("User requested to stop movement...")
        return "Stopping movement!"

    else:
        return "Bad movement request!"
