#def do_twice (f):
#    f()
#    f()

#def print_spam():
#    print('spam')

def print_twice(x):
    print(x)
    print(x)
    
def do_twice (t, s):
    t(s)
    t(s)
 
do_twice(print_twice, "spam")