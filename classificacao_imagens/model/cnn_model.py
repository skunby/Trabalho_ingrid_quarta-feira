from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

def build_model():
    # Define as dimensões das imagens de entrada
    input_shape = (32, 32, 3)
    num_classes = 10

    # Criação do modelo sequencial
    model = Sequential()

    # Adiciona as camadas convolucionais e de pooling
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))

    # Camada de flatten para transformar os mapas de características em um vetor unidimensional
    model.add(Flatten())

    # Camadas densas (totalmente conectadas) com função de ativação relu
    model.add(Dense(64, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))  # Camada de saída com ativação softmax para classificação multiclasse

    # Compilação do modelo
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    return model
