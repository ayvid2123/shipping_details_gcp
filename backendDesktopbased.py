import sqlite3

def connect():
    db=sqlite3.connect("shipments.db")
    cur=db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS shipment(id integer PRIMARY KEY ,ORDER_NO INTEGER,CONSIGNER_ID INTEGER,CONSIGNEE_NAME VARCHAR(20),SHIPPING_ADDRESS VARCHAR(50),CONSIGNEE_CONTACT INTEGER,PACKAGE_WEIGHT REAL)")
    db.commit()
    db.close()

def insert(ORDER_NO,CONSIGNER_ID,CONSIGNEE_NAME,SHIPPING_ADDRESS,CONSIGNEE_CONTACT,PACKAGE_WEIGHT):
    db=sqlite3.connect("shipments.db")
    cur=db.cursor()
    cur.execute("INSERT INTO shipment VALUES(NULL,?,?,?,?,?,?)",(ORDER_NO,CONSIGNER_ID,CONSIGNEE_NAME,SHIPPING_ADDRESS,CONSIGNEE_CONTACT,PACKAGE_WEIGHT))
    db.commit()
    db.close()

def view():
    db=sqlite3.connect("shipments.db")
    cur=db.cursor()
    cur.execute("SELECT * FROM shipment")
    rows=cur.fetchall()
    db.close()
    return rows

def select(ORDER_NO="",CONSIGNER_ID="",CONSIGNEE_NAME="",SHIPPING_ADDRESS="",CONSIGNEE_CONTACT="",PACKAGE_WEIGHT=""):
    db=sqlite3.connect("shipments.db")
    cur=db.cursor()
    cur.execute("SELECT * FROM shipment WHERE ORDER_NO=? OR CONSIGNER_ID=? OR CONSIGNEE_NAME=? OR SHIPPING_ADDRESS=? OR CONSIGNEE_CONTACT=? OR PACKAGE_WEIGHT=?",(ORDER_NO,CONSIGNER_ID,CONSIGNEE_NAME,SHIPPING_ADDRESS,CONSIGNEE_CONTACT,PACKAGE_WEIGHT))
    rows=cur.fetchall()
    db.close()
    return rows

def delete(id):
    db=sqlite3.connect("shipments.db")
    cur=db.cursor()
    cur.execute("DELETE FROM shipment WHERE id=?",(id,))
    db.commit()
    db.close()

def update(id,ORDER_NO,CONSIGNER_ID,CONSIGNEE_NAME,SHIPPING_ADDRESS,CONSIGNEE_CONTACT,PACKAGE_WEIGHT):
    db=sqlite3.connect("shipments.db")
    cur=db.cursor()
    cur.execute("UPDATE shipment SET OREDR_NO=?,CONSIGNER_ID=?,CONSIGNEE_NAME=?,SHIPPING_ADDRESS=?,CONSIGNEE_CONTACT=?,PACKAGE_WEIGHT=? WHERE id=?",(ORDER_NO,CONSIGNER_ID,CONSIGNEE_NAME,SHIPPING_ADDRESS,CONSIGNEE_CONTACT,PACKAGE_WEIGHT,id))
    db.commit()
    db.close()

connect()
#print(delete(4))
#print(select(CONSIGNEE_NAME="ANSHUL GUPTA"))
