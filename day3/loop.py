
lists = ["hello", "how", "are", "you"]
for i in range(4):
    print(lists[i])

for ele in lists:
    print(ele)

for i, ele in enumerate(lists):
    print(f"index is {i} value is {ele}")

for i in range(4, -1,-1):
    print(i)

i = 0
while(i<5):
    print(i)
    i = i+1
