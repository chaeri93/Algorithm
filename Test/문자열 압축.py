"""
EPPER 문자열 압축
https://level.goorm.io/exam/100821/15%ED%9A%8C-epper-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%95%95%EC%B6%95/quiz/1
"""

def solution(s):
    answer = ""
    cnt = 0

    if s[0] == "1":
        answer += "1"

    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            # ord: 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.
            # chr: 하나의 정수를 인자로 받고 해당 정수에 해당하는 유니코드 문자를 반환합니다.
            answer += chr(ord('A') + cnt)
            cnt = 0
        else:
            answer += 1
    answer += chr(ord('A') + cnt)
    return answer
