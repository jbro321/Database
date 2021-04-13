import pymysql # pymysql 임포트

# 전역변수 선언부
conn = None
cur = None

data1 = ""
data2 = ""
data3 = ""
data4 = ""

sql=""

# 메인 코드
conn = pymysql.connect(host='127.0.0.1', user='root', password='99022807', db='pythondb', charset='utf8')
cur = conn.cursor()

while (True) : # break를 만날때까지 계속 반복
    data1 = input("사용자 ID를 입력하세요(엔터 클릭 시 종료): ") # data1변수에 ID 입력받기
    if data1 == "" : # 만약 data1에 아무값도 입력받지 않는다면
        break; # break;로 while문을 떠남
    data2 = input("사용자 이름을 입력하세요: ")
    data3 = input("사용자 이메일을 입력하세요: ")
    data4 = input("사용자 출생연도를 입력하세요: ")
    sql = "INSERT INTO userTable VALUES(" + data1 + "," + data2 + "," + data3 + "," + data4 + ")" # sql변수에 INSERT SQL문 입력
    cur.execute(sql) # 커서로sql 실행

conn.commit() # 최종 저장
conn.close() # 접속 종료










































