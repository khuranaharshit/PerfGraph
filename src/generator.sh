#!/bin/bash

# Script to generate load on the endpoints

for endpoint in quadratic_time factorial_time nlogn_time logn_time linear_time constant_time
do
    echo -en "[*] Executing $endpoint in background... \n"
    curl -s "http://localhost:8000/${endpoint}" > /dev/null &
done

# Wait for all background processes to complete
wait

echo "[*] All requests completed."
