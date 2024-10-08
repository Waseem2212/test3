# Decorators in python
# def decorator(func):
#     def wrap(*args, **kwargs):
#         print(f"Calling {func.__name__} with: {args}, kwargs: {kwargs}")

#         result = func(*args, **kwargs)

#         print(f"{func.__name__} returned: {result}")

#         return result
#     return wrap


# @decorator
# def multiply_number(x,y):
#     return x * y

# result = multiply_number(10,20)
# print('Result: ', result)

# def decorator(func):
#     def wrap(*args, **kwargs):
#         # Log the function name and arguments
#         print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        
#         # Call the original function
#         result = func(*args, **kwargs)
        
#         # Log the return value
#         print(f"{func.__name__} returned: {result}")
        
#         # Return the result
#         return result
#     return wrap

# # Example usage
# @decorator
# def multiply_numbers(x, y):
#     return x * y

# # Call the decorated function
# result = multiply_numbers(10, 20)
# print("Result:", result)


# Generator in Python
# reading large files:
# def read_lrg_file(file_path):
#     with open(file_path, 'r') as file:
#         for line in file:
#             yield line

# for line in read_lrg_file('python.txt'):
#     print(line)

# def read_large_file(file_path):
#     with open(file_path, 'r') as file:
#         for line in file:
#             yield line

# for line in read_large_file('python.txt'):
#     print(line)

# Generationg Infinit Sequence
# def fibonacci():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b = b, a+b

# fib_gen = fibonacci()
# for _ in range(10):
#     print(next(fib_gen))

# Pipelining Data Processing
# def integers():
#     for i in range(1,9):
#         yield i
# def squared(seq):
#     for i in seq:
#         yield i * i

# def negated(seq):
#     for i in seq:
#         yield -i
# chain = negated(squared(integers()))
# for number in chain:
#     print(number)


# Context Manager in Python
# class OpenFile:
#     def __init___(self,filename,mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = None
    
#     def __inter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#     def __exit__(self, exc_type, exc_val, traceback):
#         self.file.close()

# with OpenFile('wasi.txt', 'w') as f:
#     f.write('Wasi Developer')

# print(f.closed)

# class OpenFile:
#     def __init__(self, filename, mode) :
#         self.filename = filename
#         self.mode = mode

#     def _enter__(self):
#         self. file = open(self. filename, self .mode)
#         return self.file

#     def __exit__(self, exc_type, exc_val, traceback):
#         self. file. close()


# with OpenFile('sample.txt', 'W') as f:
#     f.write('Testing')
    
# print(f.closed)

# class OpenFile:
#     def __init__(self, filename, mode) :
#         self.filename = filename
#         self.mode = mode

#     def _enter__(self):
#         self. file = open(self. filename, self .mode)
#         return self.file

#     def __exit__(self, exc_type, exc_val, traceback):
#         self. file. close()


# with OpenFile('sample.txt', 'W') as f:
#     f.write('Testing')
    
# print(f.closed)

# class FileManager():
#     def __init___(self, filename,mode):
#         self.filename = filename
#         self.mode = mode

#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()

# with FileManager('test.txt','w') as f:
#     f.write('Waseem','Hasnain')

# Meta Class in Python
# class UpperAttriMeta(type):
#     def __new__(cls, name, bases, dct):
#         uppercase_attr = {}
#         for name, value in dct.items():
#             if not name.startswith('__'):
#                 uppercase_attr[name.upper()] = value
#             else:
#                 uppercase_attr[name] = value
#         return super().__new__(cls, name, bases, uppercase_attr)
# class MyClass(metaclass=UpperAttriMeta):
#     foo = 'bar'
#     baz = 'qux'

# print(hasattr(MyClass,'foo'))
# print(hasattr(MyClass,'FOO'))
# print(MyClass.FOO)

# Async in python
# import aiohttp
import asyncio
# import time

# async def fetch(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as res:
#             return await res.text()


