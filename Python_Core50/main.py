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

# """
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
# """