# TPShop API 自动化测试框架

## 项目简介

基于 Python + Pytest + Requests + Allure 搭建的接口自动化测试框架。

项目以 TPShop 电商系统为测试对象，实现了登录、商品、购物车、订单等核心业务接口的自动化测试，并支持数据驱动、数据库断言、测试报告生成等功能。

---

## 技术栈

* Python 3.12
* Pytest
* Requests
* Allure Report
* MySQL
* PyYAML
* OpenPyXL
* Git
* GitHub

---

## 项目结构

```text
api/
├── login_api.py
├── goods_api.py
├── cart_api.py
└── order_api.py

common/
├── request_util.py
├── response_util.py
├── assert_util.py
├── db_util.py
├── yaml_util.py
├── excel_util.py
└── log_util.py

conf/
└── config.yaml

data/
├── order_data.yaml
└── order_data.xlsx

testcases/
├── conftest.py
├── test_login.py
├── test_goods.py
├── test_cart.py
├── test_order_submit.py
└── test_order_detail.py

.github/
└── workflows/

README.md
requirements.txt
```

---

## 已实现功能

### 接口封装

* 登录接口
* 商品接口
* 购物车接口
* 订单接口

### 框架能力

* BaseApi 二次封装
* Session 会话保持
* 公共请求工具封装
* 日志记录
* 数据库操作封装

### 数据驱动

* Excel 数据驱动
* YAML 数据驱动
* Pytest 参数化

### 断言体系

* AssertUtil 封装
* 数据库断言
* 接口返回断言

### 测试报告

* Allure 测试报告
* 测试步骤展示
* 附件信息展示

---

## 业务流程覆盖

实现完整电商下单流程自动化：

用户登录

↓

加入购物车

↓

查询购物车

↓

选中商品

↓

提交订单

↓

数据库校验订单信息

---

## 运行方式

安装依赖：

```bash
pip install -r requirements.txt
```

执行测试：

```bash
pytest -vs
```

生成 Allure 数据：

```bash
pytest --alluredir=report
```

查看 Allure 报告：

```bash
allure serve report
```

---

## 项目亮点

* 基于 Pytest Fixture 实现业务流程复用
* 支持 YAML 数据驱动测试
* 支持数据库自动校验
* 支持 Allure 可视化报告
* 支持 GitHub 版本管理
* 采用分层设计思想，提高代码复用性和可维护性

---

## 作者

简旭杰
