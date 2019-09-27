import time

start = time.perf_counter()


def do_something():
    print('Sleeping...')
    time.sleep(1)
    print('Sleeping done.')


do_something()
do_something()

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} second(s)")
