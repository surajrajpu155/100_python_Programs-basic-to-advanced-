# 93. Write a program to print all prime numbers between two given numbers a and b.

"""
DAY 8/75
PYTHON PROJECT JOURNEY
"""

import random

name = input("Enter your name: ").lower()
number = random.randint(10, 99)

styles = [
    # Aesthetic & Minimalist
    "_" + name + "_",
    name + "_visuals",
    name + ".jpeg",
    name + "x",
    
    # Personal Brand & Daily Life
    "its_" + name,
    "i_am_" + name,
    "just_" + name,
    name + "_diaries",
    name + "_journal",
    
    # Curated & Club Vibes
    "the_" + name,
    name + "_society",
    name + "_club",
    "vibe_" + name,
    
    # Combined with Numbers (Like your original style)
    name + "_" + str(number),
    "its_" + name + str(number)
]

print("\n✨ USERNAME GENERATOR")

for i, username in enumerate(styles, 1):
    print(f"{i}. @{username}")
