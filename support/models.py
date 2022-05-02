from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Faq(models.Model):
    question_categori = [
        ('account', '계정'),
        ('general', '일반'),
        ('other', '기타'),
    ]
    question = models.TextField(verbose_name='질문', blank=True)
    cartegori = models.CharField(
        verbose_name='카테고리', max_length=8, choices=question_categori, default='general')
    answer = models.TextField(verbose_name="답변", blank=True)

    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    last_updated_at = models.DateTimeField(verbose_name='최종수정일', auto_now=True)

    writer = models.ForeignKey(
        User, verbose_name='작성자',  on_delete=models.CASCADE, related_name='Fap_writer_name')
    last_updated_user = models.ForeignKey(
        User, verbose_name="최종 수정자", on_delete=models.CASCADE, related_name='Fap_updater_name')


class Inquiry(models.Model):
    category = [
        ('account', '계정'),
        ('general', '일반'),
        ('other', '기타'),
    ]
    condition = [
        ('register', '문의 등록'),
        ('Received', '접수 완료'),
        ('finish', '답변 완료'),
    ]
    condition_category = models.CharField(
        verbose_name='상태', max_length=8, choices=condition, default='register')
    title_category = models.CharField(
        verbose_name="문의분류", max_length=8, choices=category, default='general')
    title = models.TextField(verbose_name="제목", max_length=30, blank=True)

    email = models.EmailField(
        verbose_name="이메일", max_length=254, default='honggildong@example.com')
    email_btn = models.BooleanField(verbose_name="이메일로답변수신", default=False)
    message = models.CharField(
        verbose_name="전화번호", max_length=11, default='-없이 입력해 주세요')
    message_btn = models.BooleanField(verbose_name="문자메세지수신", default=False)

    content = models.TextField(verbose_name="내용", blank=True)
    image = models.ImageField(verbose_name="이미지", null=True, blank=True)

    created_at = models.DateTimeField(verbose_name="생성시간", auto_now_add=True)
    last_updated_at = models.DateTimeField(
        verbose_name="최종 수정 일자", auto_now=True)

    writer = models.ForeignKey(
        User, verbose_name="생성자", on_delete=models.CASCADE, related_name='Inquiry_writer_name')
    last_updater = models.ForeignKey(
        User, verbose_name="최종수정자", on_delete=models.CASCADE, related_name='Inquiry_updater_name')
    finish = models.BooleanField(verbose_name="답변완료여부", default=False)


class Answer(models.Model):
    content = models.TextField(verbose_name="답변내용", blank=True)
    Inquiry = models.ForeignKey(
        Inquiry, verbose_name='참조 문의글', on_delete=models.CASCADE)

    created_at = models.DateTimeField(verbose_name="생성일시", auto_now_add=True)
    last_updated_at = models.DateTimeField(
        verbose_name="최종수정일시", auto_now=True)

    writer = models.ForeignKey(
        User, verbose_name="생성자", on_delete=models.CASCADE, related_name='Answer_writer_name')
    last_updater = models.ForeignKey(
        User, verbose_name="최종수정자", on_delete=models.CASCADE, related_name='Answer_updater_name')
