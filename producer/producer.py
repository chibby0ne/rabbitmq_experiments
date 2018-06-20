#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kombu import Connection, Producer, Exchange, Queue


def main():
    """Main program function"""
    with Connection('amqp://rabbitmq_host:5672') as conn:
        with conn.channel() as channel:
            producer = Producer(channel)
            exchange = Exchange(
                    name='producer_consumer_exchange',
                    type='fanout',
                    channel=channel)

            queue = Queue(
                    name='only_queue',
                    exchange=exchange,
                    routing_key='producer_key')

            producer.publish(
                    body={'hello': 'world'},
                    retry=True,
                    exchange=queue.exchange)


if __name__ == "__main__":
    main()
