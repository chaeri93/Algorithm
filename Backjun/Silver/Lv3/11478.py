s = list(input())
diff = set()

for i in range(len(s)):
    result = s[i]
    diff.add(result)
    for j in range(i+1, len(s)):
        result += s[j]
        diff.add(result)


print(len(diff))