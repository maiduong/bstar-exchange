#!/usr/bin/env python

import amqplib.client_0_8 as amqp
import random

def callback(msg):
  print (msg.body)
  msg.channel.basic_ack(msg.delivery_tag)
  
def main():
  conn = amqp.Connection()
  channel = conn.channel()
  exch = channel.exchange_declare("test", "x-bstar", auto_delete=False)
  
  queue_name = "test_queue_" + str(random.randint(10,99))
  print "declare queue ", queue_name

  q, _, _ = channel.queue_declare(queue = queue_name)
  channel.queue_bind(q, "test", "test")
  channel.basic_consume(q, callback=callback)
  
  while channel.callbacks:
    channel.wait()
    
  channel.close()
  conn.close()

if __name__ == '__main__':
  main()
