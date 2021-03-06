### 크래인 인형뽑기 게임
***
### 문제 
게임개발자인 “죠르디”는 크레인 인형뽑기 기계를 모바일 게임으로 만들려고 합니다. “죠르디”는 게임의 재미를 높이기 위해 화면 구성과 규칙을 다음과 같이 게임 로직에 반영하려고 합니다.

![](https://velog.velcdn.com/images/chaeri93/post/ea2cc055-4f9e-4c96-85bb-f39d348ecbc7/image.png)    
게임 화면은 “1 x 1” 크기의 칸들로 이루어진 “N x N” 크기의 정사각 격자이며 위쪽에는 크레인이 있고 오른쪽에는 바구니가 있습니다. (위 그림은 “5 x 5” 크기의 예시입니다). 각 격자 칸에는 다양한 인형이 들어 있으며 인형이 없는 칸은 빈칸입니다. 모든 인형은 “1 x 1” 크기의 격자 한 칸을 차지하며 격자의 가장 아래 칸부터 차곡차곡 쌓여 있습니다. 게임 사용자는 크레인을 좌우로 움직여서 멈춘 위치에서 가장 위에 있는 인형을 집어 올릴 수 있습니다. 집어 올린 인형은 바구니에 쌓이게 되는 데, 이때 바구니의 가장 아래 칸부터 인형이 순서대로 쌓이게 됩니다. 다음 그림은 [1번, 5번, 3번] 위치에서 순서대로 인형을 집어 올려 바구니에 담은 모습입니다.
![](https://velog.velcdn.com/images/chaeri93/post/a45fedd1-ba90-428d-8219-e095f318d04b/image.png)    
만약 같은 모양의 인형 두 개가 바구니에 연속해서 쌓이게 되면 두 인형은 터뜨려지면서 바구니에서 사라지게 됩니다. 위 상태에서 이어서 [5번] 위치에서 인형을 집어 바구니에 쌓으면 같은 모양 인형 두 개가 없어집니다.    
크레인 작동 시 인형이 집어지지 않는 경우는 없으나 만약 인형이 없는 곳에서 크레인을 작동시키는 경우에는 아무런 일도 일어나지 않습니다. 또한 바구니는 모든 인형이 들어갈 수 있을 만큼 충분히 크다고 가정합니다. (그림에서는 화면표시 제약으로 5칸만으로 표현하였음)

게임 화면의 격자의 상태가 담긴 2차원 배열 board와 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves가 매개변수로 주어질 때, 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 하도록 solution 함수를 완성해주세요.
***
### 제한사항
- board 배열은 2차원 배열로 크기는 “5 x 5” 이상 “30 x 30” 이하입니다.
- board의 각 칸에는 0 이상 100 이하인 정수가 담겨있습니다. 0은 빈 칸을 나타냅니다.
- 1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냅니다.
- moves 배열의 크기는 1 이상 1,000 이하입니다.
- moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수입니다.
***
### 입출력 예

|board|moves|result|
|---|---|---|
|[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]|[1,5,3,5,1,2,1,4]|4|

### Solution
- 먼저 스택에 해당 리스트의 마지막부터 담고 0으로 바꿔준다.
- 그다음 스택에 2개이상이 담겨 있을경우 마지막값과 마지막 이전값을 비교하여 일치하면 제거한다.
- 스택에서 마지막 2개를 비교하고 제거할 때 어떤 함수를 쓸지 고민했다.
  - .pop() : 지우고자 하는 리스트의 인덱스를 받아서 지우는 방식이다. pop()은 지워진 인덱스의 값을 반환한다. 해당 값을 삭제 후, 리스트를 재조정한다.
    ```python
      a = [1,2,1,3,4,5,1]
      removed = a.pop(1)
      print(a) 
      print(removed) 
      # [1, 1, 3, 4, 5, 1] 
      # 2 
    ```
  - del :  지우고자 하는 리스트의 인덱스를 받아서 지우는 방식이다. del이 pop()보다 수행속도가 더 빠르다. 해당 값을 삭제 후, 리스트를 재조정한다.
    ```python
      a = [1,2,1,3,4,5,1] 
      del a[1]
      print(a) 
      print(a[0])
      # [1, 1, 3, 4, 5, 1] 
      # 1
    ```
  - slice : 슬라이싱은 위와 같이 리스트의 값을 지우는 것이 아닌, 사용자가 원하고자 하는 범위를 출력한다. 즉, 원본 리스트는 그대로 존재하며 원하고자 하는 범위만큼 출력을 하기 위해 새로운 리스트가 생성된다 .
    ```python
      a = [1,2,1,3,4,5,1]
      b = a[1:]
      print(b)
      print(a)
      # [2, 1, 3, 4, 5, 1]
      # [1, 2, 1, 3, 4, 5, 1]
      ```
  - .remove() : 지우고자 하는 인덱스가 아닌, 값을 입력하는 방식이다. 만약 지우고자 하는 값이 리스트 내에 2개 이상이 있다면 순서상 가장 앞에 있는 값을 지우게 된다. 해당 값을 삭제 후, 리스트를 재조정한다.
    ```python
      a = [1,2,1,3,4,5,1]
      a.remove(1)
      print(a)
      # [2, 1, 3, 4, 5, 1]
    ```  
    > 원본 리스트가 변질이 되지 않아야 하면 슬라이싱을 사용하는 것이 좋다.    
     하지만 슬라이싱은 데이터를 삭제하는 del, remove(), pop()에 비해 50% 이상 느리다.
     del이 가장 빠르고 pop()과 remove()는 비슷한 수행시간을 가지며 슬라이싱이 가장 느리다. 