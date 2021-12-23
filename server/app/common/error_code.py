# -*- coding: utf-8 -*-
"""
=======================================
Filename: error_code
Description: error code type about Yogurt
=======================================
"""
OP_SUCCESS = 200
THROW_EXP = 1000
OP_DB_FAILED = 1001

ERR_CODE = {
    OP_SUCCESS: '操作成功',
    THROW_EXP: '抛出异常',
    OP_DB_FAILED: '数据库请求失败'
}