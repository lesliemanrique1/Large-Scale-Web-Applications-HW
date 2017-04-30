from concurrent import futures
from grpc.beta import implementations
import time
from random import randint 
import grpc
import re 
import debate_pb2
import consultation_pb2 
_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Candidate(debate_pb2.CandidateServicer):
	def Answer(self,request,context):
		quest = request.question.split()
		start = quest[0].lower()
		#does the question start with why,what,how,who or when? 
		match = re.search(r'what|why|how|who|when',start)
		if not match:
			rando = randint(0,1) #flip a coin 
			if rando == 0:
				answer = "your 3 cent titanium tax goes too far"
			else:
				answer = "your 3 cent titanium tax doesn't go too far enough"
			return debate_pb2.AnswerReply(answer=answer)
		else:
			quest_sub = [] 
			for word in quest:
				word = word.lower()
				if word == "you":
					word ="I"
				elif word == "your":
					word = "my"
				quest_sub.append(word)
			string = " ".join(quest_sub)
			print string 
			#make rpc call to external server on port 50051

			channel = grpc.insecure_channel('localhost:50051') #grpc channel
			stub = consultation_pb2.CampaignManagerStub(channel) 
		
			try:
				retort = stub.Retort(consultation_pb2.RetortRequest(original_question=string))
				#reply back to the client
				reply = "You asked me " + string + " but i want to say " + retort; 
			except grpc.framework.interfaces.face.face.ExpirationError:
				reply = "nothing to say here"
			return debate_pb2.AnswerReply(answer=reply) 


	def Elaborate(self,request,context):
			
			answer = ""
			topic = request.topic 
			blah = request.blah_run  
			#blah_run is empty 
			if len(blah) == 0:
				answer = topic 
			elif len(blah) == 1:
				answer = 'blah ' * blah[0] + topic 
			else:
				for i in range(len(blah)-1):
					answer += " blah " * blah[i] + topic 
				answer += " blah " * blah[-1]

			return debate_pb2.ElaborateReply(answer=answer)


def run():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	debate_pb2.add_CandidateServicer_to_server(Candidate(), server)
	server.add_insecure_port('localhost:29999')
	server.start()
	try:
		while True:
		  time.sleep(_ONE_DAY_IN_SECONDS)
	except KeyboardInterrupt:
		server.stop(0)
if __name__ == '__main__':
	run()
