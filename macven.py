import os
from time import sleep
sleep(1)
import LCD1602
LCD1602.init(0x27, 1)
print ("promo test")


def main():
	import datetime
	import random
	import string
	import os
	import sys
	import unicodedata
	dg = unicodedata.lookup('DEGREE SIGN')
	activate=''
	activated=''
	update=''
	updated=''
	first=''
	firstd=''
	val=''
	usern=''

	LCD1602.clear()
	LCD1602.write(2, 0, 'TRILAST-MILE')
	LCD1602.write(3, 1, 'WiFi VENDO' )

    
	try:
			file = open('/root/temp/first.txt','r')
			first=file.read()
			first=str.strip(first)
	except:
			pass
			
			if first == '1':
				firstd='1'
			else:
				firstd='0'
			print('firstd:'+firstd )

	
	try:
		import printer
	except:
		pass

	try:
	    file = open('/root/temp/activate.txt','r')
	    activate=file.read()
	    activate=str.strip(activate)
	except:
	    pass
	try:
	    file = open('/root/temp/update.txt','r')
	    update=file.read()
	    update=str.strip(update)
	except:
	    pass
	
	
	if activate == '1':
	    activated='1'
	else:
	    activated='0'
	    
	if update == '0':
	    updated='0'
	else:
	    updated='1'
	

	print('activated:'+activated)
	print('updated:'+updated)
	
	wifivendo='WIFIVENDO V.1.0'
	
	demo=0
	promo=20
	promo6=999
	promo12=999
	promo1d=999
	ratex=''
	rate1=999
	rate2=999
	rate3=999
	rate4=999
	rate5=999
	dummy=0
	counter=0
	coincounter=0
	coin=0
	coinv=0
	coinn=""
	coindrp=""
	countd=10
	countdd=99
	test=0
	tempx=30
	blinker=0
	nocoina=1
	nocoinb=1  #ENABLE COIN
	nobill=0  #ENABLE BILL
	buttonap=5
	buttonbp=10
	buttonbr=0
	switch=''
	ticketr=4
	pesorate=10
	datacap=200
	valuex=0
	title='WELCOME DEMOMODE'
	usrn='admin'
	passwd='test1234'
	from time import sleep
	from pyA20.gpio import gpio
	from pyA20.gpio import port
	datex = datetime.datetime.now()
	datex = datex.strftime("%x")
	datew=  datetime.datetime.now()
	datew = datew.strftime("%w")
	print ('date')
	print(datex)
	sleep(2)
	datew=  datetime.datetime.now()
	datew = datew.strftime("%w")
	print('datew: '+datew)
	activate=''
	relay='0'
	ipv4 = os.popen('ip addr show eth0').read().split("inet ")[1].split("/")[0]
	ipv4=str(ipv4[0:11])
	ipv4=ipv4+'1'
	ipadd=str(ipv4)
	global plag
	global profx

	LCD1602.clear()
	LCD1602.write(0, 0, wifivendo )
	LCD1602.write(0, 1, 'DATE:"'+datex+'"')
	
	device=0
	led = port.PA3
	coinpulse  = port.PA20
	billpulse  = port.PA8
	billpulse2  = port.PA1
	relays  = port.PA10
	buttonred = port.PA9
	buttonpro = port.PA7
	buttona = port.PA18
	buttonb = port.PA19
	buttonr = port.PA2
	buttonblue = port.PA0
	remarks=''
	gpio.init()
	gpio.setcfg(relays, gpio.OUTPUT)
	gpio.setcfg(led, gpio.OUTPUT)
	gpio.setcfg(coinpulse, gpio.INPUT)
	gpio.setcfg(billpulse, gpio.INPUT)
	gpio.setcfg(billpulse2, gpio.INPUT)
	gpio.setcfg(buttonred, gpio.INPUT)
	gpio.setcfg(buttonblue, gpio.INPUT)
	gpio.setcfg(buttonpro, gpio.INPUT)
	gpio.setcfg(buttona, gpio.INPUT)
	gpio.setcfg(buttonb, gpio.INPUT)
	gpio.setcfg(buttonr, gpio.INPUT)
	gpio.pullup(buttona, gpio.PULLUP)
	gpio.pullup(buttonb, gpio.PULLUP)
	gpio.pullup(buttonr, gpio.PULLUP)
	gpio.pullup(buttonred, gpio.PULLUP)
	gpio.pullup(buttonblue, gpio.PULLUP)
	gpio.pullup(buttonpro, gpio.PULLUP)
	gpio.pullup(coinpulse, gpio.PULLUP)
	gpio.pullup(billpulse, gpio.PULLUP)
	gpio.pullup(billpulse2, gpio.PULLUP)
	gpio.setcfg(buttonred, gpio.OUTPUT)
	gpio.output(buttonred, 0)
	gpio.setcfg(buttonred, gpio.INPUT)
	gpio.output(led, 0)
	gpio.output(relays, 1)
	try:
		file = open('/root/temp/demo.txt','r')
		demo=file.read()
		demo=str.strip(demo)
		print(demo)
	except:
		pass
	
		try:
			file = open('/root/temp/valuex.txt','w')
			valuex='0'
			file.write(str(valuex))
			file.close()
		except:
			pass
		
	from time import sleep
	import urllib

	def connected(host='http://google.com'):
		try:
			urllib.urlopen(host)
			return True
		except:
			return False

	nonet=1
	if updated=='1':
	    pass
	    while not connected():
	        print('no internet')
	        sleep(5)
	        LCD1602.clear()
	        LCD1602.write(0, 0, 'CHECKING NET ')
	        LCD1602.write(0, 1, 'PLEASE WAIT ...')
	        sleep(60)
	        nonet=0
	        break
	    print('connected')
	    

    
          
               

	print('offmode')
	sleep(1)


	def getserial():
		cpuserial = "0000000000000000"
		try:
			f = open('/proc/cpuinfo','r')
			for line in f:
				if line[0:6]=='Serial':
					cpuserial = line[10:26]
			f.close()
		except:
			cpuserial = "ERROR000000000"
		return cpuserial

	myserial = getserial()
	idno=str(myserial[6:16])
	print(idno)


	from time import sleep
	import urllib

	if activated == '1':
	    print('pass activate')
	    device = 1
	    os.system('sudo printf 0 > update.txt')
	    firstd='1'
	    file = open('/root/temp/valuex.txt','r')
	    valuex=file.read()
	    valuex=str(valuex)
	    file = open('/root/temp/buttonap.txt','r')
	    buttonap=file.read()
	    buttonap=str(buttonap)
	    file = open('/root/temp/buttonbp.txt','r')
	    buttonbp=file.read()
	    buttonap=str(buttonap)
	    file = open('/myfiles/pisopermin.txt','r')
	    pesorate=file.read()
	    pesorate=str(pesorate)
	    file = open('/myfiles/banner.txt','r')
	    title=file.read()
	    title=str(title)
	    file = open('/root/temp/relay.txt','r')
	    relay=file.read()
	    relay=str(relay)
	    file = open('/myfiles/passwd.txt','r')
	    passwd=file.read()
	    passwd=str(passwd)
	    file = open('/root/temp/datacap.txt','r')
	    datacap=file.read()
	    datacap=str(datacap)
	    try:
	        file = open('/root/temp/promo.txt','r')
	        promo=file.read()
	        promo=str(promo)
	    except:
	        pass
	    try:
	        file = open('/myfiles/promo6.txt','r')
	        promo6=file.read()
	        promo6=str(promo6)
	    except:
	        pass	    
	    try:
	        file = open('/myfiles/promo12.txt','r')
	        promo12=file.read()
	        promo12=str(promo12)
	    except:
	        pass	    
	    try:
	        file = open('/myfiles/promo1d.txt','r')
	        promo1d=file.read()
	        promo1d=str(promo1d)
	    except:
	        pass
	    try:
	        file = open('/root/temp/ratex.txt','r')
	        ratex=file.read()
	        ratex=str(ratex)
	    except:
	        pass

	if datacap == '':
	    datacap='0'		    
	if promo == '':
	    promo='20'
	if promo6 == '':
	    promo6='999'
	if promo12 == '':
	    promo12='999'	    
	if promo1d == '':
	    promo1d='999'
	if ratex == '':	
	    ratex=',,,,'
	ratex = ratex.split(',')
	print(ratex)
	try:
	    rate1=ratex[0]
	except:
	    pass
	try:
	    rate2=ratex[1]
	except:
	    pass
	try:
	    rate3=ratex[2]
	except:
	    pass
	try:
	    rate4=ratex[3]
	except:
	    pass
	try:
	    rate5=ratex[4]
	except:
	    pass	
	if rate1 == '':
	    rate1='999'	    
	if rate2 == '':
	    rate2='999'	
	if rate3 == '':
	    rate3='999'	
	if rate4 == '':
	    rate4='999'	
	if rate5 == '':
	    rate5='999'	
	    
	try:
	    rate11=0
	    promo=str(promo)
	    promo6=int(promo6)
	    promo12=int(promo12)
	    promo1d=int(promo1d)
	    rate1=int(rate1)
	    rate2=int(rate2)
	    rate3=int(rate3)
	    rate4=int(rate4)
	    rate5=int(rate5)
	    print('testing pass')
	except:
	    rate11=1
	    pass
	
	if rate11==1:
	    LCD1602.clear()
	    LCD1602.write(0, 0, 'ERROR INVALID!!!')
	    LCD1602.write(0, 1, 'CUSTOM RATE DATA')
	    rate1=999
	    rate2=999
	    rate3=999
	    rate4=999
	    rate5=999
	    print('testing errror')
	    sleep(10)
	else:
	    print('testing pass')
	    
	    
	print('promo:'+promo)
	print('promo6:'+str(promo6))	
	print('promo12:'+str(promo12))
	print('promo1d:'+str(promo1d))
	print('rate1:'+str(rate1))
	print('rate2:'+str(rate2))
	print('rate3:'+str(rate3))
	print('rate4:'+str(rate4))
	print('rate5:'+str(rate5))
	
	if device == 1:
		LCD1602.clear()
		LCD1602.write(2, 0, 'DEVICE READY')
		LCD1602.write(7, 1, '...')
		buttonck='THANK YOU!ENJOY!'

	if device == 2:
		LCD1602.clear()
		LCD1602.write(0, 0, 'S/N:"'+ idno+'"')
		LCD1602.write(0, 1, 'ALREADY MAXFIVE!')
		sleep(10)
		LCD1602.clear()
		exit()
	sleep(1)

	if buttonap=='' or buttonbp=='':
	    buttonap=5
	    buttonbp=10
	
	if nonet==1:
		try:
			valuex = worksheet.cell(cell.row, 4 ).value
		except:
			pass

	LCD1602.clear()
	LCD1602.write(0,0, ' "Total Sales"')
	LCD1602.write(3,1,'* '+str(valuex)+' PHP *')
	sleep(2)
	pass
	
	#COIN INSERTED
	
	varc=0
	coinnn=0
	def hanghere():
		blinker=0
		global plag
		global prof
