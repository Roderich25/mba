import time
import concurrent.futures

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s).')
    time.sleep(seconds)
    return f'{seconds} second(s) sleeping done.'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [0, 1, 2, 3, 4, 5]
    results = executor.map(do_something, secs)
    for result in results:
        print(result)

    # results = [executor.submit(do_something, sec) for sec in secs]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} second(s).")