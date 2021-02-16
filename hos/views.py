from django.http import JsonResponse
from django.shortcuts import render, redirect
# Create your views here.
import ctypes  # An included library with Python install.

from config.settings import UPLOAD_DIR
from frame.error import ErrorCode
from frame.util import PatientDb, DoctorDb, ChartDb, DiseaseDb, TreatmentDb


def graph(request):
    beds = 19;
    patients = PatientDb().select();
    patNum = patients[-1].pid;
    print(patNum);
    datas= [
            ['Empty beds', beds - patNum],
            ['Patients', patNum],
        ]
    context = {
      'datas':datas
    };
    return JsonResponse(context);

def graph1(request):
    charts = ChartDb().select();
    temp = {};
    data = {};
    for c in charts:
        temp[c.pid] = DiseaseDb().selectone(c.dcode).name;
    temp1 = sorted(list(temp.values()));
    for t in temp1:
        if t not in data:
            data[t] = 1;
        else:
            data[t] += 1;
    label = list(data.keys());
    yval = list(data.values());
    datas= {
            'label':label,
            'yval':yval,
    }
    context = {
      'datas':datas
    };
    return JsonResponse(context);


def index(request):
    doctors = DoctorDb().select();
    patients = PatientDb().select();
    context={
        'menu':1,
        'section':'index.html',
        'doctNum':doctors.index(doctors[-1]) + 1,
        'patNum':patients.index(patients[-1]) + 1,
        'loginuser': DoctorDb().selectone(request.session['suser']),
    };
    return render(request, 'base.html', context);


### Doctor 관련 ###
def doctors(request):
    rdoctors = DoctorDb().select();

    dd = [];
    for d in rdoctors:
        if d.dept not in dd:
            dd.append(d.dept);
    context={
        'menu': 3,
        'section':'doctors.html',
        'doctors':rdoctors,
        'doc_deptlist': dd,
        'loginuser': DoctorDb().selectone(request.session['suser']),
    };
    return render(request, 'base.html', context);

def add_doctor(request):
    context={
        'menu': 3,
        'section': 'add-doctor.html',
        'loginuser': DoctorDb().selectone(request.session['suser']),
    };
    return render(request, 'base.html',context);

def docaddimpl(request):
    id = request.POST['id'];
    pwd = request.POST['pwd'];
    name = request.POST['name'];
    office = request.POST['office'];
    phone = request.POST['phone'];
    dept = request.POST['dept'];
    imgname = '';
    if 'img' in request.FILES:
        img = request.FILES['img']
        imgname = img._name

        fp = open('%s/%s' % (UPLOAD_DIR, imgname), 'wb')
        for chunk in img.chunks():
            fp.write(chunk);
            fp.close();

    DoctorDb().insert(id, pwd, name, office, phone, dept, imgname);
    return redirect('doctors');

def doc_patientlist(request):
    did = request.GET['id'];
    docplist = DoctorDb().selectone(did);
    chartinfo = ChartDb().select();
    cpatient = PatientDb().select();
    context={
        'doc_patient': docplist,
        'chartinfo': chartinfo,
        'cpatient': cpatient
    };
    return render(request, 'doc_patientlist.html',context);

def docdelete(request):
    did = request.GET['id'];
    try:
        DoctorDb().delete(did);
    except:

        return render(request,'doc_delete_error.html');
    return redirect('doctors');


def add_treatment(request):
    did = request.GET['id'];
    doc = DoctorDb().selectone(did);
    spatientlist = PatientDb().select();
    context={
        'menu': 3,
        'section': 'add_treatment.html',
        'doc': doc,
        'rsusers': spatientlist,
        'loginuser': DoctorDb().selectone(request.session['suser']),
    };
    return render(request, 'base.html',context);


def treataddimpl(request):
    doctorid = request.POST['doctorid'];
    patientid = request.POST['pid'];
    treat_desc = request.POST['treatment'];
    try:
        TreatmentDb().insert(doctorid, int(patientid), treat_desc);
    except:
        context={
            'section':'treat_insert_error.html'
        };
        return render(request, 'doctors', context);
    return redirect('doctors');


