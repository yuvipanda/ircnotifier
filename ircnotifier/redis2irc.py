#!/usr/bin/env python

import asyncio
import asyncio_redis
import asyncio_redis.encoders
import json
import irc3
import traceback

__version__ = '3.0alpha'


class Redis2Irc(irc3.IrcBot):
    def __init__(self, conf,  **kwargs):
        """
        :type conf: dict
        """
        super(Redis2Irc, self).__init__(**kwargs)
        self._conf = conf

    @property
    def conf(self):
        return self._conf

    @asyncio.coroutine
    def start(self):
        while True:
            try:
                yield from self.process_message()
            except Exception:
                self.log.critical(traceback.format_exc())
                self.log.info("...restarting Redis listener in a few seconds.")
            yield from asyncio.sleep(5)


    @asyncio.coroutine
    def process_message(self):
        # Create connection
        connection = yield from asyncio_redis.Connection.create(
            host=self.conf.get('REDIS_HOST', 'localhost'),
            port=6379,
        )

        while True:
            try:
                future = yield from connection.blpop([self.conf.get('REDIS_QUEUE_NAME')])
                message = json.loads(future.value)
                channels = message['channels']
                message = message['message']
                # FIXME: Actually join channel if they aren't joined already
                # FIXME: Actually send message, yo!
            except:
                self.log.critical(traceback.format_exc())
                yield from asyncio.sleep(1)


if __name__ == '__main__':
    main()
