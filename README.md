# Script Mejorado para Verificación de Usuarios SMTP (VRFY)

## Mejoras realizadas y explicación:

1. **Shebang actualizado**: Usa `#!/usr/bin/env python3` para mayor portabilidad.

2. **Manejo profesional de argumentos**:
   - Chequeo manual con el módulo `argparse` 
   - Opción para puerto personalizado (por defecto 25)
   - Mensajes de ayuda automáticos

3. **Manejo de contexto del socket**:
   - Se usa `with` para que el socket se cierre automáticamente
   - Se agrega timeout para evitar bloqueos infinitos

4. **Mejor manejo de errores**:
   - Captura específica de diferentes tipos de errores de conexión
   - Mensajes de error claros que se envían a stderr

5. **Mejor formato de salida**:
   - Salidas con prefijos informativos ([*], [+], [-])
   - Decodificación adecuada de las respuestas (con manejo de errores)

6. **Codificación adecuada**:
   - Uso consistente de UTF-8 para encoding/decoding
   - Manejo de errores en la decodificación

7. **Estructura modular**:
   - Código encapsulado en una función main()
   - Chequeo de ejecución como script principal

## ¿Cómo usar el script ?

```bash
# Uso básico (puerto 25):
./vrfy.py usuario 192.168.1.100

# Especificando puerto diferente:
./vrfy.py usuario 192.168.1.100 -p 2525

# Mostrar ayuda:
./vrfy.py -h
```
