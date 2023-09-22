nu = []
nu.append(range(0, 100))
total = 0
for c in range(1, len(nu)):
    if nu % c == 0:
        total += 1
if total == 2:
    print(nu, ' eh primo')
elif total >= 3:
    print(nu, ' nao eh primo')
else:
    print(nu, ' nao eh primo')
