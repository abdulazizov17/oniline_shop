from django.shortcuts import render
def product_list(request):
    return render(request,'online_shop/home.html')
def comment_list(request):
    return render(request,'online_shop/detail.html')
# def order_list(request):
#     return render(request,)