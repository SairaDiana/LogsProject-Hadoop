# Proyecto_logs
Proyecto_Final

En este repositorio, se encuantra el proyecto final que consistio en lo siguiente:

1-.Lo primero que se tenia que hacer era saber en donde se encuantran todos los logs que se generan en nuestra maquina local, se encuantran en la siguiente ruta: /var/log/messages

2-.Una vez que se tenga lo anterior ahora se procede a realizar la configuración Flume, para esto una vez que descargamos e instalamos dicho programa, entramos a su carpeta de conf, en donde se va a guardar el archivo de configuración el cual se llama: flume-log-kafka.
Para mas detalles visitar las siguientes páginas:
  1-.  http://www.w3ii.com/es/apache_flume/apache_flume_configuration.html
  2-.  https://www.ibm.com/support/knowledgecenter/es/SSPT3X_4.1.0/com.ibm.swg.im.infosphere.biginsights.admin.doc/doc/ManagingFlume.html
  
3-.Por último, la instancia de nuestros mensajes va a ser HDFS, en donde se hizo uso de Docker y creamos un contenedor de Hadoop, para madar la información a HDFS se decribe en el script llamado consumidor.py.