#!/usr/bin/python

#import requests
import sys, os, socket

#------------ /-/ ------------#


if (len(sys.argv) != 2) or (sys.argv[1] == '-h'):
	print('Este script necesita un argumento para funcionar\n')
	print('python requester.py <file>\n')
	print('\targ1: fichero con IPs para checkear')
	exit(1)


ips = open(str(sys.argv[1]), 'r')

os.system('rm -f output')
os.system('echo "" > output')
output = open('output', 'w')

request = []

for ip in ips.readlines():
  c = 0

  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    s.connect((ip, 443))
    c = 1
    output.write('IP: ' + ip.strip('\n') + ' - Hit - Service on port 443\n')

  except ConnectionRefusedError:
    output.write('IP: ' + ip.strip('\n') + ':443 - Miss - Connection Refused\n')

  except socket.gaierror:
    output.write('IP: ' + ip.strip('\n') + ':443 - Miss - gaierror\n')

  except socket.timeout:
    output.write('IP: ' + ip.strip('\n') + ':443 - Miss - timeout\n')
  
  finally:
    s.close()


  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    s.connect((ip, 80))
    output.write('IP: ' + ip.strip('\n') + ' - Hit - Service on port 80\n')

    if c == 1:
      c = 3
    else:
      c = 2
    
  except ConnectionRefusedError:
    output.write('IP: ' + ip.strip('\n') + ':80 - Miss - Connection Refused\n')
    
  except socket.gaierror:
    output.write('IP: ' + ip.strip('\n') + ':80 - Miss - gaierror\n')
    
  except socket.timeout:
    output.write('IP: ' + ip.strip('\n') + ':80 - Miss - timeout\n')
    
  finally:
    s.close()

  t = (ip,c)
  request.append(t)

print(request)

#111 -> ConnectionRefusedError
#-2  -> gaierror
#timeout -> timeout

ips.close()
output.close()




"""
  except Exception as e:
    print(e)
    r = requests.get('http://' + ip, timeout=3)
    output.write(ip.strip('\n') + 'http ' + str(r) + '\n')


for ip in ips.readlines():
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 443))

  except:
    print('a')

"""

