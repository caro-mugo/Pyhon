from multiprocessing.connection import answer_challenge


def add(a,b):
    answer=a+b
    return answer

def multiply(a,b):
     answer=a*b
     return answer
def subtract(a,b):
    answer=a+b
    return answer
def division(a,b):
    answer=a/b
    return answer
def modulus (a,b):
    answer=a%b
    return answer
def square (a,b):
    answer=a**b
    return answer
def exponent(a,b):
    answer=a**b
def integer_division(a,b):   
    answer=a//b
def cube (a,b): 
    answer=a*a*a   
def factl(a):  
    fact=1
    for num in range (1, a+1):
        fact *=num
    return fact





  