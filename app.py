import streamlit as st
import pandas as pd
import os


# إعداد الصفحة
st.set_page_config(
    page_title="الهيئة القومية لسلامة الغذاء - قاعدة بيانات المنشآت الغذائية",
    page_icon="",
    layout="wide"
)

# تنسيق عام CSS
st.markdown("""
    <style>
    body {
        background-color: #ffffff;
    }
    .main {
        background-color: #f8fff8;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 0 8px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
        color: #006b3c;
    }
    .stTextInput>div>div>input {
        border: 2px solid #006b3c;
        border-radius: 10px;
        padding: 8px;
    }
    footer {
        text-align: center;
        color: gray;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# شعار الهيئة
logo_path = os.path.join(os.path.dirname(__file__), "3.png")
st.image(logo_path, width=120)
st.markdown("<h1 style='text-align:center; color:#006b3c;'>الهيئة القومية لسلامة الغذاء</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>قاعدة بيانات المنشآت الغذائية</h3>", unsafe_allow_html=True)
st.markdown("---")

# رابط بيانات Google Sheet (ضع رابطك هنا)
sheet_url = "https://docs.google.com/spreadsheets/d/1ABCDeFGHIJK12345/export?format=csv"

try:
    data = pd.read_csv(sheet_url)
except Exception as e:
    st.error("⚠️ لم يتم تحميل البيانات، تأكد من صلاحيات المشاركة في Google Sheets.")
    st.stop()

# مربع البحث
search = st.text_input("🔍 ابحث باسم المنشأة أو رقم الترخيص:")

# عرض النتائج
if search:
    filtered = data[data.apply(lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1)]
    if filtered.empty:
        st.warning("❌ لا توجد نتائج مطابقة.")
    else:
        st.success(f"تم العثور على {len(filtered)} نتيجة.")
        st.dataframe(filtered, use_container_width=True)
else:
    st.info("أدخل اسم المنشأة أو رقم الترخيص للبحث عن بياناتها.")

# حقوق
st.markdown("---")
st.markdown(
    "<footer>© الهيئة القومية لسلامة الغذاء - جميع الحقوق محفوظة</footer>",
    unsafe_allow_html=True
)
