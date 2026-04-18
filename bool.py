#when false is come:
# anythime variable has an empty set,list,turple, and empty braces, it will always returs false and the boolean 
a = ()
print(bool(a))
ab= []
print(bool(ab))
x = ''
print(bool(x))
g = False
print(bool(g))
#when true is come:
# true will come when something has been assigned to the variable rather than being empty
a = "hi"
print(bool(a))
b = True
print(bool(b))
c= 10
print(bool(c))
d= {"name" : "oladimeji"}
print(bool(d))
g = {1,2,3,4,5}
print(bool(g))