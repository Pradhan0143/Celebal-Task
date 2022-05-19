def catAndMouse(x, y, z):
    
    CatA= abs(x-z)
    CatB= abs(y-z)
    
        
    if(CatA==CatB):
        return "Mouse C"
    elif(CatA<CatB):
        return "Cat A"
    else:            
        return "Cat B"