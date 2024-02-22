# Rede-Neural---Pycharm

#Tensores em PyTorch
Tensores são estruturas de dados fundamentais em PyTorch, um framework popular de aprendizado de máquina e computação científica. Eles são essenciais para representar dados multidimensionais, como matrizes e vetores, e realizar operações eficientes sobre eles. No contexto de PyTorch, os tensores são muito semelhantes aos arrays NumPy, mas com a vantagem de suportar cálculos em GPUs para aceleração de computação. Isso os torna ideais para processar grandes conjuntos de dados e executar operações intensivas em termos computacionais, como treinamento de redes neurais profundas. Com tensores, os desenvolvedores podem implementar algoritmos de aprendizado de máquina e realizar manipulações de dados de forma eficiente e flexível, aproveitando a infraestrutura de computação paralela oferecida por GPUs.

#Perceptrons
Os perceptrons são modelos de neurônios artificiais básicos que formam as unidades fundamentais das redes neurais. Eles foram introduzidos por Frank Rosenblatt na década de 1950 e constituem a base dos primeiros modelos de aprendizado de máquina. Um perceptron recebe múltiplas entradas, cada uma ponderada por um peso, e produz uma saída binária com base em uma função de ativação, como a função degrau. Embora perceptrons individuais sejam limitados a modelar apenas problemas linearmente separáveis, eles formam blocos de construção cruciais para redes neurais mais complexas, como redes multicamadas. Com o advento de algoritmos de treinamento mais avançados, como o algoritmo de retropropagação, os perceptrons evoluíram para neurônios mais sofisticados e poderosos, tornando-se componentes essenciais em uma variedade de aplicações de aprendizado de máquina, como classificação de imagens, reconhecimento de fala e processamento de linguagem natural.


<h1>Classificão Linear</h1>

#O codigo está na pasta aprendendo 

<h3>Função plotmodel(w1, w2, b)</h3>
Esta função plota um modelo linear com os pesos w1 e w2 e o viés b. Ele cria um gráfico de dispersão dos dados de entrada X e os colore de acordo com as saídas esperadas Y. Em seguida, desenha a linha do modelo no gráfico.

<h3>Função classify(ponto, w1, w2, b)</h3>
Esta função classifica um ponto ponto com base nos pesos w1 e w2 e no viés b. Retorna a classe da amostra (0 ou 1) e a cor correspondente.

Uso do código
Defina os pesos w1, w2 e o viés b.
Chame a função plotmodel(w1, w2, b) para plotar o modelo.
Classifique um ponto usando a função classify(ponto, w1, w2, b).
Plote o ponto classificado usando a função plotmodel(w1, w2, b) novamente.
Calcule a acurácia do modelo em relação aos dados de entrada X e saídas esperadas Y.
