import re
class Validation:
    def __init__(self) -> None:
        pass  
    
    def validString(self,obj,minLength=3,maxLength=6): 
        '''
        this function to check word is all alpha 
        check length between min and max
        take 3 parameters  object,min length ,max length 
        
        return true if all conditions True
        '''
        
        if not re.sub(r'[^ \w+]', '', obj):
           print("%s Must not contain numbers -_-"%obj) 
           return False
        elif len(str(obj))<minLength or len(str(obj))>maxLength:
           print ("%s Must be between %d and %d"%(obj,minLength,maxLength))
           return False
        else:
            return True
    def validtring(self,obj,minLength=3,maxLength=6): 
        if not re.sub(r'[^ \w+]', '', obj):
           print("%s Must not contain numbers -_-"%obj) 
           return False
        elif len(str(obj))<minLength or len(str(obj))>maxLength:
           print ("%s Must be between %d and %d"%(obj,minLength,maxLength))
           return False
        else:
            return True    
        
             



validation=Validation()
# validation=Validation()
print(validation.validString("ff g",6,9))