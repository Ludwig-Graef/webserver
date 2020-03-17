'''
Erstellt am

@author: 
'''

import re
import os
import socket
from datetime import datetime

        
def handle_request(message):
    """
    Parse the received request.
    Check if request is valid.
    Check if file exist (os.path.exists(path)).
    Create and return answer with or without file content.
    """
    print("Received Message: " + message)
    
    # TODO: parse message into an array to make the received message readable 
    messageArray = "Your code here"
    
    # check if the 1st line of the message is valid 
    matchTxt = HTTP_REQUEST_TXT.match(messageArray[0])
    matchJpg = HTTP_REQUEST_JPG.match(messageArray[0])
    
    # TODO: build path of requested file from file name and current directory
    path = os.curdir + "file"
    print("Requested File: " + path)
    fileExists = os.path.exists(path)
    
    if matchTxt and fileExists:
        
        # TODO: Construct response for txt-files
        
        returnMessage = "Your code here"
        
    elif matchJpg and fileExists:
                
        # TODO: Construct response for jpg-files
        
        returnMessage = "Your code here"
    else:
        # if request is not correct, return the 404 response
        returnMessage = response404_NotFound()
        
    return returnMessage
            
def response404_NotFound():
    """
    Create and return a 404 Not Found message
    """
    statusLine = "HTTP/1.1 404 Not Found\r\n"
    headerLines = SERVER_LINE + "\r\n"
    # TODO: add missing mandatory headerLines
    
    message = statusLine + headerLines + "\r\n" + HTML404 + "\r\n"
    return bytes(message, encoding="utf-8")
    
def status200_OK():
    """
    Create and return a 200 OK Status-Line.
    """
    # TODO: implement function
    return None

def read_and_return_file(path):
    """
    Read file and return the data
    """
    f = open(path, 'rb')
    outputdata = f.read()
    f.close()
    return outputdata

##############################################################################
##############################################################################
# Start your server application here
# Use the given functions to implement your WebServer
##############################################################################
##############################################################################

def serve(address, port):
    """Serve local directory via the HTTP protocol.

    Keyword arguments:
        address (string): The IP(v4) to listen on
        port (int): The TCP port to listen on.

    Returns:
        int: Return 0 for success and not 0 for failure.
    """
    
    # TODO: create socket, bind socket to address and listen for connections
    
    while True:
        
        # TODO: accept and receive connections 
        #       and call handle_request() with decoded message
        
        returnMessage = handle_request(receivedMessage)
        
        # TODO: send returnMessage to the client and close the connection
        
    return 0

    
    
###############################################################################
###############################################################################
# initial code 
###############################################################################
###############################################################################

# regex for HTTP Request Header
HTTP_REQUEST_TXT = re.compile("GET /.*\.txt HTTP/1\.1.*", re.I)
# regex for HTTP Request Header 
HTTP_REQUEST_JPG = re.compile("GET /.*\.jpg HTTP/1\.1.*", re.I) 
# HTML content of 404 response
HTML404 = "<html><head></head><body><h1>404 Not Found</h1></body></html>" 
# Server response-header field
SERVER_LINE="Server: Python Tutorial WebServer" 








