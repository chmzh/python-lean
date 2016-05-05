from importlib import import_module

abcd = import_module("com.abc.abcd")
#abcd = import_module("abcd",package="com.abc")
test=abcd.Test("你好")
print(test.getname())
