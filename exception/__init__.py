import os
import sys


class ReviewException(Exception):
    def __init__(self, error_message: Exception,error_detail: sys):  # When you raise HousingException("something went wrong", sys), Python:
        super().__init__(error_message)  # Calls your __init__ method.
        self.error_message = ReviewException.get_detailed_error_message(error_message=error_message,
                                                                         error_detail=error_detail)  # super().__init__(error_message) passes the message to the base Exception class.
        # So str(your_exception) will return that error_message

    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_detail: sys) -> str:
        """
        error_message: Exception object
        error_detail: object of sys module
        """
        _, _, exec_tb = error_detail.exc_info()  # sys.exc_info()->(type,value,traceback) i want traceback there we find line no and file name
        exception_block_line_number = exec_tb.tb_frame.f_lineno
        try_block_line_number = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename

        error_message = f"""
            Error occured in script:
            [ {file_name} ] at 
            try block line number: [{try_block_line_number}] and exception block line number: [{exception_block_line_number}] 
            error message: [{error_message}]

            """

        # error_message = f"""
        # Error occured in script: [{file_name}]
        # at line number: [{line_number}]
        # error message: [{error_message}]

        # """

        return error_message

    def __str__(self):
        return self.error_message

    def __repr__(self) -> str:
        return ReviewException.__name__.str()


