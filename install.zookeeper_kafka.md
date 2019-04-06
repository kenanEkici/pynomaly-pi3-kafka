#!/bin/sh

# downloading zookeeper
wget http://www-eu.apache.org/dist/zookeeper/zookeeper-3.4.14/zookeeper-3.4.14.tar.gz
sudo tar -zxvf zookeeper-3.4.14.tar.gz -C /usr/local
sudo mv /usr/local/zookeeper-3.4.14/ /usr/local/zookeeper
rm zookeeper-3.4.14.tar.gz


sudo nano /usr/local/zookeeper/conf/zoo.cfg

# The number of milliseconds of each tick
tickTime=5000
# The number of ticks that the initial 
# synchronization phase can take
initLimit=10
# The number of ticks that can pass between 
# sending a request and getting an acknowledgement
syncLimit=5
# the directory where the snapshot is stored.
dataDir=/usr/local/zookeeper
# the port at which the clients will connect
clientPort=2181

server.1=raspberrypi-1:2888:3888

# run zookeeper server
sudo /usr/local/zookeeper/bin/zkServer.sh start

# downloading kafka
wget http://www-eu.apache.org/dist/kafka/2.2.0/kafka_2.12-2.2.0.tgz
sudo tar -zxvf kafka_2.12-2.2.0.tgz -C /usr/local
sudo mv /usr/local/kafka_2.12-2.2.0/ /usr/local/kafka
rm kafka_2.12-2.2.0.tgz

# start kafka
sudo nano /usr/local/kafka/bin/kafka-server-start.sh

# replace if fi
# JVM performance options
# with
if [ -z "$KAFKA_JVM_PERFORMANCE_OPTS" ]; then
KAFKA_JVM_PERFORMANCE_OPTS="-client -XX:+UseParNewGC -XX:+UseConcMarkSweepGC -XX:+CMSClassUnloadingEnabled -XX:+CMSScavengeBeforeRemark -XX:+DisableExplicitGC -Djava.awt.headless=true"
fi

# run kafka
sudo /usr/local/kafka/bin/kafka-server-start.sh /usr/local/kafka/config/server.properties &


