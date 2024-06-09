import socket
import threading


# bank accounts
details = {'Mohammed': {'password': '555', 'balance': 2000},'Ali': {'password': '444', 'balance': 1000}, 'Ahmad': {'password': '333', 'balance': 5000},
}
answer = ["A" , "B" , "C" , "D"]


def handle_Clients(socketCleint, addr):
        # accsess client
        socketCleint.send(b"Enter your name : ")
        name = socketCleint.recv(1024).decode().strip()
        socketCleint.send(b"Enter your Password : ")
        password = socketCleint.recv(1024).decode().strip()
        if name in details and details[name]['password'] == password:
            socketCleint.send(b"accsess successful!\n")
        else:
            socketCleint.send(b"wrong details please try later !\n")
            socketCleint.close()
            return
        
        while True:
            socketCleint.send(b"what do you want: A. Check Balance B. Deposit C. Withdraw D. Exit\n")
            process = socketCleint.recv(1024).decode().strip()
            if process in answer :
            # Operation-1 
              if process == 'A':
                socketCleint.send(f"Your balance is: ${details[name]['balance']}\n".encode())
               
            # Operation-2
              elif process == 'B':
                socketCleint.send(b"how much you want to deposit ?  ")
                money = int(socketCleint.recv(1024).decode().strip())
                details[name]['balance'] += money
                socketCleint.send(b"successful!\n")
            
            # Operation-3
              elif process == 'C':
                socketCleint.send(b"how much you want to withdraw: ")
                money = int(socketCleint.recv(1024).decode().strip())
                if details[name]['balance'] >= money :
                        details[name]['balance'] -= money
                        socketCleint.send(b"successful!\n")
                else:
                    socketCleint.send(b"you don't have enough money !\n")
            
            # Operation-4
              elif process == 'D':
                TotalBalance = details[name]['balance']
                socketCleint.send(f"Total-balance for client ${addr} is : ${TotalBalance}\n".encode())
                socketCleint.close()
                break
            
            else:
                socketCleint.send(b"please ty agin\n")
i = 1
while True:
    server_S = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_S.bind(('localhost',9999))
    server_S.listen(5)
    socketCleint, addr = server_S.accept()
    print(f"Accepted connection from {addr}")
    thread = threading.Thread(target=handle_Clients, args=(socketCleint,addr))
    thread.start()



