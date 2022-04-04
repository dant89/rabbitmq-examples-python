import pika

credentials = pika.PlainCredentials("guest", "guest")
conn_param = pika.connection.ConnectionParameters(credentials=credentials)

# establish tcp connection
connection = pika.BlockingConnection(conn_param)
# get channel
channel = connection.channel()

# use queue
queue_name = 'pika_queue'
channel.queue_declare(queue_name, False, True)

exchange = "amq.direct"
routing_key = "test"
message = "Hello World from publisher!"
message_bytes = str.encode(message)

channel.basic_publish(exchange, routing_key, message_bytes)

channel.close()
