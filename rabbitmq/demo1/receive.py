#! /usr/bin/env python

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))

channel = connection.channel()

channel.queue_declare(queue = 'hello')

print '[x] Waiting for message . To exit press Ctrl + C'

def callback(ch, method, properties, body):
	print '[x] Receive %r ' % body

channel.basic_consume(callback, 
					  queue = 'hello',
					  no_ack = True)

channel.start_consuming()
