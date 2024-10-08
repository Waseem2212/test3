class FileManager():
    def __init___(self, filename,mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileManager('test.txt','w') as f:
    f.write('Waseem','Hasnain')