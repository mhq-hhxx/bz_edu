from rest_framework.generics import ListAPIView

from home.models import Banner
from home.serializer import BannerModelSerializer


class BannerAPIView(ListAPIView):
    """轮播图接口"""
    queryset = Banner.objects.filter(is_show=True, is_delete=False).order_by("-orders")
    serializer_class = BannerModelSerializer
