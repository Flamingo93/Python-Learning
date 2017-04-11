while 1:
    n = int(input())
    money = 1
    day = 1
    up_day = 1
    while day <= n:
        if day + up_day <= n:
            day += up_day
            money += up_day
        else:
            print(money + (n - day))
            break
        up_day += 1

        if day + 1 <= n:
            day += 1
            money -= 1
        else:
            print(money)
            break