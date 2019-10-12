import difflib

text1 = """
what a wonderful day.
my name is Lilei.
I'm 12.
"""
text2 = """
what a wonderful day.
my name is Hanmeimei.
I'm 9!
"""


text1_lines = text1.splitlines()
text2_lines = text2.splitlines()

diff = difflib.unified_diff(text1_lines,
                            text2_lines,
                            lineterm='',)

print('\n'.join(list(diff)))
