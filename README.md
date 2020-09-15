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

