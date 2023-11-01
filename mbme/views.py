from django.template import loader, TemplateDoesNotExist, TemplateSyntaxError
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def default(request): return redirect('blog_v1:index')


def blog(request, slug):
    from apps.blog.blog_v1.views import post_select_view
    return post_select_view(request, slug=slug)


def login(request): return render(request, 'login.html')


def stylesheet(request, template_name):
    template_path = f'css/{template_name}.css'
    try:
        loader.get_template(template_path)
    except (TemplateSyntaxError, TemplateDoesNotExist) as e:
        raise Http404(e)
    return render(request, template_path, content_type='text/css')


def script(request, template_name):
    template_path = f'js/{template_name}.js'
    try:
        loader.get_template(template_path)
    except (TemplateSyntaxError, TemplateDoesNotExist) as e:
        raise Http404(e)
    return render(request, template_path, content_type='text/javascript')