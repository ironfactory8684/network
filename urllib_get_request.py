from urllib import parse, request

data = {'temperature':'25C','humidity':'60%'} #query를 딕셔너리로 표현
encoded_data = parse.urlencode(data) # 딕셔너리로부터  query URL 생성
print("Encoded: ", encoded_data)
url = "http://localhost:8080/?"+encoded_data
resp = request.urlopen(url)# GET request 서버 응답
print(resp.read().decode('utf-8'))#응답 내용 출력