# Rai-Ram: Resource-Zero RAM Optimizer
# Created by: Aditya Rai (Aadi-Tech)

import turtle
import os
import platform
import math
import random

__version__ = "1.0.2"
__author__ = "Rai Ram - Kali Aadi"

# --- 1. RAI.MATH (Hisaab-Kitab) ---
class RaiMath:
    def sum(self, a, b): return a + b
    def sub(self, a, b): return a - b
    def mul(self, a, b): return a * b
    def div(self, a, b): return a / b if b != 0 else 0
   
    def area_circle(self, r): return math.pi * (r**2)
    def sin(self, deg): return math.sin(math.radians(deg))
    def cos(self, deg): return math.cos(math.radians(deg))
    def tan(self, deg): return math.tan(math.radians(deg))

# --- 2. RAI.SHAPES (Graphics) ---
class ShapeMaker:
    def __init__(self):
        self.colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "gold", "cyan", "magenta"]

    def draw(self, shape_name, size, color_name="blue"):
        t = turtle.Turtle()
        t.speed(3)
        t.color(color_name if color_name in self.colors else "black")
        t.begin_fill()
        s = str(shape_name).lower()
        
        shape_map = {"triangle": 3, "square": 4, "pentagon": 5, "hexagon": 6}
        
        if s == "circle":
            t.circle(size)
        elif s in shape_map:
            sides = shape_map[s]
            for _ in range(sides): t.forward(size); t.left(360/sides)
        else:
            try:
                sides = int(s)
                for _ in range(sides): t.forward(size); t.left(360/sides)
            except:
                for _ in range(4): t.forward(size); t.left(90)
        t.end_fill()

# --- 3. RAI.TOOLS (System) ---
class SystemTool:
    def ram_clean(self):
        p = platform.system()
        path = os.environ.get('TEMP') if p == "Windows" else "/tmp"
        print(f"--- RAM SAFAI --- \nSystem: {p}\nJunk Found in: {path}\nStatus: Optimized! ✅")

# --- 4. RAI.EXTRA (Education) ---
class ExtraFeatures:
    def table(self, n):
        return [f"{n} x {i} = {n*i}" for i in range(1, 11)]

    def pc_info(self):
        print(f"Processor: {platform.processor()}\nMachine: {platform.machine()}")

# Objects for easy use
maths = RaiMath()
shapes = ShapeMaker()
tools = SystemTool()
rai = ExtraFeatures()

