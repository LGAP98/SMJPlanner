#!/usr/bin/env python
import os
import amqp

from solver import generate_plan_from_message, generate_rides

# generate_plan_from_message("e87a548a-516b-40e3-826d-b10fae00d503")

ampq_url = "amqp://localhost:5672"  # os.environ.get('AMQP_URL')
q_name = "planner"  # os.environ.get('QUEUE_NAME')

with amqp.Connection(ampq_url) as c:
    ch = c.channel()

    def on_message(message):
        print('Received message (delivery tag: {}): {}'.format(message.delivery_tag, message.body))
<<<<<<< HEAD
=======
        generate_plan_from_message("9fdcbb17-5ade-4a68-a51d-1a9e7dc9e10b", )

>>>>>>> 7a3011c (WIP)
        ch.basic_ack(message.delivery_tag)


    ch.basic_consume(queue=q_name, callback=on_message)
    while True:
        c.drain_events()
