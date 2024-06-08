def calculate(r,unit,arr):
    n = len(arr)

    if n == 0:
        return -1
    
    totalFoodReq = r*unit
    foodtillNow= 0
    

    for house in range(n):
        foodtillNow += arr[house]
        if foodtillNow >= totalFoodReq:
            break
    if totalFoodReq> foodtillNow:
        return 0
    return foodtillNow,totalFoodReq

r= 7
unit = 2
arr = [2, 8, 3, 5, 7, 4, 1, 2]
print(calculate(r,unit,arr))