#!/usr/bin/env python3.5.2
# -*- coding: utf-8 -*-
#参考：http://blog.csdn.net/zhangfh1990/article/details/72732458
#“发布/订阅”模式，实质上，被发布的消息将会广播给所有接收
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',exchange_type="fanout")

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()