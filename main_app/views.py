from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plant
from .forms import FeedingForm

# plants = [
#     {'name': 'Bird of Paradise', 'type': 'Tropical', 'description': 'The banana-like leaves on the bird of paradise are an attractive feature that makes them stand out. They love bright, indirect sunlight (at least six hours a day) and require constant misting during the spring and summer months.'},
#     {'name': 'Money Tree', 'type': 'Tropical', 'description': 'Native to Central and South America, the money tree, also known as pachira aquatic, grows between six and eight feet tall indoors. They are considered one of the best Feng Shui plants for good energy and wealth, and have shiny green leaves that symbolize the five elements of balance: earth, fire, water, wind and metal.'},
#     {'name': 'Cane Dragon Tree', 'type': 'Tropical', 'description': 'Otherwise known as the dracaena marginata, these ornamental houseplants have slim candelabra-shaped trunks and spiky leaves with hints of red. Indoors, they''ll grow to about six feet tall, making them striking additions to your greenery collection.'},
#     {'name': 'Fiddle Leaf Fig Tree', 'type': 'Tropical', 'description': 'Keep this tall plant in a space where it''ll receive tons of indirect sunlight — next to a large, sunny window with a sheer curtain, for example. The fiddle leaf will flourish in stable temperatures and is ideal for a bedroom or bathroom.'},
#     {'name': 'Braided Benjamina Ficus Tree', 'type': 'Tropical', 'description': 'The braided benjamina ficus tree is known for its braided trunk and weeping leaves. They enjoy bright, indirect light (at least six hours a day) and environments with high humidity.'},
#     {'name': 'Rubber Tree', 'type': 'Tropical', 'description': 'Based on Feng Shui principles, placing rubber plants in corners helps to soften sharp angles. They have shiny, thick leaves with hints of red and black tones, and can grow six to 10 feet tall indoors.'},
#     {'name': 'Ficus Audrey', 'type': 'Tropical', 'description': 'Also known as banyan trees, ficus audreys have emerald-green leaves and thick stems. Although they love bright, indirect sunlight, they can handle being in minimal direct sun and other unfavorable light conditions.'},
#     {'name': 'Peruvian Apple Cactus', 'type': 'Desert', 'description': 'This impressive cactus, also known the Queen of the Night, flowers throughout the summer. Their stunning flowers open for one night and close in the morning, but you can see this Cereus bloom all season long!'},
#     {'name': 'Pencil Cactus', 'type': 'Desert', 'description': 'This euphorbia has rigid, upright stalks that create a bush form as it grows. The lack of spikes makes it a better option for homes with pets or children, and it''s easy care makes it a good option for all plant lovers!'},
#     {'name': 'String of Pearls', 'type': 'Desert', 'description': 'String of pearls blooms in summer, producing ½ inch compound, daisy-like flowers of white discoid flowers with long red stamens and bright yellow anthers on 1½ inch long peduncles. The small flowers are not showy but are fragrant; it is said to have a sweet and spicy, cinnamon-like scent.'},
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

# code About view function to render about.html template
def about(request):
    return render(request, 'about.html')

# def plants_index(request):
#     return render(request, 'plants/index.html', {
#         'plants': plants
#     })

def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', # get all plants
    {
        'plants': plants
    }
    )

def plants_detail(request, plant_id ):
    plant = Plant.objects.get(id=plant_id)
    feeding_form = FeedingForm()
    return render(request, 'plants/detail.html', {
        'plant': plant, 'feeding_form': feeding_form
    })

def add_feeding(request, plant_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.plant_id = plant_id
        new_feeding.save()
    return redirect('detail', plant_id=plant_id)



class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'

class PlantUpdate(UpdateView):
  model = Plant
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['name', 'type', 'description']

class PlantDelete(DeleteView):
  model = Plant
  success_url = '/plants'