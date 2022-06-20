### 소수 만들기
***
### 문제 설명
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

### 제한사항
- nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다. 
- nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

### 입출력  
|nums|result|
|---|---|
|[1,2,3,4]|1|
|[1,2,7,6,4]|4|

### Solution
- 소수 찾기 알고리즘
    - 2부터 n-1까지 나누기 - 시간 복잡도가 O(n)
        ```python
            def isPrime(n):
                for i in range(2, n):
                    if n % i == 0:
                        return False  
                return True
        ```
    - n/2까지 나누기 - 시간 복잡도가 O(n)
        ```python
            def isPrime(n):
                for i in range(2, n//2+1):
                    if n % i == 0:
                        return False  
                return True
        ```
    - n의 제곱근까지 나누기 -시간 복잡도는 O(√n)
        ```python
            def isPrime(n):
                for i in range(2, int(n**0.5)+1):
                    if n % i == 0:
                        return False  
                return True
        ```
- python으로 순열 및 조합 만들기
    - 순열(=permutations)
        ```python
            from itertools import permutations
            
            for i in permutations([1,2,3,4], 2):
                print(i, end=" ")
            # (1, 2) (1, 3) (1, 4) (2, 1) (2, 3) (2, 4) ...
            # (3, 1) (3, 2) (3, 4) (4, 1) (4, 2) (4, 3) 
            
        ```
    - 조합(=combinations)
        ```python
            from itertools import combinations
            
            for i in combinations([1,2,3,4], 2):
                print(i, end=" ")
            # (1, 2) (1, 3) (1, 4) (2, 3) (2, 4) (3, 4) 
        ```  