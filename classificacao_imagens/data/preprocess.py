import tensorflow as tf

def load_and_preprocess_data():
    # Carrega os dados CIFAR-10
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.cifar10.load_data()

    # Normaliza os valores dos pixels para o intervalo [0, 1]
    MAX_PIXEL_VALUE = 255.0
    train_images = train_images.astype('float32') / MAX_PIXEL_VALUE
    test_images = test_images.astype('float32') / MAX_PIXEL_VALUE

    # Define os nomes das classes
    class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
                   'dog', 'frog', 'horse', 'ship', 'truck']

    return (train_images, train_labels), (test_images, test_labels), class_names
