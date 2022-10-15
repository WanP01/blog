#!python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
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

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
