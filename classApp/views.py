from typing import Any
from django.shortcuts import render
from django. shortcuts import render, redirect 
from django. views. generic import ListView, DetailView, CreateView, DeleteView, UpdateView 
from django. urls import reverse_lazy 
from django. contrib. auth. models import User 
from django. db import IntegrityError
from django.core.exceptions import ValidationError

# Create your views here.

from django. contrib. auth import authenticate, login ,logout 

from .models import MemoModel
from .forms import TestForm


class MemoList( ListView ):
    template_name = 'list.html'
    model = MemoModel 
    # context_object_name = "memo_list_data"

class MemoDetail( DetailView ): 
    template_name = 'detail.html' 
    model = MemoModel
    # context_object_name = "detail_data"


class MemoDelete( DeleteView ): 
    template_name = 'delete.html' 
    model = MemoModel
    context_object_name = "delete_data"
    success_url = reverse_lazy('list_url')


class MemoCreate(CreateView):

    model = MemoModel
    # form_class = TestForm
    #入力項目定義
    fields = ("title","memo")

    #テンプレートファイル連携
    template_name = "form.html"
    success_url = reverse_lazy('list_url')

    def get_form_kwargs(self):
        kwargs = super(MemoCreate, self).get_form_kwargs()
        kwargs['label_suffix'] = '***'
        return kwargs    
    
    # 以下は保存前に値を変更する場合
    # def form_valid(self, form):
    #         post = form.save(commit=False)
    #         post.updated_by = self.request.user
    #         post.updated_at = timezone.now()
    #         post.save()
    #         return redirect('topic_posts', pk=post.topic.board.pk, topic_pk=post.topic.pk)

class MemoUpdate(UpdateView):

    template_name = "update.html"
    model = MemoModel
    #入力項目定義
    fields = ("title","memo")
    # form_class = TestForm

    #テンプレートファイル連携
    context_object_name = "form_data"
    success_url = reverse_lazy('list_url')

    # def get_form_kwargs(self):
        # kwargs = super(MemoCreate, self).get_form_kwargs()
        # kwargs['label_suffix'] = ''
        # return kwargs   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test_message'] = "テストメッセージです。"
        # print("-----------", context['form'] )
        # s= str(context['form']).replace(":</","</")

        fm =[]
        for a in context['form']:
            # print( a.label_suffix )
            # a.class = "fm"
            fm.append(a)
        context['fm'] = fm

        return context
         
    def get_initial(self):
        initial = super().get_initial()
        # initial['user'] = test.user   #testモデルのuserを初期値としてセット
        initial['memo'] = 'bc'
        return initial
    
    def form_valid(self, form):
        # ここでフォームのデータを処理
        # 例：フォームに初期データを設定
        form.instance.title = "some_value"
        return super().form_valid(form)
