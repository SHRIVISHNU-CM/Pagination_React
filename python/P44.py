def simplify(path):
    components =path.split("/")

    simplified =[]

    for i in components:
        if i == "..":
            if simplified:
                simplified.pop()
        elif i and i != ".":
            simplified.append(i)

    simplified_path = "/" +"/".join(simplified)

    return simplified_path


num = "/a//b////c/d//././/.."

res = simplify(num)
print(res)
print(num.split("/"))