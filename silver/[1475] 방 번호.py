n = input()

data = [0]*10
for i in range(len(n)):
    num = int(n[i])
    # 만약 6이나 9일 경우
    if num == 6 or num == 9:
        # 하나의 수만 증가하는 것이 아닌 각각의 수를 올
        if data[6] <= data[9]:
            data[6] += 1
        else:
            data[9] += 1
    else:
        data[num] += 1
print(max(data))
