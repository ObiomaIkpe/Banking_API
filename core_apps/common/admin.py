from django.contrib import admin

from typing import Any
from django.contrib.contenttypes.admin import GenericTabularInline
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _
from .models import ContentView

@admin.register(ContentView)
class ContentViewAdmin(admin.ModelAdmin):
    list_display = ["content_object", "content_type", "user", "viewer_ip", "last_viewed"]

    list_filter = ["content_type", "last_viewed", "created_at"]

    date_hierarchy = "last_viewed"

    readonly_fields = ["content_type", "content_object", "user", "viewer_ip", "last_viewed"]

    fieldsets = (
        (None, {"fields": ("content_type", "object_id", "content_object")}),
        (_("View_details"), {"fields": ("user", "viewer_ip", "last_viewed")}),
       (
        _("TimeStamps"), {
            "fields": ("created_at", "updated_at"), "classes":("collapse",)
        }   
    ),
)
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False
    
    def has_change_permission(self, request: HttpRequest, obj: Any =None) ->  bool:
        return False
    
    class ContentViewInline(GenericTabularInline):
        model = ContentView
        extra = 0
        readonly_fields = ["user", "viewer_ip", "created_at", "last_viewed"]
        can_delete =False


        def has_add_permission(self, request: HttpRequest, obj: Any = None) -> bool:
            return False