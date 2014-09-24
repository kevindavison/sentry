# Bootstrap the Sentry environment
from sentry.utils.runner import configure
configure()

from sentry.models import Team, Project, ProjectKey, User

user, created = User.objects.get_or_create(username='ozan', defaults={
    'email': 'oz@vida.com',
    'is_superuser': True
})

if created:
    user.set_password('YL*Jg%*AeL^fCY3%xjhr2ZaYw')
    user.save()


team, created = Team.objects.get_or_create(name='Vida', defaults={
    'owner': user
})


for project_name in ('webserver', 'webclient', 'socketserver', 'ios'):
    project, created = Project.objects.get_or_create(name=project_name)
    if created:
        project.team = team
        project.owner = user
        project.save()

    key = ProjectKey.objects.filter(project=project)[0]
    print project_name, 'SENTRY_DSN = {}'.format(key.get_dsn())
