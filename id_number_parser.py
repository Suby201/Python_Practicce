id = "901212-1234567"
year = int(id[0:2])
month = int(id[2:4])
day = int(id[4:6])
year += 1900
print(f'{year}년 {month}월 {day}일')