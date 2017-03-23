from random import randint


def colored_message(message):
    return '\033[0;{};01m{message}\033[0m'.format(randint(30, 37), message=message)


class Resume:
    def __str__(self):
        return '***的简历'

    def show(self):
        print(colored_message('基本信息:'))
        for k, v in self.basic:
            print('\t{}: {}'.format(k.ljust(12), v))

        print(colored_message('毕业学校:'))
        for k, v in self.collage:
            print('\t{}: {}'.format(k.ljust(12), v))

        print(colored_message('工作经历:'))
        for index, career in enumerate(self.career):
            print(colored_message('\t[{}]:'.format(index + 1)))
            for k, v in career:
                print('\t{}: {}'.format(k.ljust(12), v))

        print(colored_message('项目经历:'))
        for index, project in enumerate(self.projects):
            print(colored_message('\t[{}]:'.format(index + 1)))
            for k, v in project:
                print('\t{}: {}'.format(k.ljust(12), v))

        print(colored_message('个人技能:'))
        for index, skill in enumerate(self.skills):
            print(colored_message('\t[{}]:'.format(index + 1)))
            for k, v in skill:
                print('\t{}: {}'.format(k.ljust(12), v))

    @property
    def basic(self):
        return [('name', '***'),
                ('sex', '男'),
                ('birthday', '1993'),
                ('phone', '176*********'),
                ('email', 'gaojiuli@gmail.com'),
                ('address', '四川成都'),
                ('github', 'https://github.com/gaojiuli'),
                ('blog', 'https://segmentfault.com/blog/xiuxian')]

    @property
    def collage(self):
        return [('school', '西南交通大学'),
                ('degree', '本科'),
                ('period', '2012.09 - 2016.06'),
                ('major', '材料工程')]

    @property
    def career(self):
        return [(('company', '四川科技有限公司'),
                 ('period', '2016.07 - 至今'),
                 ('position', 'Python开发工程师'),
                 ('duty', '服务器架构,数据库设计,接口设计,接口开发,文档编写,接口测试,爬虫编写,服务器运维'))]

    @property
    def projects(self):
        return [(('name', 'e催宝'),
                 ('description', ('Django + Mysql + Redis + Celery + RabbitMQ'
                                  ' + Scrapy + MkDocs + Requests + Fabric + Git  + Pytest')),
                 ('duty', '后端开发'),
                 ('url', 'AppStore, 各大安卓市场')),
                (('name', '评估宝'),
                 ('description', ('Django + Mysql + Redis + Celery + RabbitMQ'
                                  ' + MkDocs + Pytest + Fabric + Git')),
                 ('duty', '后端开发'),
                 ('url', 'AppStore')),
                (('name', 'xweb'),
                 ('description', '基于WSGI的微型web框架, 无第三方依赖'),
                 ('duty', '作者'),
                 ('url', 'https://github.com/gaojiuli/xweb')),
                (('name', 'xorm'),
                 ('description', '接口更人性化的新型ORM库'),
                 ('duty', '作者'),
                 ('url', 'https://github.com/gaojiuli/xorm'))]

    @property
    def skills(self):
        return [(('name', '后端开发'),
                 ('description', '利用Python相关技术快速完成后端开发, 部署, 运维')),
                (('name', '网络爬虫'),
                 ('description', '利用Python相关技术快速完成网络爬虫编写')),
                (('name', '前端开发'),
                 ('description', '熟悉前端开发相关的各项技术')),
                (('name', '数据库'),
                 ('description', '熟悉常用数据库的设计, 运维'))]


resume = Resume()
resume.show()
