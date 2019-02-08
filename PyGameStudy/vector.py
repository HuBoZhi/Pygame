# -*- coding: utf-8 -*-
# Time : 2019/2/3 17:51 
# Author : hubozhi
import math

# 我们先考虑二维的向量，三维也差不多了，而游戏中的运动最多只用得到三维，更高的留给以后的游戏吧
# 向量的表示和坐标很像，(10, 20)
# 对坐标而言，就是一个固定的点，然而在向量中，它意味着x方向行进10，y方向行进20，所以坐标(0, 0)加上向量(10,20)后，就到达了点(10,20)
# 向量可以通过两个点来计算出来，如下图，A经过向量AB到达了B，则向量AB就是(30, 35) – (10, 20) = (20, 15)。
# 我们也能猜到向量BA会是(-20,-15)，注意向量AB和向量BA，虽然长度一样，但是方向不同。
# 创建向量
# 在Python中，我们可以创建一个类来存储和获得向量（虽然向量的写法很像一个元组，但因为向量有很多种计算，必须使用类来完成）：

class Vec2d():
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    @classmethod
    def from_points(cls, P1, P2):
        return cls(P2[0]-P1[0], P2[1]-P1[1])

    # 向量的大小可以简单的理解为那根箭头的长度，勾股定理熟稔的各位立刻知道怎么计算了
    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # 一开头说过，向量有着大小和方向两个要素，通过刚刚的例子，我们可以理解这两个意思了。在向量的大家族里，有一种比较特殊的向量叫“单位向量”，
    # 意思是大小为1的向量，我们还能把任意向量方向不变的缩放（体现在数字上就是x和y等比例的缩放）到一个单位向量，这叫向量的规格（正规）化，
    # 代码体现如下：
    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude

    def __add__(self, rhs):
        return super(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return super(self.x - rhs.x, self.y - rhs.y)

    def __mul__(self, scalar):
        return Vec2d(self.x * scalar, self.y * scalar)

    def __rtruediv__(self, scalar):
        return Vec2d(self.x / scalar, self.y / scalar)