from fabric.api import lcd, local

def prepare_deployment(branch_name):
    # local('python manage.py test django_project')
    local('git add -p && git commit')

def deploy():
    with lcd('/Users/rhurst/no_fee_staged/'):

        # With git...
        local('git pull /Users/rhurst/no_fee/')

        # With both
        # local('python manage.py migrate myapp')
        # local('python manage.py test myapp')
        # local('/my/command/to/restart/webserver')    