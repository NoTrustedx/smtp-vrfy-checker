#!/usr/bin/env python3

import socket
import sys
import argparse

def main():
    # Configuración del parser de argumentos
    parser = argparse.ArgumentParser(description='Herramienta para verificación de usuarios SMTP mediante comando VRFY')
    parser.add_argument('username', help='Nombre de usuario a verificar')
    parser.add_argument('target_ip', help='Dirección IP del servidor SMTP')
    parser.add_argument('-p', '--port', type=int, default=25, help='Puerto SMTP (por defecto: 25)')
    args = parser.parse_args()

    try:
        # Creación del socket con manejo de contexto (auto-cierre)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Configuración de timeout (10 segundos)
            s.settimeout(10)
            
            print(f"[*] Conectando a {args.target_ip}:{args.port}...")
            s.connect((args.target_ip, args.port))
            
            # Recibir banner
            banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
            print(f"[*] Banner del servidor:\n{banner}")
            
            # Enviar comando VRFY
            vrfy_command = f"VRFY {args.username}\r\n"
            print(f"[*] Enviando: {vrfy_command.strip()}")
            s.send(vrfy_command.encode())
            
            # Recibir respuesta
            response = s.recv(1024).decode('utf-8', errors='ignore').strip()
            print(f"[+] Respuesta del servidor:\n{response}")
            
    except socket.timeout:
        print("[-] Error: Tiempo de espera agotado", file=sys.stderr)
        sys.exit(1)
    except ConnectionRefusedError:
        print("[-] Error: Conexión rechazada por el servidor", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[-] Error inesperado: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
