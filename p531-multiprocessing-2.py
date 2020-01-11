import multiprocessing
import time


def worker():
    name = multiprocessing.current_process().name
    print name, 'Starting\n'
    time.sleep(1)
    print name, 'Exiting\n'


def my_service():
    name = multiprocessing.current_process().name
    print name, 'Starting\n'
    time.sleep(5)
    print name, 'Exiting\n'


if __name__ == '__main__':
    service = multiprocessing.Process(name='my_service',
                                      target=my_service
                                      )
    worker_1 = multiprocessing.Process(name='worker 1',
                                       target=worker
                                       )
    worker_2 = multiprocessing.Process(target=worker)

    worker_1.start()
    worker_2.start()
    service.start()
