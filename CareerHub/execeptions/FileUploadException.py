class FileUploadException(Exception):
    def __init__(self, message="File upload error occurred. Check the file size, format, and existence."):
        self.message = message
        super().__init__(self.message)
