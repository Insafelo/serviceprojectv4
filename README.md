Проект начало с главной страницы с двух кнопок, это "Найти механика" и "Стать исполнителем" (Я автомеханик)
При переходе по "Найти механика" открывается список механиков (который должен тянуться из базы, там пока чисто хтмл код) и получается клиент выбирает механика из списка (можно оставить также 3 механика), после выбора открывается http://127.0.0.1:8000/profile_auto/payment/ 
пользователь выбирает услуги нужные ему (у каждого механика свои услуги), способ оплаты, адресс, после того как все ввел появляется кнопка оплатить и сообщение что успешно механик принял Ваш вызов.

Со стороны механика же, с главной страницы прожимает на кнопку "Я механик" попадает на авторизацию, проходит ее, попадает в свой профиль, где может добавлять услуги или удалять, и снизу две таблицы где справа новые, которые он может взять и слева, те которые выполнил. (те, которые выполнены переходят по логике в левую таблицу)

Ну и главная страница конечно сухая без ничего, это добавить верстку туда с дизайном, по типу актуальности и снизу шапку наши контакты было бы кулл.
