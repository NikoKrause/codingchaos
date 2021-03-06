import socket

HOST = "irc.freenode.net"
PORT = 6667

NICK = "jvonbehren"
IDENT = "jvonbehren"
REALNAME = "jvonbehren"
CHANNEL = "#codingchaos"
MESSAGE = "hello!"

readbuffer = ""

s = socket.socket()
s.connect((HOST, PORT))

s.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
s.send(bytes("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME), "UTF-8"))
s.send(bytes("JOIN %s\r\n" % CHANNEL, "UTF-8"))

while 1:
    readbuffer = readbuffer+s.recv(1024).decode("UTF-8")
    temp = str.split(readbuffer, "\n")
    readbuffer = temp.pop()

    for line in temp:
        line = str.rstrip(line)
        line = str.split(line)

        if line[0] == "PING":
            s.send(bytes("PONG %s\r\n" % line[1], "UTF-8"))

        if line[1] == "PRIVMSG":
            if line[3] == ":!say":
                s.send(bytes("PRIVMSG %s :%s\r\n" % (CHANNEL, MESSAGE), "UTF-8"))

        # print(line)
