try:
    import cPickle as pickle
except:
    import pickle
from StringIO import StringIO


class SimpleObject(object):
    def __init__(self, name):
        self.name = name
        self.name_backwards = name[::-1]
        return


data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('cPickle'))
data.append(SimpleObject('last'))

out_s = StringIO()

for o in data:
    print("WRITING: %s(%s)" %(o.name, o.name_backwards))
    pickle.dump(o, out_s)
    out_s.flush()

in_s = StringIO(out_s.getvalue())

while True:
    try:
        o = pickle.load(in_s)
    except EOFError:
        break
    else:
        print("READ: %s (%s)"%(o.name, o.name_backwards))