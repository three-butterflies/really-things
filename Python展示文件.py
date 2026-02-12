#!/usr/bin/env python3
"""
Python语法与特性综合示例
展示Python的各种语法、数据结构和高级特性
"""

import os
import sys
import math
import json
from typing import List, Dict, Tuple, Optional, Union, Any, Callable
from collections import Counter, namedtuple
from datetime import datetime
from dataclasses import dataclass
from functools import reduce, lru_cache
from abc import ABC, abstractmethod
import itertools
import re

# ============================================
# 1. 基本语法与数据结构
# ============================================

def basic_syntax_demo():
    """基础语法示例"""
    
    # 变量与基本数据类型
    integer_var = 42
    float_var = 3.14159
    string_var = "Hello, Python!"
    boolean_var = True
    none_var = None
    
    print("=" * 50)
    print("1. 基本语法与数据结构")
    print("=" * 50)
    print(f"整数: {integer_var}, 类型: {type(integer_var)}")
    print(f"浮点数: {float_var}, 类型: {type(float_var)}")
    print(f"字符串: {string_var}, 类型: {type(string_var)}")
    print(f"布尔值: {boolean_var}, 类型: {type(boolean_var)}")
    print(f"None: {none_var}, 类型: {type(none_var)}")
    
    # 算术运算
    a, b = 10, 3
    print(f"\n算术运算: {a} + {b} = {a + b}")
    print(f"算术运算: {a} - {b} = {a - b}")
    print(f"算术运算: {a} * {b} = {a * b}")
    print(f"算术运算: {a} / {b} = {a / b}")
    print(f"算术运算: {a} // {b} = {a // b} (整除)")
    print(f"算术运算: {a} % {b} = {a % b} (取余)")
    print(f"算术运算: {a} ** {b} = {a ** b} (幂运算)")
    
    # 比较运算
    print(f"\n比较运算: {a} > {b} = {a > b}")
    print(f"比较运算: {a} == {b} = {a == b}")
    print(f"比较运算: {a} != {b} = {a != b}")
    
    # 逻辑运算
    x, y = True, False
    print(f"\n逻辑运算: {x} and {y} = {x and y}")
    print(f"逻辑运算: {x} or {y} = {x or y}")
    print(f"逻辑运算: not {x} = {not x}")
    
    # 位运算
    print(f"\n位运算: {a} & {b} = {a & b} (与)")
    print(f"位运算: {a} | {b} = {a | b} (或)")
    print(f"位运算: {a} ^ {b} = {a ^ b} (异或)")
    print(f"位运算: ~{a} = {~a} (取反)")
    print(f"位运算: {a} << 1 = {a << 1} (左移)")
    print(f"位运算: {a} >> 1 = {a >> 1} (右移)")
    
    # 字符串操作
    s1 = "Python"
    s2 = "Programming"
    print(f"\n字符串连接: '{s1}' + ' ' + '{s2}' = '{s1 + ' ' + s2}'")
    print(f"字符串重复: '{s1}' * 3 = '{s1 * 3}'")
    print(f"字符串切片: '{s2}'[2:6] = '{s2[2:6]}'")
    print(f"字符串长度: len('{s1}') = {len(s1)}")
    print(f"字符串格式化: f-string: {s1} {s2.lower()} = {s1} {s2.lower()}")
    print(f"字符串格式化: format: {s1} has {len(s1)} letters = {s1} has {len(s1)} letters")
    
    # 类型转换
    print(f"\n类型转换: str({integer_var}) = '{str(integer_var)}'")
    print(f"类型转换: int('100') = {int('100')}")
    print(f"类型转换: float('3.14') = {float('3.14')}")
    print(f"类型转换: bool(0) = {bool(0)}, bool(1) = {bool(1)}")
    print(f"类型转换: chr(65) = '{chr(65)}', ord('A') = {ord('A')}")

# ============================================
# 2. 控制流
# ============================================

