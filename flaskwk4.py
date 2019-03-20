from flask import Flask, render_template, request
import requests

app = Flask("MyApp")


def send_simple_message(emailaddress):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox2dead1799f1340f8b75a02d73e0a09d5.mailgun.org/messages",
        auth=("api", "b6893791b11f1c3d588452ef3fea7fdc-de7062c6-b23a9e4e"),
        data={"from": "Excited User <mailgun@sandbox2dead1799f1340f8b75a02d73e0a09d5.mailgun.org>",
        "to": [emailaddress],
        "subject": "Subscription successful",
        "text": "Testing some Mailgun awesomeness!"})




@app.route("/")
def hello():
    return "Hello world"

# @app.route("/jo")
# def helloJo():
#     return "Hello Jo"

@app.route("/hi/")
def hi():
    return "Hi!"

@app.route("/bye")
def bye():
    return "Goodbye!"

@app.route("/<name>")
def HelloStranger(name):
    return render_template("hello1.html" , name = name )

# @app.route("/signup", methods=["POST"])
# def sign_up():
#     form_data = request.format
#     print (form_data["email"])
#     return "All OK"



@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print(form_data["email"])
    send_simple_message(form_data["email"])
    return "All OK"   #now submiting email should work in form

app.run(debug=True)