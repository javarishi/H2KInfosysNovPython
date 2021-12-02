import queue

simpleQueue = queue.SimpleQueue()
lifoQueue = queue.LifoQueue()

# Sending message to Queue
for i in range(5):
    simpleQueue.put("Message {}".format(i))
    lifoQueue.put("Message {}".format(i))

# Checking Size of Queue
print("SimpleQueue Size:: ", simpleQueue.qsize())
print("LifoQueue Size:: ", lifoQueue.qsize())

# Getting messages from Queue
if not simpleQueue.empty():
    print("SimpleQueue Get:: ", simpleQueue.get())
else:
    print("Simple Queue is Empty")
print("LifoQueue Get:: ", lifoQueue.get())
print("SimpleQueue get_nowait:: ", simpleQueue.get_nowait())

# Checking Size of Queue
print("SimpleQueue Size:: ", simpleQueue.qsize())
print("LifoQueue Size:: ", lifoQueue.qsize())