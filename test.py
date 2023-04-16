import math
import matplotlib.pyplot as plt

def cyclical_learning_rate(epoch, lr):
    base_lr = 0.001  # The minimum learning rate
    max_lr = 0.01    # The maximum learning rate
    step_size = 3   # The number of epochs between each cycle

    cycle = math.floor(1 + epoch/(2*step_size))
    x = abs(epoch/step_size - 2*cycle + 1)
    new_lr = base_lr + (max_lr - base_lr) * max(0, (1 - x))

    return new_lr * (6 / (cycle + 5))


x = [x for x in range(100)]

y = [y for y in range(100)]

y[0] = cyclical_learning_rate(1, 0.001)

for nr in x[1:]:
    y[nr] = cyclical_learning_rate(nr, y[nr-1])

plt.plot(y)
plt.xlabel("epochs")
plt.ylabel("learning rate")
plt.show()

plt.savefig("Stanford", format='png')

def graph(history):
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label = 'val_loss')
    plt.title('Variant one')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.ylim([0.2, 0.8])
    plt.legend(loc='lower left')
    plt.savefig("Stanford")