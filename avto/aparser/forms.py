from django.forms import ModelForm
from .models import AvtoImport


class ProductImportForm(ModelForm):
    class Meta:
        model = AvtoImport
        fields = ('csv_file',)


