import gradiente2
import csv

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    areaList = []
    priceList = []
    qualidadeList = []
    with open('house_prices_train.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            areaList.append(int(row['GrLivArea']))
            priceList.append(int(row['SalePrice']))
            qualidadeList.append(int(row['OverallQual']))

    maxArea = max(areaList)
    minArea = min(areaList)

    maxQualidade = max(qualidadeList)
    minQualidade = min(qualidadeList)

    for i in range(len(areaList)):
        areaList[i] = (areaList[i] - minArea) / (maxArea - minArea)
        qualidadeList[i] = (qualidadeList[i] - minQualidade) / (maxQualidade - minQualidade)


    data = [[areaList[i], qualidadeList[i], priceList[i]] for i in range(len(priceList))]
    theta_0, theta_1, theta_2, cost_graph, theta_0_progress, theta_1_progress, theta_2_progress = gradiente2.gradient_descent(data, starting_theta_0=0, starting_theta_1=0, starting_theta_2=0, learning_rate=0.1, num_iterations=1000)
    
    print("error = ", gradiente2.compute_cost(theta_0, theta_1, theta_2, data), "theta 0: ", theta_0, "theta 1: ", theta_1, "theta 2: ", theta_2)

    #plt.figure(figsize=(10, 6))
    #plt.scatter(areaList+qualidadeList, priceList)

    #pred0 = [458.35999 * item + 0.001 for item in areaList]
    #pred1 = [theta_1 * item + theta_0 for item in areaList]
    #plt.plot(areaList, pred0, c='r')
    #plt.plot(areaList, pred1, c='r')

    #plt.xlabel('Area (normalized)')
    #plt.ylabel('Preço')
    #plt.title('Custo beneficio')
    #plt.show()