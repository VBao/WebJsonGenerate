import random
import hashlib
import unidecode

# *******************************list*********************************************

contentOfDeadline = ["Nộp lần 1", "Nộp bài lần 1", "Nộp phần 1", "Nộp bài tập", "Nộp chương đầu", "Nộp bài tập lớn",
                     "Kiểm tra tiến độ", "Kiểm tra lần 2",
                     "Nộp chương 2", "Nhớ nộp bài", "nộp bài nha mấy bạn!", "hạn chót", "phần 4", "phần 7", "phần 6",
                     "Nộp lấy điểm cộng",
                     "Nộp cho thầy", "Nộp cho cô", "Nộp bài cuối"]

firstNames = ["Nguyễn", "Trần", "Lâm", "Đỗ", "Huỳnh", "Phan", "Văn", "Hồ", "Đặng"]
middleNames = {
    "female": ["Thị", "Kim", "Vân", "Bảo", "Mỹ", "Huyền", "Ngọc", "Tú", "Thùy", "Mai", "Diễm", "Hồng"],
    "male": ["Trí", "Công", "Văn", "Hùng", "Minh", "Việt", "Trọng", "Thành", "Phương", "Chí", "Trung"]}
lastNames = {
    "female": ["Thị", "Kim", "Vân", "Vĩ", "Bảo", "Mỹ", "Huyền", "Ngọc", "Tú", "Thùy", "Mai", "Diễm", "Hồng", "Anh",
               "Tú", "Quỳnh", "Trang", "Huyền", "Lan", "Hương", "Trúc"],
    "male": ["Trí", "Công", "Văn", "Hùng", "Minh", "Việt", "Trọng", "Thành", "Phương", "Chí", "Trung", "Hậu", "Hưng",
             "Nhân", "Khải", "Khánh", "Duy", "Lợi", "Quân"]}


# *******************************time*********************************************

def create_birthday(startYear, endYear):
    dd = str(random.randrange(1, 32))
    mm = str(random.randrange(1, 13))
    if (len(dd) == 1):
        dd = "0" + dd
    if (len(mm) == 1):
        mm = "0" + mm
    yyyy = str(random.randrange(startYear, endYear))
    return dd + "-" + mm + "-" + yyyy


def check_time(time):
    if (len(time) == 1):
        return "0" + time
    return time


def split_time(t1):
    time = t1.split("-")
    yyyy = "2020"
    dd = int(time[0]) + 7
    mm = time[1]
    if (dd > 30):
        dd = "01"
        mm = check_time(str(int(time[1]) + 1))
    dd = check_time(str(dd))
    return "%s-%s-%s %s" % (dd, mm, yyyy, create_time())


def create_time():
    hh = check_time(str(random.randrange(1, 24)))
    MM = str(random.choice(["00", "30", "45", "15"]))
    ss = "00"
    return "%s:%s:%s" % (hh, MM, ss)


def create_date_time(n):
    ds = []
    yyyy = "2020"
    dd = check_time(str(random.randrange(1, 32)))
    mm = check_time(str(random.randrange(1, 9)))
    start_time = "%s-%s-%s %s" % (dd, mm, yyyy, create_time())
    # ******************************************************
    dd2 = check_time(str(random.randrange(1, 32)))
    mm2 = check_time(str(int(mm) + random.randrange(1, 3)))
    end_time = "%s-%s-%s %s" % (dd2, mm2, yyyy, create_time())
    ds.append(start_time)
    time = start_time
    for i in range(1, n):
        time = split_time(time)
        ds.append(time)
    ds.append(end_time)
    return ds


# *******************************function*********************************************
def remove_char_end(s):
    s = s.strip()
    return s[:len(s) - 1]


def remove_char_first(s):
    s = s.strip()
    return s[1:]


# *******************************basic*********************************************


def create_code(headerCode, lenCode):
    # head + end => 197CT + 31311
    head = random.choice(headerCode)
    lenEnd = lenCode - len(head)
    numberRangeList = {3: [100, 999], 4: [1000, 9999], 5: [10000, 99999], 6: [100000, 999999]}
    numberRange = numberRangeList[lenEnd]
    end = random.randrange(numberRange[0], numberRange[1])
    return str(head) + str(end)


def changeGender(gender):
    if (gender == "male"):
        return "MALE"
    return "FEMALE"


def create_fullName():
    fn = random.choice(firstNames)
    gender = random.choice(["male", "female"])
    mns = middleNames[gender]
    lns = lastNames[gender]
    while (True):
        mn = mns[random.randrange(len(mns))]
        ln = lns[random.randrange(len(lns))]
        if (mn != ln):
            break
    fullName = fn + " " + mn + " " + ln
    return [gender, fullName]


def create_email(code):
    end = random.choice(["@gmail.com", "@edu.vn"])
    # name = fullName.split(" ")[2]
    # head = name+"."+code
    return code + end


