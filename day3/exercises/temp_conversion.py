def c_to_f(temp):
    return (9/5)*temp + 32


def f_to_c(temp):
    return (temp - 32)*(5/9)


def c_to_k(temp): # 273 degK = 0 degC
    return temp + 273


def k_to_c(temp):
    return temp - 273


def k_to_f(temp):
    return c_to_f(
        k_to_c(temp)
    )


temps = [0, 20, 37, 100]

for i in range(len(temps)):
    temps[i] = c_to_k(temps[i])
print(temps)

for i in range(len(temps)):
    temps[i] = k_to_f(temps[i])
print(temps)