import re
def ref(inp):
    gas=""
    raw=re.compile(r"[A-Z][a-z]+")
    wrd=raw.findall(inp)
    for i, word in enumerate(wrd):
        if i!=0:
            res+=" "+word
        else:
            res+=word
    
    
    
