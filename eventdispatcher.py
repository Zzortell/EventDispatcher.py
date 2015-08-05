#!/usr/bin/python3.4
# -*-coding:Utf-8 -*


# The MIT License (MIT)
#
# Copyright (c) 2015 Rémi Blaise <remi.blaise@gmx.fr> "http://php-zzortell.rhcloud.com/"
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#


class EventDispatcher:
	'''
	A simple event dispatcher
	
	Author: Rémi Blaise (alias Zzortell) "http://php-zzortell.rhcloud.com/"
	
	'''
	
	
	def __init__(self):
		self.listeners = {}
	
	
	def listen(self, name, listener, priority=0):
		'''
		Add an event listener
		
		Parameters:
		{str} 		name 			The name of the event
		{function} 	listener 		The event listener
		{int}		priority = 0 	The priority of the listener
		
		Return: {tuple} id The ID of the listener
		
		'''
		
		# Register listener
		if name not in self.listeners:
			self.listeners[name] = {}
		if priority not in self.listeners[name]:
			self.listeners[name][priority] = []
		self.listeners[name][priority].append(listener)
		
		# Register priority
		if 'priorities' not in self.listeners[name]:
			self.listeners[name]['priorities'] = []
		if priority not in self.listeners[name]['priorities']:
			self.listeners[name]['priorities'].append(priority)
		
		return (name, priority, listener)
	
	
	def detach(self, id):
		'''
		Detach an event listener
		
		Parameter:
		{tuple} id The ID of the listener
		
		'''
		
		name, priority, listener = id
		self.listeners[name][priority].remove(listener)
	
	
	def dispatch(self, name, event=None):
		'''
		Dispatch an event
		
		Parameters:
		{str} 		name 			The name of the event
		{object} 	event = None 	The event to dispatch
		
		'''
		
		# Iterate over priorities
		self.listeners[name]['priorities'].sort()
		for priority in self.listeners[name]['priorities']:
			# Iterate over events
			for listener in self.listeners[name][priority]:
				listener(event)
