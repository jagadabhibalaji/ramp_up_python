import threading
import time
import random

def producer(consumer_ready, producer_id):
    time.sleep(random.random())
    print(f"Producer {producer_id}: Producing item")
    time.sleep(1)
    consumer_ready.set()

def consumer(consumer_ready, consumer_id):
    start_time = time.time()
    while True:
        consumer_ready.wait()
        print(f"Consumer {consumer_id}: Consuming item")
        time.sleep(1)
        time.sleep(random.random())
        consumer_ready.clear()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Consumer {consumer_id} took {elapsed_time} seconds")
        time.sleep(1)
        start_time = end_time

consumer_ready = threading.Event()

n_producers = int(input("Enter how many producers do you want :"))
n_consumers = int(input("Enter how many consumers do you want :"))

producer_threads = [threading.Thread(target=producer, args=(consumer_ready, i)) for i in range(n_producers)]
consumer_threads = [threading.Thread(target=consumer, args=(consumer_ready, i)) for i in range(n_consumers)]

start_time = time.time()

for producer_thread in producer_threads:
    producer_thread.start()

for consumer_thread in consumer_threads:
    consumer_thread.start()

for producer_thread in producer_threads:
    producer_thread.join()

for consumer_thread in consumer_threads:
    consumer_thread.join()




# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"Total time taken: {elapsed_time:.2f} seconds")

