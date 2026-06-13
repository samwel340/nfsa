import streamlit as st
from supabase import create_client, Client
from datetime import date
import os
from PIL import Image

# ==========================================
# 1. الاتصال بـ Supabase
# ==========================================
try:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    supabase: Client = create_client(url, key)
except KeyError:
    st.error("⚠️ خطأ: لم يتم العثور على مفاتيح Supabase. يرجى التأكد من ملف secrets.toml")
    st.stop()

# ==========================================
# 2. إعدادات الصفحة والتنسيقات الجمالية (Responsive)
# ==========================================
st.set_page_config(
    page_title="الهيئة القومية لسلامة الغذاء", 
    page_icon="", 
    layout="centered"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
    
    /* تنسيق عام للصفحة */
    .stApp { 
        font-family: 'Cairo', sans-serif; 
        direction: rtl; 
        text-align: right; 
        background-color: #f8f9fa;
    }
    
    /* تنسيق الشعار في الأعلى */
    .logo-container {
        text-align: center;
        margin-bottom: 25px;
    }

    /* تنسيق العنوان الرئيسي */
    .main-header { 
        background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 100%);
        color: white; 
        padding: 25px; 
        border-radius: 15px; 
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .main-header h1 { margin: 0; font-size: 2.2rem; font-weight: 700; }
    .main-header p { margin: 8px 0 0; font-size: 1.1rem; opacity: 0.95; }

    /* تنسيق حقول الإدخال */
    .stTextInput > div > div > input, 
    .stTextArea > div > div > textarea, 
    .stSelectbox > div > div > select {
        text-align: right;
        direction: rtl;
        border-radius: 8px;
        border: 1px solid #ced4da;
    }
    
    /* تنسيق الأزرار */
    .stButton > button {
        background-color: #2e7d32 !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #1b5e20 !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    /* تنسيق قسم المستندات */
    .upload-section {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border: 2px dashed #2e7d32;
        text-align: center;
        margin-top: 10px;
    }

    /* تنسيق قسم التواصل */
    .contact-footer {
        background: linear-gradient(135deg, #f5f5f5 0%, #e8e8e8 100%);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin-top: 30px;
        border: 2px solid #2e7d32;
    }
    .contact-title {
        color: #1b5e20;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 20px;
    }
    .contact-person {
        background: white;
        padding: 15px;
        margin: 10px 0;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .contact-name {
        color: #2e7d32;
        font-size: 1.2rem;
        font-weight: 600;
        margin: 5px 0;
    }
    .contact-label {
        color: #666;
        font-size: 0.9rem;
    }

    /* ==========================================
       تحسينات خاصة بالموبايل (Responsive)
       ========================================== */
    @media (max-width: 768px) {
        .main-header h1 { font-size: 1.6rem; }
        .main-header p { font-size: 1rem; }
        .main-header { padding: 18px 10px; }
        
        .stButton > button {
            font-size: 1rem !important;
            padding: 12px !important;
        }
        
        .stTextInput > div > div > input, 
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > select {
            font-size: 16px !important;
        }
        
        .block-container {
            padding-top: 2rem !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }
        
        .contact-title { font-size: 1.2rem; }
        .contact-name { font-size: 1rem; }
        .contact-footer { padding: 20px 15px; }
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. واجهة المستخدم (الشعار والصور بطريقة ذكية)
# ==========================================
st.markdown('<div class="logo-container">', unsafe_allow_html=True)

logo_path = "logo.png"
fallback_logo = "https://upload.wikimedia.org/wikipedia/ar/e/e0/National_Food_Safety_Authority_logo.png"

if os.path.exists(logo_path):
    try:
        img = Image.open(logo_path)
        st.image(img, width=220, use_container_width=False)
    except Exception:
        st.image(fallback_logo, width=220, caption="شعار الهيئة (رابط بديل)")
else:
    st.image(fallback_logo, width=220, caption="شعار الهيئة (رابط بديل - لم يتم العثور على logo.png)")

st.markdown('</div>', unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown("""
    <div class="main-header">
        <h1> الهيئة القومية لسلامة الغذاء</h1>
        <p>اعلان رقم 2 لسنة 2026 لشغل وظيفة مفتش اغذية عن طريق الاستعانة بالهيئة القومية لسلامة الغذاء</p>
    </div>
""", unsafe_allow_html=True)

# صورة المفتشين
inspector_path = "inspectors.jpg"
fallback_inspector = "https://images.unsplash.com/photo-1581093458791-9f3c3900df4b?auto=format&fit=crop&w=800&q=80"

if os.path.exists(inspector_path):
    st.image(inspector_path, caption="🌟 نفتخر بكفاءتكم في خدمة الوطن", use_container_width=True)
else:
    st.image(fallback_inspector, caption="🌟 نفتخر بكفاءتكم في خدمة الوطن", use_container_width=True)

st.markdown("---")

# ==========================================
# 4. نموذج التقديم
# ==========================================
with st.form("nfsa_application_form"):
    st.markdown("###  البيانات الشخصية")
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("1. الاسم رباعي *", placeholder="أدخل اسمك رباعي")
        national_id = st.text_input("2. الرقم القومي *", placeholder="14 رقم", max_chars=14)
        dob = st.date_input("3. تاريخ الميلاد *", min_value=date(1950, 1, 1), max_value=date.today())
        gender = st.selectbox("4. النوع *", ["ذكر", "أنثى"])
        
    with col2:
        address = st.text_area("5. العنوان بالتفصيل *", height=100)
        phone = st.text_input("6. رقم التلفون (واتس اب) *", placeholder="01xxxxxxxxx", max_chars=11)
        degree = st.selectbox("7. المؤهل الدراسى *", ["بكالوريوس زراعة", "بكالوريوس علوم", "بكالوريوس طب بيطرى"])
        sub_specialty = st.text_input("8. التخصص الفرعى *", placeholder="كما هو موضح بالاعلان")

    st.markdown("### 🎓 البيانات الأكاديمية والمهنية")
    col3, col4 = st.columns(2)
    with col3:
        grade = st.selectbox("9. التقدير *", ["امتياز", "جيد جدا", "جيد", "مقبول", "اخرى"])
        post_grad = st.text_area("10. الدراسات العليا (ان وجد)", placeholder="اكتب هنا أو اتركه فارغاً")
    
    with col4:
        experience = st.text_area("11. الخبرات السابقة (ان وجد)", placeholder="اكتب هنا أو اتركه فارغاً")

    st.markdown("### 📎 المستندات المطلوبة")
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "يرجى تحميل المستندات المطلوبة (ملف واحد بصيغة PDF، حد أقصى 10 ميجابايت) *",
        type=["pdf"]
    )
    st.markdown('</div>', unsafe_allow_html=True)

    submit_button = st.form_submit_button(" إرسال الطلب", use_container_width=True)

# ==========================================
# 5. معالجة إرسال النموذج
# ==========================================
if submit_button:
    errors = []
    if not name or len(name.split()) < 4: errors.append("يرجى إدخال الاسم رباعي بشكل صحيح.")
    if not national_id.isdigit() or len(national_id) != 14: errors.append("الرقم القومي يجب أن يتكون من 14 رقماً.")
    if not phone or not phone.isdigit() or len(phone) < 10: errors.append("يرجى إدخال رقم هاتف صحيح.")
    if not address: errors.append("يرجى إدخال العنوان بالتفصيل.")
    if uploaded_file is None: errors.append("يرجى تحميل المستندات المطلوبة (PDF).")
    elif uploaded_file.size > 10 * 1024 * 1024: errors.append("حجم الملف يتجاوز 10 ميجابايت.")

    if errors:
        for error in errors:
            st.error(f"⚠️ {error}")
    else:
        with st.spinner("⏳ جاري معالجة الطلب ورفع الملفات..."):
            try:
                file_name = f"{national_id}_{uploaded_file.name.replace(' ', '_')}"
                supabase.storage.from_("applications_docs").upload(
                    file_name, 
                    uploaded_file.getvalue(), 
                    {"content-type": "application/pdf"}
                )
                file_url = supabase.storage.from_("applications_docs").get_public_url(file_name)

                data_to_insert = {
                    "full_name": name, "national_id": national_id, "date_of_birth": str(dob),
                    "gender": gender, "address": address, "phone": phone, "degree": degree,
                    "sub_specialty": sub_specialty, "grade": grade, "postgraduate": post_grad,
                    "experience": experience, "document_url": file_url, "submission_date": str(date.today())
                }

                db_response = supabase.table("inspector_applications").insert(data_to_insert).execute()

                if db_response.data:
                    st.success("✅ تم إرسال طلبك بنجاح! سيتم مراجعته والتواصل معك قريباً.")
                    st.balloons()
                else:
                    st.error("حدث خطأ أثناء حفظ البيانات.")
            except Exception as e:
                st.error(f"حدث خطأ غير متوقع: {str(e)}")

# ==========================================
# 6. قسم التواصل والشكاوى (Footer)
# ==========================================
st.markdown("---")
st.markdown("""
    <style>
    .contact-footer {
        background: linear-gradient(135deg, #f5f5f5 0%, #e8e8e8 100%);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin-top: 30px;
        border: 2px solid #2e7d32;
    }
    .contact-title {
        color: #1b5e20;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 20px;
    }
    .contact-person {
        background: white;
        padding: 15px;
        margin: 10px 0;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .contact-name {
        color: #2e7d32;
        font-size: 1.2rem;
        font-weight: 600;
        margin: 5px 0;
    }
    .contact-label {
        color: #666;
        font-size: 0.9rem;
    }
    </style>
    
    <div class="contact-footer">
        <div class="contact-title">📞 للشكوى والاستعلام</div>
        <div style="margin: 20px 0;">
            <div class="contact-person">
                <div class="contact-label">مهندس أول</div>
                <div class="contact-name">👨‍ Eng. Samwel Atef</div>
            </div>
            <div class="contact-person">
                <div class="contact-label">مهندس</div>
                <div class="contact-name">👨‍ Eng. Ahmed El-Wahed</div>
            </div>
        </div>
        <div style="color: #666; font-size: 0.9rem; margin-top: 15px;">
            🕐 نعمل على خدمتكم من الأحد إلى الخميس<br>
            من 9:00 ص إلى 3:00 م
            01060662412
        </div>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 7. حقوق النشر
# ==========================================
st.markdown("""
    <div style='text-align: center; padding: 20px; color: #888; font-size: 0.85rem; border-top: 1px solid #ddd; margin-top: 20px;'>
        © 2024 الهيئة القومية لسلامة الغذاء - جميع الحقوق محفوظة<br>
        <span style='color: #2e7d32;'>🛡️ لسلامة غذائكم نعمل</span>
    </div>
""", unsafe_allow_html=True)