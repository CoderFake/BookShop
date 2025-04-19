from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "Show"
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartitems = order['get_cart_items']
        user_not_login = "Show"
        user_login = "hidden"
    
    categories = Category.objects.filter(is_sub=True)
    products = Product.objects.all()
    
    context = {
        "categories": categories,
        "products": products,
        "cartitems": cartitems,
        "user_not_login": user_not_login,
        "user_login": user_login
    }
    
    return render(request, 'app/home.html', context)

def cart(request): 
    if request.user.is_authenticated: 
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items' : 0, "get_cart_total": 0}
        cartitems = order['get_cart_items']
    categories = Category.objects.filter(is_sub=True)
    context = {"items" : items, "order" : order, "cartitems": cartitems, "categories": categories}
    return render(request, 'app/Cart.html', context)


def checkout(request):
    if request.user.is_authenticated: 
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_items' : 0, "get_cart_total": 0}
        cartitems = order['get_cart_items']
    context = {"items" : items, "order" : order, "cartitems": cartitems}
    return render(request, 'app/Checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    product_id  = data['product_id']
    action = data['action']
    customer  = request.user
    product = Product.objects.get(id = product_id)   
    order, created = Order.objects.get_or_create(customer = customer, complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order = order, product = product)
    if action == "add":
        orderItem.quantity += 1 
    elif action == "remove":
        orderItem.quantity -= 1 
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse("added", safe= False)

def gioithieu(request):
    if request.user.is_authenticated: 
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items' : 0, "get_cart_total": 0}
        cartitems = order['get_cart_items']
    categories = Category.objects.filter(is_sub=True)
    context = {"items" : items, "order" : order, "cartitems": cartitems, "categories": categories}
    return render(request, 'app/Gioi_thieu.html', context)

def lienhe(request):
    if request.user.is_authenticated: 
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items' : 0, "get_cart_total": 0}
        cartitems = order['get_cart_items']
    categories = Category.objects.filter(is_sub=True)
    context = {"items" : items, "order" : order, "cartitems": cartitems,"categories": categories}
    return render(request, 'app/Lien_he.html', context)

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    categories = Category.objects.filter(is_sub=True)
    context = {"form": form, "categories": categories}
    return render(request, 'app/register.html', context)
    
def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password1")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("home")  
        else: 
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng")
    categories = Category.objects.filter(is_sub=True)
    context = {"categories": categories}
    return render(request, 'app/login.html', context)  

def logoutPage(request):
    logout(request)
    return redirect('login') 

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        keys = Product.objects.filter(name_product__contains = searched)
    if request.user.is_authenticated: 
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items' : 0, "get_cart_total": 0}
        cartitems = order['get_cart_items']
    product = Product.objects.all()
    return render(request, 'app/search.html', {"searched": searched, "keys":keys, "products": product, "cartitems": cartitems}) 

def category(request):
    categories = Category.objects.filter(is_sub= True)
    active_category = request.GET.get('category', '')
    if request.user.is_authenticated: 
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "Show"
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartitems = order['get_cart_items']
        user_not_login = "Show"
        user_login = "hidden"

    if active_category:
        products = Product.objects.filter(category__slug=active_category)

    context = {
        "categories": categories,
        "products": products,
        "active_category": active_category,
        "cartitems": cartitems
    }

    return render(request, 'app/category.html', context)

    
    return render(request, 'app/home.html', context)

def detail(request): 
    if request.user.is_authenticated: 
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items' : 0, "get_cart_total": 0}
        cartitems = order['get_cart_items']
    id = request.GET.get("id","")
    products = Product.objects.filter(id = id)
    categories = Category.objects.filter(is_sub=True)
    context = {"products":products,"items" : items, "order" : order, "cartitems": cartitems, "categories": categories}
    return render(request, 'app/detail.html', context)

def information(request):
    if request.user.is_authenticated: 
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items' : 0, "get_cart_total": 0}
        cartitems = order['get_cart_items']
    categories = Category.objects.filter(is_sub=True)
    context = {"items" : items, "order" : order, "cartitems": cartitems,"categories": categories}
    return render(request, 'app/Information.html', context)


from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect
from django.conf import settings

def place_order(request):
    if request.method == 'POST':
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        name = request.POST.get('name')
        phone = request.POST.get('Số điện thoại')
        address = request.POST.get('Địa chỉ')
        email = request.POST.get('email')
        shipping_method = request.POST.get('phuong-thuc-van-chuyen')
        payment_method = request.POST.get('phuong-thuc-thanh-toan')
        discount_code = request.POST.get('Mã giảm giá')
        
        shipping_address = ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=address,
            email=email,
            mobile=phone,
            phuong_thuc_van_chuyen=shipping_method,
            phuong_thuc_thanh_toan=payment_method
        )
        
        order.complete = True
        order.save()

        subject = 'Xác nhận đơn hàng'
        message = f'Cảm ơn bạn đã đặt hàng, {name}!\n\n'
        message += 'Thông tin đơn hàng của bạn:\n\n'
        

        for item in order.orderitem_set.all():
            message += f'Sản phẩm: {item.product.name_product}, Số lượng: {item.quantity}, Giá: {item.get_total} VNĐ\n'
        
        message += f'\nTổng tiền: {order.get_cart_total} VNĐ\n'
        message += 'Địa chỉ giao hàng: ' + address + '\n'
        message += 'Phương thức giao hàng: ' + shipping_method + '\n'
        message += 'Phương thức thanh toán: ' + payment_method + '\n'
        order.orderitem_set.all().delete()
        try:
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
        except Exception as e:
            messages.error(request, f'Có lỗi xảy ra khi gửi email: {e}')

        messages.success(request, 'Đặt hàng thành công! Một email xác nhận đã được gửi tới bạn.')
        return redirect('cart') 
    
    return redirect('cart')


