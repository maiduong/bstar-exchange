#!/usr/bin/env python

import amqplib.client_0_8 as amqp
import time

def main():
  conn = amqp.Connection()
  channel = conn.channel()
  exch = channel.exchange_declare("test", "x-bstar", auto_delete=False)
  
  while 1:
    send_str = "msg time - " + time.ctime()
    msg = amqp.Message(send_str)
    server_ack = channel.basic_publish(msg, "test", "test")
    print "send: ", send_str, " - ack: ", server_ack
    time.sleep (1)
    
  channel.close()
  conn.close()

if __name__ == '__main__':
  main()
