from .user import urlpatterns as user_urlpatterns
from .accounting import urlpatterns as accounting_urlpatterns

urlpatterns = (
    [] + user_urlpatterns + accounting_urlpatterns
)