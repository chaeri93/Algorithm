### 키패드 누르기
***
### 문제 설명

스마트폰 전화 키패드의 각 칸에 다음과 같이 숫자들이 적혀 있습니다.

![https://blog.kakaocdn.net/dn/CHjpy/btq2zB4Aoqj/JsZA0XvR94iqRMEHrR3KMK/img.png](https://blog.kakaocdn.net/dn/CHjpy/btq2zB4Aoqj/JsZA0XvR94iqRMEHrR3KMK/img.png)

이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.

1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
2. 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
3. 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
4. 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.

순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

---

### 제한 사항
    - numbers 배열의 크기는 1 이상 1,000 이하입니다.
    - numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
    - hand는 "left" 또는 "right" 입니다.
        - "left"는 왼손잡이, "right"는 오른손잡이를 의미합니다.
    - 왼손 엄지손가락을 사용한 경우는 L, 오른손 엄지손가락을 사용한 경우는 R을 순서대로 이어붙여 문자열 형태로 return 해주세요.

---

### 입/출력
![](https://velog.velcdn.com/images/chaeri93/post/c9e132a4-4828-43f0-9ac5-2f3dfeef73e5/image.png)

### Solution
- 좌표 사용하여 거리 계산
- abs() python 함수 사용해서 각 좌표의 차를 절댓값으로 계산
- 다른 사람 코드, zip 사용해서 거리 계산   
    ```python
    left_d = 0
    right_d = 0
                
    # 좌표 거리 계산해주기
    for a, b, c in zip(left_s, right_s, now):
        left_d += abs(a-c)
        right_d += abs(b-c) 
    ```
    - zip() 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 터플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환
    ```python
        # 예제
        >>> numbers = [1, 2, 3]
        >>> letters = ["A", "B", "C"]
        >>> for pair in zip(numbers, letters):
        ...     print(pair)
        ...
        (1, 'A')
        (2, 'B')
        (3, 'C')
       ```   
