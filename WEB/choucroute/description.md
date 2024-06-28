# Choucroute

Encontramos otro servicio ejecutandose en el servidor de la escuela con un comportamiento aun mas sospechoso, podras revelar que es lo que hace?

# Hints

## 1

Hay un compnente con una vulnerabilidad conocida, esta dependencia se encuentra en el package.json

# Solucion


# Flag

UEIA{p1cKl3_L04d5_1s_V3ry_us4fu1l_3a5}


docker build -t choucroute:latest .

docker run -d -p 8124:8000 -it choucroute:latest
