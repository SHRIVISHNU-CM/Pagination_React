def count_fav(n, playlist):
    singer_count = {}
    for singer in playlist:
        if singer in singer_count:
            singer_count[singer] +=1
        else:
            singer_count[singer] = 1
        
    max_count = max(singer_count.values())

    num_fav = sum(1 for count in singer_count.values() if count == max_count)
    return num_fav

n = int(input().strip())
playlist = list(map(int , input().strip().split()))
res = count_fav(n,playlist)
print(res)