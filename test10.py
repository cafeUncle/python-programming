long_string = "i 'll catch you if you fall - The Floor"

print(long_string[0:4])

print(long_string[-5])
print(long_string[-5:-2])
print(long_string[-5:1])  # print ''
print(long_string[1:-5])

print(long_string[:4], "be there")

print("%c is muu %s letter and mu number %d number is %.5f" % ('X', 'favorite', 1, .14))

print(long_string.capitalize())  # 将字符串的第一个字母变成大写,其他字母变小写
print(long_string.find('Floor'))
print(long_string.isalpha())  # 检测字符串是否只由字母组成
print(long_string.isalnum())  # 检测字符串是否由字母和数字组成   有空格也返回False
print(len(long_string))
print(long_string.replace('Floor', 'Ground'))
print(long_string.strip())  # 去掉首尾指定字母，默认是空格
print(long_string.strip('I'))
print(long_string.strip('i'))
print(long_string.swapcase())  # 对大小写进行转换

quoto_list = long_string.split(" ")
print(quoto_list)

