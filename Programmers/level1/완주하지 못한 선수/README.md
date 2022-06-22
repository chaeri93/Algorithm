### 완주하지 못한 선수
***
### 문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
### 제한사항
- 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
- completion의 길이는 participant의 길이보다 1 작습니다.
- 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
- 참가자 중에는 동명이인이 있을 수 있습니다.
### 입출력 예
|participant|completion|return|		
|---|---|---|
|["leo", "kiki", "eden"]|["eden", "kiki"]|"leo"|
|["marina", "josipa", "nikola", "vinko", "filipa"]|["josipa", "filipa", "marina", "nikola"]|"vinko"|
|["mislav", "stanko", "mislav", "ana"]|	["stanko", "ana", "mislav"]|"mislav"|

### Solution
- 정렬을 한다음에 짝을 지어서 zip으로 비교 후 다른 애를 return
  >zip : 배열을 같은 인덱스끼리 짝지어준다. 만약 배열의 길이가 다를 경우 같은 인덱스끼리만 짝지어주고, zip 객체에서 나머지 인덱스는 제외된다.
- 다른 사람 풀이 : collections에서 Counter 모듈을 사용하여 해결
    ```python
    import collections
    
    
    def solution(participant, completion):
        answer = collections.Counter(participant) - collections.Counter(completion)
        return list(answer.keys())[0]
    ```
