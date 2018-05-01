# 用户登录
API: POST address/api/login 
```Json
{
    "username": userid,
    "password": password
}
```

---
## 返回值：
- `HTTP 406 Not Acceptable` 用户验证不通过（未注册或错误的用户名密码）
- `HTTP 202 Accepted` 用户验证通过

---
## 参数解释：
见注册

---
## 示例:
```Json
{
    "username": "16111111",
    "password": "12345678"
}
```
