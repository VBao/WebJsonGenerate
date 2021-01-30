from datetime import date, datetime
from flask import Flask, request, jsonify
from flask_api import status
from Generate import Generate
from flask_cors import CORS, cross_origin
import re
import json
app = Flask(__name__)
cors = CORS(app, resources={r'/test':{"origins": "http: // localhost: 3000"}})


def decode(typeFields):
    if 'custom-{' in typeFields:
        temp=typeFields.split("{")[1].strip("} ").split(';')
        rs=""
        for i in temp:
            i=i.strip()
            rs+=strToFunc(i)
        return rs
    else: 
        return strToFunc(typeFields)
def strToFunc(typeField):
    if 'number' in typeField != -1:
        if '([' in typeField:
            temp = str(re.findall(r"\[.*\]", typeField)[0])
            temp = temp[1:len(temp)-1]
            temp = temp.split(',')
            return Generate.array(temp)
        elif '(' in typeField:
            start = int(re.findall('\d+', typeField)[0])
            end = int(re.findall('\d+', typeField)[1])
            return Generate.number.number_len(start, end)
        elif '-' in typeField:
            return Generate.number.number_len(int(re.findall('\d+', typeField)[0]))
    elif 'string' in typeField:
        if '([' in typeField:
            temp = str(re.findall(r"\[.*\]", typeField)[0])
            temp = temp[1:len(temp)-1]
            temp = temp.split(',')
            return Generate.array(temp)
        elif '(' in typeField:
            return Generate.string.string(int(re.findall('\d+', typeField)[0]), int(re.findall('\d+', typeField)[1]))
        elif '-':
            return Generate.string.string(int(re.findall('\d+', typeField)[0]))
    elif 'date' in typeField and 'time' not in typeField:
        if '([' in typeField:
            temp=str(re.findall(r"\[.*\]",typeField)[0])
            temp=temp[1:len(temp)-1]
            temp=temp.split(',')
            return Generate.array(temp)
        elif '(' in typeField: 
            temp=typeField.split('-(')[1].strip(')')
            temp=temp.split(',')
            return Generate.datetime.date(temp)
        else:
            return Generate.datetime.date()
    elif 'datetime' in typeField:
        if '([' in typeField:
            temp=str(re.findall(r"\[.*\]",typeField)[0])
            temp=temp[1:len(temp)-1]
            temp=temp.split(',')
            return Generate.array(temp)
        elif '(' in typeField: 
            temp=typeField.split('-(')[1].strip(')')
            temp=temp.split(',')
            return Generate.datetime.datetime(temp)
        else:
            return Generate.datetime.datetime()
    elif 'name' in typeField: return Generate.people.name()
    elif 'gender' in typeField:
        temp=typeField.split('-')
        return Generate.people.gender(temp[1],temp[2])
    elif 'phone' in typeField:
            return Generate.people.tel(typeField.split('-')[1]) if '-' in typeField else Generate.people.tel()
    elif 'address' in typeField: return Generate.people.add()
    else:
        return False


@app.route('/test/', methods=['POST'])
@cross_origin(origin='localhost')
def convert():
    rq = request.json
    print(rq['request'])
    print(rq['total'])
    loop = rq['total']
    rquest = rq['request']
    rs = []
    for _ in range(loop):
        singleRecord = {}
        for i in rquest:
            print(i)
            # if strToFunc(i['type']) != False:
            singleRecord[i['nameField']] = decode(i['type'])
            # else:
            #     return {"Error": "Invalid type or not update"+str()}, status.HTTP_400_BAD_REQUEST
        rs.append(singleRecord)
        data = jsonify(data=rs)

    return data, status.HTTP_200_OK


if __name__ == '__main__':
    app.run()
