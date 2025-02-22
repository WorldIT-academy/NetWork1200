from django import forms
from .models import Tag, Post

# Створюємо клас для форми
class PostForm(forms.ModelForm):
    # Свторюємо клас , що відповідає за налаштування форми
    class Meta:
        # Підв'язуємо модель для форми 
        model = Post 
        # Відображаємо усі поля окрім поля автора
        fields = "__all__"  
        exclude = ("author",)
        # Задаємо атрибути для полів у HTML-документі
        widgets = {
            'title': forms.TextInput(attrs = {
                "class": "form-input",
                "placeholder": "Заголовок"
            }),
            'content': forms.Textarea(attrs = {
                "placeholder": "Контент"
            })
        }

    # Презаписуємо метод save, щоб додактово зберагіти автора та теги
    def save(self, author):
        # Створюємо об'єкт поста, проте не зберігаємо у бд (за цевідповідає параметр commit = False)
        post = super().save(commit = False)
        # Підв'язуємо та зберігаємо автора поста
        post.author = author
        post.save()
        # Підв'язуємо та зберігаємо теги
        post.tags.set(self.cleaned_data["tags"])
        post.save()
        # Повертаємо пост
        return post
        
