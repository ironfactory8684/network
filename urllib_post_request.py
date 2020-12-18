from urllib import parse, request

data = {'temperature':'25C','humidity':'60%'} #POST 내용
encoded_data = parse.urlencode(data).encode('utf-8') # POST query 구성(서브URL)
url = "http://localhost:8080"
resp = request.urlopen(url, encoded_data)# POST request 서버 응답
print(resp.read().decode('utf-8'))#응답 내용 출력