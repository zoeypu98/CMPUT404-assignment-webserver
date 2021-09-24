#  coding: utf-8 
import socketserver
import requests
import os
import urllib.parse


# Copyright 2013 Abram Hindle, Eddie Antonio Santos
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Furthermore it is derived from the Python documentation examples thus
# some of the code is Copyright © 2001-2013 Python Software
# Foundation; All Rights Reserved
#
# http://docs.python.org/2/library/socketserver.html
#
# run: python freetests.py

# try: curl -v -X GET http://127.0.0.1:8080/


class MyWebServer(socketserver.BaseRequestHandler):
    
    def handle(self):
        ## self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()

        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # full_data = b"" 
        # while True:
        #     data = s.recv(1024) 
        #     if not data:
        #         break
        #     full_data += data
        self.data = self.data.decode()
        

        # s.bind((HOST, PORT))
        # s.listen(2)
        #self.data = self.data.decode()
        #self.data.strip
        #print(data)
        print ("Got a request of: %s\n" % self.data)
        #send back the same data
        # while True:
        #     conn, addr = s.accept() 
        #     print("Connected by", addr)
        #     full_data = conn.recv(1024)
        #     time.sleep(0.5) 
        #     conn.sendall(full_data) 
        #     conn.close()

        
        scode2=404
        path = '/'
        if os.path.isdir(path) or os.path.isfile(path):
            if path.endswith((".html", ".css")):
                try:
                    requests.get('http://127.0.0.1:8080/')
                    print("open file")
                    f = open(path, 'r')
                    self.request.sendall("200 OK")
                except:
                    f = "File not found"
                    self.request.sendall("405 Method Not Allowed")
                self.wfile.write(bytes(f, 'utf-8'))

            else:
                return self.request.sendall(scode2.to_bytes(5,'little'))
        else:
            return self.request.sendall(scode2.to_bytes(5,'little'))

        self.request.sendall(bytearray("OK",'utf-8'))


        



        


if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    socketserver.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 8080
    server = socketserver.TCPServer((HOST, PORT), MyWebServer)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
