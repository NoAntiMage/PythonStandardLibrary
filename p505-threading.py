import threading


def worker():
    print 'Worker'
    return


threads = list()
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()


