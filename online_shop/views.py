from typing import Optional

from django.shortcuts import render,redirect,get_object_or_404

from online_shop.models import Catagory, Product,Comment
from online_shop.forms import CommentModelForm,OrderModelForm


def product_list(request, catagory_id: Optional[int] = None):
    catagories = Catagory.objects.all().order_by(('id'))
    if catagory_id:
        products = Product.objects.filter(category=catagory_id)
    else:
        products = Product.objects.all()
    context = {'products': products,
               'catagories':catagories

               }

    return render(request, 'online_shop/home.html', context)


def product_detail(request, product_id):
    comments = Comment.objects.filter(product=product_id,is_provide=True).order_by('-id')
    product = Product.objects.get(id=product_id)
    context = {'product': product,
               'comments':comments
               }
    return render(request, 'online_shop/detail.html', context)

# def add_comment(request,product_id):
#     product = get_object_or_404(Product,id = product_id)
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email ')
#         body = request.POST.get('body')
#         commnet = Comment(name=name,email=email,body=body)
#         commnet.product=product
#         commnet.save()
#         return redirect('product_detail',product_id )
#
#     else:
#         pass
#     return render(request,'online_shop/detail.html')

def add_comment(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    if request.method =='POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product=product
            comment.save()
            return redirect('product_detail',product_id)
    else:
        form = CommentModelForm()

    return render(request,'online_shop/detail.html',{'form':form})

def add_order(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    if request.method=='POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            product.quantity -= int(form.data.get('quantity'))
            order = form.save(commit=False)
            order.product = product
            order.save()
            if order.quantity < product.quantity:
                return render(request, 'online_shop/detail.html', {'form': form, 'product': product, })
            order.save()
            return redirect('product_detail',product_id)
    else:
        form= OrderModelForm()
    contex = {'form':form,'product':product}
    return render(request,'online_shop/detail.html',contex)

