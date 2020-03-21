#파일 불러오기
#파일 헥스값 변환
#jpg 파일이 있는가 헤더 등으로 검색
#위치를 찾고 복사해서 보완
#파일 하나로 지정해서 저장
import binascii
import sys

with open('test.docx','rb') as f:

    rdata = f.read()
data = str(binascii.hexlify(rdata)).upper()

if 'FFD8' in data:
    a=data.count('FFD8')
    print( " %d jpg is in it!"%a)
    
else :
    print('no!')
    sys.exit(0)
startp = data.find('FFD8')
try:
    endp = data.find('FFD9')
except : print("Where is the \'FF D9\'??")
content = binascii.unhexlify(data[startp:endp+4])
contentf=open('answer.jpg','wb')
contentf.write(content)
contentf.close()
