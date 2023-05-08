import pandas as pd
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import numpy as np


def clean_data(file):
    df = pd.read_csv(file)
    newdf = df.dropna()

    for x in newdf.index:
        if len(newdf.loc[x, 'rank']) > 2:
            value = newdf.loc[x, 'rank']
            new_val = value[0:2]
            newdf.loc[x, 'rank'] = new_val

        if len(newdf.loc[x, 'state']) > 2:
            value = newdf.loc[x, 'state']
            new_val = value[0:2]
            newdf.loc[x, 'state'] = new_val

    for x in newdf.index: # convert text to numeric
        if newdf.loc[x, 'rank'] == 'LO':
            value = newdf.loc[x, 'rank']
            new_val = 1
            newdf.loc[x, 'rank'] = new_val
        elif newdf.loc[x, 'rank'] == 'ME':
            value = newdf.loc[x, 'rank']
            new_val = 2
            newdf.loc[x, 'rank'] = new_val
        elif newdf.loc[x, 'rank'] == 'HI':
            value = newdf.loc[x, 'rank']
            new_val = 3
            newdf.loc[x, 'rank'] = new_val

        if newdf.loc[x, 'state'] == 'TX':
            value = newdf.loc[x, 'state']
            new_val = 1
            newdf.loc[x, 'state'] = new_val
        elif newdf.loc[x, 'state'] == 'CA':
            value = newdf.loc[x, 'state']
            new_val = 2
            newdf.loc[x, 'state'] = new_val
        elif newdf.loc[x, 'state'] == 'NY':
            value = newdf.loc[x, 'state']
            new_val = 3
            newdf.loc[x, 'state'] = new_val

    print(f"The correlation between f1 and success is: ", 
          newdf['f1'].corr(newdf['success']))
    print(f"The correlation between f2 and success is: ", 
          newdf['f2'].corr(newdf['success']))
    print(f"The correlation between f3 and success is: ", 
          newdf['f3'].corr(newdf['success']))
    print(f"The correlation between f4 and success is: ", 
          newdf['f4'].corr(newdf['success']))
    print(f"The correlation between f5 and success is: ", 
          newdf['f5'].corr(newdf['success']))
    
    '''Choose feature dataset to drop'''
    # newdf = newdf.drop('f5', axis=1)
    # newdf = newdf.drop('f2', axis=1)
    # newdf = newdf.drop('f4', axis=1)
    newdf = newdf.drop('state', axis=1)
    newdf = newdf.drop('rank', axis=1)
    raw_data = newdf.to_numpy()

    '''
        The following line was necessary to prevent throwing error:
        ValueError: Failed to convert a NumPy array to a Tensor (Unsupported object type float)
    '''
    raw_data = np.asarray(raw_data).astype(np.float32)

    '''Pick one of these standardization techniques'''
    scaled_data = data_normalize(raw_data)
    # scaled_data = data_standardize(raw_data)
    
    return scaled_data


def data_normalize(raw_data):

    norm = MinMaxScaler().fit(raw_data)
    raw_data_norm = norm.transform(raw_data)
    
    return raw_data_norm


def data_standardize(raw_data):

    scaler = StandardScaler()
    raw_data_stand = scaler.fit_transform(raw_data)

    return raw_data_stand


def nnet(scaled_data):
    inputs = 5
    seed = 7
    np.random.seed(seed)
    dataset = scaled_data
    X = dataset[:, 0:inputs]
    Y = dataset[:, inputs]
    
    model = Sequential()
    model.add(Dense(12, input_dim=inputs, activation='relu'))
    # model.add(Dense(12, activation='relu')) # add layer
    model.add(Dense(1, activation='sigmoid'))

    X_train, X_test, Y_train, Y_test = train_test_split(X, 
                                                        Y, 
                                                        test_size=0.33, 
                                                        random_state=
                                                            seed
                                                        )

    opt = keras.optimizers.Adam(learning_rate=0.001) # default 0.001
    model.compile(loss='binary_crossentropy', 
                  optimizer = opt, 
                  metrics=['accuracy'])
    
    model.fit(X_train, 
              Y_train, 
              validation_data = (X_test, Y_test), 
              epochs = 25, 
              batch_size = 10)
    

nnet(clean_data('7320.finaldata.csv'))

# Below are 5 examples of best performance
'''
Epoch 25/25
7/7 [==============================] - 0s 6ms/step - loss: 0.4560 - accuracy: 0.8769 - val_loss: 0.5698 - val_accuracy: 0.8182
'''

'''
Epoch 25/25
7/7 [==============================] - 0s 14ms/step - loss: 0.5869 - accuracy: 0.8615 - val_loss: 0.6213 - val_accuracy: 0.8182
'''

'''
Epoch 120/120
7/7 [==============================] - 0s 12ms/step - loss: 0.1763 - accuracy: 0.9231 - val_loss: 0.5681 - val_accuracy: 0.7879
'''

'''
Epoch 20/20
65/65 [==============================] - 0s 3ms/step - loss: 0.2615 - accuracy: 0.9231 - val_loss: 0.5205 - val_accuracy: 0.8182
'''

'''
Epoch 25/25
7/7 [==============================] - 0s 12ms/step - loss: 0.2262 - accuracy: 0.9077 - val_loss: 1.5943 - val_accuracy: 0.7879
'''