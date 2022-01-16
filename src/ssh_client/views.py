from ssh_client.ssh_connect import SshConnect
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.template import loader
from django.http import Http404

from .models import Ssh


# Create your views here.
# def index(request):
#     return HttpResponse(f"Hello, you are here: {settings.BASE_DIR}")

def index(request):
    print(request.session)
    ssh_list = Ssh.objects.all()
    template = loader.get_template('ssh_client/index.html')
    context = {'ssh_list': ssh_list, }
    return HttpResponse(template.render(context, request))


def ssh_connect(request, ssh_id):
    try:
        ssh = Ssh.objects.get(pk=ssh_id)
    except Ssh.DoesNotExist:
        raise Http404("SSH does not exist")
    try:
        sc = SshConnect(ssh.ip, ssh.username, ssh.password)
        result = sc.execute_command('ls')
    except Exception as err:
        return render(request, 'ssh_client/error.html', {'err': err})
    return render(request, 'ssh_client/ssh_connect.html', {'ssh': ssh, 'result': result})
