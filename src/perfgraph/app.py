import os
from perfgraph.algorithms import *
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse
import uvicorn

APP_PORT = os.environ.get("APP_PORT", 8000)

app = FastAPI()

array = [2,
6,
8,
9,
10,
10,
11,
100,
100,
100,
100,
100,
1000,
1000,
1000,
1000,
1000,
5000,
10000,
10000,
10000,
10000,
10000,
100000,
100000,
100000,
100000,
200000,
200000,
200000,
500000,
500000,
500000,
1000000,
1000000,
1000000,
10000000,
10000000,
100000000,
100000000,
500000000,
1000000000]

array_dict = {elem: list(range(elem)) if elem <= 100_000 else range(elem) for elem in array}

@app.get("/")
def redirect_root():
    return RedirectResponse(url="/home")

def execute_algorithm(algorithm, array_sizes, description):
    count = 0
    for array_size in array_sizes:
        array = array_dict.get(array_size)
        algorithm(array)
        count += 1

    return f"<html>Executed {description} {count} times</html>"

@app.get("/constant_time")
def read_constant_time():
    nsizes = [100, 1_000, 10_000, 100_000, 200_000, 500_000, 1_000_000, 10_000_000, 100_000_000, 1_000_000_000]
    return HTMLResponse(content=execute_algorithm(constant_time, nsizes, "Constant time algorithm"))

@app.get("/logn_time")
def read_logn_time():
    nsizes = [100, 1_000, 10_000, 100_000, 200_000, 500_000, 1_000_000, 10_000_000, 100_000_000, 500_000_000]
    return HTMLResponse(content=execute_algorithm(logn_time, nsizes, "Logarithmic time algorithm"))

@app.get("/linear_time")
def read_linear_time():
    nsizes = [100, 1_000, 10_000, 100_000, 200_000, 500_000, 1_000_000]
    return HTMLResponse(content=execute_algorithm(linear_time, nsizes, "Linear time algorithm"))

@app.get("/nlogn_time")
def read_nlogn_time():
    nsizes = [100, 1_000, 10_000, 100_000]
    return HTMLResponse(content=execute_algorithm(nlogn_time, nsizes, "NLogN time algorithm"))

@app.get("/quadratic_time")
def read_quadratic_time():
    nsizes = [10, 100, 1_000, 5_000, 10_000]
    return HTMLResponse(content=execute_algorithm(quadratic_time, nsizes, "Quadratic time algorithm"))

@app.get("/factorial_time")
def read_factorial_time():
    nsizes = [2, 6, 8, 9, 10, 11]
    return HTMLResponse(content=execute_algorithm(factorial_time, nsizes, "Factorial time algorithm"))

@app.get("/home")
def read_home():
    links = """
    <html>
        <body>
            <div class="container">
                <h2>Available Algorithms:</h2>
                <ul>
                    <li><a href='/constant_time'>Constant Time</a></li>
                    <li><a href='/logn_time'>Logarithmic Time</a></li>
                    <li><a href='/linear_time'>Linear Time</a></li>
                    <li><a href='/nlogn_time'>NLogN Time</a></li>
                    <li><a href='/quadratic_time'>Quadratic Time</a></li>
                    <li><a href='/factorial_time'>Factorial Time</a></li>
                </ul>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=links)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=APP_PORT)