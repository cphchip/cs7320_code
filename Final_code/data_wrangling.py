import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
import numpy as np


def clean_data(file):
    df = pd.read_csv(file)
    newdf = df.dropna()
    # print(newdf.size)

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

    raw_data = newdf.to_numpy()

    '''
        The following line was necessary to prevent throwing error:
        ValueError: Failed to convert a NumPy array to a Tensor (Unsupported object type float)
    '''
    raw_data = np.asarray(raw_data).astype(np.float32)
    
    return raw_data


def nnet(raw_data):
    seed = 7
    np.random.seed(seed)
    dataset = raw_data
    X = dataset[:, 0:8]
    Y = dataset[:, 7]
    
    model = Sequential()
    model.add(Dense(16, input_dim=8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    X_train, X_test, Y_train, Y_test = train_test_split(X, 
                                                        Y, test_size=0.33, random_state=
                                                            seed
                                                        )

    model.compile(loss='binary_crossentropy', 
                  optimizer = 'adam', 
                  metrics=['accuracy'])
    
    model.fit(X_train, 
              Y_train, 
              validation_data = (X_test, Y_test), 
              epochs = 150, 
              batch_size = 10)

    # model.fit(X, 
    #            Y, 
    #            validation_split = 0.33, 
    #            epochs = 150, 
    #            batch_size = 10)

nnet(clean_data('7320.finaldata.csv'))
