# firewall-simulation
Firewall -simulation
from http.server import BaseHTTPRequestHandler, HTTPServer

class FirewallHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.is_malicious():
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Blocked by firewall rule.")
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Request allowed.")

    def is_malicious(self):
        # Example: block requests with suspicious query strings or headers
        if "malicious" in self.path.lower():
            return True
        if "X-Attack-Type" in self.headers:
            return True
        return False

def run(server_class=HTTPServer, handler_class=FirewallHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Firewall server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

