
#######################################################
## Finding the nth Occurrence of a word in a string! ##
#######################################################


def find_nth_occurrence(substring:str, string:str, occurrence=1):
    '''
        This function takes in the substring, the string, the no. of occurrence
        Then returns back the index of the predetermined occurrence
    '''
    try:
        indx = -1
        for i in range(1, occurrence+1):
            indx = string.find(substring, indx + 1)
        return print(indx)
    
    except:
        print('error')



########################################################








#########################
## Simple String Match ##
#########################


import re
def substr_match(str_1:str, str_2: str):
    ''' 
       This function takes in two string
       The first one may include asterisk
       Then returns if the asterisk is equivalent to the its corresponding characters in the second string or not
       (i.e do they match or not? ) 
    '''
    try:
        return print(bool(re.fullmatch(str_1.replace('*', '.*'), str_2)))
    except:
        print('error') 


# def substr_match(str_1:str, str_2:str):
#     ''' 
#        This function takes in two string
#        The first one may include asterisk
#        Then returns if the asterisk is equivalent to the its corresponding characters in the second string or not
#        (i.e do they match or not? ) 
#     '''
#     if str_1 == str_2: return True
#     if "*" not in str_1: return False
  
#     edges = str_1.split("*")
#     ast_str = str_2[ len(edges[0]) : len(str_2)-len(edges[1])]
#     c = str_1.replace("*", ast_str)
#     return print(c == str_2)

##############################################################################################################################







######################
## Is a palindrome? ##
######################

def is_palindrome(txt:str):
    '''
      This function takes in a text 
      Then asserts if it can be read from both sides the same way or not?
    '''
    try:
        txt = txt.upper()
        return print(txt == txt[::-1])
    except:
        print('error')    


###############################################################################################################################







########################
## Repeated Substring ##
########################

def rep_str(txt: str):
    '''
        This function takes in a string
        Then searches for the repeated substring
        Then returns the number of repeatitions
    '''
    try:
        indx = (txt*2).find(txt, 1)
        return print(txt[:indx], len(txt) // indx)

    except:
        print('error')    

#################################################################################################################################






