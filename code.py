# delete first 10 characters from string s
s = 'abcdefghijklmniopqrstuv'
final_s = ''
mylist = list(s)
count = 0
for i in mylist:
    count+=1
    mylist.pop(0)
    if(count == 10):
        print(mylist)
        break
        
print(final_s.join(mylist))   