def add_chart(request):
    did = request.GET['id'];
    doc = DoctorDb().selectone(did);
    spatientlist = PatientDb().select();
    atreatment = TreatmentDb().select();
    adisease = DiseaseDb().select();
    context={
        'menu': 3,
        'section': 'add_chart.html',
        'doc': doc,
        'rsusers': spatientlist,
        'treat': atreatment,
        'diseasecode':adisease,
        'loginuser': DoctorDb().selectone(request.session['suser']),
    };
    return render(request, 'base.html',context);

def chartaddimpl(request):
    doctorid = request.POST['doctorid'];
    cpatientid = request.POST['patid'];
    treatid = request.POST['tid'];
    discode = request.POST['dicode'];
    nurid = request.POST['nid'];
    try:
        ChartDb().insert( int(cpatientid), doctorid, int(treatid), int(discode), nurid);
    except:
        context={
            'section':'treat_insert_error.html'
        };
        return render(request, 'doctors', context);
    return redirect('doctors');
### Doctor 관련 끝 ###


### Patients 관련 ###
def patients(request):
    spatientlist = PatientDb().select();
    context={
        'menu':4,
        'section':'patients.html',
        'patientlist.html':'patientlsit.html',
        'rsusers':spatientlist,
        'loginuser': DoctorDb().selectone(request.session['suser']),
    };
    return render(request, 'base.html',context);

def add_patient(request):
    context={
        'menu': 4,
        'section': 'add-patient.html',
        'loginuser': DoctorDb().selectone(request.session['suser']),
    };
    return render(request, 'base.html',context);

def patientaddimpl(request):
    name = request.POST['name'];
    roomno = request.POST['roomno'];
    roombed = request.POST['roombed'];
    phone = request.POST['phone'];
    home = request.POST['home'];
    try:
        PatientDb().insert(roomno, int(roombed), name, phone, home);
    except:
        context={
            'section':'pat_insert_error.html'
        };
        return render(request,'patients',context);
    return redirect('patients');



def getchart(request):
    pid = request.GET['id'];
    context = {
        'pid':pid,
    };
    return JsonResponse(context);

def chart(request):
    pid = request.GET['id'];
    cpatient = PatientDb().selectone(int(pid));
    chartinfo = ChartDb().selectone(int(pid));
    allchartinfo = ChartDb().select();
    alltreat = TreatmentDb().select();
    context = {
        'chartpatient': cpatient,
        'chartinfo': chartinfo,
        'allchartinfo': allchartinfo,
        'alltreat': alltreat,
    };
    return render(request,'chart.html',context);
### Patients 관련 끝 ###



def hospitalstructure(request):
    patients = PatientDb().select();
    context={
        'patient': patients,
        'menu':2,
        'section':'hospitalstructure.html' ,
        'loginuser': DoctorDb().selectone(request.session['suser']),
    };
    return render(request, 'base.html', context);

##########################################################
def login(request):
    context = {
        'section': 'login.html'
    };
    return render(request, 'loginpage.html',context);

def loginimpl(request):
    try:
        did = request.POST['id'];
        pwd = request.POST['pwd'];
    except:
        if 'suser' in request.session:
            context = {
                'section':'loginok.html',
                'loginuser': DoctorDb().selectone(request.session['suser']),
            };
        else:
            context = {
                'section': 'login.html'
            };
    else:
        try:
            doctor = DoctorDb().selectone(did);
            if pwd == doctor.pwd:
                # logger.debug(id);
                request.session['suser']= did;
                context = {
                    'section': 'loginok.html',
                    'loginuser': doctor
                }
            else:
                raise Exception;
        except:
            context = {
                'section': 'error.html',
                'error': ErrorCode().e0003
            }
    return render(request, 'loginpage.html',context);

def logout(request):
    if request.session['suser'] != None:
        del request.session['suser'];
    return render(request, 'loginpage.html');

def firstfloor(request):
    patients = PatientDb().select();
    context = {
        'menu': 2,
        'patient': patients,
        'section':'hospitalstructure.html',
        'content1':'firstfloor.html',
        'loginuser': DoctorDb().selectone(request.session['suser']),
    }
    return render(request, "base.html", context)

def secondfloor(request):
    patients = PatientDb().select();
    context = {
        'menu': 2,
        'patient': patients,
        'section': 'hospitalstructure.html',
        'content1':'secondfloor.html',
        'loginuser': DoctorDb().selectone(request.session['suser']),
    }
    return render(request, "base.html", context)

