def do_twice(t, s, r):
    t(s,r)
    t(s,r)

def do_four(fun, y, z):
    do_twice(fun, y, z)
    do_twice(fun, y, z)
 
#def print_twice(x):
#    print(x)
#    print(x)

def soma(x,y):
    s = x+y
    print(s)
    return s
  
do_four(soma, 3, 2)    
