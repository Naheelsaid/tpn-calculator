# ⚗️ TPN Compounding Calculator

A clinical TPN (Total Parenteral Nutrition) calculator built with Streamlit.

## Features
- Dextrose & Amino Acid gram-based dosing → auto-calculates volume
- Smart electrolyte panel (Na, K, Mg, PO₄) — subtracts AA contributions automatically
- Correct TPN osmolarity formula: **(g dextrose/L × 5) + (g AA/L × 10) + (mEq cations/L × 2)**
- Central vs Peripheral line decision (threshold 900 mOsm/L)
- Trace elements & multivitamin volumes
- Final compounding recipe with CSV download
- Clinical safety warnings

## Products included
- Dextrose 5/10/20/25/50%
- Amino Acids 10% (with built-in electrolytes)
- NaCl 3% — PSI (513.35 mmol/L)
- KCl 1:1 (1 mmol/mL)
- K Phosphate B.Braun (K⁺ 1 mmol/mL, PO₄ 0.6 mmol/mL, 20 mL amps)
- Na Phosphate Braun (Na⁺ 1 mmol/mL, PO₄ 0.6 mmol/mL)
- MgSO₄ 8 mEq/10 mL (0.4 mmol/mL)
- Trace Elements & Multivitamin (volume-only)
- Water for Injection

## Run locally
```bash
pip install -r requirements.txt
streamlit run tpn_app.py
```

## Deploy on Streamlit Cloud (free)
1. Push these files to a GitHub repository
2. Go to https://share.streamlit.io
3. Click **New app** → connect your GitHub repo
4. Set main file: `tpn_app.py`
5. Click **Deploy** — your app will be live in ~2 minutes

## Files
- `tpn_app.py` — main app
- `requirements.txt` — dependencies
- `README.md` — this file
