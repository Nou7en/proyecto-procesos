# Usa una imagen base de Python liviana
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de dependencias e instálalas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código del CRUD
COPY . .

# Expone el puerto donde corre tu app (ej. 5000 para Flask o 8000 para FastAPI)
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]