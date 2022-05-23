def timeConversion(s):
    # Write your code here
    # Si los ultimos dos caracteres son AM
    if(s[-2:]=="AM"):
    # Si los primeros dos caracteres son 12
        if(s[:2]=="12"):
    # Entonces armamos el string con 00, y despues s a partir del caracter 2, pero sin incluir los ultimos dos caracteres (AM)    
            return "00"+s[2:-2]
        else:
        # return s desde el principio menos los ultimos dos caracteres.
            return s[:-2]
    else:
        # PM Case: convert de hours.
        h = int(s[:2])
        if (h<12):
            h+=12
        return str(h)+s[2:-2]