def control_flow_demo():
    """控制流示例"""
    
    print("\n" + "=" * 50)
    print("2. 控制流")
    print("=" * 50)
    
    # if-elif-else
    score = 85
    print(f"\nif-elif-else (分数: {score}):")
    
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    print(f"  等级: {grade}")
    
    # 三元表达式
    status = "通过" if score >= 60 else "未通过"
    print(f"  三元表达式: {status}")
    
    # for循环
    print("\nfor循环:")
    print("  遍历列表:")
    fruits = ["苹果", "香蕉", "橙子", "葡萄"]
    for i, fruit in enumerate(fruits):
        print(f"    索引 {i}: {fruit}")
    
    print("  遍历字典:")
    person = {"姓名": "张三", "年龄": 25, "城市": "北京"}
    for key, value in person.items():
        print(f"    {key}: {value}")
    
    print("  range循环:")
    for i in range(1, 6):
        print(f"    {i}", end=" ")
    print()
    
    # while循环
    print("\nwhile循环:")
    count = 5
    while count > 0:
        print(f"  倒计时: {count}")
        count -= 1
    
    # break, continue, pass
    print("\nbreak, continue, pass:")
    for i in range(10):
        if i == 2:
            print("  遇到2，跳过")
            continue
        if i == 7:
            print("  遇到7，结束循环")
            break
        if i == 5:
            pass  # 什么都不做，占位符
        print(f"  当前值: {i}")

# ============================================
# 3. 数据结构
# ============================================

def data_structures_demo():
    """数据结构示例"""
    
    print("\n" + "=" * 50)
    print("3. 数据结构")
    print("=" * 50)
    
    # 列表 (List)
    print("\n列表(List):")
    numbers = [1, 2, 3, 4, 5]
    print(f"  原始列表: {numbers}")
    numbers.append(6)  # 添加元素
    print(f"  添加6后: {numbers}")
    numbers.insert(0, 0)  # 插入元素
    print(f"  插入0后: {numbers}")
    numbers.remove(3)  # 删除元素
    print(f"  删除3后: {numbers}")
    popped = numbers.pop()  # 弹出最后一个元素
    print(f"  弹出元素后: {numbers}, 弹出的元素: {popped}")
    print(f"  列表切片[1:3]: {numbers[1:3]}")
    print(f"  列表切片[::-1] (反转): {numbers[::-1]}")
    
    # 列表推导式
    squares = [x**2 for x in range(1, 6)]
    even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
    print(f"  列表推导式 (平方): {squares}")
    print(f"  列表推导式 (偶数平方): {even_squares}")
    
    # 元组 (Tuple)
    print("\n元组(Tuple):")
    coordinates = (10, 20, 30)
    print(f"  坐标: {coordinates}")
    print(f"  第一个坐标: {coordinates[0]}")
    print(f"  解包元组:")
    x, y, z = coordinates
    print(f"    x={x}, y={y}, z={z}")
    
    # 字典 (Dictionary)
    print("\n字典(Dictionary):")
    student = {
        "name": "李四",
        "age": 20,
        "major": "计算机科学",
        "grades": {"数学": 90, "英语": 85, "编程": 95}
    }
    print(f"  学生信息: {student}")
    print(f"  姓名: {student['name']}")
    print(f"  专业: {student.get('major', '未指定')}")
    print(f"  所有键: {list(student.keys())}")
    print(f"  所有值: {list(student.values())}")
    
    # 字典推导式
    square_dict = {x: x**2 for x in range(1, 6)}
    print(f"  字典推导式: {square_dict}")
    
    # 集合 (Set)
    print("\n集合(Set):")
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print(f"  集合1: {set1}")
    print(f"  集合2: {set2}")
    print(f"  并集: {set1 | set2}")
    print(f"  交集: {set1 & set2}")
    print(f"  差集 (set1 - set2): {set1 - set2}")
    print(f"  对称差集: {set1 ^ set2}")
    
    # 集合推导式
    even_set = {x for x in range(10) if x % 2 == 0}
    print(f"  集合推导式 (偶数): {even_set}")
    
    # 字符串作为序列
    print("\n字符串作为序列:")
    text = "Python"
    print(f"  字符串: {text}")
    print(f"  第一个字符: {text[0]}")
    print(f"  最后一个字符: {text[-1]}")
    print(f"  长度: {len(text)}")
    print(f"  切片[1:4]: {text[1:4]}")
    print(f"  反转: {text[::-1]}")

# ============================================
# 4. 函数
# ============================================

