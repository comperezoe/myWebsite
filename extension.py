from pelican.readers import BaseReader

class CustomReader(BaseReader):
    enabled = True
    file_extensions = ['custom']
    
    def read(self, source_path):
        # Custom parsing logic here
        with open(source_path) as f:
            content = f.read()
        return content, None
 
# In settings
READERS = {'custom': CustomReader}