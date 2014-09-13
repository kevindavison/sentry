# Bootstrap the Sentry environment
from sentry.utils.runner import configure
configure()

from sentry.models import Team, Project, ProjectKey, User

user = User()
user.username = 'ozan'
user.email = 'oz@vida.com'
user.is_superuser = True
user.set_password('ozan')
user.save()

team = Team()
team.name = 'Vida'
team.owner = user
team.save()

project = Project()
project.team = team
project.owner = user
project.name = 'Default'
project.save()

key = ProjectKey.objects.filter(project=project)[0]
print 'SENTRY_DSN = "%s"' % (key.get_dsn(),)