def function_demo():
    """函数示例"""
    
    print("\n" + "=" * 50)
    print("4. 函数")
    print("=" * 50)
    
    # 基本函数
    def greet(name: str) -> str:
        """简单的问候函数"""
        return f"你好, {name}!"
    
    print(f"\n基本函数: {greet('王五')}")
    
    # 默认参数
    def power(base: float, exponent: float = 2) -> float:
        """计算幂，指数默认为2"""
        return base ** exponent
    
    print(f"\n默认参数: power(3) = {power(3)}")
    print(f"默认参数: power(3, 3) = {power(3, 3)}")
    
    # 可变参数 (*args)
    def sum_numbers(*args: float) -> float:
        """计算任意数量数字的和"""
        return sum(args)
    
    print(f"\n可变参数: sum_numbers(1, 2, 3, 4, 5) = {sum_numbers(1, 2, 3, 4, 5)}")
    
    # 关键字参数 (**kwargs)
    def print_info(**kwargs):
        """打印关键字参数"""
        for key, value in kwargs.items():
            print(f"    {key}: {value}")
    
    print("\n关键字参数:")
    print_info(name="张三", age=25, city="北京")
    
    # 函数作为参数
    def apply_operation(x: float, y: float, operation: Callable[[float, float], float]) -> float:
        """应用操作函数"""
        return operation(x, y)
    
    add = lambda a, b: a + b
    multiply = lambda a, b: a * b
    
    print(f"\n函数作为参数:")
    print(f"  apply_operation(5, 3, add) = {apply_operation(5, 3, add)}")
    print(f"  apply_operation(5, 3, multiply) = {apply_operation(5, 3, multiply)}")
    
    # lambda表达式
    print(f"\nlambda表达式:")
    numbers = [1, 2, 3, 4, 5]
    doubled = list(map(lambda x: x * 2, numbers))
    print(f"  原始列表: {numbers}")
    print(f"  使用lambda加倍: {doubled}")
    
    # 嵌套函数
    def outer_function(x: int) -> Callable[[int], int]:
        """外部函数，返回内部函数"""
        def inner_function(y: int) -> int:
            """内部函数，可以访问外部函数的变量"""
            return x + y
        return inner_function
    
    add_five = outer_function(5)
    print(f"\n嵌套函数: add_five(10) = {add_five(10)}")
    
    # 装饰器
    def timer_decorator(func: Callable) -> Callable:
        """计时装饰器"""
        def wrapper(*args, **kwargs):
            import time
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"    函数 {func.__name__} 执行时间: {end - start:.6f}秒")
            return result
        return wrapper
    
    @timer_decorator
    def slow_function(n: int) -> int:
        """模拟慢函数"""
        import time
        time.sleep(0.1)
        return n * 2
    
    print("\n装饰器:")
    result = slow_function(5)
    print(f"  结果: {result}")
    
    # 生成器函数
    def fibonacci_generator(n: int):
        """生成斐波那契数列的生成器"""
        a, b = 0, 1
        count = 0
        while count < n:
            yield a
            a, b = b, a + b
            count += 1
    
    print("\n生成器函数 (斐波那契数列前10项):")
    fib_gen = fibonacci_generator(10)
    fib_list = list(fib_gen)
    print(f"  {fib_list}")

# ============================================
# 5. 类与面向对象编程
# ============================================

class Animal(ABC):
    """抽象基类：动物"""
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    @abstractmethod
    def speak(self) -> str:
        """动物发声方法（抽象方法）"""
        pass
    
    def info(self) -> str:
        """返回动物信息"""
        return f"{self.name}, {self.age}岁"


class Dog(Animal):
    """狗类，继承自动物"""
    
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed
    
    def speak(self) -> str:
        """狗叫"""
        return "汪汪!"
    
    def info(self) -> str:
        """返回狗的信息"""
        return f"{super().info()}, 品种: {self.breed}"
    
    def __str__(self) -> str:
        """字符串表示"""
        return f"狗: {self.name}"
    
    def __repr__(self) -> str:
        """表示形式"""
        return f"Dog(name='{self.name}', age={self.age}, breed='{self.breed}')"


