#单号注释
'''
多行注释
'''

#输出语句
print("hello")

#变量
'''
name = "大吉"
age = 23
print(type(age))
print(name,age)
'''
#input函数 ：让用户输入
'''
input("name:")
input("passwork:")
'''
_name = input("name:")
_passwork = input("passwork:")
_age = int(input("age:"))
print(type(_age))

show ='''
----------  输出  ： ------------
name:{name}
passwork:{passwork}
'''.format(name=_name,passwork=_passwork)

print(show)
