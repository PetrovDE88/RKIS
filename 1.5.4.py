list1 = [1, 2, 4]
list2 = [1, 3, 4]

concolidate_list = list1 + list2
print(concolidate_list)

for i in range(len(concolidate_list)-1):
    for j in range(i+1, len(concolidate_list)):
        if concolidate_list[i] > concolidate_list[j]:
            concolidate_list[i], concolidate_list[j] = concolidate_list[j], concolidate_list[i]

print(concolidate_list)