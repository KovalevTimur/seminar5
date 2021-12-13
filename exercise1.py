
try:
        fhand = open('mailbox.txt')
except:
        print('File cannot be opened')
        exit()

lines=fhand.readlines()
file=open('output.txt', 'w')
for line in lines:
        if line.startswith('From: '):
                tokens=line.split('@')
                ind=line.find(' ')
                print(tokens[1])
                print(tokens[ind+1:-2])
                file.write(line[ind+1:-2])
                file.write(' ')
fhand.close()
