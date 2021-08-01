
from cement import Controller, ex
from cement.utils.version import get_version_banner
from ..core.version import get_version

VERSION_BANNER = """
Remote Control for samsung tv's %s
%s
""" % (get_version(), get_version_banner())


class Base(Controller):
    class Meta:
        label = 'base'

        # text displayed at the top of --help output
        description = "Remote Control for samsung tv's"

        # text displayed at the bottom of --help output
        epilog = 'Usage: tvremotecli connect --ip xxx.xxx.xxx.xxx'

        # controller level arguments. ex: 'samsung-remotecontrol-cli --version'
        arguments = [
            ### add a version banner
            ( [ '-v', '--version' ],
              { 'action'  : 'version',
                'version' : VERSION_BANNER } ),
        ]


    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()


    @ex(
        help='connection for tv',

        # sub-command level arguments. ex: 'samsung-remotecontrol-cli command1 --foo bar'
        arguments=[
            ### add a sample foo option under subcommand namespace
            ( [ '--ip' ],
              { 'help' : 'Tv ip',
                'action'  : 'store',
                'dest' : 'ip' } ),
        ],
    )
    def connect(self):
        """Example sub-command."""

        data = {
            'ip' : 'lala',
        }

        ### do something with arguments
        if self.app.pargs.ip is not None:
            data['ip'] = self.app.pargs.ip

        self.app.render(data, 'connect.jinja2')
