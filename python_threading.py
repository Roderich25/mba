import time
import threading


def namedfunc(name):
    print(f'\tfunc {name} started.')
    time.sleep(5)
    print(f'\tfunc {name} finished.')


if __name__ == '__main__':
    print('\nmain started.')
    t = threading.Thread(target=namedfunc, args=['test'])  # daemon=True
    t.start()
    t.join()
    print('\nmain finished.')
