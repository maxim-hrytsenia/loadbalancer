class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.current_server = 0
        self.n_servers = len(servers)


    def send_request(self):
        response =  self.servers[self.current_server]
        self.current_server = (self.current_server + 1) % self.n_servers
        return response