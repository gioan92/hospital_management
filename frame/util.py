from frame.db import Db
from frame.sql import Sql
from frame.table import Doctor, Patient, Chart, Treatment, Disease, Room, RoomDetail


class ChartDb(Db):
    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.chartlist);
        result = cursor.fetchall();
        all = [];
        for c in result:
            chart = Chart(c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7]);
            all.append(chart);
        super().close(conn,cursor);
        return all;

    def selectone(self, pid):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.chartone % (pid));
        results = cursor.fetchall();
        result = None;
        for r in results:
            if result is None:
                result = r;
            else:
                if r[0] > result[0]:
                    result = r;
        chart = Chart(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7]);
        super().close(conn,cursor);
        return chart;

    def insert(self, pid, did, tid, dcode, nid):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.chartinsert % ( pid, did, tid, dcode, nid));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);


class TreatmentDb(Db):
    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.treatmentlist);
        result = cursor.fetchall();
        all = [];
        for t in result:
            treatment = Treatment(t[0], t[1], t[2], t[3], t[4]);
            all.append(treatment);
        super().close(conn,cursor);
        return all;

    def selectone(self, tid):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.treatmentone % (tid));
        result = cursor.fetchone();
        treatment = Treatment(result[0], result[1], result[2], result[3], result[4]);
        super().close(conn,cursor);
        return treatment;

    def insert(self, did, pid, desc):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.treatmentinsert % (did, pid, desc));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

class DiseaseDb(Db):
    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.diseaselist);
        result = cursor.fetchall();
        all = [];
        for d in result:
            disease = Disease(d[0], d[1]);
            all.append(disease);
        super().close(conn,cursor);
        return all;

    def selectone(self, dcode):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.diseaseone % (dcode));
        result = cursor.fetchone();
        disease = Disease(result[0], result[1]);
        super().close(conn,cursor);
        return disease;

class DoctorDb(Db):
    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.doctorlist);
        result = cursor.fetchall();
        all = [];
        for d in result:
            doctor = Doctor(d[0], d[1], d[2], d[3], d[4], d[5], d[6]);
            all.append(doctor);
        super().close(conn,cursor);
        return all;

    def selectone(self, did):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.doctorone % (did));
        result = cursor.fetchone();
        doctor = Doctor(result[0], result[1], result[2], result[3], result[4], result[5], result[6]);
        super().close(conn,cursor);
        return doctor;

    def insert(self, did, pwd, name, office, phone, dept, imgname):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.doctorinsert % (did, pwd, name, office, phone, dept, imgname));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

    def delete(self,did):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.docdelete % (did));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);


class PatientDb(Db):
    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.patientlist);
        result = cursor.fetchall();
        all = [];
        for p in result:
            patient = Patient(p[0], p[1], p[2], p[3], p[4], p[5], p[6]);
            all.append(patient);
        super().close(conn,cursor);
        return all;

    def selectone(self, pid):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.patientone % (pid));
        result = cursor.fetchone();
        patient = Patient(result[0], result[1], result[2], result[3], result[4], result[5], result[6]);
        super().close(conn,cursor);
        return patient;

    def insert(self, roomNo, roomBed, name, phone, home):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.patientinsert % (roomNo, int(roomBed), name, phone, home));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

class RoomDb(Db):
    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.roomlist);
        result = cursor.fetchall();
        all = [];
        for r in result:
            room = Room(r[0], r[1], r[2], r[3]);
            all.append(room);
        super().close(conn,cursor);
        return all;

class RoomDetailDb(Db):
    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.roomdetaillist);
        result = cursor.fetchall();
        all = [];
        for r in result:
            room = RoomDetail(r[0], r[1], r[2]);
            all.append(room);
        super().close(conn,cursor);
        return all;

    def selectone(self, rcode):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.roomdetailone % (rcode));
        result = cursor.fetchone();
        roomdetail = RoomDetail(result[0], result[1], result[2]);
        super().close(conn,cursor);
        return roomdetail;

#---------------------------------------------------------------------
#--test function--
# 차트 테이블
def chartlist_test():
    charts = ChartDb().select();
    for c in charts:
        print(c);
def chartone_test():
    chart = ChartDb().selectone(10);
    print(chart);

# 진료 테이블
def treatmentlist_test():
    treatments = TreatmentDb().select();
    for t in treatments:
        print(t);
def treatmentone_test():
    treatment = TreatmentDb().selectone(9);
    print(treatment);

# 질병 테이블
def diseaselist_test():
    diseases = DiseaseDb().select();
    for d in diseases:
        print(d);
def diseaseone_test():
    disease = DiseaseDb().selectone(4);
    print(disease);

# 의사 테이블
def doctorlist_test():
    doctors = DoctorDb().select();
    for d in doctors:
        print(d);
def doctorone_test():
    doctor = DoctorDb().selectone('doc04');
    print(doctor);

# 환자 테이블
def patientlist_test():
    patients = PatientDb().select();
    for p in patients:
        print(p);
def patientone_test():
    patient = PatientDb().selectone(7);
    print(patient);

def roomlist_test():
    rooms = RoomDb().select();
    for r in rooms:
        print(r);

def roomdetaillist_test():
    rooms = RoomDetailDb().select();
    for r in rooms:
        print(r);
def roomdetailone_test():
    room = RoomDetailDb().selectone('b');
    print(room);


if __name__=='__main__':
    pp = {};
    pp['suser'] = 'doc01';
    if pp['suser'] != None:
        del pp['suser'];
    if 'suser' in pp:
        print('있음');
    else:
        print('없음');

