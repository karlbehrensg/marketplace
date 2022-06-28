import sys
import os
import pika

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from config import Settings

settings = Settings()

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=settings.message_broker_host))

channel = connection.channel()

channel.queue_declare(queue=settings.commerce_queue)

def on_request(ch, method, props, body):
    n = body

    print(f"[.] Message: {str(n)}")
    response = "response"

    ch.basic_publish(
        exchange='',
        routing_key=props.reply_to,
        properties=pika.BasicProperties(correlation_id = props.correlation_id),
        body=str(response)
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=settings.commerce_queue, on_message_callback=on_request)

print(f"[x] Awaiting messages from {settings.commerce_queue}")
channel.start_consuming()
