FROM python:3.10-slim

# Instalar versiones específicas que son conocidas por ser compatibles
RUN pip install \
    numpy==2.1.2 \
    scikit-learn==1.5.2 \
    pandas==2.2.3 \
    flask==2.0.1 \
    gunicorn==20.1.0 \
    werkzeug==2.0.3

WORKDIR /app

# Crear la estructura de directorios y posicionarnos correctamente
RUN mkdir -p scripts models
WORKDIR /app/scripts

# Copiar los archivos en la estructura esperada
COPY ["week_5_deployment/scripts/predict_2.py", "./"]
COPY ["week_5_deployment/models/model_C=1.0.bin", "../models/"]

EXPOSE 9696

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "predict_2:app" ]
