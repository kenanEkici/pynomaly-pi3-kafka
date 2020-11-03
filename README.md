# Detecting anomalies in sensor data streamed from Raspberry PI 3  

# Project overview

- read sensor data from Raspberry PI
- use & write libraries according to data needs
- setup Apache Kafka and Zookeeper to stream sensor data from each RPI
- setup necessary brokers and write producer for each class of sensor data
- produce data to topics who will act as datapoints for master host
- consume data from topics on a central host machine with Kafka
- automate fitting PyNomaly model from specific datapoints (offset) of topic
- automate consuming test data and detecting anomalies
- write anomalies per topic and plot topics with Matplotlib

# Check the install-zookeeper_kafka.md
https://aknay.github.io/2017/05/11/how-to-install-zookeeper-and-kafka-in-raspberry-pi-3.html
### (Objective): Kafka/Zookeeper setup script

# Setup multiple RPI as cluster of nodes
https://medium.com/@oliver_hu/set-up-a-kafka-cluster-with-raspberry-pi-2859005a9bed

# Create producers
- create a topic for the RPI broker
- create the producers for the broker and emit to topic
- (Objective): Check RPI GPIO events for emitting on demand
- (Setup example): 1 device -> 1..* sensors --> RPI/device --> 1 producer/*sensor/*topics
- (Setup example): Analyze device: connect sensors to GPIO: determine stream type (actor/listener)
- (Setup exampe):  Write necessary producer and libraries to read sensor data

# RPI setup
https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi

# BME280 
https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout/python-circuitpython-test

# MatPlotlib
https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/all

# PyNomaly
https://github.com/vc1492a/PyNomaly
