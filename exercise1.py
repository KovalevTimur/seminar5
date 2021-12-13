
try:
        fhand = open('mailbox.txt')
except:
        print('File cannot be opened')
        exit()

lines=fhand.readlines()
Timur=[]
file=open('output.txt', 'w')
for line in lines:
        if line.startswith('From: '):
                token=line.split('@')
                tokens=line.split()
                ind=line.find('')
                print("Email: ", tokens[-1:])
                print("Domain: ", token[1])
                word=line[ind+1:-2]
                file.write(word)
fhand.close()
