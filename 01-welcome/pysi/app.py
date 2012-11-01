import pysi


@pysi.view('/welcome')
def welcome(rq):
    return 'Hello World!'

main = pysi.App()
