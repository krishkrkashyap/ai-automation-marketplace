from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from pages import views
from pages.views import INDUSTRIES, BOTS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
    
    path('', views.home, name='home'),
    
    path('industries/', views.industries_list, name='industries_list'),
    path('industries/<str:industry_slug>/', views.industry_detail, name='industry_detail'),
    
    path('services/', views.services_list, name='services_list'),
    path('services/<str:service_slug>/', views.service_detail, name='service_detail'),
    path('services/bots/<str:bot_slug>/', views.bot_detail, name='bot_detail'),
    
    path('case-studies/', views.case_studies, name='case_studies'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    
    path('sitemap.xml', views.sitemap_xml, name='sitemap_xml'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('search/', views.search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
