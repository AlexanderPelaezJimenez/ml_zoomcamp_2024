import pickle
from flask import Flask, request, jsonify

app = Flask('bank-prediction')

# Cargar el DictVectorizer
with open('dv.bin', 'rb') as f_in:
    dv = pickle.load(f_in)

# Cargar el modelo - nota que aquí usamos model2.bin en lugar de model1.bin
with open('model2.bin', 'rb') as f_in:
    model = pickle.load(f_in)

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    
    result = {
        'subscription_probability': float(y_pred)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)