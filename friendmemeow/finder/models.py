from django.db import models
from django.utils import timezone


def get_upload_file_name(instance, filename):
    index = len(Kitty.objects.all()) + 1
    return "images/%s_%s" % ('cat', index)


class Kitty(models.Model):
    name = models.CharField(max_length=20)
    location = models.ForeignKey('Shelter', null = True, blank = True)

    GENDER_CHOICES = (('F','Female'), ('M', 'Male'))
    gender = models.CharField(choices = GENDER_CHOICES, max_length=1, default = 'M')


    age = models.IntegerField(default=1)

    BREED_CHOICES = [('Unknown/Mixed',  'Unknown/Mixed'),('Abyssinian',  'Abyssinian'),('American Bobtail',  'American Bobtail'),('American Curl',  'American Curl'),('American Shorthair',  'American Shorthair'),('American Wirehair',  'American Wirehair'),('Balinese',  'Balinese'),('Birman',  'Birman'),('Bombay',  'Bombay'),('British Shorthair',  'British Shorthair'),('Burmese',  'Burmese'),('Burmilla',  'Burmilla'),('Chartreux',  'Chartreux'),('Chinese Li Hua',  'Chinese Li Hua'),('Colorpoint Shorthair',  'Colorpoint Shorthair'),('Cornish Rex',  'Cornish Rex'),('Devon Rex',  'Devon Rex'),('Egyptian Mau',  'Egyptian Mau'),('European Burmese',  'European Burmese'),('Exotic',  'Exotic'),('Havana Brown',  'Havana Brown'),('Japanese Bobtail',  'Japanese Bobtail'),('Korat',  'Korat'),('LaPerm',  'LaPerm'),('Maine Coon Cat',  'Maine Coon Cat'),('Manx',  'Manx'),('Norwegian Forest Cat',  'Norwegian Forest Cat'),('Ocicat',  'Ocicat'),('Oriental',  'Oriental'),('Persian',  'Persian'),('RagaMuffin',  'RagaMuffin'),('Ragdoll',  'Ragdoll'),('Russian Blue',  'Russian Blue'),('Scottish Fold',  'Scottish Fold'),('Selkirk Rex',  'Selkirk Rex'),('Siamese',  'Siamese'),('Siberian',  'Siberian'),('Singapura',  'Singapura'),('Somali',  'Somali'),('Sphynx',  'Sphynx'),('Tonkinese',  'Tonkinese'),('Turkish Angora',  'Turkish Angora'),('Turkish Van',  'Turkish Van')]
    breed = models.CharField(choices = BREED_CHOICES, max_length=30, default = 'Un')

    about = models.TextField()
    photo = models.ImageField(null=True)

    posted_date = models.DateTimeField(default=timezone.now)

    STATUS_CHOICES = ( ('Need', 'Needs a home'), ('Adopted!','Adopted!') )
    status = models.CharField(choices = STATUS_CHOICES, max_length=20, default='Need')


    def post(self):
        self.posted_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Shelter(models.Model):
    name = models.CharField(max_length=100, null=True, blank = True)

    address1 = models.CharField(max_length = 100, null=True, blank = True)
    address2 = models.CharField(max_length = 100, null=True, blank = True)
    city = models.CharField(max_length=40)
    
    STATE_CHOICES = [('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')]
    state = models.CharField(choices=STATE_CHOICES, max_length=50, default='AL')
    zip_code = models.IntegerField(max_length = 5, null=True, blank = True)

    phone = models.CharField(max_length = 10, null=True, blank = True)
    email = models.CharField(max_length = 200, null=True, blank = True)

    def __str__(self):
        return self.name
