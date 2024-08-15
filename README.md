<div align="center">

# CloudPeak OA (Backend)

✨ 开放源代码的办公自动化软件✨

![License Anti 996](https://img.shields.io/badge/license-Anti996-red)
![License LGPL 3.0](https://img.shields.io/badge/license-LGPL3.0-blue)
![Code Style Black](https://img.shields.io/badge/code%20style-black-000000.svg?logo=python&logoColor=edb641)
![Type Pyright](https://img.shields.io/badge/types-pyright-797952.svg?logo=python&logoColor=edb641)
![Linting Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)

![Auth Fief](https://img.shields.io/badge/auth-fief-red)
![Database Mongodb](https://img.shields.io/badge/database-mongodb-green)
![HTTP FastAPI](https://img.shields.io/badge/http-FastAPI-blue)

</div>

## 简介

CloudPeak OA 是**我的世界中国版网络游戏 云上之巅（PE） 开发团队**内部使用的一款**办公自动化**软件，使用 FastAPI 框架和 Mongodb 数据库构建，由 Fief 提供简单易配置的身份验证功能。

## 功能

Work In Progress...

## 特色

* 权限管理：均由外部程序提供，支持多应用互通，简单易用安全可靠。
* 便于对接：提供对外的 API 接口，方便和其它程序对接。
* 文件管理：使用 Mongodb GridFS 管理文件，不提供列出文件接口，管理仅可通过 `_id` 实现，防止文件意外泄露。
* 接口文档：得益于 FastAPI 的强大功能，接口文档自动生成，方便查看和调试。

## 快速部署

Work In Progress...

## 注意事项

### 许可证相关

CloudPeak OA 使用 LGPL-3.0 和 Anti-996 许可证，在使用本程序时，请注意以下几点：

* 在修改 CloudPeak OA 的相关代码后，请及时公布；
* 在使用 CloudPeak OA 时，您必须遵守您所在司法管辖区的相关劳动法律法规，如果没有相关法律法规，请参照有关国际公约执行；
* 其它详情请参见许可证原文。