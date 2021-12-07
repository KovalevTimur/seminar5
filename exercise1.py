
try:
        fhand = open('mailbox.txt')
except:
        print('File cannot be opened')
        exit()

lines=fhand.readlines()

file=open('output.txt', 'w')
for line in lines:
       if 'From:' in line:
           ind=line.find('F ')
           en_ind=line.find('.')
           word=line[ind+1:en_ind+30]
           print(word)
           file.write(word)
           file.write('\n')
fhand.close()
