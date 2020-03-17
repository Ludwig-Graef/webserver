import www
from multiprocessing import Process
from time import sleep
import socket
import re
if 64-64:i11iIiiIii
if 65-65:O0/iIii1I11I1II1%OoooooooOO-i1IIi
o0OO00="127.0.0.1";
oo=8080;
if 27-27:oO0OooOoO*o0Oo
i1IiI1I11=re.compile("HTTP/1\.1\s*200\s*OK",re.I);
IIiIiII11i=re.compile("HTTP/1\.1\s*404\s*Not Found",re.I)
o0oOOo0O0Ooo=re.compile("Content-Type:\s*text/.*",re.I)
I1ii11iIi11i=re.compile("Content-Type:\s*image/jpe*g.*",re.I)
I1IiI=re.compile(".?.?<html><head></head><body><h1>404 Not Found</h1></body></html>.*",re.DOTALL+re.I)
o0OOO=b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00/\x00/\x00'
if 13-13:ooOo+Oo
if 67-67:O00ooOO.I1iII1iiII
def iI1Ii11111iIi():
 www.serve(o0OO00,oo);
 if 41-41:I1II1
 if 100-100:iII1iII1i1iiI%iiIIIII1i1iI%iiI11iii111%i1I1Ii1iI1ii
def II1iI(request):
 print("\n\n\nInfo:Testing Request: ["+request+"]");
 i1iIii1Ii1II=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 try:
  i1iIii1Ii1II.settimeout(5);
  i1iIii1Ii1II.connect((o0OO00,oo));
 except OSError as i1I1Iiii1111:
  print("Connection to server not possible, check your socket code!")
  raise Exception("Error:"+str(i1I1Iiii1111))
 try:
  i1iIii1Ii1II.sendall(bytes(request+'\r\n\r\nHost: '+o0OO00+'\r\n',encoding="utf-8"))
  sleep(0.1);
  i11=i1iIii1Ii1II.recv(1024);
  i1iIii1Ii1II.close();
 except socket.timeout:
  i1iIii1Ii1II.close();
  raise Exception("Connection timeout, something is wrong with your socket code")
 print("Info: Response received:["+str(i11)+"]");
 I11=i11.split(b'\r\n\r\n');
 if len(I11)!=2:
  raise Exception("Cannot split into headers and content. Check your Header/Content separation")
 try:
  Oo0o0000o0o0=I11[0].decode()
 except:
  raise Exception("Cannot decode header")
 return(Oo0o0000o0o0.split("\r\n"),I11[1]);
 if 86-86:iiiii11iII1%O0o
def oO0(response,contentRe):
 IIIi1i1I=False
 OOoOoo00oo=False
 iiI11=False
 OOooO=re.compile("Date:\s*(Sun|Mon|Tue|Wed|Thu|Fri|Sat),\s*([1-9]|[0-3][0-9])\s*(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s*(2[0-9]{3})[.]*")
 for OOoO00o in range(1,len(response)):
  II111iiii=response[OOoO00o]
  II=re.compile("Server.*",re.I);
  oOoOo00oOo=re.compile("Content-Type",re.I);
  if II.match(II111iiii):
   Ooo00O00O0O0O=re.compile("Server:\s*Python\s*Tutorial\s*WebServer\s*",re.I)
   if Ooo00O00O0O0O.match(II111iiii):
    IIIi1i1I=True;
  elif oOoOo00oOo.match(II111iiii):
   if contentRe.match(II111iiii):
    iiI11=True;
  elif OOooO.match(II111iiii):
   OOoOoo00oo=True;
  elif II111iiii=='':
   return OOoO00o;
  else:
   print("Warning: Unknown header Line: "+II111iiii);
 OooO0OO=0
 if IIIi1i1I==False:
  print("Error: Server response-header field missing or wrong")
  OooO0OO=OooO0OO+1
 if iiI11==False:
  print("Error: Content response-header field missing or wrong")
  OooO0OO=OooO0OO+1
 if OOoOoo00oo==False:
  print("Error: Date response-header field missing or wrong")
  OooO0OO=OooO0OO+1
 return OooO0OO;
 if 28-28:iIii1
 if 71-71:IiI1I1
 if 86-86:i11iIiiIii+i1I1Ii1iI1ii+IiI1I1*iiI11iii111+I1iII1iiII
