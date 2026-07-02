from django.shortcuts import render, redirect

# ─── DUMMY DATA ───────────────────────────────────────────────
CATEGORIES = [
    {'id': 1, 'name': 'Electronics',  'icon': 'fa-solid fa-mobile-screen'},
    {'id': 2, 'name': 'Fashion',      'icon': 'fa-solid fa-shirt'},
    {'id': 3, 'name': 'Home & Living','icon': 'fa-solid fa-couch'},
    {'id': 4, 'name': 'Beauty',       'icon': 'fa-solid fa-wand-magic-sparkles'},
    {'id': 5, 'name': 'Toys',         'icon': 'fa-solid fa-gamepad'},
    {'id': 6, 'name': 'Sports',       'icon': 'fa-solid fa-dumbbell'},
    {'id': 7, 'name': 'Food',         'icon': 'fa-solid fa-bowl-food'},
    {'id': 8, 'name': 'Pets',         'icon': 'fa-solid fa-paw'},
    {'id': 9, 'name': 'Books',        'icon': 'fa-solid fa-book'},
    {'id':10, 'name': 'Automotive',   'icon': 'fa-solid fa-car'},
]

PRODUCTS = [
    {
        'id': 1,
        'name': 'Wireless Earbuds Pro X',
        'price': '999',
        'original_price': '1,499',
        'discount': 33,
        'rating': 4.8,
        'sales': 1200,
        'image': 'https://images.unsplash.com/photo-1590658268037-6bf12165a8df?q=80&w=400&auto=format&fit=crop',
        'is_flash': True,
        'description': 'High quality wireless earbuds with active noise cancellation and 30-hour battery life.',
    },
    {
        'id': 2,
        'name': 'Men Casual Cotton T-Shirt',
        'price': '199',
        'original_price': '350',
        'discount': 43,
        'rating': 4.5,
        'sales': 5400,
        'image': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?q=80&w=400&auto=format&fit=crop',
        'is_flash': True,
        'description': 'Comfortable premium cotton t-shirt. Available in 10 colors.',
    },
    {
        'id': 3,
        'name': 'Smart Watch Series X',
        'price': '1,299',
        'original_price': '1,999',
        'discount': 35,
        'rating': 4.6,
        'sales': 210,
        'image': 'https://images.unsplash.com/photo-1579586337278-3befd40fd17a?q=80&w=400&auto=format&fit=crop',
        'is_flash': True,
        'description': 'Fitness tracker with heart rate monitor, GPS, and 7-day battery.',
    },
    {
        'id': 4,
        'name': 'Minimalist LED Desk Lamp',
        'price': '450',
        'original_price': '600',
        'discount': 25,
        'rating': 4.9,
        'sales': 320,
        'image': 'https://images.unsplash.com/photo-1513506003901-1e6a229e9d15?q=80&w=400&auto=format&fit=crop',
        'is_flash': False,
        'description': 'Touch-sensitive LED desk lamp with adjustable brightness and warm/cool modes.',
    },
    {
        'id': 5,
        'name': 'Vitamin C Brightening Serum',
        'price': '299',
        'original_price': '450',
        'discount': 33,
        'rating': 4.7,
        'sales': 890,
        'image': 'https://images.unsplash.com/photo-1620916566398-39f1143ab7be?q=80&w=400&auto=format&fit=crop',
        'is_flash': False,
        'description': 'Anti-aging brightening face serum with 20% Vitamin C complex.',
    },
    {
        'id': 6,
        'name': 'Running Shoes Air Boost',
        'price': '1,890',
        'original_price': '2,500',
        'discount': 24,
        'rating': 4.4,
        'sales': 670,
        'image': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=400&auto=format&fit=crop',
        'is_flash': False,
        'description': 'Lightweight running shoes with air cushion sole for maximum comfort.',
    },
    {
        'id': 7,
        'name': 'Portable Bluetooth Speaker',
        'price': '799',
        'original_price': '1,200',
        'discount': 33,
        'rating': 4.6,
        'sales': 455,
        'image': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?q=80&w=400&auto=format&fit=crop',
        'is_flash': False,
        'description': 'Waterproof 360° sound Bluetooth speaker with 20-hour playback.',
    },
    {
        'id': 8,
        'name': 'Mechanical Gaming Keyboard',
        'price': '1,590',
        'original_price': '2,100',
        'discount': 24,
        'rating': 4.8,
        'sales': 1100,
        'image': 'https://images.unsplash.com/photo-1618384887929-16ec33fab9ef?q=80&w=400&auto=format&fit=crop',
        'is_flash': False,
        'description': 'RGB mechanical gaming keyboard with cherry MX red switches.',
    },
    {
        'id': 9,
        'name': 'Ceramic Coffee Mug Set',
        'price': '349',
        'original_price': '490',
        'discount': 29,
        'rating': 4.7,
        'sales': 780,
        'image': 'https://images.unsplash.com/photo-1514228742587-6b1558fcca3d?q=80&w=400&auto=format&fit=crop',
        'is_flash': False,
        'description': 'Set of 4 handcrafted ceramic mugs with minimalist design.',
    },
    {
        'id': 10,
        'name': 'Yoga Mat Premium Non-Slip',
        'price': '590',
        'original_price': '800',
        'discount': 26,
        'rating': 4.9,
        'sales': 2300,
        'image': 'https://images.unsplash.com/photo-1601925228008-4de7ef6ea1da?q=80&w=400&auto=format&fit=crop',
        'is_flash': False,
        'description': 'Extra thick 6mm non-slip yoga mat with carry strap and alignment lines.',
    },
    {
        'id': 11,
        'name': 'Stainless Steel Water Bottle',
        'price': '250',
        'original_price': '380',
        'discount': 34,
        'rating': 4.5,
        'sales': 3100,
        'image': 'https://images.unsplash.com/photo-1602143407151-7111542de6e8?q=80&w=400&auto=format&fit=crop',
        'is_flash': False,
        'description': 'Double-wall insulated bottle, keeps drinks cold 24h / hot 12h.',
    },
    {
        'id': 12,
        'name': 'Wireless Phone Charger Pad',
        'price': '390',
        'original_price': '550',
        'discount': 29,
        'rating': 4.6,
        'sales': 980,
        'image': 'https://images.unsplash.com/photo-1633269540827-728aabbb7646?q=80&w=400&auto=format&fit=crop',
        'is_flash': False,
        'description': '15W fast wireless charging pad compatible with all Qi devices.',
    },
]

