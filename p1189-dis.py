import dis


class MyObject(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'MyObject(%s)' % self.name


dis.dis(MyObject)