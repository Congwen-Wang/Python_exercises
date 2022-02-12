# 面向对象编程

"""
# 一、教学例子（最简单的例子）
# step1 定义类和方法
class Student:

    def study(self,course_name):
        print(f'He/She is studying {course_name}.')

    def play(self):
        print(f'He/She is playing.')

# step2 创建对象
stu1 = Student()
print(stu1)

# step3 调用方法
stu1.study('CS') # 对象.方法
"""

"""
# 二、增加「初始化」和「返回」
# step1 定义类和方法
class Student: # 定义类

    def __init__(self, name, age): # 初始化方法
        self.name = name
        self.age = age

    def study(self, course_name): # 定义方法
        print(f'{self.name} is studying {course_name}.')

    def play(self): # 定义方法
        print('They are playing.')

    def __repr__(self):
        return f'{self.name}: {self.age}'

# step2 创建对象
stu1 = Student('Peter', 18)
print(stu1) # 增加了「返回」，所以这里会打印出返回值

# step3 调用方法
stu1.study('CS')
"""

"""
# 三、练习例子 定义一个类描述数字时钟
import time
class Clock(object):

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.min = minute
        self.sec = second

    def run(self):
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1
            if self.min == 60:
                self.min = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0
    def show(self):
        return f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}'

clock = Clock(0,0,0)
while True:
    print(clock.show())
    time.sleep(1)
    clock.run()
"""

"""
# 四、练习例子 定义一个类描述平面上的点，要求提供计算到另一个点距离的方法。
class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def distance_to(self,target):
        dx = self.x - target.x
        dy = self.y - target.y
        return (dx * dx + dy * dy) ** 0.5
    def __str__(self):
        return f'({self.x},{self.y})'

p1 = Point(3,5)
p2 = Point(6,9)
print(p1, p2)
print(p1.distance_to(p2))
"""

# 字典
"""
# 一、教学例子（最简单的例子）
xinhua = {
    '麓': '山脚下',
    '路': '道,往来通行的地方;方面,地区:南~货,外~货;种类:他俩是一~人',
    '蕗': '甘草的别名',
    '潞': '潞水,水名,即今山⻄省的浊漳河;潞江,水名,即云南省的怒江'
}
print(xinhua)

person = {
    'name': '王大锤',
    'age': 55,
    'weight': 60,
    'office': '科华北路62号',
    'home': '中同仁路8号',
    'tel': '13122334455',
    'econtact': '13800998877'
}
print(person)
"""

# """
# 二、练习例子
sentence = input('请输入一句话：')
counter = {}
for ch in sentence:
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        counter[ch] = counter.get(ch, 0) +1
for key, value in counter.items():
    print(f'字母{key}出现了{value}次。')
# """