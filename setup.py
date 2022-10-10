from setuptools import setup, find_packages


setup(
    name='blog',
    version='${version}',
    description='Blog System base on Django',
    author='wanpeng',
    author_email='wanpwc@163.com',
    # url='https://www.the5fire.com',
    license='MIT',
    packages=find_packages('blog'),
    package_dir={'': 'blog'},
    # package_data={'': [    # 打包数据文件，方法一
        # 'themes/*/*/*/*',  # 需要按目录层级匹配
    # ]},
    include_package_data=True,  # 方法二 配合 MANIFEST.in文件
    install_requires=[
'asgiref==3.5.2',
'certifi==2022.9.24',
'charset-normalizer==2.1.1',
'Django==4.1.1',
'django-autocomplete-light==3.9.4',
'django-ckeditor==6.5.1',
'django-crispy-forms==1.14.0',
'django-debug-toolbar==3.7.0',
'django-debug-toolbar-line-profiling==0.7.3',
'django-formtools==2.2',
'django-js-asset==2.0.0',
'djangorestframework==3.14.0',
'djdt-flamegraph==0.2.13',
'docopt==0.6.2',
'httplib2==0.9.2',
'idna==3.4',
'line-profiler==3.5.1',
'mistune==2.0.4',
'mysqlclient==2.1.1',
'Pillow==9.2.0',
'pip==22.2.2',
'pipreqs==0.4.11',
'Pympler==1.0.1',
'pytz==2022.2.1',
'requests==2.28.1',
'setuptools==65.3.0',
'six==1.16.0',
'sqlparse==0.4.2',
'urllib3==1.26.12',
'wheel==0.37.1',
'yarg==0.1.9',
    ],
    scripts=[
        'blog/manage.py',
        # 'typeidea/typeidea/wsgi.py',
    ],
    entry_points={
        'console_scripts': [
            'blog_manage = manage:main',
        ]
    },
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Blog :: Django Blog',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.10',
    ],

)