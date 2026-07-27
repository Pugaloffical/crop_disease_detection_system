from django import forms
from .models import Category, UploadedImage


class UploadImageForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.none(),
        required=False,
        empty_label='Auto-detect category',
        widget=forms.Select(attrs={'class': 'select-field'})
    )

    class Meta:
        model = UploadedImage
        fields = ['image', 'category']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'file-input'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()


class SearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search diseases, categories, or uploads',
            'class': 'search-input'
        })
    )
