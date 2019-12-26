from flask import Flask
from apps import config  # 导入配置文件

app = Flask(__name__)

# todo 加载配置文件
app.config.from_object(config)

# 注册蓝图
from apps.goods import good as good_blueprint
app.register_blueprint(good_blueprint)