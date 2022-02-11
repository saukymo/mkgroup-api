# from datetime import datetime
from flask import render_template, request
from run import app
# from wxcloudrun.dao import delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid
# from wxcloudrun.model import Counters
# from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response
from wxcloudrun.response import make_succ_response, make_err_response


scripts = [
    {
        "id": 1,
        "author": "平民大侦探实景探案馆",
        "cover": "https://cdn.qiandaoapp.com/cloudbase-cms/upload/init/竹罄南山2.jpg",
        "desc": "陇州中心有一青竹山，山两端以双色竹子而闻名，半山通红，半山翠绿，更有传闻青竹山上每晚有绿色鬼火。附近村民夜不出户。而陇州刺史董山明在青竹山南边山脚小南山地区上盖了一座青竹山在。今天是董山明的七十大寿，来贺寿者众多，就连旁边废弃的道观也跟着热闹了起来",
        "duration": 3.5,
        "name": "竹罄南山",
        "quorum": {
            "female": 2,
            "male": 5,
            "total": 7
        },
        "tags": [
            "古代",
            "开放",
            "剧情",
            "江湖"
        ],
        "type": "独家",
        "xgender": True
    },
    {
        "id": 2,
        "author": "玄学探案工作室",
        "cover": "https://cdn.qiandaoapp.com/cloudbase-cms/upload/init/雪上梅色2.jpg",
        "desc": "今日早晨，天刚蒙蒙亮的时候，因着昨日里赏梅大会让梅林里人太多了，于是有下人一大早起来前去梅林里打扫，忽然，下人发现了有一块地方的雪鼓鼓的很奇怪，上面的落的胭脂梅花瓣也比其他地方要稠密许多。下人好奇的走过去，发现厚厚的白雪地中露出了一角女人衣物，下人扯了扯，瞬时掀起了一地胭脂梅与点点白雪，洋洋洒洒在空中飞舞继而落至一旁，下人看着眼前的半截女尸，认出来，这是二小姐梅月希穿的衣服。大家再赶到梅月希房间时，大小姐梅月霖已紧跟着赶了过来，大家发现她房间门半掩着，里面的床上赫然躺着上半截的尸身...",
        "duration": 3,
        "name": "雪上梅色",
        "quorum": {
            "female": 3,
            "male": 3,
            "total": 6
        },
        "tags": [
            "还原",
            "开放",
            "武侠",
            "变格"
        ],
        "type": "独家",
        "xgender": True
    }
]

@app.route('/scripts')
def get_all_scripts():
    return make_succ_response(scripts)

@app.route('/scripts/<int:script_id>')
def get_script_by_id(script_id: int):
    if script_id <= 2:
        return make_succ_response(scripts[script_id])
    else:
        return make_err_response("剧本id没有找到.")

# @app.route('/')
# def index():
#     """
#     :return: 返回index页面
#     """
#     return render_template('index.html')


# @app.route('/api/count', methods=['POST'])
# def count():
#     """
#     :return:计数结果/清除结果
#     """

#     # 获取请求体参数
#     params = request.get_json()

#     # 检查action参数
#     if 'action' not in params:
#         return make_err_response('缺少action参数')

#     # 按照不同的action的值，进行不同的操作
#     action = params['action']

#     # 执行自增操作
#     if action == 'inc':
#         counter = query_counterbyid(1)
#         if counter is None:
#             counter = Counters()
#             counter.id = 1
#             counter.count = 1
#             counter.created_at = datetime.now()
#             counter.updated_at = datetime.now()
#             insert_counter(counter)
#         else:
#             counter.id = 1
#             counter.count += 1
#             counter.updated_at = datetime.now()
#             update_counterbyid(counter)
#         return make_succ_response(counter.count)

#     # 执行清0操作
#     elif action == 'clear':
#         delete_counterbyid(1)
#         return make_succ_empty_response()

#     # action参数错误
#     else:
#         return make_err_response('action参数错误')


# @app.route('/api/count', methods=['GET'])
# def get_count():
#     """
#     :return: 计数的值
#     """
#     counter = Counters.query.filter(Counters.id == 1).first()
#     return make_succ_response(0) if counter is None else make_succ_response(counter.count)
