from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model): #model 정의
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #다른 모델에 대한 링크
    title = models.CharField(max_length=200)
    #charField = 글자수 제한 텍스트 정의(제목 등)
    text = models.TextField()
    #TextField = 글자수 제한 없는 텍스트 정의(콘텐츠)
    created_date = models.DateTimeField(default=timezone.now)
    #날짜 및 시간
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #post model의 text 호출
        return self.title
        
