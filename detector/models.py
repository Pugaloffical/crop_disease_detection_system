from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Disease(models.Model):
    category = models.ForeignKey(Category, related_name='diseases', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, unique=True)
    description = models.TextField(blank=True)
    symptoms = models.TextField(blank=True)
    prevention = models.TextField(blank=True)
    keywords = models.CharField(
        max_length=500,
        blank=True,
        help_text='Comma-separated keywords that help detect this disease from filenames or labels.'
    )

    class Meta:
        unique_together = ('category', 'name')
        ordering = ['category__name', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class UploadedImage(models.Model):
    class ImageType(models.TextChoices):
        PLANT = 'plant', 'Plant'
        HUMAN = 'human', 'Human'
        ANIMAL = 'animal', 'Animal'
        OTHER = 'other', 'Other'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='uploads'
    )
    image = models.ImageField(upload_to='uploads/')
    original_filename = models.CharField(max_length=255, blank=True)

    # Image type detection gate (Plant/Human/Animal/Other)
    image_type = models.CharField(max_length=20, choices=ImageType.choices, default=ImageType.OTHER)

    # Plant category + disease prediction (only meaningful when image_type=plant)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    predicted_disease = models.ForeignKey(Disease, null=True, blank=True, on_delete=models.SET_NULL)

    # AI outputs
    prediction_confidence = models.FloatField(null=True, blank=True)
    severity = models.CharField(max_length=20, blank=True, default='')

    prediction_text = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.original_filename or f"Upload {self.pk}"

