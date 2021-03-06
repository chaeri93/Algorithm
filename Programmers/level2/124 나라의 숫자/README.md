### 124 나라의 숫자
***
### 문제 설명
124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.

1. 124 나라에는 자연수만 존재합니다.
2. 124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.   

예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.

![](https://velog.velcdn.com/images/chaeri93/post/28d17bfe-2220-4b02-898b-143625dda132/image.png)

### 제한사항
- n은 500,000,000이하의 자연수 입니다.
### 입출력 예
|n|result|
|---|---|
|1|1|
|2|2|
|3|4|
|4|11|

### Solution
- nums = ["1", "2", "4"]라는 하나의 배열을 생성해준후 배열 인덱스인 0,1,2를 사용하여 접근
- n-1을 하여 %3 을 해 배열 결과물 출력
- 몫이 3이상이면 위에 코드 반복
- 다른 사람 풀이 : 재귀함수 사용해서 반복
    ```python
    def change124(n):
        if n<=3:
            return '124'[n-1]
        else:
            q, r = divmod(n-1, 3) 
            return change124(q) + '124'[r]
    ```