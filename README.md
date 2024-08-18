## PerfGraph: **Algorithm Time Complexity Visualization and Scalability Analysis**

### Objective:
- The project helps to visualise the effect of application logic on end to end latency and scalability of the application using Grafana.

### Components:
1. **k8s Setup:**
   - Use `kind` (or `k3ds`, `minikube` etc) to create a local Kubernetes cluster, providing a controlled environment for deploying the app.

2. **Backend API**
   - FasAPI frontend to provide different APIs.
   - Each endpoint will trigger the execution of the algorithm and measure the execution time.

3. **Visualisation Metrics:**
   - ***Prometheus*** with the API to scrape and collect metrics on:
     - Execution latency of each algorithm
     - "N" used for execution of algo
   - ***Grafana*** dashboard to visualize the collected metrics -
     - Execution time of each algorithm wrt "N"

### Internals

### Tools Used:
- `rye` for package management for Python
- `prometheus` for metrics capturing and exporting
- `grafana` for metrics dashboarding and visualisation

### Testing Steps
- Follow the below steps to get it up and running:- 
  - TODO: Add Steps

### Temp Steps
- Run Prometheus
   `docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus`
- Run Grafana
   `brew services start grafana`