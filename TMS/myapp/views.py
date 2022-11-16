from datetime import datetime, timedelta
from django.contrib import auth
from django.shortcuts import render, redirect
from .models import Landlord, Property, House, Tenant, HouseAllocation, Payment, Turnover
import pandas as pd
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def loginUser(request):
    if request.method == 'POST':
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')

        user = auth.authenticate(username=username1, password=password1)

        if user is not None:
            login(request, user)
            return redirect('/index')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


@login_required(login_url="/")
def logoutUser(request):
    logout(request)
    return redirect('/')


@login_required(login_url="/")
def index(request):
    turn = Turnover.objects.all()
    amt = []
    for p in turn:
        amt.append(p.amount)

    amt = [int(i) for i in amt]
    total = sum(amt)

    pstat = Payment.objects.all()

    mn = datetime.today()
    dat = mn.strftime("%B-%Y")

    act = []
    tt = Tenant.objects.all()
    ac = HouseAllocation.objects.filter(status="Allocated")

    hse = House.objects.all()
    for i in tt:
        ti = i.tid
    for h in ac:
        act.append(h.tname)

    active = len(act)

    for i in hse:
        hon = i.hid

    free = hon - active

    return render(request, 'index.html',
                  {'ti': ti, 'active': active, 'hon': hon, 'free': free, 'dat': dat, 'pstat': pstat,
                   'total': total})


@login_required(login_url="/")
def registerlandlord(request):
    if request.method == "POST":
        name = request.POST.get('name')
        spouse = request.POST.get('spouse')
        id = request.POST.get('id')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        ld = Landlord(name=name, spouse=spouse, id=id, email=email, phone=phone, address=address, gender=gender,
                      date=datetime.today())
        ld.save()

    return render(request, 'registerlandlord.html')


@login_required(login_url="/")
def registerproperty(request):
    var = Landlord.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        hn = request.POST.get('hn')
        location = request.POST.get('location')
        landlord = request.POST.get('landlord')

        pr = Property(name=name, hn=hn, location=location, landlord=landlord, date=datetime.today())
        pr.save()

    return render(request, 'registerproperty.html', {'var': var})


@login_required(login_url="/")
def propertylist(request):
    pr = Property.objects.all()
    return render(request, 'propertylist.html', {'pr': pr})


@login_required(login_url="/")
def landlordlist(request):
    lad = Landlord.objects.all()
    return render(request, 'landlordlist.html', {'lad': lad})


@login_required(login_url="/")
def registerhouse(request):
    pro = Property.objects.all()
    if request.method == "POST":
        hname = request.POST.get('name')
        desc = request.POST.get('desc')
        hrent = request.POST.get('hrent')
        type = request.POST.get('type')
        property = request.POST.get('property')

        hr = House(housename=hname, desc=desc, hrent=hrent, type=type, property=property, date=datetime.today())
        hr.save()

    return render(request, 'registerhouse.html', {'pro': pro})


@login_required(login_url="/")
def houselist(request):
    hl = House.objects.all()
    if request.method == "POST":
        delete = request.POST.get('delete')
        de = hl.filter(hid=delete)
        de.delete()
        return redirect('/houselist')

    return render(request, 'houselist.html', {'hl': hl})


@login_required(login_url="/")
def allocated(request):
    hal = HouseAllocation.objects.all()
    if request.method == "POST":
        hid = request.POST.get('vacate')
        vac = hal.filter(hid=hid)
        if vac.exists():
            vac.update(status="Vacant")
            return redirect('/allocated')
        else:
            return redirect('/allocated')

    return render(request, 'allocated.html', {'hal': hal})


@login_required(login_url="/")
def tenantregister(request):
    global tname
    global ten
    if request.method == "POST":
        tname = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        idtype = request.POST.get('idtype')
        idn = request.POST.get('idn')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')

        ten = Tenant(name=tname, email=email, phone=phone, address=address, idtype=idtype, idn=idn, dob=dob,
                     gender=gender, date=datetime.today())

        return redirect('/addhouse')

    return render(request, 'registertenant.html')


@login_required(login_url="/")
def addhouse(request):
    ha = HouseAllocation.objects.all()
    hn = House.objects.all()
    if request.method == "POST":
        house = request.POST.get('house')
        deposit = request.POST.get('deposit')
        had = ha.filter(housename=house)

        if had.exists():
            for i in had:
                st = i.status
            if st == "Allocated":
                return render(request, 'housefull.html')
            elif st == "Vacant":
                ho = HouseAllocation(tname=tname, housename=house, status="Allocated", deposit=deposit,
                                     date=datetime.today())
                ten.save()
                ho.save()
            return redirect('/tenantregister')

        else:
            ho = HouseAllocation(tname=tname, housename=house, status="Allocated", deposit=deposit,
                                 date=datetime.today())

            ten.save()
            ho.save()

            return redirect('/tenantregister')

    return render(request, 'addhouse.html', {'hn': hn, 'tname': tname})


