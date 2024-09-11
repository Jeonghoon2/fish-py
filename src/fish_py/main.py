from fastapi import FastAPI, HTTPException
import os
import pickle
from src.fish_py.utils.util import make_knn_model, make_lr_model
from sklearn.neighbors import KNeighborsClassifier
app = FastAPI()


def get_path():
    return os.path.dirname(__file__)
    
def load_model(file_name):

    dir = os.path.join(get_path(), "model")
    full_path = os.path.join(dir, file_name)

    try:
        with open(full_path, 'rb') as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="모델을 찾을 수 없습니다.")


# Linear Regression request
@app.get("/fish/weight")
def get_weight(length: float):
    model = load_model("lr.pkl")
    length_squared = length ** 2
    prediction = model.predict([[length_squared, length]])
    return prediction[0]

# KNeighbors request
@app.get("/fish/type")
def kn_n(length: float, weight: float):
    model = load_model("knn.pkl")  # 훈련된 모델 불러오기
    if model.predict([[length, weight]])[0] == 1:
        return {"type": "도미"}
    else:
        return {"type": "빙어"}

    
# 모델 생성 (Linear Regression)
@app.get("/make/lr/model")
def make_regression_model():
    dir = get_path()
    
    if make_lr_model(dir):
        return "성공적으로 모델을 생성하였습니다."
    else:
        return "이미 생성된 모델이 있습니다."
    

# 모델 생성 (K-NN)
@app.get("/make/k-nn/model")
def make_k_nn_model():
    dir = get_path()

    if make_knn_model(dir):
        return "성공적으로 모델을 생성하였습니다."
    else:
        return "이미 생성된 모델이 있습니다."