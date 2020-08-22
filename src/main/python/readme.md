For Running sample_word_count.py program, Login to the master node of the cluster

~~~~
ssh master_node_ip
~~~~
Change to root user so that you have enough privileges
~~~~
sh-4.2$ sudo su -
Last login: Sat Aug 22 11:08:49 UTC 2020

EEEEEEEEEEEEEEEEEEEE MMMMMMMM           MMMMMMMM RRRRRRRRRRRRRRR
E::::::::::::::::::E M:::::::M         M:::::::M R::::::::::::::R
EE:::::EEEEEEEEE:::E M::::::::M       M::::::::M R:::::RRRRRR:::::R
  E::::E       EEEEE M:::::::::M     M:::::::::M RR::::R      R::::R
  E::::E             M::::::M:::M   M:::M::::::M   R:::R      R::::R
  E:::::EEEEEEEEEE   M:::::M M:::M M:::M M:::::M   R:::RRRRRR:::::R
  E::::::::::::::E   M:::::M  M:::M:::M  M:::::M   R:::::::::::RR
  E:::::EEEEEEEEEE   M:::::M   M:::::M   M:::::M   R:::RRRRRR::::R
  E::::E             M:::::M    M:::M    M:::::M   R:::R      R::::R
  E::::E       EEEEE M:::::M     MMM     M:::::M   R:::R      R::::R
EE:::::EEEEEEEE::::E M:::::M             M:::::M   R:::R      R::::R
E::::::::::::::::::E M:::::M             M:::::M RR::::R      R::::R
EEEEEEEEEEEEEEEEEEEE MMMMMMM             MMMMMMM RRRRRRR      RRRRRR

[root@ip-mymaster ~]#
~~~~

**Create a folder files on HDFS** 
copy file from which you want to count the words to this folder
We are taking spark-defaults.conf for our example

~~~~
[root@ip-mymaster ~]# hdfs dfs -mkdir -p files
[root@ip-mymaster ~]# hdfs dfs -put /etc/spark/conf.dist/spark-defaults.conf files
~~~~

run the spark submit 
We will discuss the spark submit parameters later
~~~~
$ spark-submit --master yarn --deploy-mode client --executor-memory 1g \
--name mywordcount --conf "spark.app.id=mywordcount" sample_word_count.py files/spark-defaults.conf 2
~~~~

Output of this file
 Find this line in stdout (collect at /root/sample_word_count.py:38) finished in 1.290 s
 You will find the output

`(u'', 130), (u'true', 9), (u'file', 3), (u'You', 2), (u'-XX:CMSInitiatingOccupancyFraction=70', 2), (u'#', 14), (u'with', 2), (u'distributed', 3), (u'for', 2), (u'may', 2), (u'-XX:+UseConcMarkSweepGC', 2), (u':/usr/lib/hadoop-lzo/lib/*:/usr/lib/hadoop/hadoop-aws.jar:/usr/share/aws/aws-java-sdk/*:/usr/share/aws/emr/emrfs/conf:/usr/share/aws/emr/emrfs/lib/*:/usr/share/aws/emr/emrfs/auxlib/*:/usr/share/aws/emr/goodies/lib/emr-spark-goodies.jar:/usr/share/aws/emr/security/conf:/usr/share/aws/emr/security/lib/*:/usr/share/aws/hmclient/lib/aws-glue-datacatalog-spark-client.jar:/usr/share/java/Hive-JSON-Serde/hive-openx-serde.jar:/usr/share/aws/sagemaker-spark-sdk/lib/sagemaker-spark-sdk.jar:/usr/share/aws/emr/s3select/lib/emr-s3-select-spark-connector.jar', 2), (u'Apache', 2), (u'-XX:+CMSClassUnloadingEnabled', 2), (u'License', 3), (u'the', 9), (u'this', 3), (u'-9', 2), (u"-XX:OnOutOfMemoryError='kill", 2), (u'See', 2), (u'in', 2), (u'or', 3), (u'to', 3), (u'under', 4), (u'-XX:MaxHeapFreeRatio=70', 2), (u'/usr/lib/hadoop/lib/native:/usr/lib/hadoop-lzo/lib/native', 2), (u'License.', 2), (u"%p'", 2), (u'hdfs:///var/log/spark/apps', 2)`
