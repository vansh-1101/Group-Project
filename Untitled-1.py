filee=open("this.txt","w")
filee.write("hello world\n")
filee.write("how are you\n")
this line is adde
filee.write("Hello From AB")
filee.close()

filee=open("this.txt","r")
data=filee.read()
filee.close()

filee2=open("this.txt","w")
filee2.write(data)
filee2.close()