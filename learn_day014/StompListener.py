import stomp
import time

host =  "localhost"
port = 61613
dest = "/topic/H2K.TOPIC.CHECK"

class StompListener:

    def __init__(self, conn):
        self.connection = conn
        self.count = 0

    def on_error(self, message):
        print('received an error {}'.format(message))


    def on_message(self, message):
        print(message.body)
        print(message.headers.get('message-id'))


conn = stomp.Connection(host_and_ports = [(host, port)])
listener = StompListener(conn)
conn.connect()
conn.set_listener('RishizListener', listener)
conn.subscribe(destination=dest, id=1, ack='auto')
print("Done!")
print("Waiting for messages...")
while True:
    time.sleep(10)



