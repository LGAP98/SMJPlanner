#!/usr/bin/env python
import os
from solver import generate_plan
import amqp

ampq_url = "amqp://localhost:5672"  # os.environ.get('AMQP_URL')
q_name = "planner"  # os.environ.get('QUEUE_NAME')

with amqp.Connection(ampq_url) as c:
    ch = c.channel()

    def on_message(message):
        print('Received message (delivery tag: {}): {}'.format(message.delivery_tag, message.body))
        ch.basic_ack(message.delivery_tag)


    ch.basic_consume(queue=q_name, callback=on_message)
    while True:
        c.drain_events()
