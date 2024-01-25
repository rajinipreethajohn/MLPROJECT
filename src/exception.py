import sys

def error_message_detail(error, sys):
    _,_,exc_tb= sys.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error has occured while processing the python script named [{0}] in line number [{1}] error message [{2}] .".format()
    file_name,  exc_tb.tb_lineno, str(error)
    
    return error_message
    
class CustomException(Exception):
    def __init__(self,error_message,sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, sys)
        
    def __str__(self):
        return self.error_message