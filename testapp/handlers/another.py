from pyramid_handlers import action
from testapp.handlers.base import Handler

class AnotherHandler(Handler):

    @action(renderer='string')
    def index(self):
        return "Another index"

    @action(renderer="string")
    def hello(self):
        return "Another hello"
    
    @action(renderer="string")
    def edit(self):
        return 'Another '+ self.request.matchdict.get('id','nothing')