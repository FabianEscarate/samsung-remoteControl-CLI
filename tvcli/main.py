
import os
from cement import App, TestApp, init_defaults
from cement.utils import fs
from cement.core.exc import CaughtSignal
from tinydb import TinyDB
from .core.exc import tvcliError
from .controllers.base import Base

# configuration defaults
CONFIG = init_defaults('tvcli')
CONFIG['tvcli']['db_path'] = './db/tvsip.json'

def extends_db(app):
    app.log.info('extending todo application with tinydb')
    db_file = app.config.get('tvcli', 'db_path')
    
    # ensure that we expand the full path
    db_file = fs.abspath(db_file)
    app.log.info('tinydb database file is: %s' % db_file)
    
    # ensure our parent directory exists
    db_dir = os.path.dirname(db_file)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

    app.extend('db', TinyDB(db_file))

class tvcli(App):
    """remoteControl primary application."""

    class Meta:
        label = 'tvcli'

        # configuration defaults
        config_defaults = CONFIG

        # call sys.exit() on close
        exit_on_close = True

        # load additional framework extensions
        extensions = [
            'yaml',
            'colorlog',
            'jinja2',
        ]

        # configuration handler
        config_handler = 'yaml'

        # configuration file suffix
        config_file_suffix = '.yml'

        # set the log handler
        log_handler = 'colorlog'

        # set the output handler
        output_handler = 'jinja2'
        # template_dir = './templates`'

        # register handlers
        handlers = [
            Base
        ]

        # Hooks
        hooks = [
            ('post_setup',extends_db),
        ]


class tvcliTest(TestApp,tvcli):
    """A sub-class of tvcli that is better suited for testing."""

    class Meta:
        label = 'tvcli'


def main():
    with tvcli() as app:
        try:
            # print(app.Meta)
            app.run()

        except AssertionError as e:
            print('AssertionError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except tvcliError as e:
            print('tvcliError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()
