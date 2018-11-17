# RC4

def rc4_crypt(plain,key='郑召作'):
    i=0
    j=0
    s=list(range(256))
    t=list(range(256))
    for i in range(256):
        s[i]=i
        t[i]=ord(key[i % len(key)])
    for i in range(256):
        j=(j+s[i]+t[i])% 256
        s[i],s[j]=s[j],s[i]
    i=0
    j=0
    out = []
    for sz in plain:
        i=(i+1)%256
        j=(j+s[i])%256
        s[i],s[j]=s[j],s[i]
        t=(s[i]+s[j])%256
        k=s[t]
        out.append(chr(ord(sz)^k))
    return ''.join(out)
        
rc4_crypt("中国地质大学（武汉）")

