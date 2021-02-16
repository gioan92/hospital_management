## v06 수정내용 

# chart, treatment TABLE 16번 insert문 추가
# room TABLE room_peo COLUMN 삭제
# treatment 오타(traet_date -> treat_date)  수정

DROP TABLE IF EXISTS chart;
DROP TABLE IF EXISTS disease;
DROP TABLE IF EXISTS treatment;
DROP TABLE IF EXISTS doctor;
DROP TABLE IF EXISTS patient;
DROP TABLE IF EXISTS room;
DROP TABLE IF EXISTS roomdetail;

CREATE TABLE doctor(
   doctor_id NVARCHAR(20),
   doctor_pwd NVARCHAR(20),
   doctor_name NVARCHAR(10),
   doctor_office NVARCHAR(10),
   doctor_phone NVARCHAR(15),
   doctor_dept NVARCHAR(10),
   doctor_img NVARCHAR(20)
);

CREATE TABLE disease(
   disease_code INT,
   disease_name NVARCHAR(30)
);

CREATE TABLE treatment(
   treat_id INT,
   doctor_id NVARCHAR(20),
   patient_id INT,
   treat_desc NVARCHAR(30),
   treat_date DATE
);

CREATE TABLE chart(
   chart_id INT,
   patient_id INT,
   doctor_id NVARCHAR(20),
   treat_id INT,
   disease_code INT,
   chart_desc NVARCHAR(30),
   nurse_id NVARCHAR(20),
   chart_date DATE
);

CREATE TABLE patient(
   patient_id INT,
   room_no NVARCHAR(10),
   room_bed INT,
   patient_name NVARCHAR(10),
   patient_date DATE,
   patient_phone NVARCHAR(15),
   patient_home NVARCHAR(15)
);

CREATE TABLE room(
   room_no NVARCHAR(10),
   room_bed INT,
   room_code NVARCHAR(5)
);

CREATE TABLE roomdetail(
   room_code NVARCHAR(5),
   room_accomodation INT,
   room_codename NVARCHAR(10)
);

#-----------------------------------------
# PRIMARY KEY 설정
ALTER TABLE doctor ADD PRIMARY KEY (doctor_id, doctor_pwd);
ALTER TABLE disease ADD PRIMARY KEY (disease_code);
ALTER TABLE treatment ADD PRIMARY KEY (treat_id);
ALTER TABLE chart ADD PRIMARY KEY (chart_id);
ALTER TABLE patient ADD PRIMARY KEY (patient_id);
ALTER TABLE room ADD PRIMARY KEY (room_no, room_bed);
ALTER TABLE roomdetail ADD PRIMARY KEY (room_code);

#-----------------------------------------
# AUTO INCREMENT 설정
ALTER TABLE treatment CHANGE COLUMN treat_id treat_id INT AUTO_INCREMENT;
ALTER TABLE chart CHANGE COLUMN chart_id chat_id INT AUTO_INCREMENT;
ALTER TABLE patient CHANGE COLUMN patient_id patient_id INT AUTO_INCREMENT;

#-----------------------------------------
# FOREIGN KEY 설정
ALTER TABLE treatment ADD CONSTRAINT treatment_FK_doctor FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id);
ALTER TABLE treatment ADD CONSTRAINT treatment_FK_patient FOREIGN KEY (patient_id) REFERENCES patient(patient_id);

ALTER TABLE chart ADD CONSTRAINT chart_FK_patient FOREIGN KEY (patient_id) REFERENCES patient(patient_id);
ALTER TABLE chart ADD CONSTRAINT chart_FK_doctor FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id);
ALTER TABLE chart ADD CONSTRAINT chart_FK_treatment FOREIGN KEY (treat_id) REFERENCES treatment(treat_id);
ALTER TABLE chart ADD CONSTRAINT chart_FK_disease FOREIGN KEY (disease_code) REFERENCES disease(disease_code);

ALTER TABLE patient ADD CONSTRAINT patient_FK_room FOREIGN KEY (room_no, room_bed) REFERENCES room(room_no, room_bed);

ALTER TABLE room ADD CONSTRAINT room_FK_roomdetail FOREIGN KEY (room_code) REFERENCES roomdetail(room_code);

