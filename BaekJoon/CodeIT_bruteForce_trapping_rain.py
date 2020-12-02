def trapping_rain(buildings):
    N = len(buildings)
    count = 0

    for i in range(1, N - 1):
        left = buildings[i]
        for j in range(i):
            left = max(left, buildings[j])
            right = buildings[i]

        for j in range(i + 1, N):
            right = max(right, buildings[j])
        count += (min(left, right) - buildings[i])
    return count

    # 코드를 작성하세요


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))