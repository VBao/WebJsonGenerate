import random
from time import strftime
import rstr
from datetime import *
last_name = open('../Dictionary/lastname.txt', 'r+').readlines()
first_name = open('../Dictionary/firstname.txt', 'r+').readlines()
timez = open('../Dictionary/timezone.txt', 'r+').readlines()


class Generate:
    def array(*args): return random.choice(args[0]).strip()

    class number:
        def number(*args):
            if len(args) == 1:
                return random.randint(0, args[0])
            elif len(args) == 2:
                return random.randint(args[0], args[1])
        def number_len(*args): return random.randint(int("1" +
                                                         "0" * (int(args[0]) - 1)), int("9" * int(args[0])))

    class string:
        def string(*args):
            if len(args) == 1:
                return rstr.xeger(r'^[a-zA-Z]{'+str(args[0])+r'}$')
            if len(args) == 2:
                rs = ""
                for _ in range(random.randint(args[0], args[1])):
                    rand = [random.randint(65, 90), random.randint(49, 57)]
                    func = random.choice(rand)
                    rs += chr(func)
                return rs

    # TODO continue update datetime
    class datetime:
        def date(*args):
            if len(args) == 0:
                year = random.randint(1975, date.today().year)
                month = random.randint(1, 12)
                if month in [1, 3, 5, 7, 9, 11]:
                    day = random.randint(1, 31)
                elif month in [4, 6, 8, 10, 12]:
                    day = random.randint(1, 30)
                else:
                    day = random.randint(
                        1, 28) if year % 4 == 0 and year % 400 == 0 else random.randint(1, 29)
                day = '0'+str(day) if day < 10 else str(day)
                month = '0'+str(month) if month < 10 else str(month)
                return str(day+'/'+month+'/'+str(year))
            elif len(args) == 2:
                startDate = datetime.strptime(args[0], "%d/%m/%Y")
                endDate = datetime.strptime(args[1], "%d/%m/%Y")
                year = random.randint(startDate.year, endDate.year)
                month, day = 0, 0
                if year == startDate.year:
                    month = random.randint(startDate.month, 12)
                    if month != 2 and month % 2 == 0:
                        day = random.randint(startDate.day, 30)
                    elif month == 2:
                        day = random.randint(1, 29)
                day = '0'+str(day) if day < 10 else str(day)
                month = '0'+str(month) if day < 10 else str(month)
                return str(day+'/'+month+'/'+str(year))

        def datetime(*args):
            zone = random.choice(timez)
            try:
                if len(args) == 0:
                    year = random.randint(1975, date.today().year)
                    month = random.randint(1, 12)
                    if month in [1, 3, 5, 7, 9, 11]:
                        day = random.randint(1, 31)
                    elif month in [4, 6, 8, 10, 12]:
                        day = random.randint(1, 30)
                    else:
                        day = random.randint(
                            1, 28) if year % 4 == 0 and year % 400 == 0 else random.randint(1, 29)
                    tempDate = datetime(
                        year, month, day).strftime("%a %b %d %Y ")
                    h = random.randint(0, 24)
                    h = '0'+str(h) if h < 10 else str(h)
                    m = random.randint(0, 60)
                    m = '0'+str(m) if m < 10 else str(m)
                    s = random.randint(0, 60)
                    s = '0'+str(s) if s < 10 else str(s)
                    tempTime = h+":" + m+":"+s
                    return tempDate + tempTime + ' UTC '+zone.split(" UTC ")[1].strip('\n')+' (' + zone.split(" UTC ")[0]+')'
                elif len(args) == 2:
                    startDate = datetime.strptime(args[0], "%d/%m/%Y")
                    endDate = datetime.strptime(args[1], "%d/%m/%Y")
                    year = random.randint(startDate.year, endDate.year)
                    if year == startDate.year:
                        month = random.randint(startDate.month, 12)
                        # print(str(month))
                        if month != 2:
                            day = random.randint(
                                1, 30) if month % 2 == 0 else random.randint(1, 31)
                        elif month == 2:
                            day = random.randint(
                                1, 28) if year % 400 == 0 else random.randint(1, 29)
                    else:
                        month = random.randint(1, 12)
                        # print(str(month))

                        if month != 2:
                            day = random.randint(
                                1, 30) if month % 2 == 0 else random.randint(1, 31)
                        elif month == 2:
                            day = random.randint(
                                1, 28) if year % 400 == 0 else random.randint(1, 29)
                    tempDate = datetime(int(year), int(
                        month), int(day)).strftime("%a %b %d %Y ")
                    tempTime = str(random.randint(
                        0, 24))+":" + str(random.randint(0, 60))+":"+str(random.randint(0, 60))
                    return tempDate + tempTime + ' UTC '+zone.split(" UTC ")[1].strip('\n')+' (' + zone.split(" UTC ")[0]+')'
            except ValueError:
                Generate.datetime.datetime(args)

    class people:
        def name():
            return str(random.choice(last_name).strip('\n')+' ' + random.choice(first_name).strip('\n'))

        def gender(*arsg):
            if len(arsg) == 0:
                return random.choice(['male', 'female'])
            else:
                return random.choice(arsg[0], arsg[1])

        def tel(*args):
            return ('0' if len(args) == 0 else args[0])+str(random.randint(100000000, 999999999))

        def add():
            return str(random.randint(1, 500)) + ' ' + str(random.choice(last_name).strip('\n')+' ' + random.choice(first_name).strip('\n'))


# for _ in range(50):
#     a = Generate.datetime.datetime('01/02/2001', '01/02/2020')
#     print(a)
# print('=============================')
# for _ in range(50):
#     b = Generate.datetime.datetime('01/02/2001', '01/02/2020')
#     print(b)
# print(Generate.people.name())
