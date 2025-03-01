"""
names = []
score = []
#data = []

file = open("file.txt", "r")
contents = file.readlines()
for line in contents:
    data = line.strip().split(" ")
    names.append(data[0])
    score.append(data[1])

print(names)
print(score)
"""
file_write = open("file.txt", "a")
user_score = [8,3,6,3,5,7]
user_name = ["bob", "bill", "kate", "john", "ava", "janice"]

for i in range(len(user_score)):
    data = f"\n {user_name[i]} {user_score[i]}"
    file_write.write(data)

file_write.close