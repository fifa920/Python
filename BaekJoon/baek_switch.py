import sys
sys.stdin = open("baek_switch.txt","r")

switch_num = int(input())                                   # switch 개수
switch_stat = list(map(int, input().split()))               # switch 상태를 list로
stu_num = int(input())                                      #학생의 수

for i in range(stu_num) :
    gender, where = map(int, input().split())
    if gender == 1:                                     # 남자일 때
        for now in range(where-1, switch_num, where) :
            switch_stat[now] = 1-switch_stat[now]


    else :
        switch_stat[where-1] = 1 - switch_stat[where-1]  #where 자리 값은 무조건 변경
        left = where -2
        right = where
        while left >= 0 and right <= switch_num-1 :
            if switch_stat[left] == switch_stat[right] :
                switch_stat[left] = 1-switch_stat[left]
                switch_stat[right] = 1 - switch_stat[right]
                left -= 1
                right += 1


print(switch_stat)