VOUCHERS = [
    {'value': '฿30 OFF',   'condition': 'Min. spend ฿199',    'code': 'SAVE30'},
    {'value': '20% OFF',   'condition': 'All Electronics',    'code': 'ELEC20'},
    {'value': 'FREE SHIP', 'condition': 'All Orders Today',   'code': 'FREESHIP'},
    {'value': '฿100 OFF',  'condition': 'Min. spend ฿999',   'code': 'BIG100'},
]

# ─── MOCK CART stored in session ─────────────────────────────
def get_cart(request):
    return request.session.get('cart', {})

def get_cart_items(cart):
    items = []
    for pid, qty in cart.items():
        product = next((p for p in PRODUCTS if str(p['id']) == str(pid)), None)
        if product:
            items.append({'product': product, 'quantity': qty,
                          'subtotal': int(product['price'].replace(',','')) * qty})
    return items

def get_cart_count(request):
    cart = get_cart(request)
    return sum(cart.values())

# ─── VIEWS ───────────────────────────────────────────────────
def home(request):
    flash_deals = [p for p in PRODUCTS if p['is_flash']]
    return render(request, 'chopee/home.html', {
        'categories': CATEGORIES,
        'flash_deals': flash_deals,
        'products': PRODUCTS,
        'vouchers': VOUCHERS,
        'cart_count': get_cart_count(request),
    })

def product_detail(request, product_id):
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if not product:
        return redirect('chopee:home')
    related = [p for p in PRODUCTS if p['id'] != product_id][:4]
    return render(request, 'chopee/product_detail.html', {
        'product': product,
        'related': related,
        'cart_count': get_cart_count(request),
    })

def cart(request):
    cart_data = get_cart(request)
    items = get_cart_items(cart_data)
    total = sum(i['subtotal'] for i in items)
    return render(request, 'chopee/cart.html', {
        'items': items,
        'total': f'{total:,}',
        'cart_count': get_cart_count(request),
    })

def add_to_cart(request, product_id):
    cart_data = get_cart(request)
    pid = str(product_id)
    cart_data[pid] = cart_data.get(pid, 0) + 1
    request.session['cart'] = cart_data
    request.session.modified = True
    return redirect('chopee:cart')

def remove_from_cart(request, product_id):
    cart_data = get_cart(request)
    pid = str(product_id)
    if pid in cart_data:
        del cart_data[pid]
    request.session['cart'] = cart_data
    request.session.modified = True
    return redirect('chopee:cart')

def checkout(request):
    cart_data = get_cart(request)
    items = get_cart_items(cart_data)
    total = sum(i['subtotal'] for i in items)

    if request.method == 'POST' and items:
        # Clear cart and redirect to mock order tracking
        request.session['cart'] = {}
        request.session['last_order'] = {
            'name': request.POST.get('name', 'Customer'),
            'address': request.POST.get('address', '-'),
            'total': f'{total:,}',
            'items': items,
        }
        return redirect('chopee:order_tracking', order_id=1001)

    return render(request, 'chopee/checkout.html', {
        'items': items,
        'total': f'{total:,}',
        'cart_count': get_cart_count(request),
    })

def order_tracking(request, order_id):
    order = request.session.get('last_order', {
        'name': 'Demo Customer',
        'address': '123 Main Street, Bangkok 10110',
        'total': '2,298',
        'items': [],
    })
    return render(request, 'chopee/order_tracking.html', {
        'order_id': order_id,
        'order': order,
        'cart_count': 0,
    })
