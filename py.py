import pickle
import numpy as np
import cv2
import os 
import glob
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import tensorflow as tf
# ase_model = tf.keras.applications.InceptionV3(
#     weights='imagenet',
#     input_shape=(150, 150, 3),
#     include_top=False)
path= "model.pkl"
# with open(path, "rb") as file:
#     loaded_model = pickle.load(file)
loaded_model = keras.models.load_model('model.h5')
#loaded_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])'
img_dir = 'G:/Project/python/model/stored_images'
data_path = os.path.join(img_dir , '*g')
images = glob.glob(data_path)
x=[]
for image in images:
    img = cv2.imread(image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (150,150))
    x.append(np.array(img))
x = np.array(x)
x=x.astype('float32')/255
new_test= []
for i in x:
    new_test.append(cv2.resize(i,(150,150)))
new_test = np.array(new_test)

prediction = loaded_model.predict(new_test)
index = 0
img_to_find = prediction[index]


from scipy import spatial 
cosine_list2 = []
for index_image,xt in enumerate(prediction): # 
    result = 1 - spatial.distance.cosine(img_to_find.reshape(-1), xt.reshape(-1))
    cosine_list2.append(dict({'res':result, 'i':index_image}))

from operator import itemgetter
cosine_list2.sort(key=itemgetter('res'), reverse=True)

#%matplotlib inline

fig, ax = plt.subplots(nrows=1, ncols=4,figsize=(20, 4))
plt.gray()
for indice, row in enumerate(ax):
    if indice < len(cosine_list2):
        print (cosine_list2[indice]['i'])
        row.imshow(new_test[cosine_list2[indice]['i']].reshape(150,150,3))


plt.show()




# new_test = []
# for x in X_test:
#     new_test.append(cv2.resize(x, (150,150)))
# new_test = np.array(new_test)
# new_test.shape

# prediction = base_model.predict(new_test)
# index = 5
# img_to_find = prediction[index]

# # Finding similar images using cosine similarity
# cosine_list2 = []
# for index_image, xt in enumerate(prediction):
#     result = 1 - spatial.distance.cosine(img_to_find.reshape(-1), xt.reshape(-1))
#     cosine_list2.append(dict({'res':result, 'i':index_image}))
# from operator import itemgetter
# cosine_list2.sort(key=itemgetter('res'), reverse=True)

# # Displaying the top 10 similar images
# fig, ax = plt.subplots(nrows=1, ncols=10, figsize=(20, 4))
# plt.gray()
# for indice, row in enumerate(ax):
#     print(cosine_list2[indice]['i'])
#     row.imshow(new_test[cosine_list2[indice]['i']].reshape(150,150,3))

# plt.show()

# for dirname in os.listdir(img_dir):
#         print(dirname)
#         label_names.append(dirname)
#         data_path = os.path.join(img_dir + "/" + dirname, '*g')
#         files = glob.glob(data_path)
#         n = 0
#         for f1 in files:
#             if n > nmax:
#                 break
#             img = cv2.imread(f1)
#             img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#             img = cv2.resize(img, (xdim, ydim))
#             X.append(np.array(img))
#             n = n + 1
#         print(n, 'images read')