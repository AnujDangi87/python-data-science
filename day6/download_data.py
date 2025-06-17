from pyodide.http import pyfetch

import pandas as pd

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt"
filename = "example1.txt"

async def download(url, filename):
    response = await pyfetch(url)

    if(response.status == 200):
        with open(filename, "wb") as f:
            f.write(await response.byte())

download(url, filename)

print("Done")