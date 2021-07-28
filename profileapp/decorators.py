from django.http import HttpResponseForbidden

from profileapp.models import profile


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_profile = profile.objects.get(pl=kwargs['pk'])
        if target_profile.user == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
        return decorated