import sys
import logging


logging.basicConfig(filename='logs/error.log', level=logging.INFO, format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s')


logger = logging.getLogger('src.logger')



def error_message_detail(error, sys_info):
    _,_,exc_tb= sys_info
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error has occured while processing the python script named [{0}] in line number [{1}] error message [{2}] .".format(
    file_name,  exc_tb.tb_lineno, str(error))
    return error_message
    
class CustomException(Exception):
    def __init__(self,error,sys_info):
        super().__init__(str(error))
        self.error_message = error_message_detail(error, sys_info)
        
    def __str__(self):
        return self.error_message
