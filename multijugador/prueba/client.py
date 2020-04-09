import socket
client_socket = socket.socket()
port = 5000
client_socket.connect(('localhost',port))
#recieve connection message from server
recv_msg = client_socket.recv(1024)
print(recv_msg)
#send user details to server
send_msg = input("Enter your user name(prefix with #):")
client_socket.send(str.encode(send_msg))
#receive and send message from/to different user/s
while True:
    recv_msg = client_socket.recv(1024)
    print(recv_msg)
    send_msg = input("Send your message in format [@user:message] ")
    if send_msg == 'exit':
        break;
    else:
        client_socket.send(str.encode(send_msg))
client_socket.close()