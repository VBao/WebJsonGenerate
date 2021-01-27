from flask import Flask,request,jsonify
from flask_api import status
from Generate import Generate
from flask_cors import CORS, cross_origin
import re
import json
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

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
            return Generate.string.array(temp)
        elif '(' in typeField:
            return Generate.string.string(int(re.findall('\d+',typeField)[0]),int(re.findall('\d+',typeField)[1]))
        elif '-':
            return  Generate.string.string(int(re.findall('\d+',typeField)[0]))
    # TODO Datetime here
    else:
        return False

# @app.route('/<int:loop>/',methods=['POST'])
# def convert(loop:int):
#     rq=request.json
#     rs=[]
#     for _ in range(loop):
#         singleRecord={}
#         for i in rq:
#             if strToFunc(rq[i]) != False:
#                 singleRecord[i]=strToFunc(rq[i])
#                 return {"Error":"Invalid type or not update"},status.HTTP_400_BAD_REQUEST
#         rs.append(singleRecord)
#     return {"result":rs},status.HTTP_200_OK

@app.route('/test/',methods=['POST'])
@cross_origin()
def convert():
    rq=request.json
    print(rq['request'])
    print(rq['total'])
    loop=rq['total']
    rquest=rq['request']
    rs=[]
    for _ in range(loop):
        singleRecord={}
        for i in rquest:
            print(i)
            if strToFunc(i['type']) != False:
                singleRecord[i['nameField']]=strToFunc(i['type'])
            else:    
                return {"Error":"Invalid type or not update"+str()},status.HTTP_400_BAD_REQUEST
        rs.append(singleRecord)
        data=jsonify(rs)
        data.headers.add("Access-Control-Allow-Origin", "*")
    return data,status.HTTP_200_OK
if __name__ == '__main__':
    app.run()
