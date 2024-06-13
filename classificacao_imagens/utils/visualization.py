import cv2
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model


# Função para pré-processar a imagem
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (32, 32))
    img = img / 255.0
    return np.expand_dims(img, axis=0)


# Função para visualizar a previsão do modelo
def visualize_prediction(image_path, model, class_names):
    img = preprocess_image(image_path)
    prediction = model.predict(img)
    predicted_class = class_names[np.argmax(prediction)]

    plt.imshow(cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB))
    plt.title(f'Prediction: {predicted_class}')
    plt.show()


# Exemplo de uso:
def main():
    # Carrega o modelo treinado (substitua 'nome_do_modelo.h5' pelo caminho correto do seu modelo)
    model = load_model('nome_do_modelo.h5')

    # Lista de nomes das classes (substitua pelos nomes das suas classes)
    class_names = ['classe1', 'classe2', 'classe3', 'classe4', 'classe5']

    # Caminho da imagem para fazer a previsão (substitua 'caminho_para_sua_imagem.jpg' pelo caminho da sua imagem)
    image_path = 'caminho_para_sua_imagem.jpg'

    # Visualiza a previsão
    visualize_prediction(image_path, model, class_names)


if __name__ == "__main__":
    main()
