fhandle= open('C:/Users/lpers/Downloads/colonne.txt')
righe=0
somma=0
for riga in fhandle:
    if righe==0:
        righe=righe+1
        continue
    
    riga=riga.rstrip()
    c=0
    last=riga.rfind('\t')
    
    while True:
    
        
        if c==0:
          i=riga.find('\t') 
          num=riga[0:i]
          num=float(num)
          somma=somma+num
          print(num)
          k=i
          c=c+1
        else:
          
          i=riga.find('\t',k+1) 
          num=riga[k+1:i]
          num=float(num)
          somma=somma+num
          print(num)
          k=i
          if i==last:
              num=riga[last+1:]
              num=float(num)
              somma=somma+num
              print(num)
    
              break
          

print(somma)
fhandle.close()
          