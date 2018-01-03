#!/usr/bin/env python3.5.2
# -*- coding: utf-8 -*-
#参考：http://blog.csdn.net/zhangfh1990/article/details/72677093
import pika
import sys

#新的生产者，轮询派发（Round-robin dispatching）
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print(" [x] Sent %r" % message)
connection.close()