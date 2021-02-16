
class Sql:
    chartlist = "SELECT * FROM chart";
    chartone = "SELECT * FROM chart WHERE patient_id = %d"
    chartinsert = "INSERT INTO chart VALUES (null,%d,'%s',%d,%d,null,'%s',CURRENT_DATE())";

    treatmentlist = "SELECT * FROM treatment";
    treatmentone = "SELECT * FROM treatment WHERE treat_id = %d"
    treatmentinsert = "INSERT INTO treatment VALUES (null,'%s',%d,'%s',CURRENT_DATE())";

    diseaselist = "SELECT * FROM disease";
    diseaseone = "SELECT * FROM disease WHERE disease_code = %d"

    doctorlist = "SELECT * FROM doctor";
    doctorone = "SELECT * FROM doctor WHERE doctor_id = '%s' "
    doctorinsert = "INSERT INTO doctor VALUES ('%s','%s','%s','%s','%s','%s','%s')";
    docdelete = "DELETE FROM doctor WHERE doctor_id= '%s' ";

    patientlist = "SELECT * FROM patient";
    patientone = "SELECT * FROM patient WHERE patient_id = %d"
    patientinsert = "INSERT INTO patient VALUES (null,'%s',%d,'%s',CURRENT_DATE(),'%s','%s')";

    roomlist = "SELECT * FROM room";

    roomdetaillist = "SELECT * FROM roomdetail";
    roomdetailone = "SELECT * FROM roomdetail WHERE room_code = '%s'"

    # userlistone = "SELECT * FROM usertb WHERE id= '%s' ";
    # userinsert = "INSERT INTO usertb VALUES ('%s', '%s', '%s')";
    # userdelete = "DELETE FROM usertb WHERE id= '%s' ";
    # userupdate = "UPDATE usertb SET pwd='%s', name='%s' WHERE id='%s' ";
    #
    # itemlist = "SELECT * FROM itemtb";
    # itemlistone = "SELECT * FROM itemtb WHERE id= %d ";
    # iteminsert = "INSERT INTO itemtb VALUES (null, '%s', %d, CURRENT_DATE(), '%s')";
    # itemdelete = "DELETE FROM itemtb WHERE id= %d ";
    # itemupdate = "UPDATE itemtb SET name='%s', price=%d, imgname='%s' WHERE id=%d ";

