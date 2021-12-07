# Read Data
my_file = open("day1.txt","r")
content = my_file.read()
content_list = content.split("\n")
my_file.close()

# Data prep
content_list = [int(x) for x in content_list]


# Part 1
# count = 0
# for i in range(len(content_list)-1):
#     # print(content_list[i])
#     if content_list[i] < content_list[i+1]:
#         # print("increasing")
#         count += 1
# print(count)


# Part 2

count = 0
for i in range(len(content_list)-2):
    if sum(content_list[i:i+3]) < sum(content_list[i+1:i+4]):
        count += 1
print(count)