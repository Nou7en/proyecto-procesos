# Usa una imagen base de Python liviana
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de dependencias e instálalas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código del CRUD
COPY . .

# Expone el puerto donde corre la app
EXPOSE 5000

# Comando para ejecutar la aplicación (FastAPI)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]