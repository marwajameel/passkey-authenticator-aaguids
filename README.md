import time
import base64
import requests 
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# --- 1. اپنی ضروری معلومات (ان 2 لائنوں کو تبدیل کریں) ---
# ⚠️ 1. اپنی ٹیسٹ نیٹ API Key ID یہاں لکھیں
API_KEY = "YOUR_TESTNET_API_KEY_ID" 

# ⚠️ 2. اپنی Ed25519 نجی کلید فائل کا درست راستہ یہاں دیں
PRIVATE_KEY_PATH = "binance-ed25519-private.pem" 

# ٹریڈنگ کے پیرامیٹرز (آپ انہیں اپنی ضرورت کے مطابق بدل سکتے ہیں)
symbol = "BNBUSDT"
side = "BUY" # خرید کا آرڈر
quantity = "0.01"
price = "300"
order_type = "LIMIT"

# --- 2. پیغام (Payload) تیار کرنا اور دستخط (Signing) ---
timestamp = int(time.time() * 1000)
# تمام پیرامیٹرز کو ایک سٹرنگ میں ترتیب دیں
payload = f"symbol={symbol}&side={side}&type={order_type}&quantity={quantity}&price={price}&timeInForce=GTC&timestamp={timestamp}"

# نجی کلید (Private Key) لوڈ کرنا
try:
    with open(PRIVATE_KEY_PATH, "rb") as key_file:
        private_key_bytes = key_file.read()
    
    private_key = serialization.load_pem_private_key(
        private_key_bytes,
        password=None, 
        backend=default_backend()
    )
except FileNotFoundError:
    print(f"غلطی: نجی کلید فائل نہیں ملی: {PRIVATE_KEY_PATH}")
    exit()

# پیغام پر دستخط کرنا (Ed25519 Signature)
signature_bytes = private_key.sign(payload.encode('utf-8'))

# دستخط کو URL کے لیے تیار کرنا (Base64 URL-safe Encoding)
signature = base64.urlsafe_b64encode(signature_bytes).decode().rstrip('=')

# --- 3. درخواست (Request) بھیجنا ---
full_params = payload + f"&signature={signature}"

# ٹیسٹ نیٹ URL
url = "https://testnet.binance.vision/api/v3/order" 

headers = {
    "X-MBX-APIKEY": API_KEY 
} 

print(f"آرڈر کی تفصیلات: {full_params}")

try:
    # بائنانس کو POST درخواست بھیجنا
    response = requests.post(url, headers=headers, params=full_params)
    
    print("\n--- بائنانس کا جواب (Response) ---")
    print(response.json())

except Exception as e:
    print(f"\nدرخواست بھیجنے میں غلطی: {e}")# Passkey Provider AAGUIDs

This is a **community-driven** list of known passkey provider AAGUIDs to assist with naming passkeys in end user passkey management interfaces (e.g. account settings). **It is not intended to be used for any other purpose** and **_could go away at any time_**. 

> [!IMPORTANT]  
> When this list is officially retired at some point in the future, the contents of both `aaguid.json` and `combined_aaguid.json` will be removed, **leaving an empty object**.
>
> It is **_highly_** recommended that you add some code that checks for an empty object after fetching the document (ex: `Object.keys(aaguid).length === 0`), and notifying the appropriate team(s). This README will also be updated with details.

This does not replace [FIDO's Metadata Service (MDS)](https://fidoalliance.org/metadata/), which should continue to be used for all authoritative security details about FIDO authenticators. Some AAGUIDs in this list may not appear in FIDO MDS.

A visual explorer of the list is available here: https://passkeydeveloper.github.io/passkey-authenticator-aaguids/explorer/

## Schema

For full details, see the latest JSON schema file: [https://github.com/passkeydeveloper/passkey-authenticator-aaguids/blob/main/aaguid.json.schema](https://github.com/passkeydeveloper/passkey-authenticator-aaguids/blob/main/aaguid.json.schema)

The top level property value is the AAGUID itself. For consistency in this file, ensure it is lowercase.

Each AAGUID member has at minimum, a `name` property. This property represents the friendly name of the passkey provider for display in RP interfaces. For example, "Google Password Manager", "Dashlane", or "1Password".

Each AAGUID member can also _optionally_ contain embedded icon data, for use next to the friendly name in RP interfaces.

The properties are `icon_dark` and `icon_light`. The values of these properties must be SVG data encoded into a base64 data URI. `icon_dark` should be a version targeted at dark mode and/or dark backgrounds. `icon_light` should be a version targeted at light mode and/or light backgrounds. The image must be square. The icon must be completely vector based and cannot contain embedded images (PNG, JPG, etc).

Many web-based tools can do this encoding/formatting, including: [https://base64.guru/converter/encode/image/svg](https://base64.guru/converter/encode/image/svg) (select `Data URI` under "Output Format").

Example of the Google G icon as a base64 encoded SVG data URI:

![]تحصیل پریس کلب رجسٹرڈ سرائے عالمگیر کی تق