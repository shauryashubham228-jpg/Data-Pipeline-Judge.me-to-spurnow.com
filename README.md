# Data-Pipeline-Judge.me-to-spurnow.com
---

# 📂 Project: Automated Review-to-Broadcast Pipeline

**Status:** 🟢 Operational | **Tools:** Node.js, Shopify, Judge.me, Spurnow

---

## 📝 1. Executive Summary

This project automates the extraction of customer reviews and synchronizes them with real-time marketing consent data from Shopify. The final output is a verified, compliant list of customers ready for high-conversion broadcasts via **Spurnow**.

---

## 🛠 2. Configuration & Credentials

> [!IMPORTANT]
> 
> 
> Keep these keys secure. Do not share them in public repositories.
> 

| **Service** | **Variable** | **Purpose** |
| --- | --- | --- |
| **Judge.me** | `JUDGEME_API_TOKEN` | Fetches all customer review data. |
| **Shopify** | `SHOPIFY_TOKEN` | Verifies customer marketing opt-in status. |
| **Shopify** | `SHOPIFY_STORE` | Target store domain (`lagorii-kids.myshopify.com`). |
| **Spurnow** | **Import Tool** | Final destination for the broadcast list. |

---

## 🔄 3. The Data Pipeline Flow

The system follows a strict 4-step process to ensure compliance and data accuracy:

1. **Ingestion:** Script pulls all reviews from **Judge.me**.
2. **Cross-Reference:** Script searches **Shopify** via API for each reviewer's email.
3. **Consent Gate (Compliance):** * If `subscribed` $\rightarrow$ Added to CSV with Phone/Email.
    - If `not_subscribed` $\rightarrow$ Customer is skipped entirely.
4. **Export:** Generates `reachable_review_customers.csv`.

---

## 💻 4. Technical Implementation

### **The Logic Gate Snippet**

This part of the code prevents us from messaging customers who have opted out, keeping the brand compliant with GDPR/TCPA.

JavaScript

`// Verification Logic
const emailConsent = customer.email_marketing_consent?.state === "subscribed";
const smsConsent = customer.sms_marketing_consent?.state === "subscribed";

// Skip if NO marketing permission exists
if (!emailConsent && !smsConsent) continue;

rows.push([
  csvSafe(r.id),
  csvSafe(emailConsent ? email : ""),           // Email included ONLY if opted-in
  csvSafe(smsConsent ? customer.phone : ""),    // Phone included ONLY if opted-in
  csvSafe(r.product_title)                      // Product name for personalization
].join(","));`

---

## 📢 5. Spurnow Broadcast Strategy

Once the CSV is ready, follow these steps to reach your customers:

### **A. CSV Upload Mapping**

When importing the list into **Spurnow**, map the following:

- **Phone Number** $\rightarrow$ `phone` column.
- **Custom Attribute 1** $\rightarrow$ `product` (Use this to mention their specific purchase).
- **Custom Attribute 2** $\rightarrow$ `rating` (Use this to segment 5-star fans).

### **B. Recommended Message Template**

> "Hi {{name}}! 👋 Thank you for the {{rating}}-star review on your **{{product}}**! 🌟 We truly appreciate your support.
> 
> 
> As a thank you, use code **THANKS10** for 10% off your next order! Want to be featured? Reply with a photo of your little one with their item! 🎁"
> 

---

## ⚠️ 6. Maintenance & Safety

- **Rate Limits:** The script includes a `800ms` delay. **Do not remove this**, or Shopify will block the connection.
- **Data Hygiene:** Run the script immediately before every Spurnow broadcast to ensure you are using the most current "Subscribed" list.
- **Storage:** Delete the `reachable_review_customers.csv` after the Spurnow import to maintain PII (Personally Identifiable Information) security.

---

## ✅ 7. Success Checklist

- [ ]  Run `node export.js`.
- [ ]  Confirm `reachable_review_customers.csv` is created.
- [ ]  Upload CSV to **Spurnow**.
- [ ]  Verify message variables (`{{product}}`, `{{name}}`) are working.
- [ ]  **Launch Broadcast.**
