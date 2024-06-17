coding = int(input("Press 1 for Coding or 0 for Decoding : "))

st = input("Enter the Message : ")
words = st.split()
nwords = []

if(coding == 1):
    for word in words:
        if len(word) >= 3:
            r1 = "wer"
            r2 = "sdf"
            stnew = r1 + word[1:] + word[0] + r2 
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
    
else:
    for word in words:
        if len(word) >= 3:
            stnew = word[3:-3]
            stnew = stnew[-1:] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))