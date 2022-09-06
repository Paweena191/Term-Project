# ระบบติดตามและตรวจสอบคุณภาพอากาศภายในอาคารสำหรับผู้ป่วยระบบทางเดินหายใจฃ
   ระบบติดตามคุณภาพอากาศคุณภาพอากาศที่จะใช้สำหรับเฝ้าระวังผู้ป่วยระบบทางเดินหายใจแบบอัตโนมัติ โดยการเก็บข้อมูลจากสภาพแวดล้อมที่มีผลต่อผู้ป่วยระบบทางเดินหายใจโดยตรงผลลัพธ์จากการวิเคราะห์ดังกล่าวได้นำเสนอระบบผู้เชี่ยวชาญในรูปแบบบนเว็บแอปพลิเคชัน ระบบดังกล่าวสามารถช่วยในการตัดสินใจ และวินิจฉัยของแพทย์ผู้เชี่ยวชาญเพื่อสรุปเหตุการณ์ที่เป็นไปได้และอาจจะกระทบผู้ป่วยระบบทางเดินหายใจ 

## ตัวต้นแบบ
![program](https://github.com/Paweena191/Term-Project/blob/main/IMG_7086.jpg)

## คุณสมบัติ
- 

## ส่วนประกอบ
- Node Micro-Controller Unit: MCU node
    ESP32 เป็นอุปกรณ์สำหรับการประมวลผล
- Print Circuit Board
    ใช้สำหรับเป็นทางเดินสัญญาณไฟฟ้าของอุปกรณ์อิเล็กทรอนิกส์ต่าง ๆ ที่อยู่บนแผงวงจรทำให้อุปกรณ์ต่าง ๆ เชื่อมต่อกันได้ และสามารถทำงานได้อย่างถูกต้องตามที่ได้ออกแบบไว้
- DHT22
    ใช้สำหรับตรวจวัดค่าความชื้นและอุณหภูมิในอากาศ
- Nova PM Sensor Laser PM 2.5 Air Quality Detection Sensor (SDS011) 
    ใช้สำหรับตรวจวัดค่าฝุ่นละอองขนาดไม่เกิน 2.5 และขนาดไม่เกิน 10
 

## ไลบรารี่บน visual studio code
- Micro Python
    เป็นภาษาที่ใช้พัฒนาชอฟต์แวร์ในการควบคุมเซ็นเซอร์
- ESP32 Firmware
    เป็นระบบปฏิบัติการใช้สำหรับควบคุมการทำงานของ ESP32
- DHT sensor library
    เป็นชุดคำสั่งสำหรับการเปิดใช้งานของเซ็นเซอร์ DHT22
- SDS011 sensor Library
    เป็นชุดคำสั่งสำหรับการเปิดใช้งานของเซ็นเซอร์ SDS011


## ผลลัพธ์
### Web Application
![program](https://github.com/Paweena191/Term-Project/blob/main/display.png)
