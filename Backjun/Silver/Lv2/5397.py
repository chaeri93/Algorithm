import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        tmp = input()
        pwd = []
        pointer = []
        for i in tmp:
            if i == "-":
                if pwd:
                    pwd.pop()
            elif i == "<":
                if pwd:
                    pointer.append(pwd.pop())
            elif i == ">":
                if pointer:
                    pwd.append(pointer.pop())
            else:
                pwd.append(i)
        pwd.extend(reversed(pointer))
        print(''.join(pwd))
