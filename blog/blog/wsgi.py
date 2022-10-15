"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# 初始设置
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
# 生产上线设置
# profile = os.environ.get('BLOG_PROFILE','product')
# 开发配置
profile = os.environ.get('BLOG_PROFILE', 'develop')
# print('1',profile)
# print(os.environ.get('BLOG_PROFILE'))
# print(os.environ)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings.%s' % profile)

application = get_wsgi_application()
