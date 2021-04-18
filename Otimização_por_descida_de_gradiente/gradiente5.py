import numpy as np

def compute_cost(theta_0, theta_1, theta_2, theta_3, theta_4, theta_5, data):
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
    d = theta_3
    e = theta_4
    f = theta_5

    for row in data:
        preco = row[5]
        condicao = row[4]
        garagem = row[3]
        sala = row[2]
        ano = row[1]
        qualidade = row[0]
        sum0 += (preco-(a+(b*condicao)+(c*garagem)+(d*sala)+(e*ano)+(f*qualidade)))**2

    error_theta_0 = (sum0/len(data))

    return error_theta_0

def step_gradient(theta_0_current, theta_1_current, theta_2_current, theta_3_current, theta_4_current, theta_5_current, data, alpha):
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
    sum3 = 0
    sum4 = 0
    sum5 = 0
    n = len(data)
    for row in data:
      x = row[0]
      x2 = row[1]
      x3 = row[2]
      x4 = row[3]
      x5 = row[4]
      y = row[5] 

      h0 = theta_0_current + theta_1_current*x + theta_2_current*x2 + theta_3_current*x3 + theta_4_current*x4 + theta_5_current*x5

      sum0 += h0 - y
      sum1 += (h0 - y) * x
      sum2 += (h0 - y) * x2
      sum3 += (h0 - y) * x3
      sum4 += (h0 - y) * x4
      sum5 += (h0 - y) * x5

    der0 = 2/n * sum0
    der1 = 2/n * sum1
    der2 = 2/n * sum2
    der3 = 2/n * sum3
    der4 = 2/n * sum4
    der5 = 2/n * sum5

    theta_0_updated = theta_0_current - alpha*der0
    theta_1_updated = theta_1_current - alpha*der1
    theta_2_updated = theta_2_current - alpha*der2
    theta_3_updated = theta_3_current - alpha*der3
    theta_4_updated = theta_4_current - alpha*der4
    theta_5_updated = theta_5_current - alpha*der5

    return theta_0_updated, theta_1_updated, theta_2_updated, theta_3_updated, theta_4_updated, theta_5_updated

def gradient_descent(data, starting_theta_0, starting_theta_1, starting_theta_2, starting_theta_3, starting_theta_4, starting_theta_5, learning_rate, num_iterations):
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
    theta_3 = starting_theta_3
    theta_4 = starting_theta_4
    theta_5 = starting_theta_5

    
    # variável para armazenar o custo ao final de cada step_gradient
    cost_graph = []
    
    # vetores para armazenar os valores de Theta0 e Theta1 apos cada iteração de step_gradient (pred = Theta1*x + Theta0)
    
    # Para cada iteração, obtem novos (Theta0,Theta1) e calcula o custo (EQM)
    for i in range(num_iterations):
        cost_graph.append(compute_cost(theta_0, theta_1, theta_2, theta_3, theta_4, theta_5, data))
        theta_0, theta_1, theta_2, theta_3, theta_4, theta_5 = step_gradient(theta_0, theta_1, theta_2, theta_3, theta_4, theta_5, data, learning_rate)
        
    return [theta_0, theta_1, theta_2, theta_3, theta_4, theta_5, cost_graph]