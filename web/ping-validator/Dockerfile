# Usa una imagen base de Node.js
FROM node:alpine3.19@sha256:6d0f18a1c67dc218c4af50c21256616286a53c09e500fadf025b6d342e1c90ae

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el package.json y package-lock.json (si existe) al directorio de trabajo
COPY src/* ./

# Instala las dependencias del proyecto
RUN npm install

# Expone el puerto 3000 (o el puerto en el que tu aplicación esté escuchando)
EXPOSE 8000

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["node", "index.js"]
