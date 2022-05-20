def hello(name,age):
     year=2022-age
     print(f"Hello {name} you were born in {year}")
def hello2(name):
     print(f"Hello {name}")  
    
     print("Welcome to Adalab")
def hello3(name):
    return f"Hello {name}" 
def hello_multi(*names):
     for name in names:
         print(f"Hello{name}")
def sum_number(numbers):
     number=0
     for number in numbers:
         sum=number
     return sum
def greet_multiple(**kwargs):
     print(kwargs)
    
def greet_multiple(**kwargs):
    keys=kwargs.keys()
    if "name" in keys:
        print("Hello {kwargs['name']")
    elif "country" in keys:
        print("Hello from{kwargs['country']")
    else:
        print("Hello anonymous")
        
def sum_and_greet(*args,**kwargs):
    print(args)
    print(kwargs)
   
    
    

