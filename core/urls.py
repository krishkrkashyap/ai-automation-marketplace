from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from pages import views
from pages import api_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("favicon.ico", RedirectView.as_view(url="/static/favicon.ico", permanent=True)),
    path("", views.home, name="home"),
    path("industries/", views.industries_list, name="industries_list"),
    path("industries/<str:industry_slug>/", views.industry_detail, name="industry_detail"),
    path("services/", views.services_list, name="services_list"),
    path("services/bots/", views.bots_list, name="bots_list"),
    path("services/bots/<str:bot_slug>/", views.bot_detail, name="bot_detail"),
    path("services/<str:service_slug>/", views.service_detail, name="service_detail"),
    path("automations/", views.automation_list, name="automation_list"),
    path("automations/<str:automation_slug>/", views.automation_detail, name="automation_detail"),
    path("case-studies/", views.case_studies, name="case_studies"),
    path("case-studies/<str:slug>/", views.case_study_detail, name="case_study_detail"),
    path("blog/", views.blog_list, name="blog_list"),
    path("blog/<str:slug>/", views.blog_detail, name="blog_detail"),
    path("pricing/", views.pricing, name="pricing"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("privacy/", views.privacy, name="privacy"),
    path("terms/", views.terms, name="terms"),
    path("sitemap.xml", views.sitemap_xml, name="sitemap_xml"),
    path("robots.txt", views.robots_txt, name="robots_txt"),
    path("search/", views.search, name="search"),
    path("api/", api_views.api_root, name="api_root"),
    path("api/workflows/", api_views.list_workflows, name="list_workflows"),
    path("api/workflows/<str:automation_slug>/status/", api_views.workflow_status, name="workflow_status"),
    path("api/workflows/<str:automation_slug>/execute/", api_views.execute_workflow, name="execute_workflow"),
    path("api/workflows/<str:automation_slug>/create/", api_views.create_workflow, name="create_workflow"),
    path("api/workflows/<str:automation_slug>/executions/", api_views.workflow_executions, name="workflow_executions"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
