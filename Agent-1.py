import socket
Agent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Agent.connect(('127.0.0.1', 9999))   
incoming = ''
while True:
        incoming = Agent.recv(1024).decode()
        if incoming == '':
            break
        print(incoming, end="")
        Input = input()
        Agent.send(Input.encode())
        if Input == "D" :
            print(incoming, end="")
            


