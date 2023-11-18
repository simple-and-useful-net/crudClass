from django. urls import path 
from .views import MemoList, MemoDetail,MemoCreate,MemoDelete, MemoUpdate

urlpatterns=[
                path('list/',           MemoList.as_view(),   name ='list_url'), 
                path('create/',         MemoCreate.as_view(), name ='create_url'), 
                path('detail/<int:pk>', MemoDetail.as_view(), name ='detail_url'), 
                path('delete/<int:pk>', MemoDelete.as_view(), name ='delete_url'), 
                path('update/<int:pk>', MemoUpdate.as_view(), name ='update_url'), 
]

