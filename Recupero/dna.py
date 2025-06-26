'''s1= "GGTACCGTGA"

s2= "CGTGAACCTT"

s1= "TTGACCAGGTCA"
s2= "AACCGGTTAA"'''

s1= "TTACGAGTACGCTAGT"
s2= "ACGCTAGTCCGA"
print(s1, s2)

s3= ""
for i in range(min(len(s1), len(s2))):
    if s2[0:i+1] == s1[-1-i:]:
        s3 = s2[0:i+1]
        break

print(s3, len(s3))