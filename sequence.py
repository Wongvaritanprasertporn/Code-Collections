def the3np1(n):
    counter = 0
    while n != 1:
        if n % 2 == 0: # n is even
            n = n // 2
        else: # n is odd
            n = n * 3 + 1
        counter += 1
    return counter

counter_values = []
plt.ion()
fig, ax = plt.subplots()

for i in range(1, 51):
    counter_values.append(the3np1(i))
    ax.plot(range(1, i + 1), counter_values, marker='o', color='b')  # Plot counter values
    ax.set_title('3n+1 Sequence Counter')
    ax.set_xlabel('Input Value')
    ax.set_ylabel('Counter')
    plt.pause(0.1)  # Pause to allow the plot to be displayed

plt.ioff()  # Turn off interactive mode
plt.show()