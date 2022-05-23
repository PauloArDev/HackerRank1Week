def lonelyinteger(a):
    # Write your code here
    resultado = 0
    for i in a:
        resultado = resultado^i
        
    return(resultado)