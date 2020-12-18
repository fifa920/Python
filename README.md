# Python_개념

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



3. 반올림 round(a,b)

round(a,b) 를 통해 a라는 수를 소수점 b 번째 자리까지 표현할 수 있다.

```python
x = round(123.456, 2)
print(x)

소수점 3 번째에서 반올림 하게 되면 123.46이 나오게 된다.
>> 123.46
```



4. List slicing

콜론(:) 을 이용해 리스트를 슬라이싱 할 수 있다.

이 때, 마지막 인덱스 숫자보다 1을 크게 한다.(마지막 인덱스는 포함x)

- 시작 인덱스가 없을 경우 처음부터

- 마지막 인덱스가 없을 경우 끝까지
- [a​ : b : ​x] : a번부터 b-1 까지 x개씩 띄워서 나타낸다.

```python
arr = [0,4,2,7,1,9,6,3,8,5]
#	   0,1,2,3,4,5,6,7,8,9

print(arr[3:7])
>> [7,1,9,6]

print(arr[:4])
>> [0,4,2,7]

print(arr[1:8:2])
>> [4, 7, 9, 3]

```



5. List Comprehension

대괄호([]) 안에 조건문과 반복문을 주어 리스트를 초기화 할 수 있다.

특히 2차원 배열을 초기화 할 때 유용하게 쓰일 수 있다.

```python
arr = [i for i in range(10)]
print(arr)

>> [0,1,2,3,4,5,6,7,8,9]

arr = [i for i in range(20) if i % 2 ]
print(arr)

>> [1,3,5,7,9,11,13,15,17,19]

n,m = 4, 6
arr = [[0]*n for _ in range(m)]

>> 이런 식으로 활용 가능 !
```



6. List 관련 Method

   1. sort()
      - 오름차순 정렬
      - 내림차순 정렬은 arr.sort(reverse=True)

   

   ```python
   a = [1, 4, 3, 2]
   a.sort()
   print(a)
   [1, 2, 3, 4]
   ```



​		2. reverse()

​			- 배열을 거울에 mirroring 하듯 뒤집는다.

```python
arr = [1,8,5,2,4]
arr.reverse()
print(arr)

>> [4,2,5,8,1]
```



​		3. index()

​			- index(x) 함수는 리스트에 x 값이 있으면 x의 위치 값을 돌려준다.

```python
arr = [1,5,9,7,2]
x = arr.index(5)
print(x)

>>> 1
```



​		4. insert(a,b)

​			- arr.insert(a,b) : `a` 자리에 `b` 를 넣기

```python
x = [1,5,7]
x.insert(1,2)
print(x)

>>> [1, 2, 5, 7]
```



​		5. remove(a)

​		- `arr.remove(a)` 형태로 쓰며 a 값을 찾아 삭제해 준다. 이 때, arr 안에 a라는 값이 여러 개일 경우 첫 번째 		   값만 삭제해준다.

```python
arr = [1,2,3,1]
arr.remove(1)
print(arr)

>> [2, 3, 1]
```



​		6. count()

​		- `arr.count(x)` : arr 의 리스트 안에 x라는 값이 몇 개 존재하는지 count 해주는 메서드

```python
arr = [1, 2, 3, 1, 4, 1]
print(arr.count(1))

>>> 3
```





5. 사전형 자료(dictionary)

- key, value 형태로 존재하며, 한번 설정된 값은 변경 불가(immutable)

- 시간복잡도 측면에서 O(1) 이므로 상당한 이득이다.
- `data.keys()` or `data.values()` or `data.items()` 를 이용하여 for 문으로 사용할 때 유용하다. (리스트는 아님)
- `list(daya.keys())` or `list(data.values())` 를 이용하면 리스트로 만들어서 활용 가능
- `data[key]` == `data.get(key)` , 즉 get 을 통해 값을 얻을 수 있다.

```python
# dict() 를 이용하여 선언 ! or data = {'사과': 'apple', .....}  이런 식으로 선언 가능
data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'Coconut'

print(data)

>> {'사과': 'apple', '바나나': 'banana', '코코넛': 'Coconut'}

for key in data.keys():
    print(key)


```



6. 집합 자료형 set()

   6.1 집합 자료형 선언

   - `s1 = set()` 으로 빈 집합 선언 or `s1 = set([1,2,3])`

   - s1 = {1,2,3,4} 이런 식으로도 선언 가능

   ```python
   s1 = set()
   s1 = set([1,2,3,4,1,2])
   print(s1)
   
   >> {1,2,3,4}
   
   s1 = {1,2,3,4,5,1,2}
   print(s1)
   >> {1,2,3,4,5}
   
   s2 = set("Hello")
   print(s2)
   >> {'e', 'H', 'l', 'o'}
   ```

   

   6.2 

7. deque

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


  

  1. Queue 구현

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