from django.db import models

# Create your models here.
# class랑 블로그를 만들고 블로그라는 클래스가 어떻게 생겼는지 정의해주는 것
# 제목을 쓰고 charfield라는 타이틀을 정하고 날짜랑 글 쓴 시간을 알아내는 변수를 처리하는 것
# body는 텍스트 필드라는 긴 글의 형식을 저장하는 변수
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] #글이 길어지면 자름. 글자 100개까지만 볼 수 있게