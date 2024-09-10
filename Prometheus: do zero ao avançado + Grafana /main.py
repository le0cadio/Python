import prometheus_client as prom

from random import randrange
import time

EXEMPLO_COUNTER = prom.Counter('exemplo_counter', 'Random number between 1 - 100')
EXEMPLO_GAUGE = prom.Gauge('exemplo_gauge', 'Random number between 1 - 100')
EXEMPLO_SUMMARY = prom.Summary('exemplo_summary', 'Random number between 1 - 100')
EXEMPLO_HISTOGRAM = prom.Histogram('exemplo_histogram', 'Random number between 1 - 100')

def generate_random_numbers():
    while True:
        random_number = randrange(10)
        EXEMPLO_COUNTER.inc(random_number)
        EXEMPLO_GAUGE.set(random_number)
        EXEMPLO_SUMMARY.observe(random_number)
        EXEMPLO_HISTOGRAM.observe(random_number)
        time.sleep(5)

if __name__ == '__main__':
    prom.start_http_server(8000)
    generate_random_numbers()
