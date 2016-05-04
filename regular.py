import re

def getCountSql(sql):
    wbol = re.search("where", sql, flags=re.IGNORECASE)
    lbol = re.search("limit", sql, flags=re.IGNORECASE)
    restr = 'select(?P<c>.*)from(?P<t>.*)'
    if wbol:
        restr = restr+'where(?P<w>.*)'
    if lbol:
        restr = restr+'limit(?P<l>.*)'

    m = re.match(restr, sql, flags=re.IGNORECASE)
    if wbol:
        sql = 'select count(*) from ' + m.group("t") + ' where ' + m.group("w")
    else:
        sql = 'select count(*) from ' + m.group("t")
    return sql

print(getCountSql("select DISTINCT(ts),count(*) as a from abcd where a=b group by abc limit 1 offset 10"))


