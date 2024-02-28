import re
def conv(inpstr):
    cam=""
    dsu=re.compile(r"[_]")
    wrd=dsu.split(inpstr)
    for i,word in enumerate(wrd):
     if i!=0:
        cam+=wrd.capitalize()
    else:
        cam+=wrd
        return cam  
