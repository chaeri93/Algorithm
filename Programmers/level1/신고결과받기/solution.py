from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    # 중복신고 제거후 리스트로 반환
    report = list(set(report))

    # 유저별 신고한 id 저장
    user = defaultdict(set)
    # 유저별 신고당한 횟수 저장
    cnt = defaultdict(int)

    for i in report:
        # a는 신고자id, b는 신고당한 id
        a, b = i.split()
        # 신고자가 신고한 id 추가
        user[a].add(b)
        # 신고당한 id의 신고 횟수 추가
        cnt[b] += 1

    for i in id_list:
        result = 0
        # 유저가 신고한 id가 k번 이상 신고 당했으면, 받을 메일(result) 추가
        for u in user[i]:
            if cnt[u] >= k:
                result += 1
        answer.append(result)

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
solution(id_list, report, 2)
