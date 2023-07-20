# Exception Handling
# TypeError, IndexError, ReferenceError, RecursionError, ZeroDivisionError
# try -- except -- else -- finally blocks
# try block -- to execute a set of statements anticipating some errors to occur
# except block -- Handle/filter the error and take corrective actions
# else  block - executes  after  no exception are reported or without exceptions
# finally block -- always executes  - with exceptions or without exceptions

try:
    #x = 10/1
    raise ValueError('Some Value has gone wrong!!')  # raise is the one that throws an error in other words generates an error
    print('Statement after division')
except ZeroDivisionError:
    print('Zero error occured')
except ValueError:
    print("Some values are missing.")
else:
    print("No error reported be the try block")
finally:
    print('Successfully completed the try... except section')