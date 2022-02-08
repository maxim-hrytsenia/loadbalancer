import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from collections import Counter
from advanced_load_balancer import AdvancedLoadBalancer
from config import server_ids
import time


class TestAdvancedLoadBalancer:
    def test_distribution(self):
        lb = AdvancedLoadBalancer(server_ids)
        number_of_requests = 100000
        counter = Counter()
        for _ in range(number_of_requests):
            counter[lb.send_request()] += 1
        expected_requests = int(number_of_requests / len(server_ids))
        # check that load is distributed to all servers
        assert(len(counter) == len(server_ids))
        min_requests = min(counter.values())
        max_requests = max(counter.values())
        # check that the load in persentage points does not differ between server 
        # with the minimum and maximum number of requests
        assert(abs(min_requests - expected_requests) / expected_requests < 0.01)
        assert(abs(max_requests - expected_requests) / expected_requests < 0.01)


    def test_requests_cleaning(self):
        lb = AdvancedLoadBalancer(server_ids)
        number_of_requests = 100000
        for _ in range(number_of_requests):
            lb.send_request()
        assert(sum(lb.load) > 0)
        time.sleep(10)
        assert(sum(lb.load) == 0)
    