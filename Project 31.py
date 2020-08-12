import time
target = int(input("How many cents: "))

money = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
outcomes = [1] + [0]*target

start_time = time.time()
for CurrentMoney in money:
    for i in range(CurrentMoney, target+1):
        outcomes[i] += outcomes[i-CurrentMoney]
        
TimeEnd = round(time.time()-start_time,4)

print()
print("outcomes to make change =", outcomes[target])
print("Run Time: {}s".format(TimeEnd))