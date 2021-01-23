import random
import rstr
from datetime import datetime


class Generate:
    class number:
        def number(*args):
            if len(args) == 1:
                return random.randint(0, args[0])
            elif len(args) == 2:
                return random.randint(args[0], args[1])
        # Get random number with total single number in that number
        def number_len(*args): return random.randint(int("1" + "0" * (int(args[0]) - 1)), int("9" * int(args[0])))
        def array(*args): return random.choice(args[0])
    class string:
        def string(*args):
            if len(args) == 1: return rstr.xeger(r'^[a-zA-Z]{'+str(args[0])+r'}$')
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
                try:
                    return datetime.strptime(args[0], "%d/%m/%Y")
                except ValueError:
                    return "Date not valid"
            elif len(args) == 2:
                start = datetime.strptime(args[0], "%d/%m/%Y")
                end = datetime.strptime(args[1], "%d/%m/%Y")