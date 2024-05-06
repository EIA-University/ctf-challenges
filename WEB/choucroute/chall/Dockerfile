# Usa la imagen oficial de Python como base
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY app /app
COPY requirements.txt .
COPY gunicorn_config.py .
COPY flag .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

RUN ls

RUN pwd

# Define las variables de entorno
ENV FLASK_APP=app
ENV FLASK_ENV=production

# Expone el puerto 8000
EXPOSE 8000

# Ejecuta Gunicorn para servir la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8000","-c", "gunicorn_config.py", "wsgi:application"]
