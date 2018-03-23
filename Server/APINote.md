## 注册
```json 
{
    "ID": Integer, # 学号（正整数、唯一且不为空）
    "name": Char(max_length = 50), # 姓名
    "password": Char(max_length = 50), # 密码（非空）
    "email": Email, # 邮箱（非空）
    "mPhone": Char(max_length = 20), # 手机号
    "userType": ("SD" or "TR"), # 用户类型
    "status": false, # 自动生成
    "actiCode": "NULL", # 自动生成
    "tokenExptime": "2018-03-14T02:39:17.113783Z" # 自动生成
}
```
- API `POST url/register/`