def create_id(s, e):
    return random.randrange(s, e + 1)


def create_phone():
    head = random.choice(["09", "08", "01"])
    end = random.randrange(10000000, 99999999)
    return head + str(end)


def create_username(name, code):
    name = name.split(" ")[2]
    name = unidecode.unidecode(name)
    return name + "." + code


def create_password(code):
    hash_obj = hashlib.md5(code.encode())
    return hash_obj.hexdigest()


# *******************************json*********************************************

def jsonStudent(code, name, gender, birthday, email, phone, facultyId, username, password):
    return '{ "code":"%s", "name":"%s", "gender":"%s", "birthday":"%s", "email":"%s", "phone":"%s", "facultyId":%d,"username":"%s","password":"%s" }%s' % (
    code, name, gender, birthday, email, phone, facultyId, username, password, ",")


def jsonTeacher(code, name, gender, birthday, email, phone, academyId, positionId, facultyId, username, password):
    return '{ "code":"%s", "name":"%s", "gender":"%s", "birthday":"%s", "email":"%s", "phone":"%s", "academyId":%d,"positionId":%d,"facultyId":%d,"username":"%s","password":"%s" }%s' % (
    code, name, gender, birthday, email, phone, academyId, positionId, facultyId, username, password, ",")


def jsonTopic(code, name, startTime, endTime, teacherId, typeTopicId, deadlines):
    return '{ "code":"%s", "name":"%s", "startTime":"%s", "endTime":"%s", "teacherId":%d, "typeTopicId":%d, "deadlines":%s}%s' % (
    code, name, startTime, endTime, teacherId, typeTopicId, deadlines, ",")


def jsonTeam(name, topicId):
    return '{ "name":"%s", "topicId":%d}%s' % (name, topicId, ",")


def jsonJoinTeam(timeJoin, studentId, teamId):
    return '{ "timeJoin":"%s", "studentId":%d, "teamId":%d }%s' % (timeJoin, studentId, teamId, ",")


# *******************************format*********************************************

def runForStudent(limit):
    jsonContent = ""
    for i in range(limit):
        code = create_code(["197CT", "197TC", "197XD"], 10)
        fullName = create_fullName()
        name = fullName[1]
        gender = changeGender(fullName[0])
        birthday = create_birthday(1990, 2004)
        email = create_email(code)
        phone = create_phone()
        facultyId = create_id(1, 5)
        username = create_username(name, code)
        password = create_password(code)

        jsonContent += jsonStudent(code, name, gender, birthday, email, phone, facultyId, username, password)
    return '[%s]' % (jsonContent)


def runForTeacher(limit):
    jsonContent = ""
    for i in range(limit):
        code = create_code(["100CT", "100TC", "100XD"], 10)
        fullName = create_fullName()
        name = fullName[1]
        gender = changeGender(fullName[0])
        birthday = create_birthday(1990, 2004)
        email = create_email(code)
        phone = create_phone()
        academyId = create_id(1, 4)
        positionId = create_id(1, 10)
        facultyId = create_id(1, 6)
        username = create_username(name, code)
        password = create_password(code)

        jsonContent += jsonTeacher(code, name, gender, birthday, email, phone, academyId, positionId, facultyId,
                                   username, password)
    return '[%s]' % (jsonContent)


def runForTopic(limit):
    jsonContent = ""
    for i in range(limit):
        code = "do-an-so-" + str(i)
        name = "DO AN " + str(i)
        dateTime = create_date_time(random.randrange(2, 4))
        lenDateTime = len(dateTime)
        startTime = dateTime[0]
        endTime = dateTime[lenDateTime - 1]
        deadlineContent = ""
        for i in range(0, lenDateTime - 1):
            deadlineContent += '"%s",' % (
                str(dateTime[i] + "**" + dateTime[i + 1] + "**" + str(random.choice(contentOfDeadline))))

        teacherId = create_id(1, 20)
        typeTopicId = create_id(1, 6)
        deadlines = '[%s]' % (remove_char_end(deadlineContent))

        jsonContent += jsonTopic(code, name, startTime, endTime, teacherId, typeTopicId, deadlines)
    return '[%s]' % (jsonContent)


def runForTeam(limit):
    jsonContent = ""
    for i in range(limit):
        name = "team " + str(i)
        topicId = create_id(1, 9)

        jsonContent += jsonTeam(name, topicId)
    return '[%s]' % (jsonContent)


def runForJoinTeam(limit):
    jsonContent = ""
    for i in range(limit):
        timeJoin = "2021-01-01 08:00:00"
        studentId = create_id(1, 40)
        teamId = create_id(1, 40)

        jsonContent += jsonJoinTeam(timeJoin, studentId, teamId)
    return '[%s]' % (jsonContent)


# *******************************run*********************************************
print(runForStudent(40))
# print(runForTeacher(30))
# print(runForTopic(10))
# print(runForTeam(40))
# print(runForJoinTeam(40))
