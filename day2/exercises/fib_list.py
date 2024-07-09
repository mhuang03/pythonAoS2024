num = int(input("How many fibonaccis? "))

fibs = [1, 1]
approx = []

while len(fibs) < num:
    approx.append(fibs[-1] / fibs[-2])
    fibs.append(fibs[-1] + fibs[-2])

print(fibs)
print(approx)