@login_required(login_url="/")
def tenantlist(request):
    tr = Tenant.objects.all()
    return render(request, 'tenantlist.html', {'tr': tr})


@login_required(login_url="/")
def payrent(request):
    ha = HouseAllocation.objects.all()
    hal = ha.filter(status="Allocated")

    if request.method == "POST":
        amount = request.POST.get('amount')
        pmonth = request.POST.get('pmonth')
        amount = int(amount)
        pn = request.POST.get('pay')

        tn = Tenant.objects.filter(name=pn)
        for q in tn:
            idi = q.idn

        hse = ha.filter(status="Allocated") & ha.filter(tname=pn)
        for i in hse:
            house = i.housename

        hr = House.objects.all()
        ren = hr.filter(housename=house)
        for i in ren:
            hrent = int(i.hrent)
            pmt = Payment.objects.all()
            pchk = pmt.filter(name=pn) & pmt.filter(month=pmonth)

            if pchk.exists():
                for h in pchk:
                    bal = int(h.balance)
                    newbal2 = bal - amount
                    if newbal2 > 0:
                        status = "Unpaid"
                    elif newbal2 < 0:
                        status = "Adv. Payment"
                    else:
                        status = "Paid"

                    pchk.update(balance=newbal2, amount=amount, status=status)

                    turn = Turnover(name=pn, id=idi, amount=amount, date=datetime.today())
                    turn.save()
                    return redirect('/payrent')

            else:
                newbal = hrent - amount
                if newbal > 0:
                    status = "Unpaid"
                elif newbal < 0:
                    status = "Adv. Payment"
                else:
                    status = "Paid"

                pay = Payment(name=pn, house=house, hrent=hrent, month=pmonth, amount=amount, balance=newbal,
                              status=status,
                              date=datetime.today())
                pay.save()

                turn = Turnover(name=pn, id=idi, amount=amount, date=datetime.today())
                turn.save()
                return redirect('/payrent')

    return render(request, 'payrent.html', {'hal': hal})


@login_required(login_url="/")
def paymentstatus(request):
    pstat = Payment.objects.all()
    return render(request, 'paymentstatus.html', {'pstat': pstat})


@login_required(login_url="/")
def turnover(request):
    turn = Turnover.objects.all()
    amt = []
    for p in turn:
        amt.append(p.amount)

    amt = [int(i) for i in amt]
    totalsum = sum(amt)

    return render(request, 'turnover.html', {'turn': turn, 'totalsum': totalsum})


@login_required(login_url="/")
def duelist(request):
    per = HouseAllocation.objects.filter(status="Allocated")

    list = []

    rent = []

    for i in per:

        dt = i.date
        hy = i.housename

        mn = datetime.today()
        month = mn.strftime("%B")

        lt = [i.strftime("%B") for i in pd.date_range(start=dt, end=mn, freq='MS')]
        list.append(lt)

        num = (mn.year - dt.year) * 12 + (mn.month - dt.month)

        hrt = House.objects.filter(housename=hy)
        for g in hrt:
            tp = int(g.hrent)
            rent.append(num * tp)

    return render(request, 'duelist.html', {'per': per, 'list': list, 'rent': rent})


@login_required(login_url="/")
def invoice(request):
    inv = Payment.objects.all()
    tn = Tenant.objects.all()
    hr = House.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        tname = request.POST.get('tname')
        mn = request.POST.get('month')
        var = mn.split('-')
        mnt = int(var[1])
        year = int(var[0])

        month = datetime(year, mnt, 1).strftime('%B')

        if name:
            ine = inv.filter(name=name) & inv.filter(month=month)
        elif tname:
            ine = inv.filter(name=tname) & inv.filter(month=month)

        for e in ine:
            tt = e.name
            house = e.house
            ten = tn.filter(name=tt)
            for t in ten:
                tname = t.name
                email = t.email
                phone = t.phone
        hre = hr.filter(housename=house)
        for h in hre:
            hrent = h.hrent

        today = datetime.now()
        due = today + timedelta(days=7)

        duedate = due.strftime('%d-%m-%Y')

        return render(request, 'bill.html',
                      {'ine': ine, 'today': today, 'duedate': duedate, 'tname': tname, 'email': email, 'phone': phone,
                       'house': house, 'month': month, 'hrent': hrent})

    return render(request, 'invoice.html', {'inv': inv})
