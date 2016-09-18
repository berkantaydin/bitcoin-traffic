#!/usr/bin/python

import json
from websocket import create_connection

ws = create_connection("wss://ws.blockchain.info/inv")
print "Sending 'Hello, BlockChain...'"
ws.send('{"op":"unconfirmed_sub"}')
print "Sent"
print "Receiving..."
while True:
	result = ws.recv()
	result = json.loads(result)
	relayed_by = result["x"]["relayed_by"]
	hash = result["x"]["hash"]
	total = 0
	for item in result["x"]["out"]:
		total += item['value']
	total = total / 100000000.
	print "%s\t%s\thttps://blockchain.info/tx/%s" % (total, relayed_by, hash)
ws.close()
