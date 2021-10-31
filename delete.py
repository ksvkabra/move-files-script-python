
# Python program to explain os.remove() method  
      
# importing os module  
import os 
    
# File name 
file = 'file1.txt'
    
# File location 
location = "D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil/"
    
# Path 
path = os.path.join(location, file) 
    
# Remove the file 
# 'file.txt' 
os.remove(path) 