class Cat(Animal):
    """猫类，继承自动物"""
    
    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self.color = color
    
    def speak(self) -> str:
        """猫叫"""
        return "喵喵!"
    
    def info(self) -> str:
        """返回猫的信息"""
        return f"{super().info()}, 颜色: {self.color}"
    
    @property
    def age_in_cat_years(self) -> int:
        """猫的年龄（猫年）"""
        return self.age * 7
    
    @classmethod
    def create_kitten(cls, name: str, color: str) -> 'Cat':
        """类方法：创建小猫"""
        return cls(name, 0, color)
    
    @staticmethod
    def is_cat_sound(sound: str) -> bool:
        """静态方法：判断是否是猫的声音"""
        return sound.lower() in ["喵", "喵喵", "meow"]


@dataclass
class Point:
    """数据类：点"""
    x: float
    y: float
    
    def distance_to(self, other: 'Point') -> float:
        """计算到另一个点的距离"""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


def oop_demo():
    """面向对象编程示例"""
    
    print("\n" + "=" * 50)
    print("5. 类与面向对象编程")
    print("=" * 50)
    
    # 创建对象
    dog = Dog("旺财", 3, "金毛")
    cat = Cat("咪咪", 2, "白色")
    
    print(f"\n创建对象:")
    print(f"  狗: {dog}")
    print(f"  猫: {cat}")
    
    # 调用方法
    print(f"\n调用方法:")
    print(f"  {dog.name}说: {dog.speak()}")
    print(f"  {cat.name}说: {cat.speak()}")
    print(f"  {dog.info()}")
    print(f"  {cat.info()}")
    
    # 访问属性
    print(f"\n访问属性:")
    print(f"  狗的品种: {dog.breed}")
    print(f"  猫的颜色: {cat.color}")
    
    # 特殊方法
    print(f"\n特殊方法:")
    print(f"  str(dog): {str(dog)}")
    print(f"  repr(cat): {repr(cat)}")
    
    # 属性装饰器
    print(f"\n属性装饰器:")
    print(f"  猫的实际年龄: {cat.age}岁")
    print(f"  猫的猫年年龄: {cat.age_in_cat_years}猫岁")
    
    # 类方法和静态方法
    print(f"\n类方法和静态方法:")
    kitten = Cat.create_kitten("小咪", "黑白")
    print(f"  创建的小猫: {kitten.info()}")
    print(f"  '喵喵'是猫的声音吗? {Cat.is_cat_sound('喵喵')}")
    print(f"  '汪汪'是猫的声音吗? {Cat.is_cat_sound('汪汪')}")
    
    # 数据类
    print(f"\n数据类:")
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    print(f"  点1: {p1}")
    print(f"  点2: {p2}")
    print(f"  两点距离: {p1.distance_to(p2):.2f}")
    
    # 命名元组
    print(f"\n命名元组:")
    Person = namedtuple('Person', ['name', 'age', 'city'])
    person = Person('张三', 30, '上海')
    print(f"  人物: {person}")
    print(f"  姓名: {person.name}")
    print(f"  年龄: {person.age}")

# ============================================
# 6. 异常处理
# ============================================

def exception_handling_demo():
    """异常处理示例"""
    
    print("\n" + "=" * 50)
    print("6. 异常处理")
    print("=" * 50)
    
    # 基本异常处理
    print("\n基本异常处理:")
    
    def divide(a: float, b: float) -> float:
        """除法函数，处理除零异常"""
        try:
            result = a / b
        except ZeroDivisionError:
            print("  错误: 除数不能为零!")
            return float('inf') if a > 0 else float('-inf') if a < 0 else float('nan')
        except TypeError:
            print("  错误: 参数类型不正确!")
            return 0.0
        else:
            print(f"  除法成功: {a} / {b} = {result}")
            return result
        finally:
            print("  除法操作完成")
    
    print(f"  10 / 2 = {divide(10, 2)}")
    print(f"  10 / 0 = {divide(10, 0)}")
    print(f"  10 / 'a' = {divide(10, 'a')}")
    
    # 自定义异常
    print("\n自定义异常:")
    
    class NegativeNumberError(Exception):
        """负数异常"""
        def __init__(self, value: float):
            self.value = value
            super().__init__(f"负数错误: {value}")
    
    def square_root(x: float) -> float:
        """计算平方根，处理负数"""
        if x < 0:
            raise NegativeNumberError(x)
        return math.sqrt(x)
    
    try:
        print(f"  sqrt(4) = {square_root(4)}")
        print(f"  sqrt(-1) = {square_root(-1)}")
    except NegativeNumberError as e:
        print(f"  捕获自定义异常: {e}")
    
    # 多个异常处理
    print("\n多个异常处理:")
    
    def process_number(num_str: str):
        """处理数字字符串"""
        try:
            num = float(num_str)
            result = 100 / num
            print(f"  100 / {num} = {result}")
        except (ValueError, TypeError):
            print(f"  错误: '{num_str}' 不是有效的数字")
        except ZeroDivisionError:
            print(f"  错误: 除数不能为零")
        except Exception as e:
            print(f"  未知错误: {type(e).__name__}: {e}")
    
    process_number("10")
    process_number("0")
    process_number("abc")
    process_number([1, 2, 3])

