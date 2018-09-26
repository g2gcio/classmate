import dataset

db = dataset.connect('sqlite:///sgtalk.db')

authors = db['authors'].all()
num = 1

for a in authors:
   print("%5d" % num, "%25s" % a['name'],a['article'])
   num = num+1

num=1
result = db.query('SELECT * FROM authors ORDER BY name')
for a in result:
   print("%5d" % num, "%25s" % a['name'],a['article'])
   num = num+1
