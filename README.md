# Projects for Raspberry PI and IoT/AI

# Project overview

## 1. Read sensor data from Raspberry PI
## 2. Use/Write libraries according to data needs
## 3. Setup Apache Kafka and Zookeeper to stream sensor data from each RPI
## 4. Setup necessary brokers and write producer for each class of sensor data
## 5. Produce data to topics who will act as datapoints for master host
## 6. Consume data from topics on a central host machine with Kafka
## 7. Automate fitting PyNomaly model from specific datapoints (offset) of topic
## 8. Automate consuming test data and detecting anomalies
## 9. Write anomalies per topic and plot topics with Matplotlib

# Check the install-zookeeper_kafka.md
https://aknay.github.io/2017/05/11/how-to-install-zookeeper-and-kafka-in-raspberry-pi-3.html
### (Objective): Kafka/Zookeeper setup script

# Setup multiple RPI as cluster of nodes
https://medium.com/@oliver_hu/set-up-a-kafka-cluster-with-raspberry-pi-2859005a9bed

# Create producers
### Create a topic for the RPI broker
### Create the producers for the broker and emit to topic
### (Objective): Check RPI GPIO events for emitting on demand
### (Setup example): 1 device -> 1..* sensors --> RPI/device --> 1 producer/*sensor/*topics
### (Setup example): Analyze device: connect sensors to GPIO: determine stream type (actor/listener)
### (Setup exampe):  Write necessary producer and libraries to read sensor data

# RPI setup
https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi

# BME280 
https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout/python-circuitpython-test

# MatPlotlib
https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/all

# PyNomaly
https://github.com/vc1492a/PyNomaly
