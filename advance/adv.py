# decorater
import time
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(f"Func {fun.__name__} took {end_time - start_time:.4f} second")
        return res
    return wrapper



@timer_decorator
def slow_function(sec):
    time.sleep(sec)
    return 'Done'

print('Execution started')
print(slow_function(2))

# def my_decorator(func):
#     def wrapper():
#         print()
#         func()
#         print()
#         return wrapper

# @my_decorator
# def say_hello():
#     print('Hello!')

# say_hello