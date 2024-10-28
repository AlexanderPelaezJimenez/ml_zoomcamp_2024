import pickle

with open('dv.bin', 'rb') as f_in:
    dv = pickle.load(f_in)

with open('model1.bin', 'rb') as f_in:
    model = pickle.load(f_in)
    
customer = {"job": "management", "duration": 400, "poutcome": "success"}

X = dv.transform([customer])
y_pred = model.predict_proba(X)[0, 1]

print('input:', customer)
print('probability:', round(y_pred, 3))