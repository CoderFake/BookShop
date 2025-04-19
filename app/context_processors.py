from .models import Link, Category

def global_links(request):
    categories = Category.objects.all()
    print("Danh mục con", categories)
    links = Link.objects.all()
    print("Danh mục", links)
    return {'global_links': links,'global_category': categories}