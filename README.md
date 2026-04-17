# AXLerate SDK

Cisco Unified Communications SDK עבור פלטפורמת AXLerate - ספריית פייתון לניהול מערכות טלפוניה של סיסקו.

## 🚀 התקנה

```bash
pip install axlerate-sdk
```

## 📋 דרישות מקדימות

- Python 3.8+
- גישה לשרתי Cisco Unified Communications Manager (CUCM)
- גישה לשרתי Cisco Unified Contact Center Express (UCCX)
- הרשאות מתאימות במערכות הטלפוניה

## 🔧 שימוש בסיסי

```python
from axlerate.client import CiscoUCClient

# יצירת חיבור ל-CUCM
cucm_client = CiscoUCClient(
    server="cucm.example.com",
    username="admin",
    password="password",
    version="12.5"
)

# קבלת רשימת מכשירים
devices = cucm_client.get_devices()
print(f"נמצאו {len(devices)} מכשירים")

# קבלת מידע על מכשיר ספציפי
device_info = cucm_client.get_device("SEP1234567890AB")
print(f"מכשיר: {device_info['name']}, סטטוס: {device_info['status']}")

# קבלת סטטוס שירותים
services_status = cucm_client.get_all_services_status("cucm-server")
for service, status in services_status.items():
    print(f"{service}: {status}")
```

## 📚 תכונות עיקריות

### 🏢 CUCM (Cisco Unified Communications Manager)
- ניהול מכשירים (Phones, Gateways, Trunks)
- ניהול משתמשים וקווים טלפוניים
- ניהול פרופילים והגדרות
- קבלת סטטוס שירותים ובקרת שירותים
- תמיכה מלאה ב-AXL API

### 🎧 UCCX (Cisco Unified Contact Center Express)
- ניהול סוכנים וצוותים
- ניהול מיומנויות ורמות הרשאה
- קבלת סטטיסטיקות ודוחות
- ניהול תורים ומסלולי שיחות
- ניהול קמפיינים וקידומות

### 🔧 תכונות כלליות
- טיפול אוטומטי בשגיאות ו-retry
- תמיכה ב-SSL/TLS
- לוגים מפורטים ל-debugging
- תמיכה ב-session management
- תיעוד מלא של כל הפונקציות

## 🎯 דוגמאות מתקדמות

### ניהול מכשירים

```python
# הוספת מכשיר חדש
new_device = {
    "name": "SEP1234567890CD",
    "description": "iPhone User",
    "product": "Cisco 8841",
    "device_pool": "Default",
    "location": "Hub_None",
    "protocol": "SIP"
}

result = cucm_client.add_device(new_device)
if result['success']:
    print("מכשיר נוסף בהצלחה")
else:
    print(f"שגיאה: {result['error']}")

# עדכון מכשיר קיים
update_data = {
    "description": "Updated iPhone User",
    "device_pool": "NewPool"
}

result = cucm_client.update_device("SEP1234567890CD", update_data)

# מחיקת מכשיר
result = cucm_client.delete_device("SEP1234567890CD")
```

### ניהול משתמשים

```python
# קבלת רשימת משתמשים
users = cucm_client.get_users()

# הוספת משתמש חדש
new_user = {
    "userid": "johndoe",
    "firstname": "John",
    "lastname": "Doe",
    "mailid": "john.doe@example.com",
    "primaryextension": "1001"
}

result = cucm_client.add_user(new_user)

# הקצאת מכשיר למשתמש
cucm_client.associate_device_to_user("johndoe", "SEP1234567890AB")
```

### ניהול שירותים

```python
# קבלת סטטוס כל השירותים
services = cucm_client.get_all_services_status("cucm-server")

# הפעלת שירות
result = cucm_client.start_service("cucm-server", "Cisco CallManager")

# עצירת שירות
result = cucm_client.stop_service("cucm-server", "Cisco CTI Manager")

# הפעלה מחדש של שירות
result = cucm_client.restart_service("cucm-server", "Cisco Tftp")
```

## 🔍 Debugging ולוגים

```python
import logging

# הגדרת רמת לוגים
logging.basicConfig(level=logging.DEBUG)

# יצירת לקוח עם לוגים מפורטים
client = CiscoUCClient(
    server="cucm.example.com",
    username="admin",
    password="password",
    version="12.5",
    debug=True  # מפעיל לוגים מפורטים
)
```

## 🛠️ התקנה מקור

```bash
# שיבוט ה-repository
git clone https://github.com/MeiRR17/CMA.git
cd CMA/axlerate-sdk

# התקנה מקור
pip install -e .

# התקנה עם תלותי פיתוח
pip install -e ".[dev]"
```

## 🧪 בדיקות

```bash
# הרצת כל הבדיקות
pytest

# הרצת בדיקות עם כיסוי
pytest --cov=axlerate

# הרצת בדיקות ספציפיות
pytest tests/test_cucm.py
```

## 📖 תיעוד

תיעוד מלא זמין ב:
- [API Documentation](https://github.com/MeiRR17/CMA/wiki)
- [CUCM AXL API Reference](https://developer.cisco.com/site/axl/)
- [UCCX API Reference](https://developer.cisco.com/site/uccx/)

## 🤝 תרומה

מוזמנים לתרום לפרויקט! אנא עקבו אחר השלבים הבאים:

1. Fork את ה-repository
2. צרו branch לתכונה חדשה (`git checkout -b feature/amazing-feature`)
3. Commit את השינויים (`git commit -m 'Add amazing feature'`)
4. Push ל-branch (`git push origin feature/amazing-feature`)
5. צרו Pull Request

## 📄 רישיון

פרויקט זה רשוי תחת רישיון MIT - ראו את קובץ [LICENSE](LICENSE) לפרטים.

## 🆘 תמיכה

- 📧 Email: support@cma.local
- 🐛 Issues: [GitHub Issues](https://github.com/MeiRR17/CMA/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/MeiRR17/CMA/discussions)

## 🔄 גרסאות

- **v1.0.0** - גרסה ראשונית עם תמיכה מלאה ב-CUCM ו-UCCX
- **v1.1.0** - תכונות נוספות ושיפורי ביצועים (מתוכנן)
- **v2.0.0** - תמיכה ב-Cisco Webex ותכונות מתקדמות (מתוכנן)

---

**⚠️ הערה חשובה:** SDK זה מיועד לשימוש בסביבות מבוקרות בלבד. יש לוודא שיש לכם את כל ההרשאות הנדרשות לפני השימוש במערכות הטלפוניה.
