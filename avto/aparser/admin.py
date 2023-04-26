from django.contrib import admin
from .models import Product, AvtoImport

import csv
from .forms import ProductImportForm
from django.urls import path
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


# модель для просмотра импортируемых файлов
@admin.register(AvtoImport)
class AvtoImportAdmin(admin.ModelAdmin):
    list_display = ('csv_file', 'date_added')


# реализация самого импорта
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'link_car', 'date',)

 
    def get_urls(self):
        urls = super().get_urls()
        urls.insert(-1, path('csv-upload/', self.upload_csv))
        return urls

    def upload_csv(self, request):
        if request.method == 'POST':
            form = ProductImportForm(request.POST, request.FILES)
            if form.is_valid():
                # сохраняем загруженный файл и делаем запись в базу
                form_object = form.save()
                # обработка csv файла
                with form_object.csv_file.open('r') as csv_file:
                    rows = csv.reader(csv_file, delimiter=',')
                    if next(rows) != ['title', 'link_car', 'date']:
                        # обновляем страницу пользователя
                        # с информацией о какой-то ошибке
                        messages.warning(request, 'Неверные заголовки у файла')
                        return HttpResponseRedirect(request.path_info)
                    for row in rows:
                        print(row[2])
                        # добавляем данные в базу
                        Product.update_or_create(
                            title=row[0],
                            link_car=row[1],
                            price=row[2]
                        )
                # конец обработки файлы
                # перенаправляем пользователя на главную страницу
                # с сообщением об успехе
                url = reverse('admin:index')
                messages.success(request, 'Файл успешно импортирован')
                return HttpResponseRedirect(url)
