# Read Me

## generate debate_pb2.py
$ python -m grpc.tools.protoc -I . --python_out=. --grpc_python_out=. debate.proto

## generate consultation_pb2.py
$ python -m grpc.tools.protoc -I . --python_out=. --grpc_python_out=. consultation.proto


## Run the program 
python candidate_server.py

## In another terminal run 
./moderator.py enswer "[question]"
or 
./moderator.py elaborate "[topic]" [blah_run]

where
	your question or topic must be placed in quotation marks if more than one word
	blah_run must be a list of 0 or more numbers

Note to graders 
	I don't know how to get Answer to make an rpc call to an external server. In other 
	words, It doesn't fork for the case where the question is "what|why|how|who|when"
	i was able to get all other functionalities to work.   
