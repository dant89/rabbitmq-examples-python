import pika
import ConnectLocal as locale

with locale.do_connect() as channel:
    channel.queue_declare("request_queue", durable=True)

    channel.queue_bind("request_queue", "amq.direct", routing_key="request")


    def callback(ch, method, props, body):
        print("now doing the response!")

        ch.basic_publish(routing_key=props.reply_to, exchange="", body="response to the request: '")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume("request_queue", callback)
    channel.start_consuming()
