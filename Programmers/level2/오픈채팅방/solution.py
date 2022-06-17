def solution(record):
    user = {}
    result = []

    for r in record:
        a = r.split(" ")
        if (a[0] == "Enter") | (a[0] == "Change"):
            user[a[1]] = a[2]

    for r in record:
        a = r.split(" ")
        if a[0] == "Enter":
            result.append(user[a[1]] + "님이 들어왔습니다.")
        elif a[0] == "Leave":
            result.append(user[a[1]] + "님이 나갔습니다.")

    return result


