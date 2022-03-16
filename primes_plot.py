import matplotlib.pyplot as plt

r = []
theta = []
num = 2
num_primes = int(input("Number of primes: "))

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

while len(r) != num_primes:

    for i in range(2, int(num / 2) + 1):

        if (num % i) == 0:
            break
    else:
        r.append(num)
        theta.append(num)
    num += 1
    print(num)


ax.plot(theta, r, '.', markersize=3)
ax.set_rmax(num)
ax.grid(False)
ax.axis('off')
ax.set_title(f"First {num_primes} prime numbers plotted in polar coordinates", va='bottom')
plt.show()
