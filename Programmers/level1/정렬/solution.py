def solution(array, commands):
    answer = []
    # commands에 있는 command(i, j, k)를 뽑는다.
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        slice = array[i-1:j] # array에서 슬라이스를 하고
        slice.sort() # 정렬하고
        answer.append(slice[k-1]) # 인덱싱
    return answer
