import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Execution Time:", end - start, "seconds")
        return result

    return wrapper

@timer
def task():
    time.sleep(2)
    print("Task Completed")

task()
-




