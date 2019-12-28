# todo 生成数据库表结构的时候执行manager.py文件
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager
from apps import app

from apps.model import db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

"""
# 初始化映射仓库 （第一次时，直接执行如下的命令）  此db与第11行的db对应
# python manager.py db  init  
# 
# # 生成映射脚本
python manager.py db migrate

# 映射数据库
python manager.py db upgrade

# 如果更新了model.py模型里面的字段或其他地方，只需执行18和21行的命令即可

"""

if __name__ == '__main__':
    manager.run()