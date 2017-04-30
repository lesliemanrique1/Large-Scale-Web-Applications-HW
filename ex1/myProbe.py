#my prober 
import requests
import sys 
import time


#command line argument validation 
def main(argv):

	url = argv[1]
	file_path = argv[2]
	#check if url is valid 
	if(url.split(":")[0]!="http"):
		print("sorry, that is not a valid url")
		exit(1) 
	# open a file for writing, if already exists, overwrite
	f = open(file_path,"w")
	f.truncate()
	f.write("URL=" + url + "\n")
	while True:
		cur_time = int(time.time())
		status = 0 
		global r 
		try: 
			#waits 30 seconds for a response 
			r = requests.request('GET',url,allow_redirects = True,timeout =30)
		
		except requests.exceptions.RequestException as e:  #exceptions
	   		status = -1 #declares host down    		

		w = "" 
		if(status != -1):
			#if code has been redirected, report the original http request 
			if(len(r.history)>0):
				status= r.history[0].status_code;
			else:
				status = r.status_code	
		
		w = str(cur_time) + "," + str(status) + "\n"

		f.write(w) 

		#total process should be 30 seconds.....
		
		diff = int(time.time()) - cur_time 
		
		if(diff>30):
			continue
		else:
			time.sleep(30- diff) 
		
	f.close() 

  
if __name__ == '__main__':
  main(sys.argv)

	
