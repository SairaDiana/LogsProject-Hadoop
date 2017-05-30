#Libreria kafka
from kafka import KafkaConsumer
import json
import hdfs

#ip de nuestra máquina fisica
consumer = KafkaConsumer('topico', bootstrap_servers=['10.110.70.91:9092'])
#Dirección ip de nuestro contenedor de hadoop
client = hdfs.InsecureClient('http://172.17.0.3:50070', user='root')

#En HDFS se va a crear una carpeta llamada logs
dir = 'logs'

if(str(client.list('/')).find(dir)==-1):	
	client.makedirs('/'+dir)	

j = 0
for msg in consumer:
	#print(msg.value.decode('utf8'))

	a = msg.value.decode('utf8')

	i = 0
	c=[]
	for b in a:
		if (b==' '):
			c.append(i)
		i = i+1
	d = a[0:c[0]]
	e = a[c[0]+1:c[1]]
	f = a[c[1]+1:c[2]]
	g = a[c[2]+1:len(a)-1]
	print(d)
	print(e)
	print(f)
	print(g)

#Los logs van a tener un formato json

	DIC = {'mes':d,'dia':e,'hora':f, 'log':g}
	#twtJson = json.loads(msg.value.decode('utf8'))
	dumpsJson = json.dumps(str(DIC))
	#print(twtJson)
	mes = DIC['mes']
	dia = DIC['dia']
	hora = DIC['hora']
	#print(usuario)
	client.write('/'+dir+'/'+mes+'_'+dia+'_'+str(j)+'_saira.json', dumpsJson)
	j=j+1

