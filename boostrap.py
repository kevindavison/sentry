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

for project_name in ('webserver', 'webclient', 'socketserver', 'ios'):
    project = Project()
    project.team = team
    project.owner = user
    project.name = project_name
    project.save()

    key = ProjectKey.objects.filter(project=project)[0]
    print project_name, 'SENTRY_DSN = {}'.format(key.get_dsn())
