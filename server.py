import http.server
import socketserver
import socket

# Function to get the local IP address of the machine
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connect to an external server (doesn't send data)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"  # Fallback to localhost
    finally:
        s.close()
    return ip

PORT = 8000  # Change this if you need a different port
Handler = http.server.SimpleHTTPRequestHandler

# Get the machine's IP address
server_ip = get_ip()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server started! Access it at: http://{server_ip}:{PORT}")
    httpd.serve_forever()
