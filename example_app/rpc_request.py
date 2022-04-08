import pika
import ConnectLocal as locale


def consume_response(ch, method, props, body):
    print("consume the response!")
    print(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


with locale.do_connect() as channel:
    ok_result = channel.queue_declare("", exclusive=True, arguments={"x-expires": 30000})
    reply_to = ok_result.method.queue
    print("queue name: {0}".format(reply_to))

    properties = pika.BasicProperties(reply_to=reply_to)

    channel.basic_publish("amq.direct", routing_key="request", properties=properties,
                          body="our request waits on {0} ".format(reply_to))

    channel.basic_consume(reply_to, consume_response)
    channel.start_consuming()