#-----------------------------------------
# 룸 상세, 룸 테이블 데이터 삽입 
INSERT INTO roomdetail VALUES('a', 1, '1인실');
INSERT INTO roomdetail VALUES('b', 2, '2인실');
INSERT INTO roomdetail VALUES('c', 4, '4인실');

INSERT INTO room VALUES('101c', 1, 'c');
INSERT INTO room VALUES('101c', 2, 'c');
INSERT INTO room VALUES('101c', 3, 'c');
INSERT INTO room VALUES('101c', 4, 'c');

INSERT INTO room VALUES('102c', 1, 'c');
INSERT INTO room VALUES('102c', 2, 'c');
INSERT INTO room VALUES('102c', 3, 'c');
INSERT INTO room VALUES('102c', 4, 'c');

INSERT INTO room VALUES('103c', 1, 'c');
INSERT INTO room VALUES('103c', 2, 'c');
INSERT INTO room VALUES('103c', 3, 'c');
INSERT INTO room VALUES('103c', 4, 'c');

INSERT INTO room VALUES('201b', 1, 'b');
INSERT INTO room VALUES('202b', 2, 'b');

INSERT INTO room VALUES('203b', 1, 'b');
INSERT INTO room VALUES('203b', 2, 'b');

INSERT INTO room VALUES('301a', 1, 'a');
INSERT INTO room VALUES('302a', 1, 'a');

#-----------------------------------------
#환자 테이블 
INSERT INTO patient VALUES(1, '302a', 1, '알리바바', CURRENT_DATE, '0101234567', '두바이');
INSERT INTO patient VALUES(2, '301a', 1, '김부자', CURRENT_DATE, '01084913221', '강남');

INSERT INTO patient VALUES(3, '201b', 1, '이영표', CURRENT_DATE, '01014849993', '용산');
INSERT INTO patient VALUES(4, '202b', 2, '김세정', CURRENT_DATE, '01093821244', '신촌');
INSERT INTO patient VALUES(5, '203b', 1, '홍말숙', CURRENT_DATE, '01028312234', '모란');
INSERT INTO patient VALUES(6, '203b', 2, '김영자', CURRENT_DATE, '01035644321', '선릉');

INSERT INTO patient VALUES(7, '101c', 1, '진미령', CURRENT_DATE, '01093223821', '마포');
INSERT INTO patient VALUES(8, '101c', 2, '조혜련', CURRENT_DATE, '01032101221', '광진');
INSERT INTO patient VALUES(9, '103c', 1, '핫산', CURRENT_DATE, '01012340504', '부천');
INSERT INTO patient VALUES(10, '103c', 2, '마오', CURRENT_DATE, '01043211123', '구로');
INSERT INTO patient VALUES(11, '103c', 3, '양후이옌', CURRENT_DATE, '01040014321', '구로');
INSERT INTO patient VALUES(12, '103c', 4, '줘닝', CURRENT_DATE, '01035112030', '구로');
INSERT INTO patient VALUES(13, '102c', 1, '폰은정', CURRENT_DATE, '01075054413', '광명');
INSERT INTO patient VALUES(14, '102c', 2, '엄진식', CURRENT_DATE, '01019541881', '동작');

INSERT INTO patient VALUES(15, '101c', 3, '홍진호', CURRENT_DATE, '01012358881', '하남');

#-----------------------------------------
#의사
INSERT INTO doctor VALUES('doc01','pwd01','김철수','303','01011112222', '암센터', 'kimchulsu.jpg');
INSERT INTO doctor VALUES('doc02','pwd02','Biden','304','01022223333', '신경과','biden.jpg');
INSERT INTO doctor VALUES('doc03','pwd03','박영희','203','01055552334', '흉부외과', 'parkyounghee.jpg');
INSERT INTO doctor VALUES('doc04','pwd04','배지희','204','01065423333', '감염내과', 'baejihee.jpg');
INSERT INTO doctor VALUES('doc05','pwd05','김수형','205','01083242211', '외과', 'kimsuhyung.jpg');
INSERT INTO doctor VALUES('doc06','pwd06','이재용','206','01053247519', '감염내과', 'doctor-thumb-09.jpg');

