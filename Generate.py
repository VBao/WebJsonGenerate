import random

from datetime import datetime


class Generate:
    class number:
        def number(*args):
            if len(args) == 1:
                return random.randint(0, args[0])
            if len(args) == 2:
                return random.randint(args[0], args[1])

        # Get random number with total single number in that number
        def number_len(*args):
            return random.randint(int("1" + "0" * (args - 1)), int("9" * args))

    class string:
        def string(*args):
            if len(args) == 1:
                rs = ""
                for _ in range(len):
                    rand = [random.randint(65, 90), random.randint(48, 57),random.randint(79,122)]
                    func = random.choice(rand)
                    rs += chr(func)
                return rs
            if len(args) == 2:
                rs = ""
                for _ in range(random.randint(args[0], args[1])):
                    rand = [random.randint(65, 90), random.randint(48, 57)]
                    func = random.choice(rand)
                    rs += chr(func)
                return rs

    class datetime:
        def date(*args):
            if len(args) == 1:
                try:
                    return datetime.strptime(args[0], "%d/%m/%Y")
                except ValueError:
                    return "Date not valid"
            elif len(args) == 2:
                start = datetime.strptime(args[0], "%d/%m/%Y")
                end = datetime.strptime(args[1], "%d/%m/%Y")
                for i in range(start, end):
                    print(i)


a = Generate()
print(a.datetime.date("20/10/2001","20/12/2001"))
