import sys
print("before:")
print(sys.path)
sys.path.append(r'/home/ubuntu/.local/lib/python3.6/site-packages')
print("after:", sys.path)



import pandas

s1 = pandas.Series(["B", "a", "C"])
print(s1.sort_values())
print("Hello World from python")
