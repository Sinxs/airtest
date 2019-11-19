from urllib.request import quote
from pyquery import pyquery as pq
import requests
import pandas as pd


# def get_text_page(movie_name):
test = ["01","02","03","04","05"]
test.pop(1)
test.remove("04")
del test[1:3]
# test.insert(1,"02")
print(test)

b_list = list(range(1, 5))

print(b_list)# 将第2个到第4个（不包含）元素赋值为新列表的元素

b_list[1: 3] = ['a', 'b']

print(b_list) # [1, 'a', 'b', 4]
b_list[2:2] = ["x","y"]
print(b_list)


listtest = ["01","02","03","04","05","06","07","08"]
listtest[1:3] = []
del listtest[3::2]
print(listtest)
# listtest.remove("06").remove("08")
# print(listtest)
