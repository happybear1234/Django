# 更新日志
## 2020.12.4
- 马氏，设备参数页面增加选择框功能和请选择内容提示框
- 马氏页面所有系统显示图响应组件改为按钮
## 2020.12.3
- 修改年度图像时间选择器只展示年份
- 修改加载图像数据get请求和传递时间输入框/选项框数据post请求共用一个URL
- 增加‘查询失败’，‘请选择时间’提示模态框
- 增加前台返回ajax状态码200
- 新增系统可用度评估页面
- 图像增加滑动条
- 修正选项框内容和图像配置加载参数
- 修改图配置：滑动条位置，折线图符号大小和X轴标签大小


# 项目目录说明
```
/home/user/Projects/CShip
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   └── blog/
│   │       └── calculation.html
│   └── static/
│   │   ├── css/
│   │   ├── image/
│   │   ├── js/
│       └── plugin/
│
├── instance/
│ 
├── tests/
│   └── app.py
├── .gitignore
└── requirements.txt
```

[详细请查看文档](https://dormousehole.readthedocs.io/en/latest/tutorial/layout.html)

- `__init__.py`:配置文件

- `db.py`:数据库链接，操作

- `schema.sql`：sql语句

- `templates/`：模板，base.html整个主页作为母页，calculation为计算条件输入页面

- `static/`： 静态文件

- `instance`: 实例文件夹，放置运行时更改的文件和配置文件[详细](http://docs.jinkan.org/docs/flask/config.html#instance-folders)

- `tests/`： 测试文件不用管

- `.gitignore`:里面保存git命令push时会自动忽略掉的文件

- `requirements.txt`： 保存该项目需要用到的包，`pip >freeze requirements.txt`会更新该文档，使用命令`pip install -r requirements.txt`会一次性安装里面所有包
