from flask import Flask,request
from flask_api import status
from Generate import Generate
import re
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return {"Here":"'Hello World!'"}

def strToFunc(typeField):
    if 'number' in typeField != -1:
        if '([' in typeField:
            temp=str(re.findall(r"\[.*\]",typeField)[0])
            temp=temp[1:len(temp)-1]
            temp=temp.split(',')
            return Generate.number.array(temp)
        elif '(' in typeField:
            start=int(re.findall('\d+',typeField)[0])
            end=int(re.findall('\d+',typeField)[1])
            return Generate.number.number(start,end)
        elif '-' in typeField:
            return Generate.number.number(int(re.findall('\d+',typeField)[0]))
    elif 'string' in typeField:
        if '([' in typeField:
            temp=str(re.findall(r"\[.*\]",typeField)[0])
            temp=temp[1:len(temp)-1]
            temp=temp.split(',')
            print(temp)
            print(Generate.string.array(temp))
            return Generate.string.array(temp)
        elif '(' in typeField:
            return Generate.string.string(int(re.findall('\d+',typeField)[0]),int(re.findall('\d+',typeField)[1]))
        elif '-':
            return  Generate.string.string(int(re.findall('\d+',typeField)[0]))
    # TODO Datetime here
    else:
        print("NOT UP")
        return {},status.HTTP_403_FORBIDDEN

@app.route('/<int:loop>/',methods=['POST'])
def convert(loop:int):
    rq=request.json
    rs=[]
    for _ in range(loop):
        singleRecord={}
        for i in rq:
            singleRecord[i]=strToFunc(rq[i])
        rs.append(singleRecord)
    return {"result":rs},status.HTTP_200_OK
if __name__ == '__main__':
    app.run()
