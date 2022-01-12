import random

import numpy as np
import pandas as pd

img_0_train = np.load('mnist_data/train/img_0.npy')
img_7_train = np.load('mnist_data/train/img_7.npy')
img_0_test = np.load('mnist_data/test/img_0.npy')
img_7_test = np.load('mnist_data/test/img_7.npy')
num_0 = 0
num_7 = 0
# while (num_0 < len(img_0_train) and num_7 < len(img_7_train)):
label = []
for i in range(5000):
    img = np.zeros((100, 784))
    j = random.randint(0, 100)
    num_0 += j
    num_7 += 99 - j
    if (num_0 > len(img_0_train) or num_7 > len(img_7_train)):
        break
    img[0:j] = img_0_train[num_0 - j:num_0]
    img[j + 1:100] = img_7_train[num_7 - 99 + j:num_7]
    np.save('train_data/img_' + str(i) + '.npy', img)
    label.append(j / 100)

df = pd.DataFrame(label, columns=['0_ratio'])
df.to_excel("0_ratio.xlsx", index=True)
