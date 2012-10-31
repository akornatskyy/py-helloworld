from paste.deploy import loadapp


main = loadapp('config:development.ini', relative_to='./helloworld')
