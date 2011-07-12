from pyramid_handlers import action
from testapp.handlers.base import Handler

class TestHandler(Handler):

    @action(renderer='string')
    def hello(self):
        return "Test Hello"
    
    @action(renderer="string")
    def index(self):
        return "Test Index"
    
    @action(renderer="string")
    def edit(self):
        return 'Test ' + self.request.matchdict.get('id','nothing')