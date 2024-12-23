from tkinter import messagebox
import mysql.connector

def resetFields(inputId, inputName, inputDept):
    inputId.delete(0, "end")
    inputName.delete(0, "end")
    inputDept.delete(0, "end")


def insertData(inputId, inputName, inputDept, listbox):
    id = inputId.get()
    name = inputName.get()
    dept = inputDept.get()

    if id == "" or name == "" or dept == "":
        messagebox.showwarning("Cannot Insert", "All the fields are required. Insert them first before proceeding.")
    else:
        try:
            dbConn = mysql.connector.connect(host="localhost", user="root", password="root", database="employees", auth_plugin="mysql_native_password", port=3006)
            cursor = dbConn.cursor()
            cursor.execute("insert into empDetails (empID, empName, empDept) values(%s, %s, %s);", (id, name, dept))
            dbConn.commit()

            resetFields(inputId, inputName, inputDept)

            messagebox.showinfo("Insert Status", "Data Inserted Successfully")
            showDataInListBox(listbox)
        except mysql.connector.Error as err:
            messagebox.showerror("Database error", f"Error: {err}")
        finally:
            if dbConn:
                dbConn.close()


def updateData(inputId, inputName, inputDept, listbox):
    id = inputId.get()
    name = inputName.get()
    dept = inputDept.get()

    if id == "" or name == "" or dept == "":
        messagebox.showwarning("Cannot Update", "All the fields are required. Insert them first before proceeding.")
    else:
        try:
            dbConn = mysql.connector.connect(host="localhost", user="root", password="root", database="employees", auth_plugin="mysql_native_password", port=3006)
            cursor = dbConn.cursor()
            cursor.execute("update empDetails set empName=%s, empDept=%s where empID=%s;", (name, dept, id))
            dbConn.commit()

            resetFields(inputId, inputName, inputDept)

            messagebox.showinfo("Update Status", "Data Updated Successfully")
            showDataInListBox(listbox)
        except mysql.connector.Error as err:
            messagebox.showerror("Database error", f"Error: {err}")
        finally:
            if dbConn:
                dbConn.close()


def getData(inputId, inputName, inputDept):
    id = inputId.get()
    inputName.delete(0, "end")
    inputDept.delete(0, "end")

    if id == "":
        messagebox.showwarning("Fetch Status", "Please provide the Emp ID to fetch the data.")
    else:
        try:
            dbConn = mysql.connector.connect(host="localhost", user="root", password="root", database="employees", auth_plugin="mysql_native_password", port=3006)
            cursor = dbConn.cursor()
            cursor.execute("select * from empDetails where empID=%s;", (id,))
            rows = cursor.fetchall()

            if rows:
                for row in rows:
                    inputName.insert(0, row[1])
                    inputDept.insert(0, row[2])
            else:
                inputName.delete(0, "end")
                inputDept.delete(0, "end")

                messagebox.showinfo("Fetch Status", "No data found for the provided Emp ID.")
        except mysql.connector.Error as err:
            messagebox.showerror("Database error", f"Error: {err}")
        finally:
            if dbConn:
                dbConn.close()


def deleteData(inputId, inputName, inputDept, listbox):
    id = inputId.get()

    if id == "":
        messagebox.showwarning("Cannot Delete", "Please provide the Emp ID to fetch the data.")
    else:
        try:
            dbConn = mysql.connector.connect(host="localhost", user="root", password="root", database="employees", auth_plugin="mysql_native_password", port=3006)
            cursor = dbConn.cursor()
            cursor.execute("delete from empDetails where empID=%s;", (id,))
            dbConn.commit()

            resetFields(inputId, inputName, inputDept)

            messagebox.showinfo("Delete Status", "Data Deleted Successfully")
            showDataInListBox(listbox)
        except mysql.connector.Error as err:
            messagebox.showerror("Database error", f"Error: {err}")
        finally:
            if dbConn:
                dbConn.close()


def showDataInListBox(listbox):
    try:
        dbConn = mysql.connector.connect(host="localhost", user="root", password="root", database="employees",
                                         auth_plugin="mysql_native_password", port=3006)
        cursor = dbConn.cursor()
        cursor.execute("select * from empDetails;")
        rows = cursor.fetchall()
        listbox.delete(0, listbox.size())

        for row in rows:
            addData = f"{row[0]} {row[1]} {row[2]}"
            listbox.insert(listbox.size() + 1, addData)
    except mysql.connector.Error as err:
        messagebox.showerror("Database error", f"Error: {err}")
    finally:
        if dbConn:
            dbConn.close()


