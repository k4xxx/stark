# stark注册

from stark.service import stark
from app01.models import *
from stark.service.stark import DeFaultConfigClass



class AuthorConfig(DeFaultConfigClass):

    list_display = ['name','age']

    list_display_link = ['name']

    search_fields = ['name','age']
    filter_list = ['name','age']

    def patch_init(self, request, queryset):
        queryset.update(age=123)
    patch_init.short_description = "批量初始化"


    actions = [patch_init]




class BookConfig(DeFaultConfigClass):
    list_display = ['title','author','publish']
    list_display_link = ['title']

    filter_list = ['title','author','publish']




stark.site.register(Author,AuthorConfig)
stark.site.register(Book,BookConfig)
stark.site.register(Publish)

