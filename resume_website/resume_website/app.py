from flask import Flask, render_template

app = Flask(__name__)

user = {
    "name": "张磊奇",
    "gender": "男",
    "age": 21,
    "phone": "18251216068",
    "email": "2845926709@qq.com",
    "address": "江苏省溧阳市景盛苑",
    "political": "群众",

    "education": {
        "school": "徐州医科大学",
        "major": "智能医学工程专业",
        "degree": "本科",
        "time": "2023.09-2027.06",
        "courses": "python，机器学习和模式识别等",
        "desc": "成绩良好，态度端正，扎实掌握专业基础知识"
    },

    "campus": [
        {
            "time": "2023.09-2024.06",
            "title": "校科学技术协会社员",
            "desc": "协助校科协举办活动进行顺利，锻炼沟通协调与组织能力，做事认真负责。"
        },
        {
            "time": "2024.9",
            "title": "校园迎新志愿活动",
            "desc": "积极参与校园实践与志愿服务，吃苦耐劳，有集体荣誉感，具备良好团队协作意识。"
        }
    ],

    "practice": [
        {
            "time": "2024.7-2024.8",
            "title": "小区社区进行社会实践",
            "desc": "协助小区活动，提升执行力与人际交往能力，做事踏实细心，遵守规章制度，适应能力强。"
        }
    ],

    "skills": {
        "language": "普通话标准，英语基础良好",
        "office": "熟练使用 Word、Excel、PPT 等办公软件",
        "cert": "驾驶证、计算机二级、英语四级等"
    },

    "research": [
        "基于蛋白质语言模型与深度-核动态集成的抗 HIV 多肽预测系统V1.0软著申请中",
        "基于自然语言技术实现的智能语义查重系统V1.0软著申请中"
    ],

    "evaluation": "本人性格开朗稳重，待人真诚友善，学习态度端正，上进心强。在校认真完成学业，积极参与各类实践活动，具备良好的沟通能力、团队意识与抗压能力。做事踏实靠谱，执行力强，能够快速适应工作环境，虚心学习新知识，对待工作认真负责，愿意脚踏实地稳步成长。"
}

@app.route('/')
def index():
    return render_template("index.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)
