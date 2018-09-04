"""
Language
"""

from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1991)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
coders = [ruby, python, visual_basic]
print("The dynamically typed languages are:")
for coder in coders:
    if coder.is_dynamic():
        print("{}".format(coder.name))
