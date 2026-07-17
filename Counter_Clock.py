import time
count = int(input("Enter your time : "))

for x in range(count,0,-1):
    second = x%60
    minute = int((x/60)%60)
    hour = int(x/3600)
    print(f"{hour:02}:{minute:02}:{second:02}")
    time.sleep(1)

print("Time Over!")