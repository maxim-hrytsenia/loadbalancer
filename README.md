# Load balancer


This is the project to create a load balancer. 

# Testing

From the main directory run 
```
pytest -q src/tests/test_load_balancers.py -s
```

# Running the application

From the main directory run 
```
python src/main.py
```

# Tricks

The code contains a config file with server names and a file with a factory method for easier initialization of Load Balancer instances.

The advanced load balancer(objective 2) inherits the load balancer(objective 1).