from flask import Flask,jsonify # lower case flask is the library uppercase is the class of Flask

app= Flask(__name__) # instantiates the class __name__ references the current module which is app

@app.route("/<name>") # decorator url endpoint  or route | <name> is placeholder 
def index(name): # placeholder needs to be added as a parameter in function 
    return "Hello {}!".format(name) # don't necessarily need to write html tags can just return string and it will automatically
    # converted to html

@app.route("/test")
def test():
    return "This is my test function"

@app.route("/json")
def json():
    return jsonify({"1":"test","2":[1,2,3,4]}) # converts dict and list into json structure

if __name__=="__main__": # with this the file can run directly without flask run command
    app.run(debug=True) # debug=True allows changes in app to be automatically updates

