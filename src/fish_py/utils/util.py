import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
import pickle
import os

def make_lr_model(path):
    dir = os.path.join(path, "model")
    file = "lr.pkl"
    full_path = os.path.join(dir, file)

    # 모델 파일이 존재하지 않을 경우에만 진행
    if not os.path.exists(full_path):
        # 디렉토리가 존재하지 않는 경우 생성
        if not os.path.exists(dir):
            os.makedirs(dir)

        perch_length = np.array([
            8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0,
            21.0, 21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5,
            22.5, 22.7, 23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5,
            27.3, 27.5, 27.5, 27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0,
            36.5, 36.0, 37.0, 37.0, 39.0, 39.0, 39.0, 40.0, 40.0, 40.0,
            40.0, 42.0, 43.0, 43.0, 43.5, 44.0
        ])

        perch_weight = np.array([
            5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
            110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
            130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
            197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
            514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
            820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
            1000.0, 1000.0
        ])

        train_input, test_input, train_target, test_target = train_test_split(perch_length, perch_weight, random_state=42)
        train_input = train_input.reshape(-1, 1)
        test_input = test_input.reshape(-1, 1)
        train_poly = np.column_stack((train_input ** 2, train_input))
        lr = LinearRegression()
        lr.fit(train_poly, train_target)

        with open(full_path, "wb") as f:
            pickle.dump(lr, f)

        return True
    else:
        return False


def make_knn_model(path):
    
    dir = os.path.join(path, "model")
    file = "knn.pkl"
    full_path = os.path.join(dir, file)

    print(full_path)

    # 모델 파일이 존재하지 않을 경우에만 진행
    if not os.path.exists(full_path):

        if not os.path.exists(dir):
            os.makedirs(dir)

        full_path = os.path.join(dir, file)

        print(full_path)
        bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
        bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

        smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
        smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]


        length = bream_length + smelt_length
        weight = bream_weight + smelt_weight

        fish_data = []

        for l, w in zip(length, weight):
            fish_data.append([l, w])

        fish_target = [1] * 35 + [0] * 14

        kn = KNeighborsClassifier()

        kn.fit(fish_data, fish_target)

        with open(full_path, "wb") as f:
            pickle.dump(kn, f)
        
        return True
    else:
        return False
