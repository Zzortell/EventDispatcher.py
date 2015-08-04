#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

import unittest

from eventdispatcher import EventDispatcher


class EventDispatcherTest(unittest.TestCase):
	'''Tests the event dispatcher'''
	
	
	def setUp(self):
		self.dispatcher = EventDispatcher()
		self.listener = EventListener()
	
	
	def test_dispatch(self):
		self.dispatcher.listen('test.dispatch', self.listener.onDispatch)
		self.dispatcher.dispatch('test.dispatch', TestEvent('dispatch'))
		self.assertEqual('dispatch', self.listener.testStr)
	
	
	def test_priority(self):
		self.dispatcher.listen('test.priority', self.listener.listenPriority('d'), 1)
		self.dispatcher.listen('test.priority', self.listener.listenPriority('a'), -2)
		self.dispatcher.listen('test.priority', self.listener.listenPriority('c'))
		self.dispatcher.listen('test.priority', self.listener.listenPriority('b'), -1)
		
		self.dispatcher.dispatch('test.priority', TestEvent())
		self.assertEqual('abcd', self.listener.testStr)
	
	
	def test_detach(self):
		self.dispatcher.listen('test.detach', self.listener.onDispatch)
		listener_id = self.dispatcher.listen('test.detach', self.listener.onDispatch)
		self.dispatcher.detach(listener_id)
		
		self.dispatcher.dispatch('test.detach', TestEvent('detach'))
		self.assertEqual('detach', self.listener.testStr)


class TestEvent:
	'''A test event'''
	
	
	def __init__(self, msg='test'):
		self.msg = msg


class EventListener:
	'''An event listener'''
	
	
	def __init__(self):
		self.testStr = ''
	
	
	def onDispatch(self, e):
		self.testStr += e.msg
	
	
	def listenPriority(self, _str):
		def onPriority(e):
			self.testStr += _str
		return onPriority