#		print(countdd)
		
		coinn=str(coin)
		coinn=int(coinn)
		coinnn=int(coinn)
		if coinn in xrange(1,5):
			print("peso")
		else:

			promot=(float(promo)/100)+1
			coinn=coinn*promot
	#		print(coinn)
		varc=0
		uptime=str(coinn*int(pesorate))
		if (relay == '0' or relay == '5'):
		    if coin>=5 and coin<=9 and rate1!=999 :
		        varc=coinnn-5
		        varc=(varc*int(pesorate))+rate1
		        uptime=str(varc)
		        print('FIVE')
		    if coin>=10 and coin<=19 and rate2!=999 :
		        varc=coinnn-10
		        varc=(varc*int(pesorate))+rate2
		        uptime=str(varc)
		        print('TEN')		        
		    if coin>=20 and coin<=29 and rate3!=999 :
		        varc=coinnn-20
		        varc=(varc*int(pesorate))+rate3
		        uptime=str(varc)
		        print('20')	
		    if coin>=30 and coin<=49 and rate4!=999 :
		        varc=coinnn-30
		        varc=(varc*int(pesorate))+rate4
		        uptime=str(varc)
		        print('30')	
		    if coin>=50 and coin<=99 and rate5!=999 :
		        varc=coinnn-50
		        varc=(varc*int(pesorate))+rate5
		        uptime=str(varc)
		        print('50')			        
		        
		    
		print('testing here')
		print(coinnn)
		print(varc)
		uphr=0
		upmin=0
		uptimes=0
		uptime=str(uptime[0:4])
	#	print(uptime)
		if '.' in uptime: 
		    uptime=uptime[:uptime.index('.')]
		uptime=str(uptime)
		uptimes=int(uptime)
		uphr=(int(uptimes)/60)
		upmin=(int(uptimes)%60)
		uptimes=str(uphr)+'H'+str(upmin)+'M '
		uptimes=str(uptimes)
		uptime=str(uptime) +'min'

		if coin==promo6:
		    uptimes='6HRS'
		    LCD1602.clear()
		elif coin==promo12:
		    uptimes='12HRS'
		    LCD1602.clear()
		elif coin==promo1d:
		    uptimes='1DAY'
		    LCD1602.clear()
		else:
		    pass

		if relay =='1':
		    raten='PROMO1: '+str(rate1)+' '
		    profx=''
		    
		    if coin>=rate1 and coin<rate2:
		        raten='P1:'+str(rate1)+' P2:'+str(rate2)
		        profx='rate1'
		        plag=1
		    elif coin>=rate2 and coin<rate3:
		        raten='P2:'+str(rate2)+' P3:'+str(rate3)
		        plag=1
		    
		    elif coin>=rate3 and coin<rate4:
		        raten='P3:'+str(rate3)+' P4:'+str(rate4)
		        plag=1
		        profx='rate3'
		    elif coin>=rate4 and coin<rate5:
		        plag=1
		        profx='rate4'
		    elif coin>=rate5:
		        raten='PROMO5: '+str(rate5)+' '	
		        profx='rate5'
		        plag=1
		    else:
		        plag=0
	        
		print('plag')
		print(plag)		
		if relayes=='2':
		    LCD1602.write(0, 0, raten )
		    LCD1602.write(13, 0, '[0]')
		else:
		    LCD1602.write(0, 1, 'TIME: ' +uptimes)
		    LCD1602.write(13, 1, '[0]')
		    
		#LCD1602.write(0, 1, 'COIN CREDIT :')
		if relay=='2':
		    LCD1602.write(0, 1, 'PUSH BUTTON :')
		else:
		    LCD1602.write(0, 0, 'CREDITED: P')
		LCD1602.write(11, 0, str(coin))
	
	#THERMAL PAPER	
	def printing():
		varc=0
		uptime=str(coinn*int(pesorate))
		if (relay == '0' or relay == '5'):
		    if coin>=5 and coin<=9 and rate1!=999 :
		        varc=coinnn-5
		        varc=(varc*int(pesorate))+rate1
		        uptime=str(varc)
		        print('FIVE')
		    if coin>=10 and coin<=19 and rate2!=999 :
		        varc=coinnn-10
		        varc=(varc*int(pesorate))+rate2
		        uptime=str(varc)
		        print('TEN')		        
		    if coin>=20 and coin<=29 and rate3!=999 :
		        varc=coinnn-20
		        varc=(varc*int(pesorate))+rate3
		        uptime=str(varc)
		        print('20')	
		    if coin>=30 and coin<=49 and rate4!=999 :
		        varc=coinnn-30
		        varc=(varc*int(pesorate))+rate4
		        uptime=str(varc)
		        print('30')	
		    if coin>=50 and coin<=99 and rate5!=999 :
		        varc=coinnn-50
		        varc=(varc*int(pesorate))+rate5
		        uptime=str(varc)
		        print('50')				
		
		uphr=0
		upmin=0
		uptimes=0
		uptime=str(uptime[0:3])
		uptime = uptime.replace('.', '')
		uptime=str(uptime)
		uptimes=int(uptime)
		uphr=(int(uptimes)/60)
		upmin=(int(uptimes)%60)
		uptimes=str(uphr)+'H'+str(upmin)+'M'
		uptimes=str(uptimes)
		uptime=str(uptime) +'min'
		print('printing on')
		
		if coin==promo6:
		    print('promo6')
		    uptimes='6HRS'
		elif coin==promo12:
		    print('promo12')
		    uptimes='12HRS'
		elif coin==promo1d:
		    print('promo1d')
		    uptimes='1DAY'
		else:
		    print('promox')		
		
		try:
		    p=printer.ThermalPrinter(serialport="/dev/ttyS3")
		    p.font_b(90)
		    p.print_text("   "+str(title)+" HOTSPOT\n")
		    p.print_text('     TICKET CODE: "')
		    p.print_text(username)
		    p.print_text('"\n')
		    p.print_text('    "THANKS ENJOY! ')
		    p.print_text(uptimes)
		    p.print_text(' "')	
		    p.print_text("\n\n\n")
		    p.linefeed()
		    p.linefeed()
		except:
		    pass
		
		try:
		    with open('/dev/usb/lp0', 'w') as printusb:
		        printusb.write("   "+str(title)+" HOTSPOT\n")
		        printusb.write(" \n")
		        printusb.write('      TICKET CODE: "')
		        printusb.write(username)
		        printusb.write('" \n')
		        printusb.write(" \n")
		        printusb.write('     "THANKS ENJOY! ')
		        printusb.write(uptimes)
		        printusb.write("\n\n\n")
		        printusb.close()
		    if  os.path.isfile('/root/temp/cut.sh'):
		        print ("true print")
		    else:
		        os.system('sudo printf 1 > cut.sh')
		        f = open('/root/temp/cut.sh','r') 
		        filedata = f.read()
		        f.close()
		        bashh="#! /bin/bash \necho -e '\\012' > /dev/usb/lp0 \necho -e '\\x1b\\x69' > /dev/usb/lp0  "
		        newdata = filedata.replace("1",bashh)
		        f = open('/root/temp/cut.sh','w')
		        f.write(newdata)
		        f.close() 
		    os.system('chmod +x cut.sh')
		    os.system('./cut.sh')
		except:
		    pass
		print('promoxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')	
	def printing1():
	
		uptimes=''
		raten='PROMO1: '+str(rate1)+' '
		profx=''

		if coin>=rate1 and coin<rate2:
		    raten='P1:'+str(rate1)+' P2:'+str(rate2)
		    profx='rate1'
		    uptimes='PROMO1'
		    plag=1
		elif coin>=rate2 and coin<rate3:
		    raten='P2:'+str(rate2)+' P3:'+str(rate3)
		    plag=1
		    profx='rate2'
		    uptimes='PROMO2'
		elif coin>=rate3 and coin<rate4:
		    raten='P3:'+str(rate3)+' P4:'+str(rate4)
		    plag=1
		    profx='rate3'
		    uptimes='PROMO3'
		elif coin>=rate4 and coin<rate5:
		    raten='P4:'+str(rate4)+' P5:'+str(rate5)
		    plag=1
		    profx='rate4'
		    uptimes='PROMO4'
		elif coin>=rate5:
		    raten='PROMO5: '+str(rate5)+' '	
		    profx='rate5'
		    uptimes='PROMO5'
		    
		else:
		    plag=0
		    pass

		p=printer.ThermalPrinter(serialport="/dev/ttyS3")
		p.linefeed()
		p.print_text("   "+str(title)+" HOTSPOT\n\n")
		p.print_text('     TICKET CODE: "')
		p.print_text(username)
		p.print_text('"\n\n')
		p.print_text('    "THANKS ENJOY! ')
		p.print_text(uptimes)
		p.print_text(' "')	
		p.print_text("\n\n\n")
		p.linefeed()
		p.linefeed()
		try:
		    with open('/dev/usb/lp0', 'w') as printusb:
		        printusb.write("   "+str(title)+" HOTSPOT\n")
		        printusb.write(" \n")
		        printusb.write('      TICKET CODE: "')
		        printusb.write(username)
		        printusb.write('" \n')
		        printusb.write(" \n")
		        printusb.write('     "THANKS ENJOY! ')
		        printusb.write(uptimes)
		        printusb.write("\n\n\n")
		        printusb.close()
		    if  os.path.isfile('/root/temp/cut.sh'):
		        print ("true print")
		    else:
		        os.system('sudo printf 1 > cut.sh')
		        f = open('/root/temp/cut.sh','r') 
		        filedata = f.read()
		        f.close()
		        bashh="#! /bin/bash \necho -e '\\012' > /dev/usb/lp0 \necho -e '\\x1b\\x69' > /dev/usb/lp0  "
		        newdata = filedata.replace("1",bashh)
		        f = open('/root/temp/cut.sh','w')
		        f.write(newdata)
		        f.close() 
		    os.system('chmod +x cut.sh')
		    os.system('./cut.sh')
		except:
		    pass
				
	try:
	    relay=str.strip(relay)
	except:
	    pass
	if relay == '1':
	    relay='1'
	elif relay == '2':
	    relay='2'
	elif relay == '5':
	    relay='5'	    
	else:
	    relay='0'
	    
	relay=str(relay)
	print('relay')
	print(relay)
	relaybot='0'
	relayes='0'
	coins=1
	reboot=0
	plag=0
	onlineuser='ONLINE USER : 0'
	if firstd=='0':
	    print('rebooting')
	    LCD1602.clear()
	    LCD1602.write(0, 0, 'UPDATE FIRMWARE!')
	    LCD1602.write(0, 1, 'DEVICE REBOOTING')
	    os.system('sudo printf 1 > first.txt')
	    os.system("sudo python3 /root/temp/update.py")
	    sleep(5)
	    os.system("sudo reboot")
	    sleep(5)
	    
	else:
	    print('notrebooting')
	    try:
	        os.system('sudo rm /root/temp/first.txt')
	    except:
	        pass
	#starthere
	import paramiko

	if activated == '0':
	    os.system('sudo printf 1 > update.txt')
	    print('not activate')
	else:
	    print('test activate')

	datedx=''
	print('datedx')
	abuttonState = 0
	abuttonPin=0
	alastButtonState=0
	coin=0
	coinv=0
	mt=0
	flag=0
	import time  

	while True:

		abuttonState=gpio.input(coinpulse)
		if abuttonState != alastButtonState and nocoina==1 and (relay == '0' or relay == '5'):
		    alastButtonState = abuttonState
		    if abuttonState == 1:
		        m1=int(time.time()*1000.0)
		        flag=1
		      #  print(mt)
		        if mt in xrange(50,210):
		            coin+=1
		            countd=10

		if flag==1:
		    m2=int(time.time()*1000.0)
		    mt=m2-m1
		    if mt>=500:
		       mt=201
		    if mt>=200 and coin==0:
