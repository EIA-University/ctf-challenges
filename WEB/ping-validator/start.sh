#!/bin/sh

while true; do
    # Comprobar si el servidor de Node.js está en ejecución
    if ! pgrep -x "node" > /dev/null; then
        echo "El servidor de Node.js se detuvo. Reiniciando..."
        # Comando para ejecutar el servidor de Node.js
        node index.js &
    fi
    # Esperar un tiempo antes de volver a comprobar
    sleep 5
done