#-----------------------------------------
#질병코드
INSERT INTO disease VALUES('1','암');
INSERT INTO disease VALUES('2','코로나19');
INSERT INTO disease VALUES('3','독감');
INSERT INTO disease VALUES('4','콜레라');
INSERT INTO disease VALUES('5','외상');
INSERT INTO disease VALUES('6','뇌졸증');
INSERT INTO disease VALUES('7','심근경색');

#-----------------------------------------
#진료
INSERT INTO treatment VALUES(1, 'doc01', 1, '정기검진', CURRENT_DATE);
INSERT INTO treatment VALUES(2, 'doc01', 13, '수술확인', CURRENT_DATE);

INSERT INTO treatment VALUES(3, 'doc02', 7, '정기검진', CURRENT_DATE);
INSERT INTO treatment VALUES(4, 'doc02', 7, '퇴원검진', CURRENT_DATE);
INSERT INTO treatment VALUES(5, 'doc02', 14, '정기검진', CURRENT_DATE);

INSERT INTO treatment VALUES(6, 'doc03', 2, '정기검진', CURRENT_DATE);
INSERT INTO treatment VALUES(7, 'doc03', 8, '수술확인', CURRENT_DATE);

INSERT INTO treatment VALUES(8, 'doc04', 3, '긴급검진', CURRENT_DATE);
INSERT INTO treatment VALUES(9, 'doc04', 9, '정기검진', CURRENT_DATE);
INSERT INTO treatment VALUES(10, 'doc04', 4, '정기검진', CURRENT_DATE);
INSERT INTO treatment VALUES(11, 'doc04', 5, '정기검진', CURRENT_DATE);

INSERT INTO treatment VALUES(12, 'doc05', 10, '수술확인', CURRENT_DATE);
INSERT INTO treatment VALUES(13, 'doc05', 11, '퇴원검진', CURRENT_DATE);
INSERT INTO treatment VALUES(14, 'doc05', 12, '정기검진', CURRENT_DATE);

INSERT INTO treatment VALUES(15, 'doc06', 6, '건강검진', CURRENT_DATE);

INSERT INTO treatment VALUES(16, 'doc06', 15, '코로나검진', CURRENT_DATE);

#-----------------------------------------
#차트
INSERT INTO chart VALUES(1, 1, 'doc01', 1, 1, '정기검진', 'nur1', CURRENT_DATE);
INSERT INTO chart VALUES(2, 13, 'doc01', 2, 1, '수술확인', 'nur1', CURRENT_DATE);

INSERT INTO chart VALUES(3, 7, 'doc02', 3, 6, '정기검진', 'nur3', CURRENT_DATE);
INSERT INTO chart VALUES(4, 14, 'doc02', 4, 6, '정기검진', 'nur3', CURRENT_DATE);
INSERT INTO chart VALUES(5, 7, 'doc02', 5, 6, '퇴원검진', 'nur3', CURRENT_DATE);

INSERT INTO chart VALUES(6, 2, 'doc03', 6, 7, '정기검진', 'nur2', CURRENT_DATE);
INSERT INTO chart VALUES(7, 8, 'doc03', 7, 7, '수술확인', 'nur2', CURRENT_DATE);

INSERT INTO chart VALUES(8, 3, 'doc04', 8, 2, '긴급검진', 'nur5', CURRENT_DATE);
INSERT INTO chart VALUES(9, 9, 'doc04', 9, 4, '정기검진', 'nur4', CURRENT_DATE);
INSERT INTO chart VALUES(10, 4, 'doc04', 10, 2, '정기검진', 'nur5', CURRENT_DATE);
INSERT INTO chart VALUES(11, 5, 'doc04', 11, 2, '정기검진', 'nur5', CURRENT_DATE);

INSERT INTO chart VALUES(12, 10, 'doc05', 12, 5, '수술확인', 'nur6', CURRENT_DATE);
INSERT INTO chart VALUES(13, 11, 'doc05', 13, 5, '퇴원검진', 'nur6', CURRENT_DATE);
INSERT INTO chart VALUES(14, 12, 'doc05', 14, 5, '정기검진', 'nur6', CURRENT_DATE);

INSERT INTO chart VALUES(15, 6, 'doc06', 15, 3, '건강검진', 'nur4', CURRENT_DATE);

INSERT INTO chart VALUES(16, 15, 'doc06', 16, 2, '코로나검진', 'nur4', CURRENT_DATE);


