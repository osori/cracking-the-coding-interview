testcases = """aabcccccaaa
hongsoook
baaaabbboooo
abcd"""

def string_compression(string):
    output = []
    counter = 0
    for i in range(len(string)):
        if string[i] != string[i-1] and i != 0:
            output.append(string[i-1]+str(counter))
            counter = 0
        counter += 1

    concat = ''.join(output)
    if len(concat) > len(string):
        return string
    else:
        return concat

for test in testcases.split('\n'):
    print(string_compression(test))

