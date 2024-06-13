Passos para executar a atividade de Ingrid:

### Instalação de Pacotes Python
Para executar o projeto, primeiro é necessário instalar algumas bibliotecas Python. Abra o terminal e execute os seguintes comandos:

bash
pip install opencv-python
pip install opencv-python-headless # Contém funcionalidades adicionais, como suporte a formatos de vídeo mais avançados
pip install tensorflow
pip install matplotlib


### Explicação das Bibliotecas Utilizadas

*OpenCV (Open Source Computer Vision Library):*
OpenCV é uma biblioteca de visão computacional e aprendizado de máquina de código aberto, com mais de 2500 algoritmos otimizados para uma ampla gama de tarefas, incluindo processamento de imagem, detecção de rostos, rastreamento de objetos e mais. É escrita em C++ e possui interfaces para Python, Java e MATLAB/OCTAVE.

*TensorFlow/Keras:*
TensorFlow é uma biblioteca de código aberto do Google para computação numérica e aprendizado profundo, utilizando grafos computacionais para operações eficientes em CPUs e GPUs. Keras é uma API de alto nível para redes neurais que roda sobre TensorFlow, projetada para ser modular, extensível e fácil de usar.

*NumPy (Numerical Python):*
NumPy é essencial para computação científica em Python, fornecendo arrays multidimensionais e ferramentas para trabalhar eficientemente com eles, incluindo operações matemáticas, álgebra linear e integração com outras bibliotecas como SciPy e pandas.

*Matplotlib:*
Matplotlib é uma biblioteca de plotagem em Python que permite criar figuras de qualidade de publicação em diversos formatos e ambientes. É amplamente utilizada para criar gráficos de linha, dispersão, histogramas, entre outros, e é integrada com NumPy e pandas.

### Dataset Utilizado
O dataset utilizado neste projeto foi o CIFAR-10.

### Estrutura do Projeto

*data/preprocess.py:*
- *Objetivo:* Carregar e pré-processar o conjunto de dados CIFAR-10.
- *Importações:* TensorFlow e NumPy.
- *Função load_and_preprocess_data:* Carrega o CIFAR-10, normaliza os valores dos pixels para o intervalo [0, 1] e retorna os conjuntos de treino e teste, além dos nomes das classes.

*model/cnn_model.py:*
- *Objetivo:* Definir e compilar um modelo de rede neural convolucional (CNN).
- *Importações:* Models e layers do Keras.
- *Função build_model:* Cria um modelo sequencial com camadas convolucionais, de pooling, flatten, densas e de saída. Compila o modelo com otimizador Adam, função de perda de entropia cruzada e métrica de precisão.

*utils/visualization.py:*
- *Objetivo:* Pré-processar imagens individuais e visualizar as predições do modelo.
- *Importações:* OpenCV (cv2), NumPy e Matplotlib.
- *Função preprocess_image:* Carrega, converte, redimensiona e normaliza uma imagem para ser compatível com o modelo.
- *Função visualize_prediction:* Pré-processa a imagem e faz predições usando o modelo, exibindo a imagem original e a classe predita.

*gui/app.py:*
- *Objetivo:* Implementar a interface gráfica com Tkinter.
- *Importações:* Tkinter e a função visualize_prediction.
- *Função load_image_and_predict:* Abre uma janela de diálogo para o usuário selecionar uma imagem, e chama visualize_prediction para exibir a predição dessa imagem.
- *Função create_gui:* Cria a interface gráfica principal com um botão que carrega imagens para classificação.

*main.py:*
- *Objetivo:* Integrar todas as partes do projeto, incluindo carregamento de dados, treinamento do modelo e inicialização da interface gráfica.
- *Importações:* Funções dos módulos data, model e gui.
- *Função main:* Carrega e pré-processa os dados, constrói, treina e avalia o modelo, e inicia a interface gráfica.

### Funcionamento do Projeto

1. *Carregamento dos Dados:* Utiliza load_and_preprocess_data para carregar e normalizar o CIFAR-10.
2. *Construção do Modelo:* build_model define uma CNN utilizando Keras/TensorFlow.
3. *Treinamento do Modelo:* model.fit é utilizado para treinar a CNN com os dados de treino.
4. *Avaliação do Modelo:* model.evaluate avalia a precisão do modelo utilizando os dados de teste.
5. *Interface Gráfica:* create_gui inicia uma interface Tkinter que permite carregar imagens para classificação.
6. *Predição e Visualização:* Quando uma imagem é carregada, load_image_and_predict chama visualize_prediction para mostrar a predição da classe da imagem.

Este projeto integra diversas tecnologias e bibliotecas essenciais para ciência de dados e aprendizado de máquina em Python, proporcionando uma solução completa desde o pré-processamento de dados até a visualização interativa das predições do modelo.
