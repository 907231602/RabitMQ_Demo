#!/usr/bin/env python3.5.2
# -*- coding: utf-8 -*-
#参考：http://blog.csdn.net/zhangfh1990/article/details/72732458
#“发布/订阅”模式，实质上，被发布的消息将会广播给所有接收
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()