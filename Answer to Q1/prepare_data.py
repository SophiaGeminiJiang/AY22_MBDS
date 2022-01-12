import numpy as np
from PIL import Image
from tqdm import tqdm

from load_mnist import load_mnist

X_train, y_train = load_mnist('./mnist_data/', kind='train')
X_test, y_test = load_mnist('./mnist_data/', kind='t10k')

# Extract 0 and 7 from the data
# train data
img_0_train = X_train[y_train == 0]
img_7_train = X_train[y_train == 7]
label_0_train = y_train[y_train == 0]
label_7_train = y_train[y_train == 7]
np.save('./mnist_data/train/img_0.npy', img_0_train)
np.save('./mnist_data/train/img_7.npy', img_7_train)
np.save('./mnist_data/train/label_0.npy', label_0_train)
np.save('./mnist_data/train/label_7.npy', label_7_train)
# save data as jpg format
for i in tqdm(range(len(img_0_train))):
    img = img_0_train[i].reshape(28, 28)
    img = Image.fromarray(img)
    img.save('./mnist_data/train/0/0_' + str(i) + '.jpg')
for i in tqdm(range(len(img_7_train))):
    img = img_7_train[i].reshape(28, 28)
    img = Image.fromarray(img)
    img.save('./mnist_data/train/7/7_' + str(i) + '.jpg')
# test data
img_0_test = X_test[y_test == 0]
img_7_test = X_test[y_test == 7]
label_0_test = y_test[y_test == 0]
label_7_test = y_test[y_test == 7]
np.save('./mnist_data/test/img_0.npy', img_0_test)
np.save('./mnist_data/test/img_7.npy', img_7_test)
np.save('./mnist_data/test/label_0.npy', label_0_test)
np.save('./mnist_data/test/label_7.npy', label_7_test)
# save data as jpg format
for i in tqdm(range(len(img_0_test))):
    img = img_0_train[i].reshape(28, 28)
    img = Image.fromarray(img)
    img.save('./mnist_data/test/0/0_' + str(i) + '.jpg')
for i in tqdm(range(len(img_7_test))):
    img = img_7_train[i].reshape(28, 28)
    img = Image.fromarray(img)
    img.save('./mnist_data/test/7/7_' + str(i) + '.jpg')
print("Complete!")
