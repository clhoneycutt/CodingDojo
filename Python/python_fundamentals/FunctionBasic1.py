def a():
    return 5
print(a())     

  -|-
a()|5


Output: 5

# -------------------------------------------------------------------

def a():
    return 5
print(a()+a())     

  -|-
a()|5

Output: 10

# -------------------------------------------------------------------

def a():
    return 5
    return 10
print(a())     

  -|-
a()|5

Output: 5

# -------------------------------------------------------------------

def a():
    return 5
    print(10)
print(a())     

  -|-
a()|5

Output: 5

# -------------------------------------------------------------------

def a():
    print(5)
x = a()
print(x)     

  -|-
a()|-
  x|-


Output: 5

# -------------------------------------------------------------------

def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))   

  -|-
  b|1
  c|2
a()|-
  b|2
  c|3
a()|-

Output: 3, 5, None

# -------------------------------------------------------------------

def a(b,c):
    return str(b)+str(c)
print(a(2,5))

  -|-
  b|2
  c|5
a()|25

Output: 25

# -------------------------------------------------------------------

def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())  

  -|-
  b|100
a()|10

Output: 10

# -------------------------------------------------------------------

def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

  -|-
  b|2
  c|3
a()|7
  b|5
  c|3
a()|14
  b|2
  c|3
a()|7
  b|5
  c|3
a()|14

Output: 7, 14, 21

# -------------------------------------------------------------------

def a(b,c):
    return b+c
    return 10
print(a(3,5))     
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)  
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)  
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)