from django.urls import path
from . import views

urlpatterns = [
    path('admin_panel/', admin.site.urls),
    path('account/', include('account.urls')),
    path('blood/', include('blood.urls')),
    path('admin_panel-panel/', include('admin_panel.urls')),  # Update here
]

