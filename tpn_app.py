import streamlit as st

st.set_page_config(
    page_title="TPN Compounding Calculator",
    page_icon="⚗️",
    layout="wide"
)

# ── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
  .stApp { background-color: #0f1923; }
  section[data-testid="stSidebar"] { background-color: #162032; }
  .block-container { padding-top: 1.5rem; }

  h1 { color: #00c8a0 !important; }
  h2, h3 { color: #3a8dff !important; }
  label { color: #7a92b0 !important; }

  .metric-card {
    background: #1e2d42; border: 1px solid #2a3f5a; border-radius: 10px;
    padding: 12px 16px; text-align: center; margin-bottom: 8px;
  }
  .metric-val { font-size: 1.4rem; font-weight: 800; color: #ffffff; }
  .metric-lbl { font-size: 0.65rem; color: #7a92b0; text-transform: uppercase; letter-spacing: 0.08em; margin-top: 3px; }

  .osm-central {
    background: rgba(255,92,92,0.15); border: 1px solid rgba(255,92,92,0.4);
    border-radius: 8px; padding: 10px 16px; color: #ff7f7f;
    font-weight: 700; font-size: 1rem; text-align: center;
  }
  .osm-peripheral {
    background: rgba(0,200,160,0.12); border: 1px solid rgba(0,200,160,0.35);
    border-radius: 8px; padding: 10px 16px; color: #00c8a0;
    font-weight: 700; font-size: 1rem; text-align: center;
  }
  .warn-box {
    background: rgba(255,179,71,0.1); border: 1px solid rgba(255,179,71,0.35);
    border-radius: 8px; padding: 10px 14px; color: #ffb347;
    font-size: 0.85rem; margin-top: 6px;
  }
  .info-box {
    background: rgba(58,141,255,0.07); border: 1px solid rgba(58,141,255,0.2);
    border-radius: 7px; padding: 8px 12px; color: #8ab8ff;
    font-size: 0.78rem; margin-bottom: 8px;
  }
  .from-aa {
    background: rgba(255,179,71,0.08); border: 1px solid rgba(255,179,71,0.3);
    border-radius: 7px; padding: 7px 10px; color: #ffb347;
    font-size: 0.85rem; font-weight: 600;
  }
  .result-pill {
    display: inline-block; background: rgba(0,200,160,0.1);
    border: 1px solid rgba(0,200,160,0.25); border-radius: 20px;
    padding: 3px 10px; font-size: 0.78rem; color: #00c8a0; margin: 2px 3px;
  }
  .section-divider {
    border-top: 1px solid #2a3f5a; margin: 18px 0 14px;
  }
  div[data-testid="stNumberInput"] input,
  div[data-testid="stSelectbox"] select {
    background-color: #162032 !important;
    color: #e8f0fe !important;
    border-color: #2a3f5a !important;
  }
  div[data-testid="stDataFrame"] { background: #1e2d42; }
  .stDataFrame { background: #1e2d42 !important; }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  HEADER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("# ⚗️ TPN Compounding Calculator")
st.markdown("**Central / Peripheral Line · Osmolarity · Electrolytes · Volumes**")
st.markdown("---")


# ══════════════════════════════════════════════════════════════════════════════
#  PATIENT PARAMETERS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("### 👤 Patient Parameters")
pc1, pc2, pc3 = st.columns(3)
weight   = pc1.number_input("Weight (kg)", min_value=0.5, max_value=250.0, value=70.0, step=0.5)
goal_vol = pc2.number_input("Total Fluid Goal (mL/day)", min_value=100, max_value=10000, value=2000, step=50)
duration = pc3.number_input("Duration (hours)", min_value=1, max_value=24, value=24, step=1)

st.markdown("---")


# ══════════════════════════════════════════════════════════════════════════════
#  DEXTROSE
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("### 🍬 Dextrose (Glucose)")
st.markdown('<div class="info-box">Enter <b>grams</b> or <b>g/kg/day</b> → volume auto-calculated from selected concentration.</div>', unsafe_allow_html=True)

d1, d2, d3, d4 = st.columns(4)
dex_conc_label = d1.selectbox("Concentration (%)", ["5% (50 g/L)", "10% (100 g/L)", "20% (200 g/L)", "25% (250 g/L)", "50% (500 g/L)"], index=2)
dex_conc = float(dex_conc_label.split("%")[0])

dex_gkg   = d2.number_input("Dose (g/kg/day)", min_value=0.0, max_value=30.0, value=0.0, step=0.5)
if dex_gkg > 0:
    dex_grams = weight * dex_gkg
else:
    dex_grams = d3.number_input("Dextrose (grams)", min_value=0.0, max_value=5000.0, value=0.0, step=5.0)

dex_vol = (dex_grams / (dex_conc / 100)) if dex_grams > 0 else 0.0
d4.metric("→ Volume (mL)", f"{dex_vol:.1f}")

dex_kcal = dex_grams * 3.4
dex_gir  = (dex_grams * 1000) / (weight * duration * 60) if dex_grams > 0 and weight > 0 and duration > 0 else 0

if dex_grams > 0:
    st.markdown(f'<span class="result-pill">Glucose: <b>{dex_grams:.1f} g</b></span>'
                f'<span class="result-pill">Energy: <b>{dex_kcal:.0f} kcal</b></span>'
                f'<span class="result-pill">GIR: <b>{dex_gir:.2f} mg/kg/min</b></span>',
                unsafe_allow_html=True)

st.markdown("---")


# ══════════════════════════════════════════════════════════════════════════════
#  AMINO ACIDS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("### 🧬 Amino Acids 10%")
st.markdown('<div class="info-box"><b>Per litre:</b> Protein 100 g | Na⁺ 50 mmol | K⁺ 25 mmol | Mg²⁺ 2.5 mmol | PO₄³⁻ 10 mmol | Cl⁻ 52 mmol | Acetate 46 mmol | Citrate 2 mmol | Osm ≈ 875 mOsm/L<br>These electrolytes are <b>auto-subtracted</b> from your targets below.</div>', unsafe_allow_html=True)

a1, a2, a3 = st.columns(3)
aa_gkg = a1.number_input("Protein dose (g/kg/day)", min_value=0.0, max_value=5.0, value=0.0, step=0.1)
if aa_gkg > 0:
    aa_grams = weight * aa_gkg
else:
    aa_grams = a2.number_input("Protein (grams)", min_value=0.0, max_value=2000.0, value=0.0, step=5.0)

aa_vol  = (aa_grams / 100) * 1000 if aa_grams > 0 else 0.0
a3.metric("→ Volume (mL)", f"{aa_vol:.1f}")

aa_kcal  = aa_grams * 4
aa_frac  = aa_vol / 1000
aa_Na    = 50  * aa_frac
aa_K     = 25  * aa_frac
aa_Mg    = 2.5 * aa_frac
aa_Phos  = 10  * aa_frac
aa_Cl    = 52  * aa_frac
aa_Ace   = 46  * aa_frac
aa_Cit   = 2   * aa_frac

if aa_grams > 0:
    st.markdown(f'<span class="result-pill">Protein: <b>{aa_grams:.1f} g</b></span>'
                f'<span class="result-pill">/kg: <b>{aa_grams/weight:.2f} g/kg</b></span>'
                f'<span class="result-pill">Energy: <b>{aa_kcal:.0f} kcal</b></span>'
                f'<span class="result-pill">Na⁺: <b>{aa_Na:.1f} mmol</b></span>'
                f'<span class="result-pill">K⁺: <b>{aa_K:.1f} mmol</b></span>',
                unsafe_allow_html=True)

st.markdown("---")


# ══════════════════════════════════════════════════════════════════════════════
#  ELECTROLYTES
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("### ⚡ Electrolytes — Target Dose Entry")
st.markdown('<div class="info-box">Enter your <b>total desired dose</b>. The calculator subtracts what the Amino Acid solution already provides (shown in 🟡 orange).</div>', unsafe_allow_html=True)

# ── SODIUM ────────────────────────────────────────────────────────────────────
with st.expander("🧂 Sodium — Na⁺", expanded=True):
    ns1, ns2, ns3, ns4 = st.columns(4)
    na_target = ns1.number_input("Target Na⁺ (mmol/day)", min_value=0.0, value=0.0, step=5.0)
    ns2.markdown(f'<div class="from-aa">🟡 From AA: <b>{aa_Na:.1f} mmol</b></div>', unsafe_allow_html=True)
    na_needed = max(0.0, na_target - aa_Na) if na_target > 0 else 0.0
    ns3.metric("Still needed (mmol)", f"{na_needed:.1f}" if na_target > 0 else "—")
    na_src = ns4.selectbox("Source", ["NaCl 3% (0.513 mmol/mL)", "Na Phosphate Braun (1 mmol/mL)"])

    na_vol = 0.0
    if na_target > 0:
        if "NaCl" in na_src:
            na_vol = na_needed / 0.51335
        else:
            na_vol = na_needed / 1.0
    st.metric("→ Volume of Na source to add (mL)", f"{na_vol:.1f}" if na_target > 0 else "—")

# ── POTASSIUM ─────────────────────────────────────────────────────────────────
with st.expander("🟨 Potassium — K⁺", expanded=True):
    ks1, ks2, ks3, ks4 = st.columns(4)
    k_target = ks1.number_input("Target K⁺ (mmol/day)", min_value=0.0, value=0.0, step=5.0)
    ks2.markdown(f'<div class="from-aa">🟡 From AA: <b>{aa_K:.1f} mmol</b></div>', unsafe_allow_html=True)
    k_needed = max(0.0, k_target - aa_K) if k_target > 0 else 0.0
    ks3.metric("Still needed (mmol)", f"{k_needed:.1f}" if k_target > 0 else "—")
    k_src = ks4.selectbox("Source", ["KCl 1:1 (1 mmol/mL)", "K Phosphate B.Braun (1 mmol/mL K⁺)"])

    k_vol = k_needed if k_target > 0 else 0.0
    st.metric("→ Volume of K source to add (mL)", f"{k_vol:.1f}" if k_target > 0 else "—")

# ── MAGNESIUM ─────────────────────────────────────────────────────────────────
with st.expander("🟩 Magnesium — Mg²⁺", expanded=True):
    st.markdown('<div class="info-box">MgSO₄: <b>8 mEq / 10 mL</b>. Mg²⁺ is divalent → <b>1 mmol = 2 mEq</b>, so 8 mEq = 4 mmol per vial = <b>0.4 mmol/mL</b>. Enter target in mmol. Osmolarity uses mmol × 2 = mEq automatically.</div>', unsafe_allow_html=True)
    ms1, ms2, ms3, ms4 = st.columns(4)
    mg_target = ms1.number_input("Target Mg²⁺ (mmol/day)", min_value=0.0, value=0.0, step=0.5)
    ms2.markdown(f'<div class="from-aa">🟡 From AA: <b>{aa_Mg:.1f} mmol</b></div>', unsafe_allow_html=True)
    mg_needed = max(0.0, mg_target - aa_Mg) if mg_target > 0 else 0.0
    ms3.metric("Still needed (mmol)", f"{mg_needed:.1f}" if mg_target > 0 else "—")
    mg_vol   = mg_needed / 0.4 if mg_target > 0 else 0.0
    mg_vials = mg_vol / 10
    ms4.metric("Vials (10 mL each)", f"{mg_vials:.1f}" if mg_target > 0 else "—")
    st.metric("→ Volume of MgSO₄ to add (mL)", f"{mg_vol:.1f}" if mg_target > 0 else "—")

# ── PHOSPHATE ─────────────────────────────────────────────────────────────────
with st.expander("🟦 Phosphate — PO₄³⁻", expanded=True):
    ps1, ps2, ps3, ps4 = st.columns(4)
    phos_target = ps1.number_input("Target PO₄³⁻ (mmol/day)", min_value=0.0, value=0.0, step=2.0)
    ps2.markdown(f'<div class="from-aa">🟡 From AA: <b>{aa_Phos:.1f} mmol</b></div>', unsafe_allow_html=True)
    phos_needed = max(0.0, phos_target - aa_Phos) if phos_target > 0 else 0.0
    ps3.metric("Still needed (mmol)", f"{phos_needed:.1f}" if phos_target > 0 else "—")
    phos_src = ps4.selectbox("Source", ["K Phosphate B.Braun (0.6 mmol/mL PO₄)", "Na Phosphate Braun (0.6 mmol/mL PO₄)"])

    phos_vol = phos_needed / 0.6 if phos_target > 0 else 0.0
    st.metric("→ Volume of PO₄ source to add (mL)", f"{phos_vol:.1f}" if phos_target > 0 else "—")

st.markdown("---")


# ══════════════════════════════════════════════════════════════════════════════
#  ADDITIONAL NaCl 3%
# ══════════════════════════════════════════════════════════════════════════════
with st.expander("🧂 Additional NaCl 3% (optional)"):
    extra_nacl3 = st.number_input("Extra NaCl 3% volume (mL)", min_value=0.0, value=0.0, step=10.0)

st.markdown("---")


# ══════════════════════════════════════════════════════════════════════════════
#  TRACE ELEMENTS & MULTIVITAMIN
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("### 🧪 Additives")
ta1, ta2 = st.columns(2)
trace_vol = ta1.number_input("Trace Elements — Volume (mL)", min_value=0.0, value=0.0, step=1.0)
mv_vol    = ta2.number_input("Multivitamin — Volume (mL)", min_value=0.0, value=0.0, step=1.0)

st.markdown("---")


# ══════════════════════════════════════════════════════════════════════════════
#  WFI
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("### 💧 Water for Injection / Diluent")
used_so_far = dex_vol + aa_vol + na_vol + k_vol + mg_vol + phos_vol + extra_nacl3 + trace_vol + mv_vol
auto_wfi    = max(0.0, goal_vol - used_so_far)
wa1, wa2 = st.columns([2, 1])
wfi_vol = wa1.number_input("WFI Volume (mL)", min_value=0.0, value=0.0, step=10.0)
wa2.markdown(f"**Auto-fill suggestion:** `{auto_wfi:.1f} mL`  \n*(to reach {goal_vol} mL goal)*")

st.markdown("---")


# ══════════════════════════════════════════════════════════════════════════════
#  CALCULATIONS
# ══════════════════════════════════════════════════════════════════════════════
total_vol  = dex_vol + aa_vol + na_vol + k_vol + mg_vol + phos_vol + extra_nacl3 + trace_vol + mv_vol + wfi_vol
total_kcal = dex_kcal + aa_kcal

# Electrolyte totals
tot_Na  = aa_Na + (na_needed if na_target > 0 else 0)
if na_target > 0 and "Na Phosphate" in na_src:
    tot_Na += 0  # already counted
    tot_Phos_from_na = na_needed * 0.6
else:
    tot_Phos_from_na = 0

tot_K   = aa_K + (k_needed if k_target > 0 else 0)
tot_Mg  = aa_Mg + (mg_needed if mg_target > 0 else 0)
tot_Phos = aa_Phos + (phos_needed * 0.6 / 0.6 if phos_target > 0 else 0) + tot_Phos_from_na
tot_Cl  = aa_Cl
if na_target > 0 and "NaCl" in na_src:
    tot_Cl += na_needed
if k_target > 0 and "KCl" in k_src:
    tot_Cl += k_needed
tot_Cl += extra_nacl3 * 0.51335

# Extra NaCl Na
tot_Na += extra_nacl3 * 0.51335

# K phosphate gives extra PO4 and Na phosphate gives extra Na
if k_target > 0 and "K Phosphate" in k_src:
    tot_Phos += k_needed * 0.6
if na_target > 0 and "Na Phosphate" in na_src:
    tot_Na += na_needed   # already in na_needed

# OSMOLARITY — correct TPN formula
# Osm = (g dextrose/L × 5) + (g AA/L × 10) + (mEq cations/L × 2)
vol_L = total_vol / 1000 if total_vol > 0 else 1
dex_gPerL = dex_grams / vol_L
aa_gPerL  = aa_grams  / vol_L
cations_mEq = tot_Na + tot_K + (tot_Mg * 2)   # Mg: 1 mmol = 2 mEq
cations_mEqPerL = cations_mEq / vol_L

osm_dex = dex_gPerL * 5
osm_aa  = aa_gPerL  * 10
osm_cat = cations_mEqPerL * 2
osmolarity = round(osm_dex + osm_aa + osm_cat)


# ══════════════════════════════════════════════════════════════════════════════
#  LIVE SUMMARY
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("## 📊 Results Summary")

# Osmolarity + route
if osmolarity > 900:
    st.markdown(f'<div class="osm-central">⚠️ CENTRAL LINE Required — Osmolarity: {osmolarity} mOsm/L (>900)</div>', unsafe_allow_html=True)
else:
    st.markdown(f'<div class="osm-peripheral">✅ Peripheral Line Safe — Osmolarity: {osmolarity} mOsm/L (≤900)</div>', unsafe_allow_html=True)

osm_pct = min(100, (osmolarity / 1800) * 100)
bar_color = "#ff5c5c" if osmolarity > 900 else "#ffb347" if osmolarity > 600 else "#00c8a0"
st.markdown(f"""
<div style="background:#162032;border-radius:20px;height:14px;overflow:hidden;margin:10px 0 4px;">
  <div style="width:{osm_pct}%;height:100%;background:{bar_color};border-radius:20px;transition:width 0.4s;"></div>
</div>
<div style="display:flex;justify-content:space-between;font-size:0.7rem;color:#7a92b0;">
  <span>0</span><span>900 threshold</span><span>1800+</span>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Stat boxes
sc1, sc2, sc3, sc4 = st.columns(4)
sc1.metric("Total Volume (mL)", f"{total_vol:.0f}")
sc2.metric("Total kcal", f"{total_kcal:.0f}")
sc3.metric("Protein (g/kg)", f"{aa_grams/weight:.2f}" if aa_grams > 0 and weight > 0 else "—")
sc4.metric("GIR (mg/kg/min)", f"{dex_gir:.2f}" if dex_grams > 0 else "—")

sc5, sc6, sc7, sc8 = st.columns(4)
sc5.metric("Na⁺ total (mmol)", f"{tot_Na:.1f}")
sc6.metric("K⁺ total (mmol)", f"{tot_K:.1f}")
sc7.metric("Mg²⁺ total (mmol)", f"{tot_Mg:.1f}")
sc8.metric("PO₄³⁻ total (mmol)", f"{tot_Phos:.1f}")

st.markdown("---")


# ══════════════════════════════════════════════════════════════════════════════
#  OSMOLARITY BREAKDOWN
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("### 📐 Osmolarity Breakdown")
st.markdown('<div class="info-box"><b>Formula:</b> Osmolarity (mOsm/L) = (g dextrose/L × 5) + (g amino acid/L × 10) + (mEq cations/L × 2)<br>Mg counts as 2 mEq per mmol (divalent cation)</div>', unsafe_allow_html=True)

import pandas as pd
osm_data = []
if dex_grams > 0:
    osm_data.append({"Component": f"Dextrose ({dex_gPerL:.1f} g/L × 5)", "mOsm/L": round(osm_dex)})
if aa_grams > 0:
    osm_data.append({"Component": f"Amino Acids ({aa_gPerL:.1f} g/L × 10)", "mOsm/L": round(osm_aa)})
if cations_mEq > 0:
    osm_data.append({"Component": f"Cations ({cations_mEqPerL:.1f} mEq/L × 2)  [Na {tot_Na:.1f} + K {tot_K:.1f} + Mg {tot_Mg:.1f}×2]", "mOsm/L": round(osm_cat)})
osm_data.append({"Component": f"TOTAL  ({total_vol:.0f} mL)", "mOsm/L": osmolarity})

df_osm = pd.DataFrame(osm_data)
st.dataframe(df_osm, use_container_width=True, hide_index=True)

st.markdown("---")


# ══════════════════════════════════════════════════════════════════════════════
#  FINAL RECIPE
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("### 📋 Final Compounding Recipe")

recipe = []
if dex_vol > 0:
    recipe.append({"Component": f"Dextrose {dex_conc:.0f}%", "Volume (mL)": round(dex_vol, 1),
                   "Details": f"{dex_grams:.1f} g glucose · {dex_kcal:.0f} kcal · GIR {dex_gir:.2f} mg/kg/min"})
if aa_vol > 0:
    recipe.append({"Component": "Amino Acids 10%", "Volume (mL)": round(aa_vol, 1),
                   "Details": f"{aa_grams:.1f} g protein ({aa_grams/weight:.2f} g/kg) · {aa_kcal:.0f} kcal | Na {aa_Na:.1f} · K {aa_K:.1f} · Mg {aa_Mg:.1f} · PO₄ {aa_Phos:.1f} mmol"})
if na_vol > 0:
    src_label = "NaCl 3%" if "NaCl" in na_src else "Na Phosphate Braun"
    recipe.append({"Component": src_label, "Volume (mL)": round(na_vol, 1),
                   "Details": f"Na⁺ {na_needed:.1f} mmol" + (f" + PO₄³⁻ {na_needed*0.6:.1f} mmol" if "Phosphate" in na_src else f" + Cl⁻ {na_needed:.1f} mmol")})
if k_vol > 0:
    k_label = "KCl 1:1" if "KCl" in k_src else "K Phosphate B.Braun"
    recipe.append({"Component": k_label, "Volume (mL)": round(k_vol, 1),
                   "Details": f"K⁺ {k_needed:.1f} mmol" + (f" + PO₄³⁻ {k_needed*0.6:.1f} mmol" if "K Phosphate" in k_src else f" + Cl⁻ {k_needed:.1f} mmol")})
if mg_vol > 0:
    recipe.append({"Component": "MgSO₄ 8mEq/10mL", "Volume (mL)": round(mg_vol, 1),
                   "Details": f"{mg_vials:.1f} vials × 10 mL | Mg²⁺ {mg_needed:.1f} mmol ({mg_needed*2:.1f} mEq)"})
if phos_vol > 0:
    p_label = "K Phosphate B.Braun" if "K Phosphate" in phos_src else "Na Phosphate Braun"
    recipe.append({"Component": p_label, "Volume (mL)": round(phos_vol, 1),
                   "Details": f"PO₄³⁻ {phos_needed:.1f} mmol + {'K⁺' if 'K Phosphate' in phos_src else 'Na⁺'} {phos_vol:.1f} mmol"})
if extra_nacl3 > 0:
    recipe.append({"Component": "NaCl 3% (extra)", "Volume (mL)": round(extra_nacl3, 1),
                   "Details": f"Na⁺ {extra_nacl3*0.51335:.1f} mmol · Cl⁻ {extra_nacl3*0.51335:.1f} mmol"})
if trace_vol > 0:
    recipe.append({"Component": "Trace Elements", "Volume (mL)": round(trace_vol, 1), "Details": "Fixed additive — volume only"})
if mv_vol > 0:
    recipe.append({"Component": "Multivitamin", "Volume (mL)": round(mv_vol, 1), "Details": "Fixed additive — volume only"})
if wfi_vol > 0:
    recipe.append({"Component": "Water for Injection", "Volume (mL)": round(wfi_vol, 1), "Details": "Diluent — 0 mOsm"})

if recipe:
    recipe.append({"Component": "── TOTAL ──", "Volume (mL)": round(total_vol, 1),
                   "Details": f"Osmolarity: {osmolarity} mOsm/L · {'⚠️ CENTRAL LINE' if osmolarity > 900 else '✅ Peripheral safe'}"})
    df_recipe = pd.DataFrame(recipe)
    st.dataframe(df_recipe, use_container_width=True, hide_index=True)

    # Download button
    csv = df_recipe.to_csv(index=False)
    st.download_button("⬇️ Download Recipe as CSV", csv, "tpn_recipe.csv", "text/csv")
else:
    st.info("Fill in components above to generate the recipe.")

st.markdown("---")


# ══════════════════════════════════════════════════════════════════════════════
#  CLINICAL WARNINGS
# ══════════════════════════════════════════════════════════════════════════════
warnings = []
if osmolarity > 900:
    warnings.append("⚠️ Osmolarity >900 mOsm/L — Central venous access required.")
if na_target > 0 and na_target < aa_Na:
    warnings.append(f"⚠️ Na⁺ target ({na_target} mmol) is less than what AA solution alone provides ({aa_Na:.1f} mmol). Reconsider target or AA volume.")
if k_target > 0 and k_target < aa_K:
    warnings.append(f"⚠️ K⁺ target ({k_target} mmol) is less than what AA solution provides ({aa_K:.1f} mmol).")
if tot_K > weight * 3:
    warnings.append("⚠️ Total K⁺ may exceed safe limit (~3 mmol/kg/day max in TPN).")
if dex_grams > 0 and dex_gir > 7:
    warnings.append("⚠️ GIR >7 mg/kg/min — risk of hyperglycemia. Consider reducing dextrose.")
if total_vol > goal_vol * 1.05:
    warnings.append(f"⚠️ Total volume ({total_vol:.0f} mL) exceeds fluid goal ({goal_vol} mL).")

if warnings:
    st.markdown("### ⚠️ Clinical Warnings")
    for w in warnings:
        st.markdown(f'<div class="warn-box">{w}</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("⚗️ TPN Compounding Calculator — For clinical use by trained pharmacy/nutrition professionals only.")
