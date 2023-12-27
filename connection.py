import pymssql
serverName = '127.0.0.1'
userName = 'sa'
passWord = '123456'
# 使用 GBK 编码连接到数据库
conn = pymssql.connect(serverName, userName, passWord, "plant", charset='GBK',tds_version="7.0")
cursor = conn.cursor()
sql = "SELECT * FROM [市]=%s"
cursor.execute(sql)
#for row in cursor:
 #   print("Sno=%s, Sn=%s, Gender=%s, Class=%s, Birth=%s, Number=%s" %
  #       (row[0].strip(), row[1], row[2].strip(), row[3], row[4], row[5]))
conn.close()