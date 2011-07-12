"""View handlers package.
"""

def includeme(config):
    """Add the application's view handlers.
    """
    config.add_handler("home", "/", "testapp.handlers.main:Main",
                       action="index")
    config.add_handler("main", "/{action}", "testapp.handlers.main:Main",
        path_info=r"/(?!favicon\.ico|robots\.txt|w3c)")
    
    config.add_handler('another', '/another/{action}', 'testapp.handlers.another:AnotherHandler')
    config.add_handler('another action', '/another/{action}/{id}', 'testapp.handlers.another.AnotherHandler')
    
    config.add_handler('test', '/test/{action}', 'testapp.handlers.test:TestHandler')
    config.add_handler('test action', '/test/{action}/{id}', 'testapp.handlers.test:TestHandler')
