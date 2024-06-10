a = "shrivishnu"
for i in a:
    count = 0
    for j in a:
        if i == j:
            count +=1
        if count >1:
            break
    if count == 1:
        print(i,end=" ")




