# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Posts, category, slider, Opt

admin.site.register(Posts)
admin.site.register(category)
admin.site.register(slider)
admin.site.register(Opt)
