from http.server import BaseHTTPRequestHandler, HTTPServer

class FirewallHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')

        if self.is_malicious(post_data):
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Blocked by firewall rule.")
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Request allowed.")

    def is_malicious(self, data):
        # Block if payload contains suspicious keywords
        suspicious_keywords = ["Runtime", "<%", "exec", "tomcatwar"]
        for keyword in suspicious_keywords:
            if keyword in data:
                return True
        return False

def run(server_class=HTTPServer, handler_class=FirewallHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Firewall server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
