FROM python:3.9


COPY model.py basic.py requirements.txt graph/  ./


RUN pip install -r requirements.txt

# Comando por defecto para ejecutar el modelo
CMD ["python3", "model.py"]
