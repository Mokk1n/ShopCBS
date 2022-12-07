import smtplib

import django.core.handlers.wsgi
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from rest_framework.generics import get_object_or_404

from web.forms import ReviewForm, OrderCreateForm
from web.models import Product


class HomepageView(TemplateView):
    template_name = 'web/index.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        filter_ = request.GET.get('filter')
        f = Product.objects.all()
        context = dict()
        if filter_ == 'mobile':
            for i in f:
                if i.group == 'mobile':
                    context['pr'] = Product.objects.filter(group='mobile')
        elif filter_ == 'notebook':
            for g in f:
                if g.group == 'notebook':
                    context['pr'] = Product.objects.filter(group='notebook')
        elif filter_ == 'pc':
            for h in f:
                if h.group == 'pc':
                    context['pr'] = Product.objects.filter(group='pc')
        else:
            context['pr'] = f
        return self.render_to_response(context)


class SearchResultsView(TemplateView):
    template_name = 'web/index.html'

    def get(self, request, *args, **kwargs):
        cou = dict()
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(name=query)
        cou['pr'] = object_list
        return self.render_to_response(cou)


class DetailView(TemplateView):
    template_name = 'web/det.html'

    def get(self, request: django.core.handlers.wsgi.WSGIRequest, pk, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        product = get_object_or_404(Product, pk=pk)
        self.extra_context = {"pr": product}
        return self.render_to_response(self.get_context_data(**kwargs))


class ReviewView(TemplateView):
    template_name = 'web/review.html'

    def get(self, request: django.core.handlers.wsgi.WSGIRequest, pk, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        product = get_object_or_404(Product, pk=pk)
        self.extra_context = {'form': ReviewForm(data={'product': product.pk, 'user': request.user.pk})}
        return self.render_to_response(self.get_context_data(**kwargs))

    def post(self, request: django.core.handlers.wsgi.WSGIRequest, *args, **kwargs):
        data = request.POST
        ReviewForm(data).save()
        return HttpResponseRedirect(reverse('products_detail_view', kwargs={'pk': data.get('product')}))


class OrderView(TemplateView):
    template_name = 'order/create.html'

    def get(self, request: django.core.handlers.wsgi.WSGIRequest, pk, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        order = get_object_or_404(Product, pk=pk)
        self.extra_context = {'form': OrderCreateForm(data={'product': order.pk, 'user': request.user.pk})}
        return self.render_to_response(self.get_context_data(**kwargs))

    def post(self, request: django.core.handlers.wsgi.WSGIRequest, *args, **kwargs):
        data = request.POST
        OrderCreateForm(data).save()
        print(data)
        return HttpResponseRedirect(reverse('home'))


class EmailView(TemplateView):
    template_name = 'web/index.html'

    def get(self, request, *args, **kwargs):
        quer = self.request.GET.get('q')
        gmail_user = 'kirilmix52@gmail.com'
        gmail_password = 'eatchzrutfnlnbll'

        to = quer
        subject = 'OMG Super Important Message'
        body = 'hello, you subscribed to the store news'

        email_text = """\
            From: %s
            To: %s
            Subject: %s

            %s
            """ % (gmail_user, ", ".join(to), subject, body)

        server = smtplib.SMTP('smtp.gmail.com')
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to, email_text)
        server.close()
        return HttpResponseRedirect(reverse('home'))

