from data.preprocess import load_and_preprocess_data
from model.cnn_model import build_model
from gui.app import create_gui

def load_data():
    """Carrega e pré-processa os dados."""
    (train_images, train_labels), (test_images, test_labels), class_names = load_and_preprocess_data()
    return train_images, train_labels, test_images, test_labels, class_names

def train_model(train_images, train_labels, test_images, test_labels):
    """Constrói e treina o modelo CNN."""
    model = build_model()
    model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))
    return model

def evaluate_model(model, test_images, test_labels):
    """Avalia o modelo com dados de teste e imprime a precisão."""
    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
    print(f'\nModel accuracy: {test_acc}')

def main():
    # Carrega os dados
    train_images, train_labels, test_images, test_labels, class_names = load_data()

    # Treina o modelo
    model = train_model(train_images, train_labels, test_images, test_labels)

    # Avalia o modelo
    evaluate_model(model, test_images, test_labels)

    # Inicia a GUI
    create_gui(model, class_names)

if __name__ == "__main__":
    main()
