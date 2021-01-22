from flask import Flask
from flask_api import status
from Generate import Generate
import re
gen=Generate
app = Flask(__name__)

def res(key,value):
    return {key:value}
@app.route('/')
def hello_world():
    return {"Here":"'Hello World!'"}

@app.route("/<string:nameField>/<string:typeField>/")
def gen(nameField,typeField):
    if typeField.find('number') != -1:
        # return {nameField:str(Generate.number.number(10))},status.HTTP_200_OK
        # if typeField.find('number-(['):
        if 'number-([' in typeField:
            return res("Error","On next update"),status.HTTP_200_OK
        elif 'number-(' in typeField:
            start=int(re.findall('\d+',typeField)[0])
            end=int(re.findall('\d+',typeField)[1])
            return res(nameField,Generate.number.number(start,end)),status.HTTP_200_OK
        elif 'number-' in typeField:
            print("ADADW")
            return res(nameField,Generate.number.number(int(re.findall('\d+',typeField)[0]))),status.HTTP_200_OK
    else:
        print("NOT UP")
        return {},status.HTTP_403_FORBIDDEN
if __name__ == '__main__':
    app.run()
