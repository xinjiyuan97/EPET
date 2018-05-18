# 用户个人信息完善
API: GET, PUT address/api/register
```Json
{
    "id": id,
    "username": userid,
    "name": Name,
    "email": userEmail,
    "mPhone": phone,
    "userType": userType,
    "status": false,
    "actiCode": "NULL",
    "tokenExptime": "2018-04-13T12:53:06.662854Z"
}
```

---
## 参数解释：
- id: 数据库内置参数，不可修改
- username: 用户学号，非空，字符串
- name: 用户姓名，不超过20个字符，必填
- email: 用户邮箱，必须满足邮箱格式，必填
- mPhone: 用户手机号，长度不超过20，字符串，非空
- userType: 用户类型，置选SD，修改无效
- status: 用户是否进行邮箱注册，修改无效
- actiCode: 用户验证码，自动生成，修改无效
- tokenExptime: 用户验证过期时间，1天，修改无效

---
## 示例:
```Json
{
    "id": 16031171,
    "username": "16031171",
    "name": "童化金",
    "email": "abc@163.com",
    "mPhone": "12345678",
    "userType": "SD",
    "status": false,
    "actiCode": "NULL",
    "tokenExptime": "2018-04-20T14:50:21.282862Z"
}
```

---
## 说明：
需要相应用户权限进行处理