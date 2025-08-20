
import zipfile  
zip = zipfile.ZipFile('file.zip')  
zip.namelist()  


zip.extractall()  



zip = zipfile.ZipFile('new.zip', 'w')  
zip.write('file.txt', compress_type=zipfile.ZIP_DEFLATED)  
