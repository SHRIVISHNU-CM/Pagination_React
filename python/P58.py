def vowelRemoval(string):
    vowels = ['a','e','i','o','u']

    result = [letter for letter in string if letter.lower() not in vowels]
    a = "".join(result)
    print(a)

string = "geeks Is - A computer Science Portal"
vowelRemoval(string)