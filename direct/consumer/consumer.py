#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kombu import Connection, Queue, Exchange
from kombu.mixins import ConsumerMixin
import logging

rabbitmq_url = 'amqp://rabbitmq_host:5672'


class Consumer(ConsumerMixin):
    def __init__(self, connection, queues):
        """ Consumer """
        self.connection = connection
        self.queues = queues

        self._logger = logging.getLogger('consumer')
        self._logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s '
                                      + '- %(message)s')
        ch.setFormatter(formatter)
        self._logger.addHandler(ch)

    def get_consumers(self, Consumer, channel):
        return [Consumer(queues=self.queues,
                callbacks=[self.on_message])]

    def on_message(self, body, message):
        self._logger.info('Got a message: {}'.format(body))
        message.ack()


exchange = Exchange(
        name='producer_consumer_exchange',
        type='direct')

queues = [Queue(
    name='only_queue',
    exchange=exchange,
    routing_key='producer_key')]


def main():
    """Main program function"""
    with Connection(rabbitmq_url, heartbeat=4) as conn:
        Consumer(conn, queues).run()


if __name__ == "__main__":
    main()
