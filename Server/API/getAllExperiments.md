# 获取全部实验
API: GET address/api/experiment/all/

---
## 返回值：
- list，每一个元素为一个Json文件
```Json
{
    "priority": priority,
    "Title": title,
    "description": description,
    "expermentScore": maxScore,
    "clientView": clientView,
    "reportTemplete": reportTemplete,
    "owner": owner
}
```

---
## 参数解释：
- priority: 实验优先级，0～5之间的一个整数
- Title: 实验题目，一个字符串，Unicode编码
- description: 实验描述，长文本，字符串。MarkDown语法
- maxScore: 实验满分，一个正整数
- clientView: 学生端界面描述，用于记录需要采集那些数据，用Json记录
- reportTemplete: 实验数据模版，用于生成实验数据
- owner: 实验的创建者

---
## 权限：
创建者可以修改，非创建者只读

---
## 示例:
```Python
[
    {
        "priority": 3,
        "Title": "# This is test0",
        "description": "# This is test0",
        "expermentScore": 0,
        "clientView": "# This is test0",
        "reportTemplete": "# This is test0",
        "owner": 16031160
    },
    {
        "priority": 5,
        "Title": "# This is test0",
        "description": "userInfo.userType == 'TR'",
        "expermentScore": 3,
        "clientView": "userInfo.userType == 'TR'",
        "reportTemplete": "userInfo.userType == 'TR'",
        "owner": 16031160
    },
    {
        "priority": 1234,
        "Title": "1234",
        "description": "1234",
        "expermentScore": 1234,
        "clientView": "1234",
        "reportTemplete": "1234",
        "owner": 16031161
    }
]
```