def thirdfloor(request):
    patients = PatientDb().select();
    context = {
        'menu': 2,
        'patient': patients,
        'section': 'hospitalstructure.html',
        'content1':'thirdfloor.html',
        'loginuser': DoctorDb().selectone(request.session['suser']),
    }
    return render(request, "base.html", context)

def popup101(request):
    patients = PatientDb().select();
    context = {
        'patient': patients
    };
    return render(request, 'popup101.html', context);

def popup102(request):
    patients = PatientDb().select();
    context = {
        'patient': patients
    };
    return render(request, 'popup102.html', context);

def popup103(request):
    patients = PatientDb().select();
    context = {
        'patient': patients
    };
    return render(request, 'popup103.html', context);

def popup201(request):
    patients = PatientDb().select();
    context = {
        'patient': patients
    };
    return render(request, 'popup201.html', context);

def popup202(request):
    patients = PatientDb().select();
    context = {
        'patient': patients
    };
    return render(request, 'popup202.html', context);

def popup203(request):
    patients = PatientDb().select();
    context = {
        'patient': patients
    };
    return render(request, 'popup203.html', context);

def popup301(request):
    patients = PatientDb().select();
    context = {
        'patient': patients
    };
    return render(request, 'popup301.html', context);

def popup302(request):
    patients = PatientDb().select();
    context = {
        'patient': patients
    };
    return render(request, 'popup302.html', context);



# Guest용
def guest_index(request):
    doctors = DoctorDb().select();
    patients = PatientDb().select();
    context={
        'menu':1,
        'section':'guest_index.html',
        'doctNum':doctors.index(doctors[-1]) + 1,
        'patNum':patients.index(patients[-1]) + 1,
    };
    return render(request, 'guest_base.html', context);

def guest_doctors(request):
    rdoctors = DoctorDb().select();
    dd = [];
    for d in rdoctors:
        if d.dept not in dd:
            dd.append(d.dept);
    context={
        'menu':3,
        'section':'guest_doctors.html',
        'doctors':rdoctors,
        'doc_deptlist': dd,
    };
    return render(request, 'guest_base.html', context);

def guest_hospitalstructure(request):
    patients = PatientDb().select();
    context={
        'menu':2,
        'patient': patients,
        'section':'guest_hospitalstructure.html' ,
    };
    return render(request, 'guest_base.html', context);

def guest_firstfloor(request):
    patients = PatientDb().select();
    context = {
        'menu': 2,
        'patient': patients,
        'section':'guest_hospitalstructure.html',
        'content1':'guest_firstfloor.html'
    }
    return render(request, "guest_base.html", context);

def guest_secondfloor(request):
    patients = PatientDb().select();
    context = {
        'menu': 2,
        'patient': patients,
        'section': 'guest_hospitalstructure.html',
        'content1':'guest_secondfloor.html'
    }
    return render(request, "guest_base.html", context);

def guest_thirdfloor(request):
    patients = PatientDb().select();
    context = {
        'menu': 2,
        'patient': patients,
        'section': 'guest_hospitalstructure.html',
        'content1':'guest_thirdfloor.html'
    }
    return render(request, "guest_base.html", context);


def guest_popup101(request):
    patients = PatientDb().select();
    context = {
        'patient': patients
    };
    return render(request, 'guest_popup101.html', context);

def guest_popup102(request):
    patients = PatientDb().select();
    context = {
        'patient': patients
    };
    return render(request, 'guest_popup102.html', context);

def guest_popup103(request):
    patients = PatientDb().select();
    context = {
        'patient': patients
    };
    return render(request, 'guest_popup103.html', context);

def guest_popup201(request):
    patients = PatientDb().select();
    context = {
        'patient': patients
    };
    return render(request, 'guest_popup201.html', context);

def guest_popup202(request):
    patients = PatientDb().select();
    context = {
        'patient': patients
    };
    return render(request, 'guest_popup202.html', context);

def guest_popup203(request):
    patients = PatientDb().select();
    context = {
        'patient': patients
    };
    return render(request, 'guest_popup203.html', context);

def guest_popup301(request):
    patients = PatientDb().select();
    context = {
        'patient': patients
    };
    return render(request, 'guest_popup301.html', context);

def guest_popup302(request):
    patients = PatientDb().select();
    context = {
        'patient': patients
    };
    return render(request, 'guest_popup302.html', context);



