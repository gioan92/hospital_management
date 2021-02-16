class Chart:
    def __init__(self, cid, pid, did, tid, dcode, desc, nid, date):
        self.cid = cid;
        self.pid = pid;
        self.did = did;
        self.tid = tid;
        self.dcode = dcode;
        self.desc = desc;
        self.nid = nid;
        self.date = date;
    def __str__(self):
        return str(self.cid) + ' ' + str(self.pid) + ' ' + self.did + ' ' +\
               str(self.tid) + ' ' + str(self.dcode) + ' ' + self.desc + ' ' +\
               self.nid + ' ' + str(self.date);
class Treatment:
    def __init__(self, tid, did, pid, desc, date):
        self.tid = tid;
        self.did = did;
        self.pid = pid;
        self.desc = desc;
        self.date = date;
    def __str__(self):
        return str(self.tid) + ' ' + self.did + ' ' + str(self.pid) + ' ' +\
               self.desc + ' ' + str(self.date);

class Disease:
    def __init__(self, dcode, name):
        self.dcode = dcode;
        self.name = name;
    def __str__(self):
        return str(self.dcode) + ' ' + self.name;

class Doctor:
    def __init__(self, did, pwd, name, office, phone, dept, imgname):
        self.did = did;
        self.pwd = pwd;
        self.name = name;
        self.office = office;
        self.phone = phone;
        self.dept = dept;
        self.imgname = imgname;
    def __str__(self):
        return self.did + ' ' + self.pwd+ ' '+ self.name + ' ' + self.office + ' ' + self.phone + ' ' + self.dept + ' ' + self.imgname;
class Patient:
    def __init__(self, pid, roomNo, roomBed, name, date, phone, home):
        self.pid = pid;
        self.roomNo = roomNo;
        self.roomBed = roomBed;
        self.name = name;
        self.date = date;
        self.phone = phone;
        self.home = home;
    def __str__(self):
        return str(self.pid) + ' ' + self.roomNo + ' ' + str(self.roomBed) + ' ' +\
               self.name + ' ' + str(self.date) + ' ' + self.phone + ' ' + self.home;

class Room:
    def __init__(self, no, bed, rcode, peo):
        self.no = no;
        self.bed = bed;
        self.rcode = rcode;
        self.peo = peo;
    def __str__(self):
        return self.no + ' ' + str(self.bed) + ' ' + self.rcode + ' ' + str(self.peo);

class RoomDetail:
    def __init__(self, rcode, accom, codename):
        self.rcode = rcode;
        self.accom = accom;
        self.codename = codename;
    def __str__(self):
        return self.rcode + ' ' + str(self.accom) + ' ' + self.codename;