OooO0OO=0
(oOoO,iiI11)=II1iI('GET /LKN.txt HTTP/1.1');
OooO0OO=OooO0OO+oO0(oOoO,o0oOOo0O0Ooo);
if i1IiI1I11.match(oOoO[0])==None:
 print("Error: Status should be \"HTTP/1.1 200 OK\" is:  \""+oOoO[0]+'"');
 OooO0OO=OooO0OO+1
try:
 iiI11.decode();
except:
 print("Error: Content not delivered correctly")
 OooO0OO=OooO0OO+1
 if 68-68:O00ooOO.iII1iII1i1iiI.i11iIiiIii
 if 40-40:iII1iII1i1iiI.O00ooOO.ooOo.i1IIi
(oOoO,iiI11)=II1iI('GET /LKN.txt HTTP/1.1');
OooO0OO=OooO0OO+oO0(oOoO,o0oOOo0O0Ooo);
if i1IiI1I11.match(oOoO[0])==None:
 print("Error: Status should be \"HTTP/1.1 200 OK\" is:  \""+oOoO[0]+'"');
 OooO0OO=OooO0OO+1
try:
 iiI11.decode();
except:
 print("Error: Content not delivered correctly")
 OooO0OO=OooO0OO+1
 if 33-33:i1I1Ii1iI1ii+oO0OooOoO%i11iIiiIii.IiI1I1-o0Oo
(oOoO,iiI11)=II1iI('GET /LKW.txt HTTP/1.1');
OooO0OO=OooO0OO+oO0(oOoO,o0oOOo0O0Ooo);
if IIiIiII11i.match(oOoO[0])==None:
 print("Error:Status should be \"HTTP/1.1 404 Not Found\" is: \""+oOoO[0]+'"');
 OooO0OO=OooO0OO+1
try:
 if I1IiI.match(iiI11.decode())==None:
  print("Error: Content not delivered correct, is:"+iiI11);
  OooO0OO=OooO0OO+1
except:
 print("Error: Content not delivered correctly")
 OooO0OO=OooO0OO+1
 if 66-66:i1I1Ii1iI1ii-OoooooooOO*OoooooooOO.iiIIIII1i1iI.I1II1
(oOoO,iiI11)=II1iI('GET /LKW.jpg HTTP/1.1');
OooO0OO=OooO0OO+oO0(oOoO,o0oOOo0O0Ooo);
if IIiIiII11i.match(oOoO[0])==None:
 print("Error:Status should be \"HTTP/1.1 404 Not Found\" is: \""+oOoO[0]+'"');
 OooO0OO=OooO0OO+1
try:
 if I1IiI.match(iiI11.decode())==None:
  print("Error: Content not delivered correct, is:"+iiI11);
  OooO0OO=OooO0OO+1
except:
 print("Error: Content not delivered correctly")
 OooO0OO=OooO0OO+1
(oOoO,iiI11)=II1iI('GET /LKN.jpg HTTP/1.1');
OooO0OO=OooO0OO+oO0(oOoO,I1ii11iIi11i);
if i1IiI1I11.match(oOoO[0])==None:
 print("Error: Status should be \"HTTP/1.1 200 OK\" is:  \""+oOoO[0]+'"');
 OooO0OO=OooO0OO+1
try:
 if iiI11.startswith(o0OOO)==False:
  print("Error: Content not delivered correctly")
  OooO0OO=OooO0OO+1
except:
 print("Error:Content not delivered correctly")
 OooO0OO=OooO0OO+1
 if 22-22:OoooooooOO%iiI11iii111-iiiii11iII1.iIii1I11I1II1*i11iIiiIii
if OooO0OO:
 print('\n\n\n Final Result: Your server caused '+str(OooO0OO)+' errors');
else:
 print('Final Result: Congratulations no Errors!')
 if 32-32:ooOo*O0%iII1iII1i1iiI%i1I1Ii1iI1ii.O0o
 if 61-61:IiI1I1
 if 79-79:ooOo+o0Oo-iiiii11iII1
 if 83-83:IiI1I1
# Created by pyminifier (https://github.com/liftoff/pyminifier)

