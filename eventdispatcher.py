#!/usr/bin/python3.4
# -*-coding:Utf-8 -*


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
		self.listeners[name] = self.listeners[name] or {}
		self.listeners[name][priority] = self.listeners[name][priority] or []
		self.listeners[name][priority].append(listener)
		
		# Register priority
		self.listeners[name]['priorities'] = self.listeners[name]['priorities'] or []
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
	
	
	def dispatch(self, name, event):
		'''
		Dispatch an event
		
		Parameters:
		{str} 		name 	The name of the event
		{object} 	event 	The event to dispatch
		
		'''
		
		# Iterate over priorities
		self.listeners[name]['priorities'].sort()
		for priority in self.listeners[name]['priorities']:
			# Iterate over events
			for listener in self.listeners[name][priority]:
				listener(event)

