#返回商和模
m = divmod(5, 5)
print(m)

d = 5//3
print(d)

#x**y   x 的 y 次方
p = 2**3
p = pow(2, 3)
print(p)

#求绝对值
a = abs(-1)
print(a)

#复数
c = complex(4, 5)
b = c.conjugate()
print(c)
print(b)

#转换
x = 11
i=int(x)   #x converted to integer	(2)
#l=long(x)    #x converted to long integer	(2)
f=float(x)    #x converted to floating point

print(x)
print(f)

b'\x00\x10'
#位操作
d = 1^2      #异或 相同则为0 不同则为 1
print(d)

print(2**12)

print(int.from_bytes(b'\x00\x10', byteorder='little'))
b = (2).to_bytes(2,byteorder='big')

for i in b:
    print(i)

#list
lists = []
lists.append(1)
lists.append(2)
print(lists)

# 共亨同一个 [[]] is a one-element list containing an empty list, so all three elements of [[]] * 3 are references to this single empty list
lists = [[]] * 3
lists[0].append(3)
lists[0].append(4)
lists[2].append(5)
print(lists)

#独立
lists = [[] for i in range(3)]
lists[0].append(3)
lists[0].append(4)
lists[1].append(5)
lists[2].append(7)
print(lists)

#tuple 元组,可以存放不同的对象
t = [1,"b"]
t = tuple([1,'b'])
print(t)

# result = [obj.method() for obj in mylist]

#dict 字典
dict = {"a" : "apple", "b" : "banana", "g" : "grape", "o" : "orange"}

print(dict['a'])

none = None
print(none)

#rang 是不可变的类
lists = list(range(10))
lists.insert(2, 8)
print(lists)

#字符串
s = str(b'abAc', encoding='utf-8', errors='strict')
#s = str('你好')
s="abdfdfAdfdf"
print(s.title())
print(s.capitalize())
