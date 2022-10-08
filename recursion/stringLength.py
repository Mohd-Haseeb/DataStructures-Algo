from sqlalchemy import null


def helper(string:str):
    if string == '':
        return 0
    
    return 1 + helper(string[1:])


ans = helper('haseeb')
print(ans)