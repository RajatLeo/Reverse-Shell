# **Reverse Shell**

Reverse Shell is a type of shell in which [Client](https://github.com/RajatLeo/Reverse-Shell/blob/master/Client.py) or Victim communicate with [Server](https://github.com/RajatLeo/Reverse-Shell/blob/master/Server.py) or Attacker. [Server](https://github.com/RajatLeo/Reverse-Shell/blob/master/Server.py) is always listening for connection and accept the connection whenever connection is requested from [client](https://github.com/RajatLeo/Reverse-Shell/blob/master/Client.py) side.

**Getting Started:**

 **Modules Used:**
    
- Socket : To Establish  Connection between [Server](https://github.com/RajatLeo/Reverse-Shell/blob/master/Server.py) and [client](https://github.com/RajatLeo/Reverse-Shell/blob/master/Client.py), also to send command to [client](https://github.com/RajatLeo/Reverse-Shell/blob/master/Client.py) from [server](https://github.com/RajatLeo/Reverse-Shell/blob/master/Server.py).
    
- OS : It is used in [Client file](https://github.com/RajatLeo/Reverse-Shell/blob/master/Client.py) to access Operating system and to change directory as instructed by [server](https://github.com/RajatLeo/Reverse-Shell/blob/master/Server.py).
    
- subprocess : It is used to access subprocess of operating system and to open command prompt for execution of command given by [server](https://github.com/RajatLeo/Reverse-Shell/blob/master/Server.py).
    
- sys : It is used to close terminal of [server](https://github.com/RajatLeo/Reverse-Shell/blob/master/Server.py) after disconnecting from [client](https://github.com/RajatLeo/Reverse-Shell/blob/master/Client.py).


**How to Run Reverse shell**

- First edit [Client.py](https://github.com/RajatLeo/Reverse-Shell/blob/master/Client.py) at line 7 (host = "Replace with Server IP address") and add IP address of server in host as string. 
  
        e.g. host= "192.168.22.105"

- Run [Server.py](https://github.com/RajatLeo/Reverse-Shell/blob/master/Server.py) file on server and then [Client.py](https://github.com/RajatLeo/Reverse-Shell/blob/master/Client.py) on Client system.

- Send Valid command to [client](https://github.com/RajatLeo/Reverse-Shell/blob/master/Client.py) using [server](https://github.com/RajatLeo/Reverse-Shell/blob/master/Server.py) terminal. Send 'quit' to Disconnect from [Client](https://github.com/RajatLeo/Reverse-Shell/blob/master/Client.py).


**Author:**

-[Rajat Srivastava/RajatLeo](https://github.com/RajatLeo)
