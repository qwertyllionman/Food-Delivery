from django.shortcuts import render

# Create your views here.
"""
Delivery uchun CRUD operatsiyalari bo'ladi
Create:
    Delivery yaratilganda overall price avtomatik hisoblanadi restarantni delivery_fee siga qo'shiladi
    Many to many bo'lib bog'lanadi Delivery Detail ga (qaysi food qaysi deliveryga tegishli ekanligi) 
    
GET:
    barcha deliverylar olinadi (listda) (User olinganda unga tegishli deliverylarni ham chiqarish mumkin)
    Ma'lum bir delivery ham id bo'yicha olinadi
    
PUT/PATCH:
    Delivery statusi o'zgarib turadi (Preparing, Delivering, Delivered, Canceled)

Ushbu joyda DELETE methodi bo'lishi mumkin edi lekin DELETE o'rniga historyga qo'shiladi COMPLETED
yoki CANCELED statusli deliverylar 
"""
