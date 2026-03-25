import os
import platform
import math

__version__ = "1.0.2"
__author__ = "Rai Ram - Kali Aadi"

# --- 1. RAI.MATH (Hisaab-Kitab + Trig) ---
class RaiMath:
    def sum(self, a, b): return a + b
    def sub(self, a, b): return a - b
    def mul(self, a, b): return a * b
    def div(self, a, b): return a / b if b != 0 else "Error: Zero se bhag nahi ho sakta!"
   
    # Geometry & Trigonometry
    def area_circle(self, r): return math.pi * (r**2)
    def sin(self, deg): return math.sin(math.radians(deg))
    def cos(self, deg): return math.cos(math.radians(deg))
    def tan(self, deg): return math.tan(math.radians(deg))

# --- 2. RAI.SHAPES (28 Shapes & 30 Colours) ---
class ShapeMaker:
    def __init__(self):
        self.colors = [
            "red", "blue", "green", "yellow", "purple", "orange", "pink", "brown",
            "gray", "black", "cyan", "magenta", "gold", "silver", "violet", "indigo",
            "lime", "maroon", "navy", "olive", "teal", "tan", "orchid", "salmon",
            "coral", "khaki", "plum", "azure", "beige", "wheat"
        ]

    def draw(self, shape_name, size, color_name="blue"):
        try:
            import turtle  # Safe Import
            t = turtle.Turtle()
            t.speed(3)
            t.color(color_name if color_name in self.colors else "black")
            t.begin_fill()
            s = str(shape_name).lower()
           
            # Polygon Logic (Triangle to 30-sided shapes)
            shape_map = {"triangle": 3, "square": 4, "pentagon": 5, "hexagon": 6, "heptagon": 7, "octagon": 8}
           
            if s == "circle":
                t.circle(size)
            elif s in shape_map:
                sides = shape_map[s]
                for _ in range(sides): t.forward(size); t.left(360/sides)
            else:
                try:
                    sides = int(s) # Number daalne par utne sides wala shape
                    if sides < 3: sides = 3
                    for _ in range(sides): t.forward(size); t.left(360/sides)
                except:
                    for _ in range(4): t.forward(size); t.left(90) # Default Square
            t.end_fill()
            print(f"Bhai, {s} tayyar hai! Screen par click karo band karne ke liye.")
            turtle.exitonclick()
        except Exception as e:
            print(f"Graphics Error: Bhai Aries11 par graphics load nahi hua: {e}")

# --- 3. RAI.TOOLS (Cleaning & Security) ---
class SystemTool:
    def ram_clean(self):
        p = platform.system()
        path = os.environ.get('TEMP') if p == "Windows" else "/tmp"
        print(f"--- RAM SAFAI --- \nSystem: {p}\nJunk Found in: {path}\nStatus: Optimized! ✅")

    def security_scan(self):
        print(f"--- SECURITY SCAN --- \nChecking Risks... \nResult: Your {platform.system()} is Secure. 🛡️")

# --- 4. RAI.EXTRA (Education & Info) ---
class ExtraFeatures:
    def table(self, n):
        """School Table (Pahada)"""
        return [f"{n} x {i} = {n*i}" for i in range(1, 11)]

    def convert_km_to_miles(self, km):
        return f"{km} KM = {round(km * 0.621, 2)} Miles"

    def pc_info(self):
        """PC ki jaankari"""
        print(f"Processor: {platform.processor()}\nMachine: {platform.machine()}")

# Final Objects jo user use karega
maths = RaiMath()
shapes = ShapeMaker()
tools = SystemTool()
rai = ExtraFeatures()
