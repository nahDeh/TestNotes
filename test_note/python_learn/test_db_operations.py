import pytest
import mysql.connector
from test import DatabaseOperations

# 测试数据库配置
TEST_DB_CONFIG = {
    'host': 'localhost',
    'user': 'test_user',
    'password': 'test_password',
    'database': 'test_db'
}

@pytest.fixture(scope="module")
def setup_test_db():
    """设置测试数据库环境"""
    # 创建测试数据库连接
    conn = mysql.connector.connect(
        host=TEST_DB_CONFIG['host'],
        user=TEST_DB_CONFIG['user'],
        password=TEST_DB_CONFIG['password']
    )
    cursor = conn.cursor()
    
    # 创建测试数据库
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {TEST_DB_CONFIG['database']}")
    cursor.close()
    conn.close()
    
    # 创建数据库操作对象
    db = DatabaseOperations(**TEST_DB_CONFIG)
    
    # 创建测试表
    db.create_table('test_users', 
                   'id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), age INT')
    
    yield db  # 提供数据库操作对象给测试用例
    
    # 测试完成后清理
    db.execute_update("DROP TABLE test_users")
    db.close()

def test_insert_and_select(setup_test_db):
    """测试插入和查询操作"""
    db = setup_test_db
    
    # 插入测试数据
    affected_rows = db.insert_data('test_users', 'name, age', "'张三', 25")
    assert affected_rows == 1
    
    affected_rows = db.insert_data('test_users', 'name, age', "'李四', 30")
    assert affected_rows == 1
    
    # 查询并验证数据
    results = db.select_data('test_users')
    assert len(results) == 2
    
    # 条件查询
    results = db.select_data('test_users', condition="age > 25")
    assert len(results) == 1
    assert results[0][1] == '李四'  # 第二列是name
    assert results[0][2] == 30      # 第三列是age

def test_update_and_delete(setup_test_db):
    """测试更新和删除操作"""
    db = setup_test_db
    
    # 更新数据
    affected_rows = db.execute_update("UPDATE test_users SET age = 26 WHERE name = '张三'")
    assert affected_rows == 1
    
    # 验证更新结果
    results = db.select_data('test_users', condition="name = '张三'")
    assert results[0][2] == 26  # 验证年龄已更新
    
    # 删除数据
    affected_rows = db.execute_update("DELETE FROM test_users WHERE name = '李四'")
    assert affected_rows == 1
    
    # 验证删除结果
    results = db.select_data('test_users')
    assert len(results) == 1