# ============================================
# 7. 模块与导入
# ============================================

def module_import_demo():
    """模块与导入示例"""
    
    print("\n" + "=" * 50)
    print("7. 模块与导入")
    print("=" * 50)
    
    # 使用标准库模块
    print("\n使用标准库模块:")
    
    # math模块
    print(f"  math.pi = {math.pi:.5f}")
    print(f"  math.sin(math.pi/2) = {math.sin(math.pi/2):.5f}")
    print(f"  math.factorial(5) = {math.factorial(5)}")
    
    # datetime模块
    now = datetime.now()
    print(f"  datetime.now() = {now}")
    print(f"  当前日期: {now.date()}")
    print(f"  当前时间: {now.time()}")
    print(f"  格式化时间: {now.strftime('%Y年%m月%d日 %H:%M:%S')}")
    
    # re模块 (正则表达式)
    text = "我的电话是123-456-7890，邮箱是test@example.com"
    phone_pattern = r'\d{3}-\d{3}-\d{4}'
    email_pattern = r'[\w\.-]+@[\w\.-]+'
    
    phone_match = re.search(phone_pattern, text)
    email_match = re.search(email_pattern, text)
    
    print(f"\n正则表达式匹配:")
    print(f"  文本: {text}")
    if phone_match:
        print(f"  找到电话: {phone_match.group()}")
    if email_match:
        print(f"  找到邮箱: {email_match.group()}")
    
    # itertools模块
    print(f"\nitertools模块:")
    letters = ['A', 'B', 'C']
    combinations = list(itertools.combinations(letters, 2))
    permutations = list(itertools.permutations(letters, 2))
    
    print(f"  字母列表: {letters}")
    print(f"  所有2个字母的组合: {combinations}")
    print(f"  所有2个字母的排列: {permutations}")
    
    # collections模块
    print(f"\ncollections模块:")
    counter = Counter("abracadabra")
    print(f"  字符串'abracadabra'中字符出现次数:")
    for char, count in counter.most_common(3):
        print(f"    {char}: {count}次")

# ============================================
# 8. 文件操作
# ============================================

