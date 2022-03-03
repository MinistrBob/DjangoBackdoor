from ssh_client.ssh_connect import SshConnect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.template import loader
from django.http import Http404

import tempfile
from .models import Ssh
from .forms import CommandForm

# Create your views here.
# def index(request):
#     return HttpResponse(f"Hello, you are here: {settings.BASE_DIR}")

ssh_list = {}
TEMP_FOLDER = tempfile.gettempdir()


def get_ssh_connect(ssh):
    """
    If SSH connection already exists return it, otherwise create a new SSH connection
    :param ssh: SSH connection parameters
    :return: SshConnect instance 
    """
    sc = None
    err = None
    if ssh.ip in ssh_list:
        sc = ssh_list[ssh.ip]
    else:
        try:
            sc = SshConnect(ssh.ip, ssh.username, ssh.password)
            ssh_list[ssh.ip] = sc
        except Exception as e:
            err = e
    return sc, err


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
        sc, err = get_ssh_connect(ssh)
        print(sc, err)
        if err is not None:
            raise Exception(err)
    except Exception as e:
        return render(request, 'ssh_client/ssh_error.html', {'ssh': ssh, 'err': err})

    output = error = result = None
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CommandForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            output, error, result = sc.execute_command(form.cleaned_data['command'])
    # if a GET (or any other method) we'll create a blank form
    else:
        output = 'connected'
        error = result = None
        form = CommandForm()

    return render(request, 'ssh_client/ssh.html',
                  {'ssh_id': ssh_id,
                   'ssh': ssh,
                   'form': form,
                   'output': output,
                   'error': error,
                   'result': result,
                   'temp_folder': TEMP_FOLDER})