# async def main():
#     urls = ['https://www.programiz.com','https://www.geeksforgeeks.org']
#     tasks = [fetch(url) for url in urls]
#     res = await asyncio.gather(*tasks)
#     for i,res_ in enumerate(res):
#         print(f'Response {i+1} from {urls[i]}: {res_[:100]}')

# asyncio.run(main())
# start_time = time.time()
# print(f"Done in {time.time() - start_time} seconds")

# async def delay_msg():
#     await asyncio.sleep(2)
#     print('Wasi Developer')

# async def main():
#         await delay_msg()

# asyncio.run(main())
# async def dis_num():
#     for i in range(1,9):
#         print(i)
#         await asyncio.sleep(1)

# asyncio.run(dis_num())

# def add_logging(func):
#     def wrap(*args, **kwargs):
#         print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
#         result = func(*args, **kwargs)

#         print(f"{func.__name__} returned: {result}")

#         return result

# @add_logging

# def add_number(x,y):
#     return x + y

# result = add_number(200,300)
# print("Result: ", result)

# def add_logging(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
#         result = func(*args, **kwargs)  
#         print(f"{func.__name__} returned: {result}")
#         return result
#     return wrapper
# @add_logging
# def add_numbers(x, y,z):
#     return x + y + z
# result = add_numbers(200, 300,400)
# print("Result:", result)

# def collatz_sequence(n):
#     while n != 1:
#         yield n
#         if n % 2 == 0:
#             n = n // 2
#         else:
#             n = 3 * n + 1
#     yield 1

# # Accept input from the user
# n = int(input("Input a positive integer (n): "))

# # Generate and print the Collatz sequence
# print("Collatz sequence:")
# for num in collatz_sequence(n):
#     print(num, end=", ")

# def is_prime_num(n):
#     # Check if the number is prime
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def prime_numbers(start, end):
#     # Generate prime numbers between start and end
#     for num in range(start, end + 1):
#         if is_prime_num(num):
#             yield num

# # Accept input from the user
# start = int(input("Input the starting number: "))
# end = int(input("Input the ending number: "))

# # Create the prime numbers generator
# prime_gen = prime_numbers(start, end)

# # Generate and print all prime numbers
# print("Prime numbers between", start, "and", end, "are:")
# for prime in prime_gen:
    # print(prime, end=",")


# def string_permutations(string):
#     if len(string) <= 1:
#         yield string
#     else:
#         for i in range(len(string)):
#             current_char = string[i]
#             remaining_chars = string[:i] + string[i+1:]
#             for permutation in string_permutations(remaining_chars):
#                 yield current_char + permutation

# # Accept input from the user
# input_string = input("Input a string: ")

# # Create the string permutations generator
# permutations_gen = string_permutations(input_string)

# # Generate and print all permutations
# print("All permutations of", input_string + ":")
# for permutation in permutations_gen:
#     print(permutation, end = ", ")




# # Define a metaclass that ensures all attributes are integers
# class ValidateAttrMeta(type):
#     # Override the __new__ method of the metaclass
#     def __new__(cls, name, bases, dct):
#         # Iterate over all attributes of the class
#         for key, value in dct.items():
#             # Check if the attribute is not a special method and is not an integer
#             if not key.startswith('__') and not isinstance(value, int):
#                 # Raise a TypeError if the attribute is not an integer
#                 raise TypeError(f"Attribute {key} is not an integer")
#         # Create the new class with validated attributes
#         return super().__new__(cls, name, bases, dct)

# # Create a class using the metaclass
# class MyIntClass(metaclass=ValidateAttrMeta):
#     # Define an integer attribute
#     foo = 100
#     # Define another integer attribute
#     bar = 200
#     # Define a non-integer attribute (uncomment to test the TypeError)
#     # baz = 'not an integer'  # Uncommenting this should raise a TypeError

# # Test the class
# # Print the value of attribute foo
# print(MyIntClass.foo)  # 100
# # Print the value of attribute bar
# print(MyIntClass.bar)  # 200
 # write function add two number





