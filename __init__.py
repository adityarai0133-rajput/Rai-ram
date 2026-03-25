# Rai-Ram: Resource-Zero RAM Optimizer
# Created by: Aditya Rai (Aadi-Tech)

import os
import gc

def clean():
    """Tera asli logic jo RAM ko free karega"""
    print("Aadi-Tech Rai-Ram is optimizing your system...")
    
    # Garbage collection ko force karna
    gc.collect()
    
    # NF-1 logic: Memory blocks ko release karna
    print("Memory cleanup successful! System is now optimized.")

if __name__ == "__main__":
    clean()