#		        print(coin)
		        flag=0
		    if mt>=200 and coin>=1:
		        flag=0
		        if coinv==0:
		            LCD1602.clear()
		            coinv=1
		        hanghere()

		if  0 == gpio.input(billpulse)and nocoina==1  and relay == '0':
			sleep(.05)
			coin+=1
			coins+=10
			coincounter+=1
			if coin==1:
			    LCD1602.clear()
			    
		if  0 == gpio.input(billpulse2)and nocoina==1  and relay == '0':
			sleep(.05)
			coin+=1
			coins+=10
			coincounter+=1
			if coin==1:
			    LCD1602.clear()

		if  0 == gpio.input(coinpulse)and nocoina==1 and relayes == '1' and relay == '1':
			sleep(.05)
			coin+=1
			coins+=10
			coincounter+=1

		if  0 == gpio.input(coinpulse)and nocoina==1 and relayes == '2' and relay == '1':
			sleep(.05)
			coin+=1
			coins+=10
			coincounter+=1			
			
		while counter == coins :	
			counter=0
			coins=1
			coincounter=0	
			countd=10
			hanghere()
				
		if coincounter >= 1:		
			counter+=1
			sleep(.01)		        
			

#			print("coin up")
		if  0 == gpio.input(buttonb) and nocoinb==1 and relay == '2':
		    sleep(0.5)
		    LCD1602.clear()
		    coin=int(buttonbp)
		    countd=1
		    hanghere()
		    countdd=1
		if  0 == gpio.input(buttona) and nocoinb==1 and relay == '2':
		    sleep(0.5)
		    LCD1602.clear()
		    coin=int(buttonap)
		    countd=1
		    hanghere()
		    countdd=1
        
		if coin==0 and (relay == '0' or relay == '2' or relay == '5') and (gpio.input(buttonred)==0 or countdd==0):
			LCD1602.clear()
			print('relay off')
			LCD1602.write(0, 0, 'S/N:"'+ idno+'"')
			LCD1602.write(0, 1, str(onlineuser)+' ')
			#LCD1602.write(0,1,'THANK YOU! ENJOY')
			gpio.output(led, 0)	
			reboot+=1
			print('reboot'+str(reboot))
			test=0
			countdd=99
			sleep(2)
			LCD1602.clear()

		if coin==0 and (relay == '0' or relay == '2' or relay == '5') and (gpio.input(buttonblue)==0 or countdd==0):
			LCD1602.clear()
			print('relay off')
			LCD1602.write(0, 0, 'S/N:"'+ idno+'"')
			LCD1602.write(0, 1, str(onlineuser)+' ')
			#LCD1602.write(0,1,'THANK YOU! ENJOY')
			gpio.output(led, 0)	
			reboot+=1
			print('reboot'+str(reboot))
			test=0
			countdd=99
			sleep(2)
			LCD1602.clear()

		if coin==0 and relay == '1' and gpio.input(buttonred)==0 and countdd==99 and relaybot=='0':
		    print('relay on ')
		    LCD1602.clear()
		    gpio.output(relays, 0)
		    countd=10
		    relayes='1'
		    hanghere()
		    test=0
		    sleep(1)
		    countdd=98			    

		if coin==0 and relay == '1' and gpio.input(buttonpro)==0 and countdd==99 and relaybot=='0':
		    print('relay on promo')
		    LCD1602.clear()
		    gpio.output(relays, 0)
		    countd=10
		    relayes='2'
		    hanghere()
		    test=0
		    sleep(1)
		    countdd=98		
			
		if coin==0 and relay == '1'and relaybot=='1' and (gpio.input(buttonred)==0 or countdd==0 or gpio.input(buttonpro)==0):
			LCD1602.clear()
			LCD1602.write(0, 0, 'S/N:"'+ idno+'"')
			LCD1602.write(0, 1, str(onlineuser)+' ')
			#LCD1602.write(0,1,'THANK YOU! ENJOY')
			gpio.output(relays, 1)
			gpio.output(led, 0)
			relayes='0'
			test=0
			relaybot='0'
			print('relay off')
			sleep(2)
			countdd=99
			
		if coin==0 and gpio.input(buttonr)==0:
			LCD1602.clear()
			sleep(1)
			blinker=1
			LCD1602.write(0, 0,'SALES DB RESET!!')
			LCD1602.write(0,1,'..Please wait...')
			if blinker == 1:
		 		gpio.output(led, 1)
		 	if blinker == 3:
		 		gpio.output(led, 0)
			if blinker == 6:
		 		gpio.output(led, 1)
			if blinker == 9:
		 		gpio.output(led, 1)			
			valuex='0'
			os.system('sudo printf '+ str(valuex)+' > valuex.txt')
			LCD1602.write(0,1,'...Successful...')
			sleep(3)
			os.system("reboot")
		# BUTTON BLIKER

		if coin==0 and reboot==4 :
		    #LCD1602.clear()
		    LCD1602.write(0, 0, str(onlineuser)+' ')
		    LCD1602.write(0,1,' SALES: '+str(valuex)+' PHP   ')
		    reboot+=1
		    
		if coin==0 and reboot==5 :
		    #LCD1602.clear()
		    LCD1602.write(0, 0, str(onlineuser)+' ')
		    LCD1602.write(0,1,' SALES: '+str(valuex)+' PHP   ')
		    reboot+=1
		    
		if coin==0 and reboot==6 :
		    #LCD1602.clear()
		    #LCD1602.write(0, 0, str(onlineuser)+' ')
		    LCD1602.write(0, 0, 'S/N:"'+ idno+'"')
		    LCD1602.write(0,1,' SALES: '+str(valuex)+' PHP   ')

		if coin==0 and reboot==15:
		    print('updating')
		    LCD1602.clear()
		    LCD1602.write(0, 0, 'RESTORE FIRMWARE')
		    LCD1602.write(0, 1, 'DEVICE REBOOTING')
		    os.system("sudo cp updatebu.py update.py")
		    os.system("sudo python3 /root/temp/update.py")
		    sleep(10)
		    os.system("reboot")
		    sleep(15)
		    reboot=0
		    sleep(1)
		    
		if coin >=1 or relayes=='1' or relayes=='2' and (flag==0 or coins==1): 				
		 	blinker+=1
		 	if blinker == 1:
		 		gpio.output(led, 1)
		 	if blinker == 100000:
		 		gpio.output(led, 0)
		 	if blinker >= 200000:
		 	    if relayes=='2' and countd==1 and coin!=0 :
		 	        countd=10
		 	    else:
		 	        countd-=1
		 	        LCD1602.write(14, 1,str(countd))
		 	        blinker=0
	#LCD DISPLAY LOOP DISPLAY
		if coin == 0 and relayes=='0':
			test+=1
			countd=10
			file = open('/sys/devices/virtual/thermal/thermal_zone0/temp','r')
			tempx=file.read()
			tempx=str(tempx[0:2])
			file.close()
			if (test >= 1 and test < 5):
				LCD1602.write(0, 0, title)
				LCD1602.write(0, 1, '< WiFi HOTSPOT >')
			if (test >= 5 and test < 10):
				LCD1602.write(0, 1, '<              >')
			if (test >= 10 and test < 15):
				LCD1602.write(0, 1, '< WiFi HOTSPOT >')
			if (test >= 15 and test < 20):
				LCD1602.write(0, 1, '<              >')
			if (test >= 20 and test < 25):
				LCD1602.write(0, 1, '< WiFi HOTSPOT >')
			if (test >= 40 and test < 50):
				LCD1602.write(0, 1, '<     PRESS    >')
			if (test >= 50 and test < 60):
				LCD1602.write(0, 1, '<    BUTTON    >')
			if (test >= 60 and test < 70):
				LCD1602.write(0, 1, '<  TO  INSERT  >')
			if (test >= 70 and test < 90):
				LCD1602.write(0, 1, '< 5 , 10 COINS >')
			if (test >= 90 and test < 150):
				permin=int(pesorate)			
				LCD1602.write(0, 1, 'RATE:P5.00 ' +str(5 * permin)+'min')
			if test >=150 and test < 170:
				LCD1602.write(0, 1, 'CPU TEMP: <'+tempx+chr(223)+'C>')
			if test == 210:
				test=0
			if test >= 5000000:
				blinker+=1
				if blinker == 1:
					gpio.output(led, 1)
				if blinker == 100000:
					gpio.output(led, 0)
				if blinker >= 200000: 
					countdd-=1
					LCD1602.write(12,1 ,"["+str(countdd)+"]")
					blinker=0	
		if coin ==0  and relay=='1' and (countd==0 or gpio.input(buttonred)==0 or gpio.input(buttonpro)==0):
		    coin=0
		    countdd=99
		    coinv=0
		    relayes='0'
		    blinker=0
		    gpio.output(relays, 1)
		    gpio.output(led, 0)
		    pass
		
		#COIN & BUTTON PRESS WILL GENERATE CODE	
		if coin >=1  and (countd==0 or gpio.input(buttonred)==0 or gpio.input(buttonblue)==0) and (relayes!='2' or coin<=(rate1-1)) and coin!='' and coinn!=0:	
			if coin <=999:

				gpio.setcfg(buttonred, gpio.OUTPUT)
				gpio.output(buttonred, 0)
				gpio.setcfg(buttonred, gpio.INPUT)
				try:
				    print("delete expire")
				    
				    datex=  datetime.datetime.now()
				    datew = datex.strftime("%w")
				    dateh = datex.strftime("%H")
				    dated = datex.strftime("%d")
				    dateww = datew+'w'
				    dateww = str(dateww)
				    dateh = dateh+'h'
				    dateh = str(dateh)
				    dated = dated+'d'
				    dated = str(dated)
				    print('datew:'+datew)
				    print('dateww:'+dateww)
				    print('dateh:'+dateh)
				    print('dated:'+dated)
				    ssh=paramiko.SSHClient() 
				    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				    ssh.connect(str(ipadd),port=22, username='admin', password=str(passwd))
				    ssh.exec_command(':foreach i in [/ip hotspot user find profile="default"] do={if ([/ip hotspot user get $i uptime]>=[/ip hotspot user get $i limit-uptime]) do={/ip hotspot user remove $i } }')
				    ssh.exec_command(':foreach i in [/ip hotspot user find profile="1"] do={if ([/ip hotspot user get $i uptime]>=[/ip hotspot user get $i limit-uptime]) do={/ip hotspot user remove $i } }')
				    ssh.exec_command(':foreach i in [/ip hotspot user find profile="2"] do={if ([/ip hotspot user get $i uptime]>=[/ip hotspot user get $i limit-uptime]) do={/ip hotspot user remove $i } }')
				    print("delete successs")
				except:
				    pass
				try:
					print("successtest")
					LCD1602.write(0, 0, 'GENERATING CODE!')
					ssh=paramiko.SSHClient() 
					ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
					ssh.connect(str(ipadd),port=22, username='admin', password=str(passwd))
				except Exception as e:
					print("System Offline")	
					LCD1602.clear()
					LCD1602.write(0, 0, '!CHECK MIKROTIK!')
					LCD1602.write(0, 1, 'PLEASE TRY AGAIN')
					countd=10
					sleep(5)
					hanghere()
				else:
					datex=  datetime.datetime.now()
					datew = datex.strftime("%w")
					dateh = datex.strftime("%H")
					dated = datex.strftime("%d")
					print('dateh:'+dateh)
					print('datew:'+datew)
					print('dated:'+dated)
					coindrp=str(coin)
					expired=''
					if datew=='0':
						expired='6'
					else:
						expired= int(datew)-1
					expired = str(expired)
					coindrp=str(coindrp)
					print( 'expire')
					print (expired)
					coinv=coin	
					print("printing")
					username= ''.join( random.choice(string.ascii_uppercase + string.digits) for x in range(ticketr))
					print('---------------------------------')
					coindrp=str(coin)
					coinn=str(coin)
					coinn=int(coinn)
					coinnn=int(coinn)
					if coinn in xrange(1,5):
					    print("peso")
					else:
					    promot=(float(promo)/100)+1
					    coinn=coinn*promot
					varc=0
					uptime=str(coinn*int(pesorate))
					if (relay == '0' or relay == '5'):
					    if coin>=5 and coin<=9 and rate1!=999 :
					        varc=coinnn-5
					        varc=(varc*int(pesorate))+rate1
					        uptime=str(varc)
					        print('FIVE')
					    if coin>=10 and coin<=19 and rate2!=999 :
					        varc=coinnn-10
					        varc=(varc*int(pesorate))+rate2
					        uptime=str(varc)
					        print('ten')					
					    if coin>=20 and coin<=29 and rate3!=999 :
					        varc=coinnn-20
					        varc=(varc*int(pesorate))+rate3
					        uptime=str(varc)
					        print('20')					
					    if coin>=30 and coin<=49 and rate4!=999 :
					        varc=coinnn-30
					        varc=(varc*int(pesorate))+rate4
					        uptime=str(varc)
					        print('30')
					    if coin>=50 and coin<=99 and rate5!=999 :
					        varc=coinnn-50
					        varc=(varc*int(pesorate))+rate5
					        uptime=str(varc)
					        print('50')					        
					uptime=str(uptime)+'m'
					print('-------------------------')
					print(uptime)
					print('time:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
					
					if coin in xrange(1,3):
						prof=str(1)
						bytelimit=str(coin*int(datacap))+'M'
					elif coin in xrange(3,5) and relay=='2':
					    prof=str(1)
					    bytelimit=str(coin*int(datacap))+'M'
					    printing()

					elif coin in xrange(1,5):
					    prof=str(1)
					    bytelimit=str(coin*int(datacap))+'M'					    
					elif coin in xrange(5,11):
						bytelimit=str(coin*int(datacap))+'M'
						prof=str(2)
						printing()
						print('time:yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
					else:
						if coin==promo6:
						    print('promo6')
						    if dateh=='00':
						        expired='6h'
						    else:
						        expired= int(dateh)-1
						        expired=str(expired)+'h'
						    uptime='6h'
						    uptime=str(uptime)
						    bytelimit='0'
						elif coin==promo12:
						    print('promo12')
						    if datew=='0':
						        expired='12h'
						    else:
						        expired= int(datew)-1
						        expired=str(expired)+'w'						    
						    uptime='12h'
						    uptime=str(uptime)
						    bytelimit='0'
						elif coin==promo1d:
						    print('promo1d')
						    if dateh=='1':
						        expired='1d'
						    else:
						        expired= int(dated)-1
						        expired=str(expired)+'d'
						    uptime='1d'
						    uptime=str(uptime)
						    bytelimit='0'
						else:
						    print('promox')
						    bytelimit=str(coin*int(datacap))+'M'
						    pass
						printing()	
						prof=str('default')
					print('time:iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
					print('time:'+uptime)
					print('prof:'+prof)
					print('expired:'+expired)

				
					ssh.exec_command('ip hotspot user add name='+username+' comment='+coindrp+'  limit-uptime='+uptime+' limit-bytes-total='+bytelimit+' profile='+prof+' ' )

					LCD1602.write(12, 1, '[99]')
					LCD1602.write(0, 1, 'TIME:')
					LCD1602.write(0, 0,'TICKET : "'+username+'"  ' )
					test = 5000000
					blinker=0
					gpio.output(relays, 1)
					gpio.output(led, 0)
					try:
					    actives=0
					    valuex=coinv+int(valuex)
					    os.system('sudo printf '+ str(valuex)+' > valuex.txt')
					    stdin, stdout, stderr = ssh.exec_command('ip hotspot active print count')
					    actives = stdout.readlines()
					    actives = str(actives[0])
					    actives = str.rstrip(actives)
					    actives = 'User:'+str(actives)+'-T:'+ str(tempx)
					    actives = str(actives)
					    print(actives)
					    os.system('sudo printf '+ str(actives)+' > tempx.txt')
					    print(countdd)
					    
					except:
						pass
					coin=0
					coinv=0
					reboot=0
					relayes='0'
					relaybot='1'
					sleep(5)
					
			else:
				LCD1602.clear()
				LCD1602.write(0, 0, '!INVALID INPUT!')
				LCD1602.write(0, 1, 'PLEASE TRY AGAIN')	
				coin=0
				test=0
				countd=10
				blinker=0
				gpio.output(led, 0)		
				sleep(2)
				
		#COIN & BUTTON PRESS WILL GENERATE CODE	
		if coin >=1  and  gpio.input(buttonpro)==0 and relayes=='2' and plag==1 :	
			if coin <=999:
				gpio.setcfg(buttonred, gpio.OUTPUT)
				gpio.output(buttonred, 0)
				gpio.setcfg(buttonred, gpio.INPUT)
				try:
				    print("delete expire")
				    datex=  datetime.datetime.now()
				    datew = datex.strftime("%w")
				    dateh = datex.strftime("%H")
				    dated = datex.strftime("%d")
				    dateww = datew+'w'
				    dateww = str(dateww)
				    dateh = dateh+'h'
				    dateh = str(dateh)
				    dated = dated+'d'
				    dated = str(dated)
				    print('datew:'+datew)
				    print('dateww:'+dateww)
				    print('dateh:'+dateh)
				    print('dated:'+dated)
				    ssh=paramiko.SSHClient() 
				    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				    ssh.connect(str(ipadd),port=22, username='admin', password=str(passwd))
				    ssh.exec_command(':foreach i in [/ip hotspot user find profile="default"] do={if ([/ip hotspot user get $i uptime]>=[/ip hotspot user get $i limit-uptime]) do={/ip hotspot user remove $i } }')
				    ssh.exec_command(':foreach i in [/ip hotspot user find profile="1"] do={if ([/ip hotspot user get $i uptime]>=[/ip hotspot user get $i limit-uptime]) do={/ip hotspot user remove $i } }')
				    ssh.exec_command(':foreach i in [/ip hotspot user find profile="2"] do={if ([/ip hotspot user get $i uptime]>=[/ip hotspot user get $i limit-uptime]) do={/ip hotspot user remove $i } }')
				    print("delete successs")
				
				except:
				    pass
				try:
					print("successtest")
					LCD1602.write(0, 0, 'GENERATING CODE!')
					ssh=paramiko.SSHClient() 
					ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
					ssh.connect(str(ipadd),port=22, username='admin', password=str(passwd))
					
				except Exception as e:
					print("System Offline")	
					LCD1602.clear()
					LCD1602.write(0, 0, '!CHECK MIKROTIK!')
					LCD1602.write(0, 1, 'PLEASE TRY AGAIN')
					countd=10
					sleep(5)
					hanghere()
				else:
				
					datex=  datetime.datetime.now()
					username= ''.join( random.choice(string.ascii_uppercase + string.digits) for x in range(ticketr))
					coinv=coin
					ratenx=''
					if coin>=rate1 and coin<rate2:
					    prof='PROMO1'
					    ratenx=str(rate1)
					elif coin>=rate2 and coin<rate3:
					    prof='PROMO2'
					    ratenx=str(rate2)
					elif coin>=rate3 and coin<rate4:
					    prof='PROMO3'
					    ratenx=str(rate3)
					elif coin>=rate4 and coin<rate5:
					    prof='PROMO4'
					    ratenx=str(rate4)
					elif coin>=rate5:
					    prof='PROMO5'
					    ratenx=str(rate5)
					else:
					    pass
					printing1()					

					ssh.exec_command('ip hotspot user add name='+username+' profile='+prof+' ' )

					LCD1602.write(12, 1, '[99]')
					LCD1602.write(0, 1, prof+': '+ratenx+'P')
					LCD1602.write(0, 0,'TICKET : "'+username+'"  ' )
					test = 5000000
					blinker=0
					gpio.output(relays, 1)
					gpio.output(led, 0)
					try:
					    actives=0
					    valuex=coinv+int(valuex)
					    os.system('sudo printf '+ str(valuex)+' > valuex.txt')
					    stdin, stdout, stderr = ssh.exec_command('ip hotspot active print count')
					    actives = stdout.readlines()
					    actives = str(actives[0])
					    actives = str.rstrip(actives)
					    actives = 'User:'+str(actives)+'-T:'+ str(tempx)
					    actives = str(actives)
					    print(actives)
					    os.system('sudo printf '+ str(actives)+' > tempx.txt')
					    print(countdd)
					    
					except:
						pass
					coin=0
					coinv=0
					reboot=0
					relayes='0'
					relaybot='1'
					sleep(5)
					
			else:
				LCD1602.clear()
				LCD1602.write(0, 0, '!INVALID INPUT!')
				LCD1602.write(0, 1, 'PLEASE TRY AGAIN')	
				coin=0
				test=0
				countd=10
				blinker=0
				gpio.output(led, 0)		
				sleep(2)
				
main()

        