# Python

1. 특정 문자로 구분지어 입력 받기

```python
year, month, day = input().split('.')
# 2015.3.23 이라 입력 하게 되면 . 으로 구분지어 차례로 입력 받음
```



2. 숫자에서 빈 자리수 0으로 채우기

```python
month.zfill(2)
# 1번 예제에서 month에 3을 입력 받았지만 zfill 을 이용하면 03 으로 앞의 빈 칸을 0으로 채운다.
```



3. deque

- deque를 이용해 stack, queue 모두 이용 가능하다

  1. Stack 구현

     - stack 은 나중에 들어간게 먼저 나오는 형태 따라서 `append`, `pop`을 이용하여 오른쪽을 +, - 할 수 있다.

     ```python
     from collections import deque
     arr = deque(list(range(1,7)))
     arr.append(7)
     >>> [1,2,3,4,5,6,7]
     
     arr.pop()
     >>> 7
     ```

     

  2. Queue 구현

     - Queue는 first in - first out 이므로 `appendleft()` - `pop()` 혹은 `append()` - `popleft()` 를 이용할 수 있다.

     ```python
     from collections import deque
     arr = deque(list(range(1,7)))
     
     arr.appendleft(0)
     print(arr)
     >>> [0,1,2,3,4,5,6]
     
     arr.pop()
     >>> 6
     
     ```

     

4. input() 대신 sys.stdin.readline() 을 써서 시간을 줄이자

- 하지만 sys.stdin.readline() 을 쓰게 되면 뒤에 개행문자 \n 도 같이 나오게 되므로 `strip` 사용 !

```python
import sys
x = sys.stdin.readline()
x 에 123 입력하면
>>> '123\n' 이 입력됨

따라서 
sys.stdin.readline().strip() 을 이용하여 맨 뒤 개행문자를 자동 삭제

```

- 만약 input을 `123 456` 처럼 띄워서 받고 싶다면 `x = sys.stdin.readline().split()` 으로 받으면 된다.