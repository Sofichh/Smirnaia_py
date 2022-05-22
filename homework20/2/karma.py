import random


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class Karma:

    def __init__(self, karma=0):
        self.karma = karma

    def one_day(self, numofday):
        self.karma += numofday
        try:
            if 5 == random.randint(1, 10):
                f = open('karma.log', 'w')
                raise Exception(
                    random.choice(['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError']))
        except KillError:
            f.write('KillError')
            f.close()
        except DrunkError:
            f.write('DrunkError')
            f.close()
        except CarCrashError:
            f.write('CarCrashError')
            f.close()
        except GluttonyError:
            f.write('GluttonyError')
            f.close()
        except DepressionError:
            f.write('DepressionError')
            f.close()
        return self.karma

