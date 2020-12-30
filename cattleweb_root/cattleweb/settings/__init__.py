from .base import *
# you need to set "cattleweb = 'prod'" as an environment variable
# in your OS (on which your website is hosted)
if 'cattleweb' in os.environ.keys():
    if os.environ['cattleweb'] == 'prod':
        from .prod import *
    else:
        from .dev import *
else:
    from .dev import *