def file_operations_demo():
    """文件操作示例"""
    
    print("\n" + "=" * 50)
    print("8. 文件操作")
    print("=" * 50)
    
    # 写入文件
    print("\n文件写入:")
    
    data = {
        "name": "张三",
        "age": 25,
        "courses": ["数学", "物理", "计算机"],
        "graduated": False
    }
    
    with open("example.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("  已写入 example.json 文件")
    
    # 读取文件
    print("\n文件读取:")
    
    with open("example.json", "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
    
    print(f"  从文件读取的数据: {json.dumps(loaded_data, ensure_ascii=False, indent=2)}")
    
    # 读写文本文件
    print("\n文本文件操作:")
    
    # 写入文本文件
    with open("example.txt", "w", encoding="utf-8") as f:
        f.write("这是第一行\n")
        f.write("这是第二行\n")
        f.write("这是第三行\n")
    
    print("  已写入 example.txt 文件")
    
    # 读取文本文件
    print("\n  读取文本文件内容:")
    with open("example.txt", "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            print(f"    第{i}行: {line.strip()}")
    
    # 使用上下文管理器
    print("\n上下文管理器:")
    
    class FileManager:
        """自定义文件管理器"""
        def __init__(self, filename, mode):
            self.filename = filename
            self.mode = mode
        
        def __enter__(self):
            self.file = open(self.filename, self.mode, encoding="utf-8")
            print(f"  打开文件: {self.filename}")
            return self.file
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            self.file.close()
            print(f"  关闭文件: {self.filename}")
            if exc_type:
                print(f"  发生异常: {exc_type.__name__}: {exc_val}")
            return True  # 抑制异常
    
    with FileManager("test.txt", "w") as f:
        f.write("测试自定义上下文管理器\n")
    
    print("  自定义上下文管理器测试完成")
    
    # 清理临时文件
    import os
    for filename in ["example.json", "example.txt", "test.txt"]:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"  已删除临时文件: {filename}")

# ============================================
# 9. 高级特性
# ============================================

def advanced_features_demo():
    """高级特性示例"""
    
    print("\n" + "=" * 50)
    print("9. 高级特性")
    print("=" * 50)
    
    # 迭代器与生成器表达式
    print("\n迭代器与生成器表达式:")
    
    numbers = [1, 2, 3, 4, 5]
    squares_gen = (x**2 for x in numbers)  # 生成器表达式
    squares_list = [x**2 for x in numbers]  # 列表推导式
    
    print(f"  原始列表: {numbers}")
    print(f"  生成器表达式: {squares_gen}")
    print(f"  转换为列表: {list(squares_gen)}")
    print(f"  列表推导式: {squares_list}")
    
    # 装饰器缓存
    print("\n装饰器缓存 (lru_cache):")
    
    @lru_cache(maxsize=32)
    def fibonacci(n: int) -> int:
        """计算斐波那契数，使用缓存"""
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    print("  计算斐波那契数列:")
    for i in range(10):
        print(f"    fibonacci({i}) = {fibonacci(i)}")
    
    # 函数式编程
    print("\n函数式编程:")
    
    numbers = [1, 2, 3, 4, 5]
    
    # map
    doubled = list(map(lambda x: x * 2, numbers))
    print(f"  map (加倍): {doubled}")
    
    # filter
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"  filter (偶数): {evens}")
    
    # reduce
    product = reduce(lambda x, y: x * y, numbers)
    print(f"  reduce (乘积): {product}")
    
    # 类型注解与类型检查
    print("\n类型注解:")
    
    def add_numbers(a: int, b: int) -> int:
        """添加类型注解的函数"""
        return a + b
    
    print(f"  add_numbers(3, 5) = {add_numbers(3, 5)}")
    print(f"  函数注解: {add_numbers.__annotations__}")
    
    # 枚举
    print("\n枚举:")
    
    from enum import Enum, auto
    
    class Color(Enum):
        RED = auto()
        GREEN = auto()
        BLUE = auto()
    
    print("  颜色枚举:")
    for color in Color:
        print(f"    {color.name}: {color.value}")
    
    # 异步编程示例 (简单展示)
    print("\n异步编程 (概念示例):")
    print("  async/await 用于异步I/O操作")
    print("  asyncio 库提供事件循环")
    print("  示例: async def fetch_data(): ...")
    
    # 多线程/多进程 (概念示例)
    print("\n并发编程 (概念示例):")
    print("  threading 模块用于多线程")
    print("  multiprocessing 模块用于多进程")
    print("  concurrent.futures 提供高级接口")

# ============================================
# 10. 综合示例
# ============================================

def comprehensive_example():
    """综合示例：计算学生成绩统计"""
    
    print("\n" + "=" * 50)
    print("10. 综合示例：学生成绩统计系统")
    print("=" * 50)
    
    @dataclass
    class Student:
        """学生数据类"""
        id: int
        name: str
        scores: Dict[str, float]
        
        @property
        def average_score(self) -> float:
            """计算平均分"""
            if not self.scores:
                return 0.0
            return sum(self.scores.values()) / len(self.scores)
        
        @property
        def total_score(self) -> float:
            """计算总分"""
            return sum(self.scores.values())
        
        def add_score(self, subject: str, score: float):
            """添加科目成绩"""
            self.scores[subject] = score
        
        def get_grade(self) -> str:
            """获取等级"""
            avg = self.average_score
            if avg >= 90:
                return "A"
            elif avg >= 80:
                return "B"
            elif avg >= 70:
                return "C"
            elif avg >= 60:
                return "D"
            else:
                return "F"
    
    class GradeSystem:
        """成绩管理系统"""
        
        def __init__(self):
            self.students: List[Student] = []
        
        def add_student(self, student: Student):
            """添加学生"""
            self.students.append(student)
        
        def get_class_average(self) -> float:
            """获取班级平均分"""
            if not self.students:
                return 0.0
            total = sum(student.average_score for student in self.students)
            return total / len(self.students)
        
        def get_top_students(self, n: int = 3) -> List[Student]:
            """获取前n名学生"""
            sorted_students = sorted(self.students, 
                                    key=lambda s: s.average_score, 
                                    reverse=True)
            return sorted_students[:n]
        
        def get_subject_average(self, subject: str) -> float:
            """获取科目平均分"""
            scores = []
            for student in self.students:
                if subject in student.scores:
                    scores.append(student.scores[subject])
            
            if not scores:
                return 0.0
            return sum(scores) / len(scores)
        
        def generate_report(self) -> Dict[str, Any]:
            """生成报告"""
            report = {
                "total_students": len(self.students),
                "class_average": self.get_class_average(),
                "subject_averages": {},
                "grade_distribution": Counter(),
                "top_students": []
            }
            
            # 计算各科目平均分
            subjects = set()
            for student in self.students:
                subjects.update(student.scores.keys())
            
            for subject in subjects:
                report["subject_averages"][subject] = self.get_subject_average(subject)
            
            # 计算等级分布
            for student in self.students:
                report["grade_distribution"][student.get_grade()] += 1
            
            # 获取前三名学生
            top_students = self.get_top_students(3)
            for student in top_students:
                report["top_students"].append({
                    "id": student.id,
                    "name": student.name,
                    "average_score": student.average_score,
                    "grade": student.get_grade()
                })
            
            return report
    
    # 创建成绩管理系统
    system = GradeSystem()
    
    # 添加学生
    students_data = [
        (1, "张三", {"数学": 85, "英语": 90, "物理": 78}),
        (2, "李四", {"数学": 92, "英语": 88, "物理": 95}),
        (3, "王五", {"数学": 76, "英语": 82, "物理": 79}),
        (4, "赵六", {"数学": 88, "英语": 91, "物理": 84}),
        (5, "钱七", {"数学": 95, "英语": 96, "物理": 92}),
    ]
    
    for id, name, scores in students_data:
        student = Student(id, name, scores)
        system.add_student(student)
    
    # 生成报告
    report = system.generate_report()
    
    # 打印报告
    print(f"\n学生成绩统计报告:")
    print(f"  学生总数: {report['total_students']}")
    print(f"  班级平均分: {report['class_average']:.2f}")
    
    print(f"\n  各科目平均分:")
    for subject, avg in report["subject_averages"].items():
        print(f"    {subject}: {avg:.2f}")
    
    print(f"\n  成绩等级分布:")
    for grade, count in report["grade_distribution"].items():
        print(f"    {grade}: {count}人")
    
    print(f"\n  前三名学生:")
    for i, student in enumerate(report["top_students"], 1):
        print(f"    第{i}名: {student['name']} (ID: {student['id']})")
        print(f"      平均分: {student['average_score']:.2f}, 等级: {student['grade']}")

# ============================================
# 主程序
# ============================================

def main():
    """主函数"""
    print("Python语法与特性综合示例")
    print("=" * 60)
    
    # 执行所有演示函数
    demos = [
        basic_syntax_demo,
        control_flow_demo,
        data_structures_demo,
        function_demo,
        oop_demo,
        exception_handling_demo,
        module_import_demo,
        file_operations_demo,
        advanced_features_demo,
        comprehensive_example
    ]
    
    for i, demo_func in enumerate(demos, 1):
        try:
            demo_func()
        except Exception as e:
            print(f"\n演示{i}出现错误: {type(e).__name__}: {e}")
        
        if i < len(demos):
            print("\n" + "=" * 60)
            input("按回车键继续...")
            print()
    
    print("\n" + "=" * 60)
    print("所有演示完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()