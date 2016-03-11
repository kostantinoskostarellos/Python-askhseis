import random
import sys
import webbrowser

from PIL import Image,ImageDraw
im = Image.new("RGBA",(1024,1024),"white")
#pinakes gia apothikeysh random timwn
theshx =[]
theshy =[]
aktinar =[]
#2 ebdikthkes metablhtes gia thn metrhsh twn shmeiwn tomhs
count = 0
apeiro = 0
kukloi = 0


#to loop gia tous 20 kuklous
for i in range (0,20):
   #tuxai aktina kai suntetagmenes kentrou
   r = random.randrange(10,500)
   x = random.randrange(0,1024)
   y = random.randrange(0,1024)
   theshx.append(x)
   theshy.append(y)
   aktinar.append(r)
   draw = ImageDraw.Draw(im)
   draw.ellipse((x-r,y-r,x+r,y+r),outline='black')
   for j in range (0,i):
   #upologizw thn apostash twn kentrwn twn duo kuklwnkai xwrizw periptwseis
	   d = (((theshx[j+1]-theshx[j])**(2))+((theshy[j+1]-theshy[j])**(2)))**(0.5) 
	   R = (aktinar[j]+aktinar[j+1])
	   if d == R :
	    count +=1
	    kukloi +=1
		#posoi kukloi temnontai 
	   
	   elif R > d:
	    count +=2
	    kukloi +=1
	   elif  (theshx[j] == theshx[j+1]) and (theshy[j] == theshy[j+1]) and (aktinar[j] == aktinar[j+1]):
	    apeiro = 1
	    kukloi +=1
if apeiro == 1 :
	print("Yparxoun apeira shmeia tomhs")
	print("Oi kukloi pou temnontai einai",kukloi)
else :
	print("Ta shmeia tomhs einai",count)
	print("Oi kukloi pou temnontai einai",kukloi)
   
   
im.save('circles.png',"PNG")
#dhmiourgei to arxeio alla den to emfanizei gia kapoio logo  im.show('circles.png',"PNG")
#ayth me to webroser einai 2 lush thn epsaksa sto internet
webbrowser.open("circles.png")
 
 
 
 
 
