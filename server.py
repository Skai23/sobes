import http.server
import socketserver
import datetime
import socket
from prometheus_client import start_http_server, Counter

# Define the port number on which you want to run the server
PORT = 8000
REQUEST_COUNTER = Counter('http_requests_total', 'Total number of HTTP requests')

# Create a simple HTTP request handler
class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            # Set the response status code for health check
            self.send_response(200)
            
            # Set the response headers
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            # Send the response content for health check
            self.wfile.write(b'OK')
        elif self.path == '/':
            # Set the response status code
            self.send_response(200)

            # Increment the request counter
            REQUEST_COUNTER.inc()

            # Set the response headers
            self.send_header("Content-type", "text/plain")
            self.end_headers()
    
            # Get the current timestamp
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
            # Get the hostname
            hostname = socket.gethostname()
    
            # Build the response content
            response = f"Timestamp: {timestamp}\nHostname: {hostname}".encode("utf-8")
    
            # Send the response content
            self.wfile.write(response)
        else:
            # Set the response status code
            self.send_response(404)

            # Set the response headers
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            # Send the response content for unknown routes
            self.wfile.write(b'Not Found')

# Start the Prometheus metrics endpoint
start_http_server(PORT+1)

# Set up the server
with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print("Server running at port", PORT)
    # Start serving requests
    httpd.serve_forever()
    

