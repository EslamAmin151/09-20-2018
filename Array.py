data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
data_list_sorted = []
data_list_copy = []
data_list_rev = []

for i in data_list:
    data_list_copy.append(i)

while data_list:
    minimum = data_list[0]
    for x in data_list:
        if x < minimum:
            minimum = x
    data_list_sorted.append(minimum)
    data_list.remove(minimum)



while data_list_copy:
    maximum = data_list_copy[0]  # arbitrary number in list


    for y in data_list_copy:
        if y > maximum:
            maximum = y
    data_list_rev.append(maximum)
    data_list_copy.remove(maximum)


print(data_list_sorted)
print(data_list_rev)
