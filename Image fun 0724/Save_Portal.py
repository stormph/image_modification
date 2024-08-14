import os

#returns an iterated version of the given name
def name_checker(prename,dir):

    (name,ending) = prename.split(".")
    
    if os.path.isfile(f'{dir}/{prename}') == True:
        x=0
        while os.path.isfile(f'{dir}/{name}{str(x)}.{ending}') == True:
            x+=1
        new_name = f'{name}{str(x)}.{ending}'
        return new_name
    else:
        return name
    