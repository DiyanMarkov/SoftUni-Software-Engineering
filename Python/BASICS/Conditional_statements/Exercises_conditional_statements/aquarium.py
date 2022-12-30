length = int(input())
width = int(input())
hight = int(input())
percent = float(input())

multiplication = (length * hight * width) * 0.001
total_liters = multiplication - (multiplication * percent / 100)

print(total_liters)