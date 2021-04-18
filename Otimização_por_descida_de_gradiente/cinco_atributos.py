import gradiente5
import csv

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    areaList = []
    priceList = []
    areaGaragem = []
    condicao = []
    anoList = []
    qualidadeList = []
    with open('house_prices_train.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            areaList.append(int(row['GrLivArea']))
            priceList.append(int(row['SalePrice']))
            areaGaragem.append(int(row['GarageArea']))
            condicao.append(int(row['OverallCond']))
            anoList.append(int(row['YearBuilt']))
            qualidadeList.append(int(row['OverallQual']))

    maxArea = max(areaList)
    minArea = min(areaList)

    maxGaragem = max(areaGaragem)
    minGaragem = min(areaGaragem)

    maxAno = max(anoList)
    minAno = min(anoList)

    maxCondicao = max(condicao)
    minCondicao = min(condicao)

    maxQualidade = max(qualidadeList)
    minQualidade = min(qualidadeList)

    for i in range(len(areaList)):
        areaList[i] = (areaList[i] - minArea) / (maxArea - minArea)
        qualidadeList[i] = (qualidadeList[i] - minQualidade) / (maxQualidade - minQualidade)
        anoList[i] = (anoList[i] - minAno) / (maxAno - minAno)
        condicao[i] = (condicao[i] - minCondicao) / (maxCondicao - minCondicao)
        areaGaragem[i] = (areaGaragem[i] - minGaragem) / (maxGaragem - minGaragem)


    data = [[qualidadeList[i], anoList[i], areaList[i], areaGaragem[i], condicao[i], priceList[i]] for i in range(len(priceList))]
    theta_0, theta_1, theta_2, theta_3, theta_4, theta_5, cost_graph = gradiente5.gradient_descent(data, starting_theta_0=0, starting_theta_1=0, starting_theta_2=0, starting_theta_3=0, starting_theta_4=0, starting_theta_5=0, learning_rate=0.1, num_iterations=1000)
    
    print("error = ", gradiente5.compute_cost(theta_0, theta_1, theta_2, theta_3, theta_4, theta_5, data), "theta 0: ", theta_0, "theta 1: ", theta_1, "theta 2: ", theta_2, "theta 3: ", theta_3, "theta 4 : ", theta_4, "theta 5: ", theta_5)