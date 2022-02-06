from LoadBalancer import LoadBalancer
from config import server_ids


def main():
    lb = LoadBalancer(server_ids)
    print(lb.send_request())
    print(lb.send_request())


if __name__ == "__main__":
    main()