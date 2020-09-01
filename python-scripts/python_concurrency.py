import concurrent.futures
import time


def myfunc(name):
    print(f'\n\tfunc-{name} started.')
    time.sleep(3)
    print(f'\n\tfunc-{name} finished.')


if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
        pass
