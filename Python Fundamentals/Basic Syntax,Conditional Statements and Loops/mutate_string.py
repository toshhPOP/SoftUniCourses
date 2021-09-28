str1 = input()
str2 = input()
current_index = 0
for i in range(len(str1)):
    if str1[i] != str2[i]:
        for str2_index in range(0,i +1):
            print(str2[str2_index], end="")
        for str1_index in range(i + 1, len(str2)):
            print(str1[str1_index], end="")
        print()

# str1 = input()
# str2 = input()
# previous_string = str1
# for i in range(len(str1)):
#     current_string = ''
#     for index_str_2 in range(0,i+1):
#         current_string += str2[index_str_2]
#     for index_str_1 in range(i+1,len(str1)):
#         current_string += str1[index_str_1]
#     if current_string != previous_string:
#         print(current_string)
#         previous_string = current_string


