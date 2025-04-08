time = 12345
hour = time // 3600
minute = (time % 3600) // 60
second = time % 60
print(time, "초는", hour, "시간", minute, "분", second, "초입니다.")