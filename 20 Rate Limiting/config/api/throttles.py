from rest_framework.throttling import UserRateThrottle

class GroupRateThrottle(UserRateThrottle):
    def get_cache_key(self, request, view):
        if not request.user.is_authenticated:
            return None
        
        if request.user.groups.filter(name = "premium").exists():
            self.scope = "premium"
        else:
            self.scope = 'user'

        return super().get_cache_key(request, view)