import math

a=int(input("enter a number:"))
op=input("enter op(sin ,cos ,tan ,factorial ,sqrt):")
sin=math.sin
cos=math.cos
tan=math.tan
factorial=math.factorial
sqrt=math.sqrt

if op == "sin":
    r=sin(a)

if op == "cos":
    r=cos(a)

if op == "tan":
    r=tan(a)

if op == "factorial":
    r=factorial(a)

if op == "sqrt":
    r=sqrt(a)

print(r)