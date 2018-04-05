# test_file = open('test.txt', 'wb')
#
# print(test_file.mode)
# print(test_file.name)
#
# test_file.write(bytes('write something', 'UTF-8'))
#
# test_file.close()

test_file = open('test.txt', 'r+')

text_in_file = test_file.read()
print(text_in_file)
test_file.write('write anything')
