# This module contains inheritance with parent and child classes
# that used to get password, verify with preset password and return the access permission

class person(object):               # parent class
    def __init__(self,password):    
        self.password = password

    def getpassword(self):          # get password from user
        return self.password        
    
    def defaultpassword(self):
        return 'adminpassword'      # preset password to authenticate the user

    def isemployee(self):           # default: access permission is denied
        return False

class employee(person):             # child class
    def isemployee(self):           # alternative: access permission is granted
        return True

    
