from django.core.mail import send_mail
from django.urls import reverse


def send_verify_mail(user):
    verify_link = reverse('auth:verify', args=[user.id, user.activation_key])

    title = f'Подтверждение регистрации {user.email}'

    massage = f'Пройдите по ссылке {verify_link}'

    result = send_mail(title, massage, [user.email, ], 'admin@mail.ru', fail_silently=False)
    print(result)
    return result
