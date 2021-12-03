import stomp

host = "localhost"
port = 61613
dest = "/topic/H2K.TOPIC.CHECK"
data = "Hello World from Python"

conn = stomp.Connection(host_and_ports = [(host, port)])
conn.connect()
conn.send(destination=dest, body=data, persistent='true')
print("Connection Successful, Message Sent")
conn.disconnect()

