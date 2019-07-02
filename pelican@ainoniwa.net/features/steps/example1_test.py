# -*- coding: UTF-8 -*-
from behave import *
import socket

@given(u'127.0.0.1でnginxが起動している場合')
def step_impl(context):
    pass
    #raise NotImplementedError(u'STEP: Given 127.0.0.1でnginxが起動している場合')

@when(u'TCPポート80にアクセスしたら')
def step_impl(context):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(("127.0.0.1", 80))
	context.connection = True
    #raise NotImplementedError(u'STEP: When TCPポート80にアクセスしたら')


@then(u'TCPセッションが確立できること')
def step_impl(context):
	assert context.connection
	#raise NotImplementedError(u'STEP: Then TCPセッションが確立できること')