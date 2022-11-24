from dal import autocomplete
from django import forms

from mainblog.models import Category, Tag,Post

from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=CKEditorUploadingWidget(),label='摘要',required=False)
    # content = forms.CharField(widget=CKEditorUploadingWidget(), label='正文', required=True)
    # category = forms.ModelChoiceField(
    #     queryset=Category.objects.all(),
    #     widget = autocomplete.ModelSelect2(url='category-autocomplete'),
    #     label='分类',
    # )
    #
    # tag = forms.ModelChoiceField(
    #     queryset=Tag.objects.all(),
    #     widget = autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
    #     label='标签',
    # )

    content_ck = forms.CharField(widget=CKEditorUploadingWidget(),label='正文',required=False)

    content_md = forms.CharField(widget=forms.Textarea(attrs={"cols": "182", "rows": "20"}), label='正文', required=False)

    content = forms.CharField(widget=forms.HiddenInput(),required=False)


    def __init__(self,instance=None,initial=None,**kwargs):
        initial = initial or {}
        if instance:
            if instance.is_md:
                initial['content_md'] = instance.content
            else:
                initial['content_ck'] = instance.content
        super().__init__(instance=instance,initial=initial,**kwargs)
        # super().__init__(instance=None,initial=None,**kwargs)
        # pass

    def clean(self):
        is_md = self.cleaned_data.get('is_md')
        # import pdb;pdb.set_trace()
        print(is_md)
        if is_md:
            content_field_name = 'content_md'
        else:
            content_field_name = 'content_ck'
        content = self.cleaned_data.get(content_field_name)
        if not content:
            self.add_error(content_field_name,'必填项！')
            return
        self.cleaned_data['content'] = content
        return super().clean()

    #
    class Media:
        js = ('js/post_editor.js',)

    class Meta:
        model = Post
        fields = (
        'category', 'tag', 'title', 'desc', 'content', 'is_md', 'content', 'content_md', 'content_ck', 'status',)
        widgets = {
            'category': autocomplete.ModelSelect2(url='category-autocomplete'),
            'tag': autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
        }


