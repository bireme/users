from fabric.api import env

env.user = 'moacir.moda'
env.path = '/home/aplicacoes/accounts/'
env.rootpath = env.path + 'bireme/'
env.gitpath = env.path + 'git/'
env.virtualenv = env.path + 'env/'

def test():
    env.hosts = ['ts01dx']

def homolog():
    env.hosts = ['hm01dx']
