# Install Individual Apps in Microsoft Office 2016
## Problem
Office 2016 is all-or-nothing installation. We only need some apps (ie., Word, Excel, and PowerPoint).

### Solution
1. Download [Mircosoft Office 2016 Deployment Tool](https://www.microsoft.com/en-us/download/details.aspx?id=49117)
2. The extracted files should be setup.exe with configuration.xml. We need to revise the xml file to exclude apps we don't want. 

Here is an example of my setup -> 64 bit -> Only Word, Excel, and PowerPoint

```xml
<Add OfficeClientEdition="64" Channel="Monthly">
<!-- Change 64 to 32 if it makes sense -->
    <Product ID="O365ProPlusRetail">
      <Language ID="en-us" />
      <!-- Remove ExcludeApp tag if you want to include it-->
      <ExcludeApp ID="Access" />
      <ExcludeApp ID="Groove" />
      <ExcludeApp ID="InfoPath" />
      <ExcludeApp ID="Lync" />
      <ExcludeApp ID="OneDrive" />
      <ExcludeApp ID="OneNote" />
      <ExcludeApp ID="Outlook" />
      <ExcludeApp ID="Publisher" />
      <ExcludeApp ID="SharePointDesigner" />
      <ExcludeApp ID="Visio" />
    </Product> 
  </Add>
```

3. Run Setup.exe from the command prompt (Run as Admin if needed):
```
setup.exe \configure configuration.xml
```
4. Done!

## ไทย
### การติดตั้ง Office 2016 เฉพาะบางแอพ เช่น เวิร์ด เอ็กเซล และ พาวเวอร์พอยท์
1. ดาวน์โหลด [Mircosoft Office 2016 Deployment Tool](https://www.microsoft.com/en-us/download/details.aspx?id=49117)
2. แตกไฟล์ออกมาจะพบว่า มี setup.exe และ configuration.xml เราจะแก้ไขไฟล์ .xml เพื่อทำให้โปรแกรมติดตั้งเพียงแอพที่เราต้องการ

ตัวอย่างการติดตั้งของผม -> 64 บิท -> เฉพาะ Word, Excel และ PowerPoint ()
```xml
<Add OfficeClientEdition="64" Channel="Monthly">
<!-- เปลี่ยนจาก 64 เป็น 32 bit ตามสเปคเครื่อง -->
    <Product ID="O365ProPlusRetail">
      <Language ID="en-us" />
      <!-- ลบ ExcludeApp ออก ถ้าคุณต้องการติดตั้งแอพนั้น ๆ -->
      <ExcludeApp ID="Access" />
      <ExcludeApp ID="Groove" />
      <ExcludeApp ID="InfoPath" />
      <ExcludeApp ID="Lync" />
      <ExcludeApp ID="OneDrive" />
      <ExcludeApp ID="OneNote" />
      <ExcludeApp ID="Outlook" />
      <ExcludeApp ID="Publisher" />
      <ExcludeApp ID="SharePointDesigner" />
      <ExcludeApp ID="Visio" />
    </Product> 
  </Add>
```
3. เปิด Command Prompt (ใช้ตัวเลือก Run as Admin หากจำเป็น):
```
setup.exe \configure configuration.xml
```
4. เสร็จ!