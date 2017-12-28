#1、单号注释
'''
多行注释
'''

#2、输出语句
# print("hello")

#3、说变量
'''
name = "大吉"
age = 23
print(type(age))
print(name,age)
'''
#4、input函数 ：让用户输入
'''                      
input("name:")
input("passwork:")
'''
'''
_name = input("name:")
_passwork = input("passwork:")
_age = int(input("age:"))
print(type(_age))
'''

#5、format格式化

# show ='''
# ----------  输出  ： ------------
# name:{name}
# passwork:{passwork}
# '''.format(name=_name,passwork=_passwork)_passwork

#print(show)

#6、if-else 流程判断

# username = "jinzhong"
# passwork = 12345
# print(type(passwork))
#
# username_ = input("username :")
# passwork_ = int(input("passwork:"))
# print(type(passwork_))
#
# if username == username_ and passwork == passwork_ :
#     print("{name}欢迎您登陆。。。。".format(name = username_))
# else:
#     print("账号或密码错误")

# 猜数字游戏
# answer = 24
#
# guess = int(input("guess:"))
#
# if guess == answer :
#     print("恭喜你，答对了。。")
# elif guess > answer :
#     print("猜大了，请往小一点的猜。。")
# else:
#     print("猜小了，请往大一点的猜。。")

#7、密码加密   注意：pycharm是无法实现getpass模块的加密
import getpass

username = "jizhong"
passwork = 123456

username_ = input("请输入你的名字:")
passwork_ = getpass.getpass(input("请输入你的密码:"))



























