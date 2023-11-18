from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from .models import MemoModel

CHOICES = [
        ('123', 'Adam'),
        ('321', 'John'),
        ('666', 'Lucy'),
]


class TestForm(forms.ModelForm):


    class Meta:
        model = MemoModel
        
        # フェールドは個別に指定ができます
        # fields = ["title","memo"]
        fields = "__all__"

        # フォームページに出力される入力の名称
        labels={
            "title":"タイトル",
            "note":"メモ",
        }

        title = forms.CharField(required=False)
        # title = forms.CharField(required=False)
        # widgets = {
        #     'title': forms.TextInput( attrs={'class': 'custom-css-class',
        #                                     'required': 'true',
        #                                     'placeholder': 'This field is optional',
        #                                 },
        #                             ),
        #     'memo': forms.Textarea(attrs={'class': 'custom-css-class'}),
        # }
        widgets = {
            'type_name': forms.RadioSelect(),
            # 'type_name2': forms.CheckboxSelectMultiple(),
            'memo': forms.Textarea(attrs={
                                            'placeholder': 'custom-css-class',
                                            "required": False,
                                    }),

            }
        
    def __init__(self, *args, **kwargs):

        # ここでmy_custom_dataを使って何か処理を行うことができます

        super(TestForm, self).__init__(*args, **kwargs)
        
        instance = kwargs.get('instance', {})
        if instance:
            title_data = instance.title
        else:
            title_data = "init-DATA"
    

        # self.fields['title'].initial ="testABC"
        # self.initial['title'] ="nnn"
        # self.fields['title'].initial ="==" + title_data + "=="
        # タイトルに追加（変更）する
        # self.initial['title'] = "==" + title_data + "=="

        # if instance:
        #     self.initial['categories'] = self.instance.categories.all()

        # すべてのフィールドを指定
        for field_name, field in self.fields.items():
            field.required = False  # フィールドのrequired属性をFalseに設定

