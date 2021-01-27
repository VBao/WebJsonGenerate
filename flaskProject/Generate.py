import random
import rstr
from datetime import *


class Generate:
    class number:
        def number(*args):
            if len(args) == 1:
                return random.randint(0, args[0])
            elif len(args) == 2:
                return random.randint(args[0], args[1])
        # Get random number with total single number in that number
        def number_len(*args): return random.randint(int("1" +
                                                         "0" * (int(args[0]) - 1)), int("9" * int(args[0])))

        def array(*args): return random.choice(args[0])

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

        def array(*args): return random.choice(args[0])

    # TODO continue update datetime
    class datetime:
        def date(*args):
            if len(args) == 1:
                year = random.randint(1975, date.today().year)
                month = random.randint(1, 12)
                if month in [1, 3, 5, 7, 9, 11]: day = random.randint(1, 31)
                elif month in [4, 6, 8, 10, 12]: day = random.randint(1, 30)
                else: day = random.randint(1, 28) if year % 4 == 0 and year % 400 == 0 else random.randint(1, 29)
                return str(day+'/'+month+'/'+year)
            elif len(args) == 2:
                startDate = datetime.strptime(args[0], "%d/%m/%Y")
                endDate = datetime.strptime(args[1], "%d/%m/%Y")
                year = random.randint(startDate.year, endDate.year)
                if year == startDate.year:
                    month=random.randint(startDate.month,12)
                    if month !=2 and month %2==0:
                        day=random.randint(startDate.day,30)
                    elif month ==2:
                        day=random.randint(1,29)
                # elif year