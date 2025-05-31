import pickle
import os 

# Ensure the directory exists


with open("E:/py.proj-20250522T154056Z-1-001/py.proj/MS_sys/model_100lb_6h.pkl", "rb")as f:
    modelcals100 = pickle.load(f)

with open("E:/py.proj-20250522T154056Z-1-001/py.proj/MS_sys/model_200lb_6h.pkl", "rb")as f:
    modelcals200 = pickle.load(f)

with open("E:/py.proj-20250522T154056Z-1-001/py.proj/MS_sys/model_300lb_6h.pkl", "rb")as f:
    modelcals300 = pickle.load(f)
with open("lng_model.pkl","rb") as f:
    lng_model = pickle.load(f)
with open("E:/py.proj-20250522T154056Z-1-001/py.proj/MS_sys/diabetes_pred.pkl", "rb")as f:
    daib_model = pickle.load(f)

class MS20Models:
    def __init__(self, modelcals100, modelcals200, modelcals300,lng_model, daib_model):
        
        self.modelcals100 = modelcals100
        self.modelcals200 = modelcals200
        self.modelcals300 = modelcals300
        self.lng_model = lng_model
        self.daib_model = daib_model

models = MS20Models(modelcals100, modelcals200, modelcals300, lng_model, daib_model)



pred = models.daib_model.predict([[33.4,198,8.9,1,1,1,1]])
print(pred[0])