# -*- coding: utf-8 -*-
"""Image_Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1duMvwlUpkwKUnCpaDkAoDNUI6qySumkb

# **IMAGE PROCESSING**



---

#**STEP ! : We have to import the dataset of images first**

**Two of the ways are**

1.   Using GDrive for a permenant storage
2.   Impoting it by a lubrary

# **METHOD 1 : Mounting GDrive and using it as a storage**

Here I am going to source my datasets from [Kaggle.com](https://Kaggle.com)

**STEPS :**

1. Mount the GDrive with Google Collab by authenticating the account

**Syntax :**

```
from google.colab import drive
drive.mount('/content/gdrive')
```
"""

from google.colab import drive
drive.mount('/content/gdrive')

"""**2. Make a directory in GDrive for the dataset and download the authentication token and ** ```Kaggle.json``` **from your Kaggle profile**

**3. Upload the **```Kaggle.json``` **to the new directory**

**4. Import OS**
"""

import os
os.environ['KAGGLE_CONFIG_DIR'] = "/content/gdrive/My Drive/ML/KAGGLE"

"""**5.Change he present directory and move it to the directory where the **```Kaggle.json``` **is present**

**Syntax :**

``` cd "/Path_Of_Directory" ```
"""

cd "/content/gdrive/My Drive/ML/KAGGLE"

"""**6. Copy the API from the website and call it here and give an```!``` before it**"""

!kaggle datasets download -d cdart99/food20dataset

"""**7. UnZip it and remove the Zip file**"""

!unzip \*.zip  && rm *.zip

"""# **METHOD 2 : Installing library to downlaod the images dataset for us**"""

!pip install bing-image-downloader

from bing_image_downloader import downloader

"""# **Importing the Datasets from the downloader**

We will use the library to download the images fron bing search engine

**Syntax :**

```
# downloader.download('Search Result needed', limit=No_Of_Photos_To_Download , output_dir='Directory_to_Download', adult_filter_off=True)
```


"""

downloader.download('fruits', limit=20 , output_dir='images', adult_filter_off=True)

downloader.download('furniture', limit=20 , output_dir='images', adult_filter_off=True)

downloader.download('cars', limit=20 , output_dir='images', adult_filter_off=True)

"""# **STEP 2 : Preprocessing the images**

 1. Resizing
 2. Flattening
"""

#Preprocessing the images

import os
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.transform import resize

"""# **Flatten the images**

---



We need to faltten the images out into a single dimension
```flatten()``` converts the 2D matrix into 1D vector

3 empty lists will be taken
 For Data
 For Output
 For flattened data 

taking output as ```target```
taking data as ```images```
passing the ```flattened_data``` to pass to the ML Model
"""

Target = []
Images = []
Flattened_data = []

"""# **Now includeing the path of the data which is images in this case**

If Method 1 is used
"""

DATADIR = '/content/gdrive/MyDrive/ML/KAGGLE/food20dataset/train_set/'

DATADIR

"""If Method 2 is used

"""

DATADIR = '/content/images'

DATADIR

"""# **Now we have to create catagories for the ML Model**

These will be the ones which we will train the model to test for

If Method 1 is used
"""

CATAGORIES = ['chappati' , 'kathi_roll' , 'tandoori_chicken','upma', 'vada_pav']

"""If Method 2 is used"""

CATAGORIES = ['cars','fruits','furniture']

CATAGORIES

"""# **Now we have to iterate through these to fetch the images**

If we pass the CATAGORIES in form of numbers it becomes very easy for for the ML Model

Here we use the concept of **Label Encoding** in which we use the index number 

**Like for example here**

  ```biriyani ``` -> 0 

  ```chaat```        -> 1

  ```dhokla```    -> 2

 **Demonstration :**

Here ``` class_num```
Stores the index numbers

# **Create Path to access all Image datasets :**

```path``` here is stored in a different way

For example in this case the ```path``` here is ```/content/gdrive/MyDrive/ML/KAGGLE/food20dataset/train_set/biriyani```

And we know that

```DATADIR``` ->```/content/images```

```CATAGORIES``` -> ```Adresses_Of_The_Image_Datasets```

And ```catagory``` will iterate though ```CATAGORIES```

**SO WE WRITE PATH LIKE THIS**

```path = os.path.join( DATADIR , catagory )```

# **Some Functions Used**

```imread``` reads all the values ( images in this case )

```join``` is used to join the two paths as mentioned above

```plt.imshow(Image_Array)```used to show the images which is read

```resize(Image_Array,(Height,Width,3)``` used to resize the image

"""

