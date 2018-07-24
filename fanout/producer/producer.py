#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kombu import Connection, Producer, Exchange, Queue
import time
import logging

rabbitmq_url = 'amqp://rabbitmq_host:5672'
sending_period = 3
logger = logging.getLogger('producer')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s' + ' - %(levelname)s ' +
                              '- %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def main():
    """Main program function"""
    with Connection(rabbitmq_url) as conn:
        producer = Producer(conn)
        exchange = Exchange(
                name='producer_consumer_exchange',
                type='fanout')
        while True:
            logger.info('Sent a message: {}'.format('hello world'))
            producer.publish(
                    body={'hello': 'world'},
                    exchange=exchange)
            time.sleep(sending_period)


if __name__ == "__main__":
    main()
