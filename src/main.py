from LoadBalancer import LoadBalancer
from config import server_ids
from AdvancedLoadBalancer import AdvancedLoadBalancer
import time


def main():
    lb = AdvancedLoadBalancer(server_ids)
    print(lb.send_request())
    print(lb.send_request())
    print(lb.send_request())
    print(lb.send_request())
    print(lb.send_request())
    print(lb.send_request())
    print(lb.send_request())
    print(lb.send_request())
    print(lb.send_request())
    print(lb.send_request())
    print(lb.send_request())
    print(lb.send_request())
    print(lb.send_request())
    print(lb.send_request())
    print(lb.send_request())
    print(lb.send_request())
    print(lb.send_request())
    print(lb.send_request())
    print(lb.send_request())
    print(lb.send_request())
    print(lb.load)
    time.sleep(1)
    print(lb.load)
    time.sleep(1)
    print(lb.load)
    time.sleep(1)
    print(lb.load)
    time.sleep(1)
    print(lb.load)
    time.sleep(1)
    print(lb.load)
    time.sleep(1)
    print(lb.load)
    time.sleep(1)
    print(lb.load)
    time.sleep(1)
    print(lb.load)


if __name__ == "__main__":
    main()