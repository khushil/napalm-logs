# -*- coding: utf-8 -*-
'''
napalm-logs base
'''
from __future__ import absolute_import
from __future__ import unicode_literals

# python stdlib
from Queue import Queue


class NapalmLogsProc:
    def __init__(self,
                 name,
                 config,
                 transport,
                 log=None):
        self._name = name
        self._config = config
        self._transport = transport
        self._log = log
        self._q = Queue()
        self.__running = False

    def _parse(self, msg):
        '''
        Parse a syslog message and check what OpenConfig object should
        be generated.
        '''
        pass

    def _emit(self, **kwargs):
        '''
        Emit an OpenConfig object given a certain combination of
        fields mappeed in the config to the corresponding hierarchy.
        '''
        pass

    def _publish(self, obj):
        '''
        Publish the OC object.
        '''
        self._transport.publish(obj)

    def queue(self, msg):
        self._q.put(msg)

    def start(self):
        '''
        Start the worker process.
        '''
        self.__running = True
        while self.__running:
            self._publish(self._name)
            # msg = self._q.get(block=True)
            # # Will wait till a message is available
            # kwargs = self._parse(self, msg)
            # oc_obj = self._emit(self, **kwargs)
            # self._publish(oc_obj)

    def stop(self):
        '''
        Stop the worker process.
        '''
        self.__running = False
