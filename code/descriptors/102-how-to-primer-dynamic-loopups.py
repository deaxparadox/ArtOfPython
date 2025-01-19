# Interesting descriptors typically run computations 
# instead of returning constants.


import os

class DirectorySize:
    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))
    
class Directory:
    
    # Descriptor instance
    size = DirectorySize()
    
    def __init__(self, dirname):
        
        # Regular instance 
        self.dirname = dirname
        
if __name__ == "__main__":
    
    NEWFILE = "/home/paradox/Documents/testfile1.txt"
    DOWNLOADS = "/home/paradox/Downloads"
    DOCUMENTS = "/home/paradox/Documents"
    
    print("Descriptor on demand computation.")
    
    s = Directory(DOWNLOADS)
    g = Directory(DOCUMENTS)
    
    # Total files in Downloads
    print("Files in Downloads: %s." % s.size)
    
    # Total files in Documents
    print("Files in Documents: %s." % g.size)
    
    print("Creating a file in Documents.")
    with open(NEWFILE, 'w') as f:
        pass
    
    # File count automatically updated after added new file.
    print("Files in Documents: ", str(g.size))
    
    # File count in automatically updated after removing new file.
    print("Removing a file from Documents.")
    os.remove(NEWFILE)
    print("Files in Documents: ", str(g.size))
    
    # Parameter of `__get__` method
    # 
    # 1. obj: is either `s`` or `g`, an instance of Directory. It is 
    # the `obj` parameter that lets the `__get__` method learn about 
    # the target directory.
    # 2. objtype:  is the class Directory.