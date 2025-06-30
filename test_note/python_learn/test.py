import mysql.connector

class DatabaseOperations:
    """数据库操作类"""
    
    def __init__(self, host, user, password, database):
        """初始化数据库连接"""
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()
    
    def close(self):
        """关闭数据库连接"""
        self.cursor.close()
        self.connection.close()
    
    def execute_query(self, query):
        """执行查询语句"""
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def execute_update(self, query):
        """执行更新语句"""
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.rowcount
    
    def create_table(self, table_name, columns):
        """创建表"""
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.execute_update(query)
    
    def insert_data(self, table_name, columns, values):
        """插入数据"""
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        return self.execute_update(query)
    
    def select_data(self, table_name, columns="*", condition=None):
        """查询数据"""
        query = f"SELECT {columns} FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        return self.execute_query(query)