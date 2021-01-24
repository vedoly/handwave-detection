from sklearn.metrics import confusion_matrix
from mlxtend.plotting import plot_confusion_matrix
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import *
from tensorflow.keras.optimizers import *
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Model


def createModel():
    model = Sequential()

    inputs = Input([120, 4])

    conv1_1 = Conv1D(filters=128, kernel_size=10,
                     padding='same', activation='relu')(inputs)
    input_shortcut = conv1_1

    conv1 = Conv1D(filters=128, kernel_size=10,
                   padding='same', activation='relu')(inputs)
    batch1 = BatchNormalization()(conv1)
    drop1 = Dropout(0.3)(batch1)
    conv2 = Conv1D(filters=128, kernel_size=10,
                   padding='same', activation='relu')(drop1)
    batch2 = BatchNormalization()(conv2)
    drop2 = Dropout(0.3)(batch2)
    conv3 = Conv1D(filters=128, kernel_size=10, padding='same')(drop2)
    batch3 = BatchNormalization()(conv3)
    drop3 = Dropout(0.5)(batch3)
    res1 = Add()([input_shortcut, drop3])
    res1_1 = res2_1 = Activation('relu')(res1)

    global1 = GlobalAveragePooling1D()(res1_1)
    dense1 = Dense(128, activation='relu')(global1)
    dense2 = Dense(128, activation='relu')(dense1)
    dense3 = Dense(128, activation='relu')(dense2)
    dense4 = Dense(2, activation='softmax')(dense3)
    model = Model(inputs=inputs, outputs=dense4)
    model.compile(loss="categorical_crossentropy", optimizer=Adam(
        learning_rate=1e-3), metrics=["accuracy"])
    return model
# %%
