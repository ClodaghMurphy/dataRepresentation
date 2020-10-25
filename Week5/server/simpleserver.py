

#!flask/bin/python
from flask import Flask
#serving static content
#this code would not run for me without a definition of app
#NameError: name 'app' is not defined
#and that makes sense
app = Flask (__name__,
            static_url_path='',
            static_folder='../')#tell flask where to find the static content
#the parent folder in this instance

@app.route ('/')
def index():
    return "Hello World!"

if __name__ == '__main__' :
    app.run(debug=True)
#in a production situation, you'd need debug to be false