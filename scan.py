import nmap
scanner = nmap.PortScanner()

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
    line = line.split()[0] #splitting the metadata
    url = line.split('/')[2] #removing the http tags
    temp = url.split(':') #extracting the ip
    ip = temp[0]  #IP Address
    try:
      scanner.scan(hosts=ip,arguments='-sn') #chech if host is up
      count+=1
      print(ip+' is ' +scanner[ip].state())
      active+=1
      output_handle.write(url+'\n') #write active hosts to output
    except:
      continue
print('Scanned:',count)
print('Active:',active)
