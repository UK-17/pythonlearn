import nmap
scanner = nmap.PortScanner() #our scanner

#input file
input_file = 'input.txt'
input_handle = open(input_file,'r')

#output file
output_file = 'active.txt'
output_handle = open(output_file,'a+')

count = 0
active = 0

for line in input_handle: #pickup the list of urls
  
  if line.startswith('http'):  #taking only the urls
    count+=1
    
    line = line.split()[0] #splitting the metadata
    url = line.split('/')[2] #removing the http tags
    temp = url.split(':') #extracting the ip
    ip = temp[0]  #IP Address
    try:
       port = temp[1] #port
    except:
       port = 80  #port 80 by default
    
    try:
     res = scanner.scan(ip,port) #scan ip from list on port
     if scanner[ip].state() == 'up' : #check if host is up
       active+=1
       output_handle.write(url+'\n') #write the url
       print(active+' hosts found\n')
     
    except:
     continue
    
print('\nProcessed',count,'entries.\n')
input_handle.close()
output_handle.close()
