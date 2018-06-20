#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kombu import Connection, Queue, Exchange, Consumer


def main():
    """Main program function"""
    with Connection('amqp://rabbitmq_host:5672') as conn:
        with conn.channel() as channel:

            exchange = Exchange(
                    name='producer_consumer_exchange',
                    type='fanout',
                    channel=channel)

            queue = Queue(
                    name='only_queue',
                    exchange=exchange,
                    routing_key='producer_key')

            with Consumer(conn, [queue], accept=['json']):
                conn.drain_events(timeout=10)


if __name__ == "__main__":
    main()
