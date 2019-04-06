from kafka import KafkaConsumer
consumer = KafkaConsumer('hello-kafka')
for msg in consumer:
    print (msg)
