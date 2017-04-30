from concurrent import futures
from random import randint 
import time
import grpc
import re 
import debate_pb2
import sys

def run():
	channel = grpc.insecure_channel('localhost:29999')
	stub = debate_pb2.CandidateStub(channel)
	response = stub.Answer(debate_pb2.AnswerRequest(question="What do you feel about Trump?"))
	print("Candidate client received: " + response.answer)




if __name__ == '__main__':
	run()