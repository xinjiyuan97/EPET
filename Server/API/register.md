# 用户注册
API: POST address/api/register
```Json
{
    "username": userID,
    "password": Password
}
```

---
## 参数解释：
userID: 用户学号（唯一），字符串类型
Password: 用户密码，非空，不超过20位字符串类型
---

## 示例:
```Json
{
    "username": "16031171",
    "password": "12345678"
}
```
