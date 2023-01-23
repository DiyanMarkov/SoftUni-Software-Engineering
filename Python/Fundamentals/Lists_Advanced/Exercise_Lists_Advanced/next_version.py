version = list(map(int, input().split('.')))

increased_version = version[-1] + 1
if increased_version > 9:
    version[-1] = 0
    version[-2] += 1
    if version[-2] > 9:
        version[-2] = 0
        version[-3] += 1
    final_version = f'{version[-3]}.{version[-2]}.{version[-1]}'
else:
    final_version = f'{version[-3]}.{version[-2]}.{version[-1] + 1}'

print(''.join(str(final_version)))