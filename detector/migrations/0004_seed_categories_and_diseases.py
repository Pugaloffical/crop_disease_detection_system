from django.db import migrations


def create_default_catalog(apps, schema_editor):
    Category = apps.get_model('detector', 'Category')
    Disease = apps.get_model('detector', 'Disease')

    categories = [
        {
            'name': 'Plant Disease',
            'slug': 'plant-disease',
            'description': 'Diseases affecting crops and plant leaves.',
            'diseases': [
                {
                    'name': 'Powdery mildew',
                    'slug': 'powdery-mildew',
                    'description': 'A fungal disease that produces a white powdery coating on leaves.',
                    'symptoms': 'White or gray powder on leaf surfaces, distorted growth and stunted plants.',
                    'prevention': 'Improve air circulation, avoid overhead watering, and remove infected leaves.',
                    'keywords': 'powdery mildew, mildew, white powder, fungal leaf',
                },
                {
                    'name': 'Anthracnose',
                    'slug': 'anthracnose',
                    'description': 'A common fungal disease that causes dark lesions on stems and leaves.',
                    'symptoms': 'Dark sunken spots, leaf yellowing, dying tissue and defoliation.',
                    'prevention': 'Keep plants dry, remove infected tissue, and apply resistant varieties if possible.',
                    'keywords': 'anthracnose, dark spots, leaf lesions',
                },
                {
                    'name': 'Late blight',
                    'slug': 'late-blight',
                    'description': 'A destructive disease that affects leaves and fruit with dark lesions.',
                    'symptoms': 'Brown or black lesions, greasy patches, and rapid plant collapse.',
                    'prevention': 'Plant disease-resistant varieties, improve drainage, and rotate crops.',
                    'keywords': 'late blight, blight, brown lesions, potato blight',
                },
                {
                    'name': 'Yellow leaf curl virus',
                    'slug': 'yellow-leaf-curl-virus',
                    'description': 'A viral disease causing yellowing and curling of plant leaves.',
                    'symptoms': 'Yellow leaves, curling leaf edges, stunted growth.',
                    'prevention': 'Control insect vectors, remove infected plants, and use resistant varieties.',
                    'keywords': 'yellow leaf curl, yellowing, leaf curl, virus',
                },
                {
                    'name': 'Bacterial spot',
                    'slug': 'bacterial-spot',
                    'description': 'A bacterial disease that creates small, dark, water-soaked spots.',
                    'symptoms': 'Dark spots on leaves, fruit, and stems with yellow halos.',
                    'prevention': 'Use clean seed, avoid overhead watering, and remove infected debris.',
                    'keywords': 'bacterial spot, water-soaked spots, pepper disease',
                },
                {
                    'name': 'Healthy',
                    'slug': 'healthy',
                    'description': 'Healthy plant tissue with no visible disease symptoms.',
                    'symptoms': 'Green leaves without spots or discoloration.',
                    'prevention': 'Maintain proper care, irrigation, and preventive hygiene.',
                    'keywords': 'healthy, normal, no disease',
                },
            ],
        },
        {
            'name': 'Human Skin Disease',
            'slug': 'human-skin-disease',
            'description': 'Common skin conditions and irritations.',
            'diseases': [
                {
                    'name': 'Eczema',
                    'slug': 'eczema',
                    'description': 'A skin condition that causes itchy, inflamed patches.',
                    'symptoms': 'Red, itchy, cracked or scaly skin patches.',
                    'prevention': 'Use gentle skincare, avoid triggers, and keep skin moisturized.',
                    'keywords': 'eczema, dermatitis, itchy skin, dry patches',
                },
                {
                    'name': 'Psoriasis',
                    'slug': 'psoriasis',
                    'description': 'A chronic skin condition with red, scaly plaques.',
                    'symptoms': 'Raised red patches covered with silvery scales.',
                    'prevention': 'Reduce stress, avoid skin injuries, and follow medical care.',
                    'keywords': 'psoriasis, scaly skin, plaque, silver scales',
                },
                {
                    'name': 'Acne',
                    'slug': 'acne',
                    'description': 'A common condition that causes pimples and inflamed skin.',
                    'symptoms': 'Whiteheads, blackheads, pustules, and oily skin.',
                    'prevention': 'Keep skin clean, avoid heavy cosmetics, and use non-comedogenic products.',
                    'keywords': 'acne, pimple, blackhead, whitehead, breakouts',
                },
            ],
        },
        {
            'name': 'Eye Disease',
            'slug': 'eye-disease',
            'description': 'Conditions that affect the eye and surrounding tissues.',
            'diseases': [
                {
                    'name': 'Conjunctivitis',
                    'slug': 'conjunctivitis',
                    'description': 'An inflammation of the eye surface and inner eyelid.',
                    'symptoms': 'Red or pink eyes, irritation, discharge, and itchiness.',
                    'prevention': 'Practice good hygiene and avoid touching your eyes.',
                    'keywords': 'conjunctivitis, pink eye, red eye, discharge',
                },
                {
                    'name': 'Dry eye',
                    'slug': 'dry-eye',
                    'description': 'A condition caused by insufficient tear production or quality.',
                    'symptoms': 'Burning, stinging, or gritty sensation in the eyes.',
                    'prevention': 'Use lubricating drops and avoid dry environments.',
                    'keywords': 'dry eye, dryness, burning eyes, gritty sensation',
                },
                {
                    'name': 'Stye',
                    'slug': 'stye',
                    'description': 'A painful bump on the eyelid caused by an infected oil gland.',
                    'symptoms': 'Tender lump on the eyelid, swelling, and irritation.',
                    'prevention': 'Keep eyelids clean and avoid rubbing your eyes.',
                    'keywords': 'stye, eyelid bump, lump, swollen eyelid',
                },
            ],
        },
        {
            'name': 'Animal Disease',
            'slug': 'animal-disease',
            'description': 'Common animal skin and hoof conditions.',
            'diseases': [
                {
                    'name': 'Mange',
                    'slug': 'mange',
                    'description': 'A skin disease caused by mites that leads to itching and hair loss.',
                    'symptoms': 'Sores, itching, scabs, and hair loss on the animal skin.',
                    'prevention': 'Keep animals clean and treat parasites early.',
                    'keywords': 'mange, mites, animal rash, hair loss',
                },
                {
                    'name': 'Foot rot',
                    'slug': 'foot-rot',
                    'description': 'A bacterial infection of livestock hooves.',
                    'symptoms': 'Swollen or foul-smelling hooves with lameness.',
                    'prevention': 'Maintain dry bedding and trim hooves regularly.',
                    'keywords': 'foot rot, hoof disease, hoof infection, lameness',
                },
                {
                    'name': 'Dermatitis',
                    'slug': 'dermatitis',
                    'description': 'Skin irritation or rash on animals from contact or allergy.',
                    'symptoms': 'Red, irritated skin with itching or flaking.',
                    'prevention': 'Avoid allergens and keep skin clean.',
                    'keywords': 'dermatitis, animal rash, irritated skin, skin inflammation',
                },
            ],
        },
    ]

    for category_data in categories:
        category, created = Category.objects.get_or_create(
            slug=category_data['slug'],
            defaults={'name': category_data['name'], 'description': category_data['description']},
        )
        for disease_data in category_data['diseases']:
            Disease.objects.get_or_create(
                slug=disease_data['slug'],
                defaults={
                    'category': category,
                    'name': disease_data['name'],
                    'description': disease_data['description'],
                    'symptoms': disease_data['symptoms'],
                    'prevention': disease_data['prevention'],
                    'keywords': disease_data['keywords'],
                },
            )


def reverse_seed(apps, schema_editor):
    Category = apps.get_model('detector', 'Category')
    names = ['Plant Disease', 'Human Skin Disease', 'Eye Disease', 'Animal Disease']
    Category.objects.filter(name__in=names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('detector', '0003_auto_add_catalog_models'),
    ]

    operations = [
        migrations.RunPython(create_default_catalog, reverse_seed),
    ]
