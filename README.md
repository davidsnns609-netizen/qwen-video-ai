# Qwen Video AI

موقع بسيط: وصف نصي ← فيديو MP4 قابل للمشاهدة والتحميل.

## متطلبات التشغيل
- Python 3.10 أو أحدث
- حساب Hugging Face ومفتاح API بصلاحية Inference Providers
- اتصال بالإنترنت

## التشغيل محليًا
1. فك ضغط المشروع.
2. افتح الطرفية داخل مجلد المشروع.
3. ثبّت الحزم:
   `pip install -r requirements.txt`
4. أنشئ مفتاحًا من إعدادات Hugging Face:
   https://huggingface.co/settings/tokens
   واختر صلاحية Inference Providers.
5. عيّن المفتاح كمتغير بيئة (لا تضعه داخل ملفات الواجهة ولا تشاركه):
   - macOS/Linux: `export HF_TOKEN=hf_xxxxxxxxx`
   - Windows PowerShell: `$env:HF_TOKEN="hf_xxxxxxxxx"`
6. شغّل:
   `python app.py`
7. افتح:
   http://localhost:8000

## النشر
انشر المشروع على استضافة تدعم Python وFastAPI، وأضف `HF_TOKEN` في إعدادات Secrets/Environment Variables لدى الاستضافة. لا ترفع المفتاح إلى GitHub أو داخل كود المتصفح.

## تنبيه مهم عن المجانية
واجهة الموقع مجانية ومفتوحة المصدر. توليد الفيديو نفسه يعتمد على مزود استدلال خارجي؛ قد تتوفر أرصدة تجريبية محدودة فقط، وليست خدمة مجانية غير محدودة. راجع الأسعار والتوفر قبل الاستخدام:
https://huggingface.co/docs/inference-providers/pricing

## النموذج
يستخدم المثال نموذج `Wan-AI/Wan2.2-TI2V-5B` عبر Hugging Face InferenceClient ومزود fal-ai. قد تتغير إتاحة النموذج أو متطلبات المزود؛ راجع:
https://huggingface.co/docs/inference-providers/tasks/text-to-video
