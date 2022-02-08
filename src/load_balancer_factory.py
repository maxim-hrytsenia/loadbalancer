from advanced_load_balancer import AdvancedLoadBalancer
from load_balancer import LoadBalancer

class LoadBalancerFactory:
    def get_factory(self, type, servers):
        if type == "task2":
            return AdvancedLoadBalancer(servers)
        elif type == "task1":
            return LoadBalancer(servers)
        else:
            raise ValueError(type)

        