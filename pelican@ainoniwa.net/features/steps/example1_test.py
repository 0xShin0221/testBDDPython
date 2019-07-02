# -*- coding: UTF-8 -*-
from behave import *
import socket

@given(u'{host}でnginxが起動している場合')
def step_impl(context,host):
	context.host = host
    #raise NotImplementedError(u'STEP: Given 127.0.0.1でnginxが起動している場合')

@when(u'TCPポート{port:n}にアクセスしたら')
def step_impl(context,port):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((context.host, port))
	context.connection = True
    #raise NotImplementedError(u'STEP: When TCPポート80にアクセスしたら')


@then(u'TCPセッションが確立できること')
def step_impl(context):
	assert context.connection
	#raise NotImplementedError(u'STEP: Then TCPセッションが確立できること')