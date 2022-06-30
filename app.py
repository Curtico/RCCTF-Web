#!/usr/bin/python3

from flask import Flask, render_template, request, make_response

app = Flask(__name__, static_url_path="", static_folder="templates")

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        response = make_response(render_template('index.html'))
        req_cookie = request.cookies.get('SESSION')
        if req_cookie is None:
            response.set_cookie('SESSION', '0.0.0.0')
            
        return response
    else:
        response = make_response("")
        req_cookie = request.cookies.get('SESSION')
        if req_cookie is None:
            response.set_cookie('SESSION', '0.0.0.0')
            return response
        else:
            # Encrypted random words so it can't be guessed
            valid_cookies = ["63757274696365", "61584d3d", "59513d3d", "67616d6572"]
            actual_cookies = req_cookie.split('.')
            
            motor_status = {
                "front-left-motor": "disabled",
                "front-right-motor": "disabled",
                "rear-left-motor": "disabled",
                "rear-right-motor": "disabled"
            }
            
            if actual_cookies[0] == valid_cookies[0]:
                motor_status['front-left-motor'] = "enabled"
            if actual_cookies[1] == valid_cookies[1]:
                motor_status['front-right-motor'] = "enabled"
            if actual_cookies[2] == valid_cookies[2]:
                motor_status['rear-left-motor'] = "enabled"
            if actual_cookies[3] == valid_cookies[3]:
                motor_status['rear-right-motor'] = "enabled"
            
            return motor_status
            

@app.route("/flag-auth/", methods=['POST'])
def authenticate_flag():
    flags_dictionary = {
        "front-left-motor": "front-left{placeholder_flag_1}",
        "front-right-motor": "front-right{placeholder_flag_2}",
        "rear-left-motor": "rear-left{placeholder_flag_3}",
        "rear-right-motor": "rear-right{placeholder_flag_3}"
    }
    
    data = request.json;
    cookies = request.cookies.get('SESSION').split('.')
    
    motor = data['motor']
    flag = data['flag']
    if flag == flags_dictionary[motor]:
        response = make_response("flag_correct")
        if motor == "front-left-motor":
            cookies[0] = '63757274696365'
        elif motor == "front-right-motor":
            cookies[1] = '61584d3d'
        elif motor == "rear-left-motor":
            cookies[2] = '59513d3d'
        elif motor == "rear-right-motor":
            cookies[3] = '67616d6572'
        
        response.set_cookie('SESSION', cookies[0] + '.' + cookies[1] + '.' + cookies[2] + '.' + cookies[3])
        
        return response
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
