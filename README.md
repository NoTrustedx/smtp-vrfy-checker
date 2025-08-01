# 📧 smtp-vrfy-checker

Herramienta en Python para realizar verificación de usuarios en servidores SMTP utilizando el comando `VRFY`. Útil en auditorías de seguridad y evaluaciones de configuración de servicios de correo electrónico.

## 🛠️ Características

- ✅ Conexión TCP a servidores SMTP (IPv4)
- ✅ Uso del comando `VRFY` para validar existencia de usuarios
- ✅ Banner grabber del servidor SMTP
- ✅ Soporte de puertos personalizados (por defecto: 25)
- ✅ Manejo de errores comunes (timeout, conexión rechazada, etc.)

## 🚀 Uso

### 📥 Requisitos

- Python 3.x

### ▶️ Ejecución

```bash
python3 smtp_vrfy_checker.py usuario objetivo_ip [-p PUERTO]
````

### 📌 Parámetros

| Parámetro     | Descripción                                   |
| ------------- | --------------------------------------------- |
| `usuario`     | Nombre del usuario a verificar en el servidor |
| `objetivo_ip` | Dirección IP del servidor SMTP                |
| `-p, --port`  | Puerto del servicio SMTP (por defecto: 25)    |


### 📍 Ejemplo

```bash
python3 smtp_vrfy_checker.py root 192.168.1.100
```

Salida esperada:

```
[*] Conectando a 192.168.1.100:25...
[*] Banner del servidor:
220 mail.example.com ESMTP Postfix
[*] Enviando: VRFY root
[+] Respuesta del servidor:
250 2.1.5 User OK
```
## ⚠️ Consideraciones de seguridad

* El comando `VRFY` está **deshabilitado por defecto** en muchos servidores modernos debido a consideraciones de privacidad.
* Esta herramienta debe usarse **solo con autorización** expresa, como parte de pruebas de seguridad, auditorías o entornos de laboratorio.

## 📂 Archivos

* `smtp_vrfy_checker.py`: Script principal
* `README.md`: Este documento

## 📄 Licencia

MIT License – libre para uso, modificación y distribución.

## 👨‍💻 Autor

Erick O.
🔗 GitHub: [@NoTrustedx](https://github.com/NoTrustedx)
