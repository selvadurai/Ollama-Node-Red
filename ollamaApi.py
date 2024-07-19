import http.client

conn = http.client.HTTPConnection("192.168.0.88:1880")

payload = "{ \n\t\"prompt\":\"Discharge Temp is higher  Discharge temp Set point in hvac AHU. Is the AHU operating correctly? If not what are the possible causes? \" \n}"

headers = { 'Content-Type': "application/json" }

conn.request("POST", "/ollama1", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
