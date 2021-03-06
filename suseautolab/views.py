from django.http import HttpResponse
from django.shortcuts import render
import subprocess


def hello(request):
    return HttpResponse("Hello world ! ")


def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'runoob.html', context)


def search_form(request):
    return render(request, 'search_form.html')


def search_result(request):
    context = {}
    module = ''
    typesite = ''
    result = ''
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        module = request.GET['q']
    else:
        module = 'nothing'
    if 'sellist1' in request.GET and request.GET['sellist1']:
        typesite = request.GET['sellist1']
    else:
        typesite = 'nothing'

    context['module'] = module
    context['typesite'] = typesite

    for site in ['o3', 'osd']:
        cmd = "perl /root/website/HWPP/script/find_jobs_by_module.pl -f %s -m %s" % (
            typesite, module)
        ret = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    context['ret'] = ret
    tmpstring = bytes.decode(ret.stdout)
    tmpstring = "Site: %s\n" % typesite + "Test module: %s\n" % module + tmpstring
    stdout1 = tmpstring.replace("\n", "<br>").replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
    context['stdout'] = stdout1
    print(subprocess.run('pwd', shell=True, stdout=subprocess.PIPE).stdout)
    print(subprocess.run('touch templates/%s.html' %
                         module, shell=True, stdout=subprocess.PIPE).stdout)

    fo = open("templates/%s.html" % module, "w")
    print(stdout1)
    fo.write(stdout1)
    fo.close()
    modulename = module + ".html"
    context['modulename'] = modulename

    return render(request, 'search_result.html', context)


def search_module(request):
    return render(request, 'search_module.html')
