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
- TODO: Fix docker networking for below steps
- Follow the below steps to get it up and running:- 
1. Start prometheus
   ```bash
   $ docker run --name prometheus \
    --mount type=bind,source=./observability/prometheus.yml,destination=/etc/prometheus/prometheus.yml \
    -p 9090:9090 \
    --add-host host.docker.internal=host-gateway \
    prom/prometheus
   ```

2. Start grafana
   ```bash
   $ docker run -p 3000:3000 --add-host host.docker.internal=host-gateway --name grafana grafana/grafana
   ```

3. Setup Grafana
   1. Open grafana dashboard `http://localhost:3000` login with default creds (username/password: "admin")
   2. On the left pane, goto **Connection** then **Data Sources**.
   3. Scroll down to *Prometheus URL* add http://localhost:9090. Scroll down, click on "Save & Test".
   4. Once saved, copy the uid from the URL. Eg: url=`http://localhost:3000/connections/datasources/edit/abcd`. datasource UID =`abcd`
   5. Update the datasource-uid present in the `observability/grafana/dashboard.json`
      ```bash
      $ export OLD_DS_UID="bdv752eo8vwu8d"  # hard-coded in dashboard.json
      $ export NEW_DS_UID="abcd"
      $ ./scripts/grafana_datasource.sh $OLD_DS_UID $NEW_DS_UID 
      ```

4. Run the app - `python3 src/perfgraph/app.py`
5. On a separate terminal, run the generator script responsible to generate traffic on backend - `./scripts/generator.sh`
   - This could take upto a minute to complete

6. Once completed head over to Grafana on `http://localhost:3000/dashboard/import` and upload dashboard JSON file present under `observability/grafana/dashboard.json` & refresh
