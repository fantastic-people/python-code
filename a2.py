import re

key = r"<h1>hello world</h1>"
p1 = r"<h([1-6])>.*?</h\1>"
pattern1 = re.compile(p1)
m1 = re.search(pattern1,key)
print(m1.group(0))#这里是会报错的，因为匹配不到，你如果将源字符串改成</h1>