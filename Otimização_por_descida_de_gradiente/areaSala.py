import gradiente
import csv

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    areaList = []
    priceList = []
    with open('house_prices_train.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            areaList.append(int(row['GrLivArea']))
            priceList.append(int(row['SalePrice']))

    maxArea = max(areaList)
    minArea = min(areaList)



    for i in range(len(areaList)):
        areaList[i] = (areaList[i] - minArea) / (maxArea - minArea)


    data = [[areaList[i], priceList[i]] for i in range(len(priceList))]
    theta_0, theta_1, cost_graph, theta_0_progress, theta_1_progress = gradiente.gradient_descent(data, starting_theta_0=0, starting_theta_1=0, learning_rate=0.1, num_iterations=1000)
    
    print("error = ", gradiente.compute_cost(theta_0, theta_1, data), "theta 0 = ", theta_0, "theta 1 = ", theta_1)

    plt.figure(figsize=(10, 6))
    plt.scatter(areaList, priceList)

    pred0 = [458.35999 * item + 0.001 for item in areaList]
    pred1 = [theta_1 * item + theta_0 for item in areaList]
    plt.plot(areaList, pred0, c='r')
    plt.plot(areaList, pred1, c='r')

    plt.xlabel('Area (normalized)')
    plt.ylabel('Preço')
    plt.title('Custo beneficio')
    plt.show()