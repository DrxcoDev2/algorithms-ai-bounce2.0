FROM python:3.9


COPY model.py basic.py requirements.txt core/ia.py graph/  ./


RUN pip install -r requirements.txt

# Comando por defecto para ejecutar el modelo
CMD ["python3", "ia.py"]
