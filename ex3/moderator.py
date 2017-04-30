#!/usr/bin/env python

import grpc
import debate_pb2 
import sys 

def run():
	args = sys.argv 
	classtype = args[1] #either answer or elaborate 
	channel = grpc.insecure_channel('localhost:29999')
	stub = debate_pb2.CandidateStub(channel)

	if(classtype.lower() == "answer"):
		question = args[2]
		response = stub.Answer(debate_pb2.AnswerRequest(question=question))
		print(response.answer)
	else if(classtype.lower() == "elaborate"):
		topic = args[2]
		blah = args[3:len(args)]
		#make sure they are all integers
		for i in range(0,len(blah)):
			try:
				blah[i]=int(blah[i]) 
			except:
				print("ERROR: invalid argument!!!")
				sys.exit(1)
		response = stub.Elaborate(debate_pb2.ElaborateRequest(topic=topic,blah_run = blah))
		print(response.answer)

if __name__ == '__main__':
	run()
