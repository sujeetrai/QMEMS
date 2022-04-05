def myreduce(add,list_1):
    return a
def add(a,b):
    return a+b
list_1=[10,15,25,40,10]
a=list_1[0]
for i in range(1,len(list_1)):
    b=list_1[i]
    a=add(a,b)
print(myreduce(add,list_1))
100

def is_even(a):
    if a%2==0:
        return True
list_1=[2,3,4,5,6,7,8,9,12345,5678,890,1234,567]
list(filter(is_even,list_1))
[2, 4, 6, 8, 5678, 890, 1234]

letters = list('xyz')
pattern = []
[pattern.append(letters[i]*j) for i in range(len(letters)) for j in range(1,5)]

print(pattern)
['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']

[i*j for j in range(1,5) for i in 'xyz'] 
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']

[[x+y] for x in range(2,5)for y in range(3)]
[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]

[(x,y) for x in range(1,4) for y in range(1,4)]
[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]