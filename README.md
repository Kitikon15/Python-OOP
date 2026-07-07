# 🐍 คู่มือการศึกษา Python Object-Oriented Programming (OOP)

ยินดีต้อนรับสู่คลังรวบรวมตัวอย่างโค้ดและคำอธิบายแนวคิด **Object-Oriented Programming (OOP)** ด้วยภาษา Python คลังนี้จัดทำขึ้นเพื่อใช้เป็นสื่อการเรียนรู้ตั้งแต่พื้นฐานไปจนถึงหัวข้อขั้นสูงในการเขียนโปรแกรมเชิงวัตถุอย่างมีระบบ

---

## 📌 สารบัญ (Table of Contents)
1. [คุณลักษณะเด่นของโปรเจกต์](#-คุณลักษณะเด่นของโปรเจกต์)
2. [ขั้นตอนการติดตั้งระบบสำหรับการเรียนรู้ (Installation Guide)](#-ขั้นตอนการติดตั้งระบบสำหรับการเรียนรู้-installation-guide)
3. [วิธีการรันโค้ดตัวอย่าง (Execution Guide)](#-วิธีการรันโค้ดตัวอย่าง-execution-guide)
4. [โครงสร้างบทเรียนและคำอธิบายไฟล์โค้ด (Module & File Structure)](#-โครงสร้างบทเรียนและคำอธิบายไฟล์โค้ด-module--file-structure)
5. [เจาะลึก 4 เสาหลักของ OOP และหลักการทำงาน (OOP Deep Dive)](#-เจาะลึก-4-เสาหลักของ-oop-และหลักการทำงาน-oop-deep-dive)
6. [ตารางสรุปการใช้งานคำสั่งพื้นฐาน (Quick Reference Table)](#-ตารางสรุปการใช้งานคำสั่งพื้นฐาน-quick-reference-table)

---

## ✨ คุณลักษณะเด่นของโปรเจกต์
* **ตัวอย่างโค้ดสั้น กระชับ**: เน้นตัวอย่างที่เข้าใจง่าย ไม่ซับซ้อน เหมาะแก่การเริ่มต้นเรียนรู้
* **หัวข้อครอบคลุม**: ตั้งแต่การประกาศ Class ไปจนถึง Inner Classes
* **สอดคล้องกับมาตรฐาน Python**: มีคำแนะนำเชิงลึกเกี่ยวกับตัวแปร `self` และคอนสตรักเตอร์ `__init__`
* **รองรับการทดลองใช้ในสภาพแวดล้อมจำลอง (Virtual Environment)** เพื่อความปลอดภัยและเป็นระเบียบของไลบรารี

---

## 🛠 ขั้นตอนการติดตั้งระบบสำหรับการเรียนรู้ (Installation Guide)

เพื่อที่จะเริ่มต้นทดลองรันโค้ดในเครื่องคอมพิวเตอร์ของคุณ ให้ทำตามขั้นตอนการติดตั้งตามระบบปฏิบัติการ Windows ด้านล่างนี้:

### 1. ติดตั้งซอฟต์แวร์ที่จำเป็น (Prerequisites)
* **Python**: ตรวจสอบว่าได้ติดตั้ง Python 3.8 ขึ้นไปแล้ว (แนะนำ Python 3.10+) 
* **Git**: สำหรับใช้ดึงข้อมูลโปรเจกต์ (หากต้องการ)

### 2. ดาวน์โหลดโค้ดโปรเจกต์ (Clone Project)
เปิด **Terminal** หรือ **PowerShell** จากนั้นป้อนคำสั่ง:
```bash
git clone https://github.com/your-username/Python-OOP.git
cd Python-OOP
```

### 3. สร้างและเปิดใช้งาน Virtual Environment (แนะนำ)
เพื่อหลีกเลี่ยงการชนกันของไลบรารีส่วนกลางในระบบปฏิบัติการ แนะนำให้สร้าง Virtual Environment ขึ้นมาดังนี้:

**สำหรับ Windows (PowerShell):**
```powershell
python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\Activate.ps1
```

**สำหรับ Windows (CMD):**
```cmd
python -m venv venv
.\venv\Scripts\activate.bat
```

เมื่อเปิดใช้งานสำเร็จ คุณจะเห็นข้อความ `(venv)` ปรากฏด้านหน้าบรรทัดคำสั่งใน Terminal ของคุณ

---

## 🚀 วิธีการรันโค้ดตัวอย่าง (Execution Guide)

คุณสามารถเลือกทดลองรันไฟล์ Python จากโฟลเดอร์ต่างๆ ได้ผ่าน Terminal โดยใช้รูปแบบคำสั่ง `python "ชื่อโฟลเดอร์/ชื่อไฟล์.py"` 

### ตัวอย่างคำสั่งรันในแต่ละหัวข้อ:

* **รันพื้นฐาน Class และ Object:**
  ```powershell
  python "Classes and Objects/01.Class.py"
  python "Classes and Objects/02.Object.py"
  ```

* **รันการสืบทอด (Inheritance):**
  ```powershell
  python "Inheritance/super_Function.py"
  ```

* **รันหัวข้อคลาสซ้อนคลาส (Inner Class):**
  ```powershell
  python "Inner Classes/Practical_Inner.py"
  ```

* **รันการห่อหุ้มข้อมูล (Encapsulation):**
  ```powershell
  python "Encapsulation/Get_Private_Property.py"
  ```

---

## 📂 โครงสร้างบทเรียนและคำอธิบายไฟล์โค้ด (Module & File Structure)

นี่คือคำอธิบายโดยละเอียดของไฟล์โค้ดทั้งหมดที่แบ่งตามโฟลเดอร์หัวข้อ:

### 1. [Classes and Objects](./Classes%20and%20Objects) (คลาสและวัตถุ)
การสร้างวัตถุจำลองจากแม่พิมพ์ที่ออกแบบไว้
* `01.Class.py` - วิธีประกาศคลาสเปล่าเพื่อจองพื้นที่การใช้งานหน่วยความจำ
* `02.Object.py` - การเรียกแปลงคลาสให้เป็นออบเจกต์ (Instantiation) และการดึงค่าแอตทริบิวต์
* `03.Delete-Objects.py` - การทำลายตัวแปรออบเจกต์ทิ้งออกจากหน่วยความจำด้วยคีย์เวิร์ด `del`
* `04.Multiple-Objects.py` - การสร้างวัตถุต่างกันหลายตัวจากโครงสร้างคลาสเดียวกัน

### 2. [__init__ Method](./__init__%20Method) (คอนสตรักเตอร์)
เมธอดพิเศษที่ไพทอนจะเรียกใช้ทันทีเมื่อสร้างวัตถุใหม่ เพื่อความสะดวกในการตั้งค่าข้อมูลเริ่มต้น
* `_init_Method.py` - การเขียนและใช้งานฟังก์ชัน `__init__`
* `Default_Values_init_.py` - การเขียนฟังก์ชันต้อนรับออบเจกต์โดยระบุค่าเริ่มต้นของตัวแปรไว้ล่วงหน้า
* `Multiple_Parameters.py` - การกำหนดพารามิเตอร์รับเข้าหลายๆ ค่าพร้อมกันขณะสร้างออบเจกต์
* `use_init_.py` & `use_init_02.py` - โค้ดแสดงการเรียกใช้งานจริงของเมธอดตัวสร้างข้อมูล

### 3. [self Parameter](./self%20Parameter) (ตัวแปรอ้างอิงอินสแตนซ์)
* `Self_Parameter.py` - การอ้างอิงถึงออบเจกต์ปลายทางที่กำลังเรียกใช้งานโค้ดอยู่
* `Use_self.py` - แสดงวิธีการเข้าถึงค่าตัวแปรภายในคลาส
* `Calling_Methods.py` - การใช้ `self` เพื่อให้เมธอดหนึ่งในคลาสเรียกใช้งานเมธอดอื่นที่อยู่ในคลาสเดียวกันได้
* `Properties_self.py` - การควบคุมคุณสมบัติต่างๆ ผ่าน `self`
* `Myobject_abc.py` - ตัวอย่างที่สาธิตว่าพารามิเตอร์แรกของเมธอดไม่จำเป็นต้องเขียนว่า `self` ก็ได้ (เขียนคำอื่นแทน เช่น `abc`) แต่แนะนำให้ใช้ `self` เพื่อให้อ่านเข้าใจง่ายขึ้น

### 4. [Class Properties](./Class%20Properties) (การจัดการคุณสมบัติ)
* `Properties.py` - การกำหนดค่าตัวแปรระดับ Instance (Instance Attribute)
* `Access_properties.py` - การเข้าถึงเพื่อดึงค่าของคุณสมบัติเหล่านั้นมาแสดงผล
* `Add_Properties.py` - การเพิ่มตัวแปรหรือข้อมูลย่อยใหม่ให้แก่ออบเจกต์หลังจากวัตถุถูกสร้างเสร็จสิ้น
* `Modifying_Properties.py` & `Modify_Properties.py` - การเขียนโค้ดเปลี่ยนค่าหรือข้อมูลใหม่ของตัวแปรออบเจกต์
* `Delete_Properties.py` - การลบตัวแปรเฉพาะตัวออกจากออบเจกต์
* `Class_Object_Properties.py` - การเปรียบเทียบความแตกต่างระหว่าง **Class Variables** (ใช้ร่วมกันหมดทุกออบเจกต์) และ **Instance Variables** (แยกเก็บเฉพาะวัตถุใครวัตถุมัน)

### 5. [Class Methods](./Class%20Methods) (เมธอดและพฤติกรรม)
* `Class_Method.py` - การประกาศฟังก์ชันภายในคลาส
* `Accessing_Method.py` - วิธีรันฟังก์ชันผ่านจุดอ้างอิงของตัววัตถุ (Dot Notation)
* `Method_Parameters.py` - การส่งอาร์กิวเมนต์เพิ่มเข้าสู่ฟังก์ชันนอกเหนือจากข้อมูลออบเจกต์
* `Methods_Modifying.py` - การดัดแปลงหรือเขียนทับการคำนวณในฟังก์ชัน
* `Multiple_Methods.py` - การรันหลายเมธอดต่อเนื่องกัน
* `Delete_Methods.py` - การทดลองตัดเมธอดออกจากวัตถุ
* `The __str__() Method.py` - การ Override ฟังก์ชัน `__str__` เพื่อควบคุมการแสดงผลของวัตถุเป็นสายอักขระ (String Representation) เมื่อเรียกฟังก์ชัน `print()`

### 6. [Inheritance](./Inheritance) (การสืบทอดและแชร์โค้ด)
* `Inheritance_Parent.py` - การสร้างคลาสหลักเพื่อแชร์โค้ด (Super Class)
* `Child_Class.py` - คลาสลูกที่รับความสามารถของคลาสหลักมาใช้ทันที (Sub Class)
* `super_Function.py` - การใช้ `super().__init__()` เพื่อเรียกใช้ constructor ของคลาสพ่อแม่ ช่วยไม่ให้ต้องเขียนโค้ดเริ่มต้นใหม่
* `Add_Properties.py` - การต่อเติมตัวแปรเฉพาะทางเพิ่มเติมให้แก่คลาสลูก
* `Add_Methods.py` - การเสริมสร้างทักษะความสามารถใหม่เฉพาะตัวที่คลาสลูกทำได้แต่คลาสแม่ทำไม่ได้
* `Function_Inher.py` - การสืบทอดพฤติกรรมการทำงานของฟังก์ชัน

### 7. [Polymorphism](./Polymorphism) (การมีหลายรูปทรง)
* `Class_Polymorphism.py` - คลาสคนละคลาสที่มีชื่อฟังก์ชันประพฤติตนเหมือนกัน ทำให้เรียกใช้งานร่วมกันได้ง่าย
* `Inher_Class_Poly.py` - คลาสลูกหลายตัว override เมธอดคลาสพ่อเดียวกันเพื่อพ่นผลลัพธ์ต่างกันออกไป
* `Function_Polymorphism.py` - การนำออบเจกต์ที่มีเมธอดพหุสัณฐานส่งเข้าไปวิเคราะห์และรันคำสั่งเดียวกันผ่านฟังก์ชันภายนอก
* `Tuple.py` & `Dictionary.py` - การนำออบเจกต์ต่างประเภทมาจัดชุดลงในลิสต์/ทูเพิล/ดิกชันนารี แล้วรันคำสั่งเดียวกันผ่านการวนลูป

### 8. [Encapsulation](./Encapsulation) (การควบคุมขอบเขตความปลอดภัยข้อมูล)
* `Private_Properties.py` - การซ่อนข้อมูลของคลาสด้วยการใส่เครื่องหมาย `__` (Double Underscores) ที่หน้าชื่อแอตทริบิวต์
* `Get_Private_Property.py` - การสร้างช่องทางให้อ่านข้อมูล Private ผ่าน Getter
* `Set_Private_Property.py` - การเปลี่ยนค่า Private ผ่าน Setter ซึ่งสามารถตรวจสอบความถูกต้องก่อนแก้ค่าจริงได้

### 9. [Inner Classes](./Inner%20Classes) (คลาสซ้อนคลาส)
* `Inner_Class.py` - การสร้างคลาสย่อยที่ทำงานสัมพันธ์อย่างลึกซึ้งเฉพาะภายใต้คลาสแม่เท่านั้น
* `Outer_Inner.py` - วิธีการออกแบบลำดับโครงสร้างภายใน-ภายนอก
* `Accessing_Inner.py` - การประกาศใช้งานออบเจกต์ของคลาสย่อยชั้นในผ่านตัวแปรคลาสภายนอก
* `Multiple_Inner.py` - คลาสภายนอกหนึ่งคลาสที่มีคลาสภายในมากกว่าหนึ่งคลาส
* `Practical_Inner.py` - ตัวอย่างสถานการณ์จริงของการออกแบบโมเดลคลาสซ้อนคลาส

---

## 🧠 เจาะลึก 4 เสาหลักของ OOP และหลักการทำงาน (OOP Deep Dive)

การเขียนโปรแกรมแบบเชิงวัตถุ (OOP) ในภาษา Python นั้น มีการประยุกต์ใช้งานแนวคิดหลัก 4 ประการ ดังนี้:

### 1. Encapsulation (การห่อหุ้มข้อมูล)
มีจุดประสงค์หลักเพื่อป้องกันไม่ให้ผู้อื่นแก้ไขตัวแปรภายในวัตถุโดยตรง ซึ่งอาจส่งผลเสียต่อการทำงานของระบบ
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private Attribute (คนนอกดูตรงๆ ไม่ได้)

    # Getter เพื่อขออ่านยอดเงิน
    def get_balance(self):
        return self.__balance

    # Setter เพื่อแก้ไขยอดเงิน (มีการตรวจสอบเงื่อนไขความถูกต้องก่อนเสมอ)
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("ยอดเงินไม่สามารถติดลบได้!")
```

### 2. Inheritance (การสืบทอดคุณสมบัติ)
ช่วยลดการเขียนโค้ดซ้ำซ้อน โดยการนำคุณสมบัติเดิมที่มีในคลาสแม่มาประยุกต์และเพิ่มเติมฟังก์ชันการใช้งานเฉพาะตัวในคลาสลูก
```python
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start_engine(self):
        print(f"เครื่องยนต์ของ {self.brand} เริ่มทำงานแล้ว")

# สืบทอดคุณสมบัติจาก Vehicle
class ElectricCar(Vehicle):
    def __init__(self, brand, year, battery_capacity):
        super().__init__(brand, year) # เรียกใช้คอนสตรักเตอร์คลาสแม่
        self.battery_capacity = battery_capacity # เพิ่มคุณสมบัติใหม่ของตัวเอง

    # เพิ่มเมธอดเฉพาะตัว
    def charge_battery(self):
        print("กำลังชาร์จไฟเข้ารถ...")
```

### 3. Polymorphism (การพหุสัณฐาน)
การสร้างส่วนต่อประสาน (Interface) หรือใช้ชื่อเมธอดเดียวกัน แต่ละออบเจกต์มีการเขียนประมวลผลและการทำงานที่เป็นเอกลักษณ์ของตนเอง
```python
class Dog:
    def make_sound(self):
        return "โฮ่งๆ!"

class Cat:
    def make_sound(self):
        return "เหมียวๆ!"

# ฟังก์ชันกลางรับออบเจกต์อะไรก็ได้มาส่งเสียงร้อง
def animal_sound_test(animal_object):
    print(animal_object.make_sound())

dog = Dog()
cat = Cat()

animal_sound_test(dog)  # ผลลัพธ์: โฮ่งๆ!
animal_sound_test(cat)  # ผลลัพธ์: เหมียวๆ!
```

### 4. Abstraction (การซ่อนรายละเอียดความซับซ้อน)
ใน Python มักสร้างโดยใช้คลาส Abstract จากไลบรารี `abc` เพื่อกำหนดโครงสร้างหลัก (Template) ให้คลาสลูกไปเขียนรายละเอียดต่อยอดด้วยตนเองโดยต้องสอดคล้องกับรูปแบบที่กำหนดไว้

---

## 📊 ตารางสรุปการใช้งานคำสั่งพื้นฐาน (Quick Reference Table)

| หัวข้อการเรียนรู้ | คีย์เวิร์ดสำคัญ | ตัวอย่างโค้ดสั้น | คำอธิบายย่อ |
| :--- | :--- | :--- | :--- |
| **Class Definition** | `class` | `class Car:` | ประกาศสร้างแม่แบบคลาสใหม่ |
| **Constructor** | `def __init__` | `def __init__(self, val):` | กำหนดฟังก์ชันเริ่มต้นให้แก่แอตทริบิวต์ |
| **Self Parameter** | `self` | `self.value = val` | อ้างอิงตัวแปรในขอบเขตออบเจกต์ |
| **Object Deletion** | `del` | `del car_object` | สั่งลบออบเจกต์ออกจากหน่วยความจำ |
| **Inheritance** | `Child(Parent)` | `class Dog(Animal):` | สืบทอดฟังก์ชันจากคลาสแม่ |
| **Super Method** | `super()` | `super().__init__(name)` | สั่งรันคำสั่งกำหนดค่าในคลาสแม่ |
| **String Presentation**| `__str__` | `def __str__(self):` | ควบคุมข้อความที่ถูกแสดงเมื่อสั่ง print ออบเจกต์ |
| **Encapsulation** | `__` (double underscore) | `self.__secret = 123` | ซ่อนตัวแปรให้เป็น Private ป้องกันคนภายนอก |
| **Inner Class** | Class nesting | `class Inner:` (ข้างในคลาสอื่น) | สร้างคลาสเฉพาะกิจซ้อนภายในคลาสหลัก |

---

*ขอให้คุณสนุกกับการศึกษาแนวคิดเชิงวัตถุ Python OOP! หากต้องการเรียนรู้เพิ่มเติม สามารถทดลองอ่านและรันสคริปต์ต่างๆ ในคลังโปรเจกต์นี้ตามลำดับเลขข้อได้เลยครับ*
