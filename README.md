### GeekShop "The Basics Of Django Framework"

#### Lesson_1 "Introduction to the framework"

#### Lesson_2 "Template + Context = html"

#### Lesson_3 "Models + ORM = Data"

#### Lesson_4 "User authentication and registration"

#### Lesson_5 "User + product = shopping cart"

#### Lesson_6 "Shopping cart + AJAX + Decorators"

#### Lesson_7 "Own admin panel"

#### Lesson_8 "Useful: page output, template filters, CBV"

### GeekShop "Django Framework. Optimization tools"

#### Lesson 1. Sending email. Context processors

./manage.py loaddata mainapp/fixtures/products.json ./manage.py loaddata mainapp/fixtures/categories.json installation
packages pip in the file requirements.txt

#### Lesson 2. Registration via a social network. Django-ORM: one-to-one communication

https://vk.com/dev  «ВКонтакте»: создаем и настраиваем приложение

#### started Lesson 3.Working with a user's order: CBV, Django formsets

1. Создать приложение для работы с заказами пользователя с использованием CBV
2. Реализовать обновление статуса заказа при совершении покупки (без оплаты).
3. Обновить контроллеры проекта – перевести на Django CBV (где в этом есть смысл).
4. Добавить заказы (order) в админку Django. Чтобы можно было редактировать из админки.

#### started Lesson 4. Working with a user's order: Updating the remaining product balances, adding the jQuery code

1. Добавить возвращение товара на склад при удалении товара из корзины (product.quantity)
2. Добавить вывод стоимости товара в заказе. P.S. django-dynamic-formset из методички добавлять в свой проект не
   обязательно. Это расширения для Django от сторонних разработчиков и последние два года не развивалось совсем. А
   значит этим не стоит пользоваться и рассматривать не имеет смысла.