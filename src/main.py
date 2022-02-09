from config import server_ids, type
from load_balancer_factory import LoadBalancerFactory


def main():
    lb = LoadBalancerFactory().get_factory(type, server_ids)
    print(lb.send_request())


if __name__ == "__main__":
    main()