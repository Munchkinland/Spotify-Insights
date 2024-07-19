# Utiliza una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos y el código fuente al contenedor
COPY requirements.txt requirements.txt
COPY api.py spotify_client.py ./

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que Flask correrá
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "api.py"]
