import http.client

conn = http.client.HTTPConnection("<IP GOES HERE>")

payload = "{ \n\t\"prompt\":\"What color is the sky? \" \n}"

headers = { 'Content-Type': "application/json" }

conn.request("POST", "/ollama", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
