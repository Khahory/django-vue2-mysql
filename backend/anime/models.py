from django.db import models
from django.utils import timezone


# donde guardaremos la imagen
def user_directory_path(instance, filename):
    nombre_carpeta = instance.titulo.replace(" ", "_")
    nombre_carpeta = nombre_carpeta.replace(":", "_")
    nombre_carpeta = nombre_carpeta.lower()
    return 'anime/{0}/{1}'.format(nombre_carpeta, filename)


class Anime(models.Model):
    class AnimeObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(estado='emision')

    # los estados -> si es draft, solo quien lo creo podra verlo, published sera para todos los users
    options = (
        ('emision', 'En emision'),
        ('concluido', 'Concluido'),
    )

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    slug = models.SlugField(max_length=250, unique_for_date='concluido', null=False, unique=True)
    concluido = models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=10, choices=options, default='emision')

    objects = models.Manager()  # default manager
    animeObjects = AnimeObjects()  # custom manager

    class Meta:
        ordering = ('-concluido',)

    def __str__(self):
        return self.titulo
