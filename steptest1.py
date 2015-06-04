import random
import os

CHUNK_SIZE  = 1024


def random_word( wlen ):
    wfile = open('/usr/share/dict/words','r')
    flen = os.stat('/usr/share/dict/words').st_size
    chunks = flen / CHUNK_SIZE
    word = None
    
    while not word:
        rpos = random.randint(0,chunks) * CHUNK_SIZE        
        wfile.seek(rpos)
        buf = wfile.read(CHUNK_SIZE)
     
        words = [x  for x in buf.split("\n")[1:-1] if len(x) == wlen ]
        if words:
            p = random.randint(0,len(words)-1)
            word = words[p]

    return word


print random_word(16)
