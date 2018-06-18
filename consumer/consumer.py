#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kombus import Connection, Queue, Exchange, Consumer


def main():
    """Main program function"""
    with Connection('amqp://rabbitmq_host:5672') as conn:
        with conn.channel() as channel:
            consumer = Consumer(channel)

            exchange = Exchange(
                    name='producer_consumer_exchange',
                    type='fanout',
                    channel=channel)

            queue = Queue(
                    name='only_queue',
                    exchange=exchange,
                    routing_key='producer_key')


if __name__ == "__main__":
    main()
