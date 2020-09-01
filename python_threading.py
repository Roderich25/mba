from time import sleep
import threading


def namedfunc1(name):
    print(f'\n\tfunc1 {name} started.')
    sleep(5)
    print(f'\tfunc1 {name} finished.')


def namedfunc2(name):
    print(f'\n\tfunc2 {name} started.')
    sleep(5)
    print(f'\n\tfunc2 {name} finished.')


def namedfunc3(name):
    print(f'\n\tfunc3 {name} started.\n')
    sleep(5)
    print(f'\n\tfunc3 {name} finished.\n')


if __name__ == '__main__':
    print('\nmain started.')
    t1 = threading.Thread(target=namedfunc1, args=['foo'])  # daemon=True
    t1.start()
    t2 = threading.Thread(target=namedfunc2, args=['bar'])
    t2.start()
    t3 = threading.Thread(target=namedfunc3, args=['baz'])
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print('\nmain finished.')
