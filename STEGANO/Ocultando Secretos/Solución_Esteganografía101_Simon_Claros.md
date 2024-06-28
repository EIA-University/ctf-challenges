# Esteganografía 101 : Ocultando Secretos
****
Recibiste un correo urgente de la UEIA pidiendo que te ayude a decifrar un bonito archivo adjunto. Todo parece normal... o no?

# Hints
***
## 1
***
Debe tener alguna propiedad fuera de lo normal... Revisa los **detalles**

# Solucion
***
El reto viene en forma de .jpg 

1. Adentro de la imagen hay un comentario (***cGFzc3BocmFzZT1qdTV0ZmluZG0z***) para ver el comentario se puede usar : 
-exiftool (**heramienta externa**).
-propiedades de la imagen (click derecho en imagen) y despues en la opcion detalles (**windows**).
-paginas web como https://www.metadata2go.com/

2. Introducir (***cGFzc3BocmFzZT1qdTV0ZmluZG0z***) en cyberchef o un decoder usando base64 a texto normal.
esto nos da la clave para el .jpg la cual es (ju5tfindm3)

3. Usar **steghide** con el comando : steghide extract -sf h4cked.jpg
4. Introducir clave : ju5tfindm3
5.  Abrir o leer "flag.txt"

# Flag
```sh
UEIA{st3g4n0gr4phy_is_t00_e4sy!}
```
#  Gracias! :D

