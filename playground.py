from downloader_bot import bot
from downloader_bot import check_slash
from downloader_bot import rename_file
from downloader_bot import write_log

name = '6. ร้อยละผู้ป่วยที่มีความผิดปกติทางจิตและพฤติกรรมที่เกิดจากการใช้สารออกฤทธิ์ต่อจิตประสาท จากระบบฐานข้อมูล บสต. และฐานข้อมูลจิตเวชในระบบ HDC ที่มีพฤติกรรมก่อความรุนแรง (SMI-V)'
url = 'https://hdcservice.moph.go.th/hdc/reports/report.php?source=pformated/format2.php&cat_id=0eb953d9735a9625ac19acfa5ebcd368&id=a43ee80c26a6f051785deecce89a931c'

check_slash(name)

bot(url)

rename_file('access.csv', name)

write_log(name)