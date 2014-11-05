text = open('/home/msenar/coding/friendmemeow/breeds.txt')
output = open('//home/msenar/coding/friendmemeow/output.txt','w')

for line in text:
    table = line.split()
    table[0] = table[1]
    string = table

    output.write(str(string) + "\n")