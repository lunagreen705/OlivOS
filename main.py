# -*- encoding: utf-8 -*-
'''
_______________________    ________________
__  __ \__  /____  _/_ |  / /_  __ \_  ___/
_  / / /_  /  __  / __ | / /_  / / /____ \
/ /_/ /_  /____/ /  __ |/ / / /_/ /____/ / 
\____/ /_____/___/  _____/  \____/ /____/

@File      :   main.py
@Author    :   lunzhiPenxil仑质
@Contact   :   lunzhipenxil@gmail.com
@License   :   AGPL
@Copyright :   (C) 2020-2025, OlivOS-Team
@Desc      :   None
'''

# here put the import lib
import os
import json
import OlivOS

def load_config(config_path):
    """ 加載配置文件並返回端口設置 """
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

if __name__ == '__main__':
    if not os.path.exists('./conf'):
        os.makedirs('./conf')

    # 加載基本配置
    config = load_config('./conf/basic.json')
    
    # 從環境變數 PORT 獲取端口，默認為 10000（Render 默認端口）
    port = int(os.environ.get("PORT", 10000))

    # 启动 OlivOS 应用，并将端口配置传递
    OlivOS.bootAPI.Entity(
        basic_conf='./conf/basic.json'
    ).start(host="0.0.0.0", port=port)
