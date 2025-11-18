str_a = "вопрос"
str_b = str_a.encode('cp1251').decode('koi8-r')
print(str_b)

str_c = "бПХЛЮМХЕ"
str_d = str_c.encode('cp1251').decode('koi8-r')
print(str_d)

import pickle