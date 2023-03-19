import nltk
nltk.download('punkt')
__name__("lotan")
# Importa a classe para o chatbot
from nltk.chat.util import Chat,reflections

# Definição das regras de conversação
pares = [
    [
        r"meu nome é (.*)",
        ["Olá %1, como posso ajudar?", "Oi %1, como posso ser útil?"],
    ],
    [
        r"qual é o seu nome?",
        ["Meu nome é ChatBot, como posso ajudar?"],
    ],
    [
        r"qual é a sua idade?",
        ["Eu sou um programa de computador, não tenho idade :)"],
    ],
    [
        r"(.*) idade (.*) você (.*)",
        ["Eu sou um programa de computador, não tenho idade :)"],
    ],
    [
        r"eu quero (.*)",
        ["Você realmente quer %1?", "Por que você quer %1?", "O que você faria se conseguisse %1?"],
    ],
    [
        r"você pode (.*)",
        ["Claro, eu posso %1. O que mais você precisa?"],
    ],
    [
        r"você sabe (.*)",
        ["Sim, eu sei sobre %1. O que mais você gostaria de saber?"],
    ],
    [
        r"(.*) (feliz|animado|contente|satisfeito)",
        ["Que bom que você está %1! O que mais posso fazer por você?"],
    ],
    [
        r"(.*) (triste|chateado|frustrado|decepcionado)",
        ["Sinto muito que você esteja %1. O que posso fazer para ajudar?"],
    ],
    [
    ]]
from sklearn import tree

# Dados de entrada e saída para treinamento do modelo
dados_entrada = [[0, 0], [0, 1], [1, 0], [1, 1]]
dados_saida = [0, 1, 1, 0]

# Criando o modelo de árvore de decisão
modelo = tree.DecisionTreeClassifier()

# Treinando o modelo com os dados de entrada e saída
modelo.fit(dados_entrada, dados_saida)

# Utilizando o modelo para fazer uma predição
resultado = modelo.predict([[1, 0]])

# Imprimindo o resultado
print(resultado)

__name__("lotan")