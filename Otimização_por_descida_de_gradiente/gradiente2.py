# -*- coding: utf-8 -*-
import numpy as np

def compute_cost(theta_0, theta_1, theta_2, data):
    """
    Calcula o erro quadratico medio
    
    Args:
        theta_0 (float): intercepto da reta 
        theta_1 (float): inclinacao da reta
        data (np.array): matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    
    Retorna:
        float: o erro quadratico medio
    """
    total_cost = 0

    ### SEU CODIGO AQUI
    sum0 = 0
    a = theta_0
    b = theta_1
    c = theta_2
    for row in data:
        preco = row[2]
        qualidade = row[1]
        area = row[0]
        sum0 += (preco-(a+(b*area)+(c*qualidade)))**2

    error_theta_0 = (sum0/len(data))

    return error_theta_0

def step_gradient(theta_0_current, theta_1_current, theta_2_current, data, alpha):
    """Calcula um passo em direção ao EQM mínimo
    
    Args:
        theta_0_current (float): valor atual de theta_0
        theta_1_current (float): valor atual de theta_1
        data (np.array): vetor com dados de treinamento (x,y)
        alpha (float): taxa de aprendizado / tamanho do passo 
    
    Retorna:
        tupla: (theta_0, theta_1) os novos valores de theta_0, theta_1
    """
    
    theta_0_updated = 0
    theta_1_updated = 0
    theta_2_updated = 0
    
    ### SEU CODIGO AQUI
    sum0 = 0
    sum1 = 0
    sum2 = 0
    n = len(data)
    for row in data:
      x = row[0]
      x2 = row[1]
      y = row[2] 

      h0 = theta_0_current + theta_1_current*x + theta_2_current*x2

      sum0 += h0 - y
      sum1 += (h0 - y) * x
      sum2 += (h0 - y) * x2

    der0 = 2/n * sum0
    der1 = 2/n * sum1
    der2 = 2/n * sum2

    theta_0_updated = theta_0_current - alpha*der0
    theta_1_updated = theta_1_current - alpha*der1
    theta_2_updated = theta_2_current - alpha*der2

    return theta_0_updated, theta_1_updated, theta_2_updated

def gradient_descent(data, starting_theta_0, starting_theta_1, starting_theta_2, learning_rate, num_iterations):
    """executa a descida do gradiente
    
    Args:
        data (np.array): dados de treinamento, x na coluna 0 e y na coluna 1
        starting_theta_0 (float): valor inicial de theta0 
        starting_theta_1 (float): valor inicial de theta1
        learning_rate (float): hyperparâmetro para ajustar o tamanho do passo durante a descida do gradiente
        num_iterations (int): hyperparâmetro que decide o número de iterações que cada descida de gradiente irá executar
    
    Retorna:
        list : os primeiros dois parâmetros são o Theta0 e Theta1, que armazena o melhor ajuste da curva. O terceiro e quarto parâmetro, são vetores com o histórico dos valores para Theta0 e Theta1.
    """

    # valores iniciais
    theta_0 = starting_theta_0
    theta_1 = starting_theta_1
    theta_2 = starting_theta_2

    
    # variável para armazenar o custo ao final de cada step_gradient
    cost_graph = []
    
    # vetores para armazenar os valores de Theta0 e Theta1 apos cada iteração de step_gradient (pred = Theta1*x + Theta0)
    theta_0_progress = []
    theta_1_progress = []
    theta_2_progress = []
    
    # Para cada iteração, obtem novos (Theta0,Theta1) e calcula o custo (EQM)
    for i in range(num_iterations):
        cost_graph.append(compute_cost(theta_0, theta_1, theta_2, data))
        theta_0, theta_1, theta_2 = step_gradient(theta_0, theta_1, theta_2, data, learning_rate)
        theta_0_progress.append(theta_0)
        theta_1_progress.append(theta_1)
        theta_2_progress.append(theta_2)
        
    return [theta_0, theta_1, theta_2, cost_graph, theta_0_progress, theta_1_progress, theta_2_progress]