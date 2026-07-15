import requests

# Download Mauna Loa CO2 data
url = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt"
response = requests.get(url)
if response.status_code == 200:
    with open("co2_mm_mlo.txt", "wb") as f:
        f.write(response.content)
    print("Mauna Loa CO2 data downloaded successfully.")