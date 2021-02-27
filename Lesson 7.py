# r = open('text.txt')
# r_1 = r.read(3)
# for line in r:
#     print(line)
# print(r)
# print(r_1)
# r.close()

with open('text.txt', 'w', encoding= 'UTF-8') as file:
    r = file.write("hello")
    print(r)
with open('text.txt', 'a', encoding= 'UTF-8') as file_2:
    i = file_2.write('\nOneMoreHello')
    print(i)

# with open('text.txt', 'a', encoding='UTF-8') as file_2:
#     i = file.write('One more hello')
#     print(i)
