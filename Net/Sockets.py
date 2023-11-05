'''
Created on 18 февр. 2016 г.

@author: Stalker
'''

from socket import *
import select
import time

DEFAULT_PORT_FTP    = 21          # default for FTP servers
DEFAULT_PORT_GOPHER = 70          #    "     "  gopher "
DEFAULT_PORT_HTTP   = 80          #    "     "  HTTP   "
DEFAULT_PORT_HTTPS  = 443         #    "     "  HTTPS  "
DEFAULT_PORT_SOCKS  = 1080        # default for SOCKS firewall servers.

cset_UNKNOWN, cset_UTF8, cset_WIN1251 = range(3)

# Сокет
class HttpSocket():
    def __init__(self, port='', host='', socket=0):
        self._host = host
        self._port = port
        self._socket = socket

    def Connect(self):
        if self._socket: return True

        self._socket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
        try:
            self._socket.connect((self._host, self._port))
#            self._socket = create_connection((self._host, self._port))
        except:
            self._socket = 0
            return False
        return True

    def Disconnect(self):
    #   SeoStr.Say("\nDisconnect " + str(self._socket))
        if self._socket:
            self._socket.close()
            self._socket = 0

    def Reconnect(self):
        self.Disconnect()
        return self.Connect()

    def IsOk(self):
        return self._socket
    def IsSSL(self):
        return self._ssl
    def  Host(self):
        return self._host

    def HasIncome(self):                # => BOOL
        return select.select((self._socket,), (), ())

    def Write(self, src, size):         # cPvoid, int => int
        if not self.IsOk(): return 0
        src = src.encode()
        sz = len(src)
        while (sz > 0):
            sent = self._socket.send(src)
            if (sent == 0): break
            if (sent < 0):
                # формально, здесь нужно обрабатывать разного рода ошибки,
                # тут всякое бывает
                return sent
            src = src[sent:]
            sz -= sent
        return size - sz

    def Read(self, size):          # Pvoid, int => int
        if not self.IsOk(): return 0
        sz = size                       # Сколько осталось прочитать.
        dst = ""
        #Say("\n")
        while (sz > 0):
            buf = self._socket.recv(sz)
            rs = len(buf)
            #Say("\n" + str(rs))
            if (rs == 0): break 
            dst += buf
            sz -= rs
        return dst

    def ReadString(self, maxsize): # Pchar dst, int => int    -> return dst 
        if not self.IsOk(): return None
        return self._socket.recv(maxsize).decode()

    def ReadChar(self):                 # => char
        ch = self._socket.recv(1, 0)
        return ch

    def ReadLine(self):                 # => PChar
        if not self.IsOk(): return None
        for itry in range(100):          # Ждём ответа 10 секунд.
            if self.HasIncome(): break
            time.sleep(100)
        else: return None                # Нормальное завершение
        s = bytes()
        c = self.ReadChar()
        while c and (c != b'\n'):
            s += c
            c = self.ReadChar()
        return s.strip()

# Серверный сокет
class HttpServer(HttpSocket):
    def __init__(self, port, host=''):
        HttpSocket.__init__(self, port, host, socket(AF_INET, SOCK_STREAM))
        try:
            self._socket.bind((self._host, port))
        except OSError as e:
            print("Failed to bind to port " + str(port))
            self._socket.close()
            self._socket = 0
        else:
            self._socket.listen(1)

# Клонированный сокет
    def Clone(self):   #  HttpServer => HttpSocket
        if self.IsOk():
            try:
                socket, addr = self._socket.accept()
            except:
                print("Failed to accept socket")
            else:
                #ioctlsocket( m_socket, FIONBIO, &nonblock )
                return HttpSocket(self._port, self._host, socket)
        return None

class HttpClient(HttpSocket):
    def __init__(self, host, ssl=0, port=0):
        HttpSocket.__init__(self, port)
        self._ssl = ssl
        
        if host:
            if self._port <= 0:
                self._port = DEFAULT_PORT_HTTP
            host = host.lower()
            if host.startswith("http://"):
                host = host[7:]
                self._ssl = False
            elif host.startswith("https://"):
                host = host[8:]
                self._ssl = True
                self._port = DEFAULT_PORT_HTTPS
            elif ssl and self._port == DEFAULT_PORT_HTTP:
                self._port = DEFAULT_PORT_HTTPS
    
            slash = host.find('/')
            self._host = host if (slash == -1) else host[:slash]
            if not self.Connect():
                print("Failed to connect to host={0}:{1}".format(self._host, self._port))
        else:
            print("Failed to use TCP/IP")

def Send(host, cookie="", method="GET", data=""):
    sock = HttpClient(host)

    q = (method + " {0} HTTP/1.0" + """
Host: {1}
User-Agent: MpvRobot
Accept: */*
Accept-Language: ru
Accept-Charset: windows-1251,utf-8
Keep-Alive: 300
Connection: keep-alive
 """).format(data, sock.Host())
    if cookie: q += "Cookie: " + cookie + "\n"
    q += "Content-Type: application/x-www-form-urlencoded\n"
    if (method == "POST"):
        q += "Content-Length: {0}".format(len(data))
    q += "\n" + data + "\n"
    size = len(q)

    for itry in range(3, 0, -1):
        ret = sock.Write(q, size)
        if ((ret == size) and Read(sock)): return True
        time.sleep(100)
        sock.Reconnect()
    
def Read(sock):
    hdr = []
    line = sock.ReadLine()
    while line:
        hdr.append(line.decode())
        line = sock.ReadLine()
    if not hdr: return False

    print( "\nHeader:_____________" )
    for h in hdr: print("\n" + h)

Send("www.sbup.com")