for catagory in CATAGORIES :
  class_num = CATAGORIES.index(catagory)
  path = os.path.join(DATADIR,catagory)
  # Now we will read the values by iterating and is stored
  for img in os.listdir(path) :
    Image_Array = imread(os.path.join(path,img))
    # plt.imshow(Image_Array) to show the images
    Image_Resized = resize(Image_Array,(150,150,3))
    # Now passing the flattened verion
    Flattened_data.append(Image_Resized.flatten())
    Images.append(Image_Resized)
    Target.append(class_num)

"""# **Converting everything to NumPy Array**

**Syntax :**

```Variable_Name = np.array(Variable_Name)```
"""

Flattened_data = np.array(Flattened_data)
Images = np.array(Images)
Target = np.array(Target)

unique,count = np.unique(Target,return_counts=True)
plt.bar(CATAGORIES,count)

"""# **Split Data into training and Testing data**

If the data is not arranged into two sets for train and test we take the help of 

```sklearn.model_selsection``` to split the data

**Syntax :**

```
X_train, X_test, y_train, y_test = train_test_split(Flattened_data,Target,test_size=0.2, random_state=42)
```


# **Concept Of test_size**

We break the who dataset into two parts. One of them is kept for training the ML Model and the other is to test the model

So as the training part requires more data we try to divide the whole dataset intto

```
Training Data : Testing data :: 70 : 30 or 80 : 20
```
So in the ```test_size``` we initialise it with 0.2 or 0.3 or 0.33 which describes the part of dataset which has to be kept for testing purpose

# **Some Important Notes**

1. The Rows of X_train and y_train must be equal 
2. The ```shape``` of the X_train will look something like this
  ```(n,m)```
3. The ```shape``` of y_train will look something like this
  ```(n,)```

  Here ```n``` is the number of Rows of X_train

  
  
  You can check the shape of the both by the function ```shape()```

  ***Syntax :***
  
  ```X_train.shape()```
"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(Flattened_data,Target,test_size=0.2, random_state=42)

X_train.shape

y_train.shape

from sklearn.model_selection import GridSearchCV
from sklearn import svm

"""# **Using GridSearchCV**

There are many methods in GridSearchV. I am taking the ```linear``` and ```gamma```.

It gives back the best possible solution between these approaches

We also want to check whats the actual probabily of success the model 

To check that we set ```probability = True```

**Syntax :**

```
svc = svm.SVC(probability = True)```
"""

param_grid = [
  {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
  {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
 ]
svc = svm.SVC(probability = True)
clf = GridSearchCV(svc,param_grid)
clf.fit(X_train,y_train)

"""# **Now Checking how accurate it is**

What we do is that we compare the predicted score of ```y``` with the real score of ```y```

**Syntrax :**

To get the predicted output

```
y_pred = clf.predict(X.test)
y_pred
```

"""

y_pred = clf.predict(X_test)
y_pred

y_test

"""# **Using sklearn.metrics**

To automate the process of creating the accuracy score we import 
```sklearn.metrics```

From this library we use ```accuracy_score,confusion_matrix```
"""

from sklearn.metrics import accuracy_score,confusion_matrix
accuracy_score(y_pred,y_test)

confusion_matrix(y_pred,y_test)

"""# **Now Storing the current set**

We dump the progress to ```pickle``` for future reference

**Syntax :**
```
pickle.dump(clf,open('Model_Name.p','wb'))
```
"""

import pickle
pickle.dump(clf,open('img_model.p','wb'))

"""**Now with the help of this pickle value I am going to load the model**

This helps to deploy the model

**Syntax :**

```
model = pickle.load(open("Model_Name.p','rb))
``` 
"""

model = pickle.load(open("img_model.p",'rb'))

"""# **Now Testing With Real Image**

We can check with an online image by this line

**Syntax :**

```
url = input("URL_Of_Image")
```
"""

Flattened_data = []
url = input("Enter URL of the image")
img = imread(url)
img_resized = resize(img,(150,150,3))
Flattened_data.append(img_resized.flatten())
Flattened_data = np.array(Flattened_data)
y_out = model.predict(Flattened_data)
y_out = CATAGORIES[y_out[0]]
print("Predicted Output :")
print(y_out)