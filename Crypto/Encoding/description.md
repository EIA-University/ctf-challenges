# El Arte de los Encoders: Protegiendo la UEIA

Se logro interceptar una data en medio de una auditoria de un equipo de la biblioteca de la UEIA, sera que es posible que puedas obtener alguna informacion?

# Hints

## 1

La receta utilizadad es de 4 encoders

Receta? hay alguna pagina que pueda hacer algo asi?


# Solucion

El reto es el siguente texto encodeado en el siguiente orden: Binario, Hexadecimal, Base64, Base32
```
Ahora si, toma tu flag: UEIA{3nc0d1ng_15_4m4z1ng@U_Enc0d3rs12}
```

Para resolverlo, puede hacerse en cyberchef usando la receta de forma inversa

Base32, base64, Hexadecimal y por ultimo Binario para volver al texto original

# Flag

UEIA{3nc0d1ng_15_4m4z1ng@U_Enc0d3rs12}
