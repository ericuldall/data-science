#!/usr/bin/python
import importlib.machinery
loader = importlib.machinery.SourceFileLoader("data", "lib/data.py")
data = loader.load_module()
list_math = data.ListMath([1, 2, 3, 4, 5])


print(list_math.getRange());
