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
  .dex-conc-pill {
    display: inline-block; background: rgba(255,179,71,0.12);
    border: 1px solid rgba(255,179,71,0.4); border-radius: 20px;
    padding: 4px 14px; font-size: 0.85rem; color: #ffb347;
    margin: 2px 3px; font-weight: 700;
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
st.markdown("""
<svg width="100%" viewBox="0 0 680 90" role="img" style="display:block;margin-bottom:4px;">
  <title>TPN Compounding Calculator</title>
  <desc>IV bag icon with title text beside it</desc>
  <path d="M44 5 Q44 2 47 2 Q50 2 50 5" fill="none" stroke="#7a92b0" stroke-width="1.4" stroke-linecap="round"/>
  <line x1="47" y1="5" x2="47" y2="12" stroke="#7a92b0" stroke-width="1" stroke-linecap="round"/>
  <rect x="12" y="12" width="70" height="48" rx="8" fill="#0d2035" stroke="#00c8a0" stroke-width="1.4"/>
  <rect x="12" y="38" width="70" height="22" rx="0" fill="#0a3d2e" style="clip-path:inset(0 0 0 0 round 0 0 8px 8px)"/>
  <path d="M12 38 Q19 34 26 38 Q33 42 40 38 Q47 34 54 38 Q61 42 68 38 Q75 36 82 38" fill="none" stroke="#00c8a0" stroke-width="0.8" opacity="0.5"/>
  <rect x="33" y="17" width="28" height="18" rx="3" fill="#071626" stroke="#00c8a0" stroke-width="0.8"/>
  <rect x="39" y="19" width="8"  height="14" rx="1.5" fill="#00c8a0"/>
  <rect x="35" y="23" width="24" height="5"  rx="1.5" fill="#00c8a0"/>
  <rect x="38" y="60" width="18" height="5"  rx="2" fill="#0d2035" stroke="#00c8a0" stroke-width="1"/>
  <rect x="41" y="65" width="12" height="3"  rx="1.5" fill="#0d2035" stroke="#00c8a0" stroke-width="0.8"/>
  <rect x="38" y="68" width="18" height="13" rx="3" fill="#071626" stroke="#3a8dff" stroke-width="1"/>
  <ellipse cx="47" cy="76" rx="2" ry="2.5" fill="#3a8dff"/>
  <path d="M47 81 Q47 87 47 88" fill="none" stroke="#3a8dff" stroke-width="1.2" stroke-linecap="round"/>
  <line x1="98" y1="5" x2="98" y2="88" stroke="#2a3f5a" stroke-width="1"/>
  <text x="112" y="40" font-family="sans-serif" font-size="22" font-weight="700" fill="#00c8a0">TPN Compounding Calculator</text>
</svg>
<hr style="border-color:#2a3f5a;margin-top:0;">
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  PATIENT TYPE
# ══════════════════════════════════════════════════════════════════════════════
pt_col1, pt_col2 = st.columns([2, 5])
patient_type = pt_col1.radio("👶 Patient Type", ["Adult", "Pediatric"], horizontal=True)
is_pediatric = patient_type == "Pediatric"

st.markdown("---")


# ══════════════════════════════════════════════════════════════════════════════
#  PATIENT PARAMETERS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("### 👤 Patient Parameters")
pc1, pc2, pc3, pc4 = st.columns(4)

_wt_default  = 10.0 if is_pediatric else 70.0
_wt_max      = 100.0 if is_pediatric else 250.0
_wt_step     = 0.1  if is_pediatric else 0.5
_vol_default = 1000 if is_pediatric else 2000
_vol_step    = 10   if is_pediatric else 50

weight   = pc1.number_input("Weight (kg)", min_value=0.1, max_value=_wt_max, value=_wt_default, step=_wt_step)
goal_vol = pc2.number_input("Total Fluid Goal (mL/day)", min_value=50, max_value=10000, value=_vol_default, step=_vol_step)
duration = pc3.number_input("Duration (hours)", min_value=1, max_value=24, value=24, step=1)
planned_rate = goal_vol / duration
pc4.metric("Infusion Rate (mL/hr)", f"{planned_rate:.1f}")

fluid_per_kg = goal_vol / weight if weight > 0 else 0
st.markdown(f'<span class="result-pill">Fluid: <b>{fluid_per_kg:.1f} mL/kg/day</b></span>', unsafe_allow_html=True)

st.markdown("---")


# ══════════════════════════════════════════════════════════════════════════════
#  DEXTROSE
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("### 🍬 Dextrose (Glucose)")
st.markdown('<div class="info-box">Enter <b>grams</b> or <b>g/kg/day</b> → volume auto-calculated from selected concentration.</div>', unsafe_allow_html=True)

d1, d2, d3, d4 = st.columns(4)
dex_conc_label = d1.selectbox("Concentration (%)", ["5% (50 g/L)", "10% (100 g/L)", "20% (200 g/L)", "25% (250 g/L)", "50% (500 g/L)"], index=2)
dex_conc = float(dex_conc_label.split("%")[0])

dex_gkg = d2.number_input("Dose (g/kg/day)", min_value=0.0, max_value=30.0, value=0.0, step=0.5)
if dex_gkg > 0:
    dex_grams = weight * dex_gkg
else:
    dex_grams = d3.number_input("Dextrose (grams)", min_value=0.0, max_value=5000.0, value=0.0, step=5.0)

dex_vol  = (dex_grams / (dex_conc / 100)) if dex_grams > 0 else 0.0
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

aa_kcal = aa_grams * 4
aa_frac = aa_vol / 1000
aa_Na   = 50  * aa_frac
aa_K    = 25  * aa_frac
aa_Mg   = 2.5 * aa_frac
aa_Phos = 10  * aa_frac
aa_Cl   = 52  * aa_frac
aa_Ace  = 46  * aa_frac
aa_Cit  = 2   * aa_frac

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

_phos_target_pre = st.session_state.get("phos_target_pre", 0.0)
_phos_src_pre    = st.session_state.get("phos_src_pre", "K Phosphate B.Braun (0.6 mmol/mL PO₄)")
_phos_needed_pre = max(0.0, _phos_target_pre - aa_Phos) if _phos_target_pre > 0 else 0.0
_phos_vol_pre    = _phos_needed_pre / 0.6 if _phos_target_pre > 0 else 0.0
k_from_phos  = _phos_vol_pre if (_phos_target_pre > 0 and "K Phosphate" in _phos_src_pre) else 0.0
na_from_phos = _phos_vol_pre if (_phos_target_pre > 0 and "Na Phosphate" in _phos_src_pre) else 0.0

# ── SODIUM ────────────────────────────────────────────────────────────────────
with st.expander("🧂 Sodium — Na⁺", expanded=True):
    ns1, ns2, ns3, ns4 = st.columns(4)
    na_target = ns1.number_input("Target Na⁺ (mmol/day)", min_value=0.0, value=0.0, step=5.0)
    ns2.markdown(f'<div class="from-aa">🟡 From AA: <b>{aa_Na:.1f} mmol</b></div>', unsafe_allow_html=True)
    na_needed = max(0.0, na_target - aa_Na) if na_target > 0 else 0.0
    ns3.metric("Still needed after AA (mmol)", f"{na_needed:.1f}" if na_target > 0 else "—")
    na_src = ns4.selectbox("Source", ["NaCl 3% (0.513 mmol/mL)"])

    na_nacl_needed = max(0.0, na_needed - na_from_phos) if na_target > 0 else 0.0

    if na_from_phos > 0 and na_target > 0:
        st.markdown(
            f'<div class="info-box">ℹ️ <b>Na Phosphate (PO₄ section) co-delivers {na_from_phos:.1f} mmol Na⁺</b> '
            f'→ NaCl 3% still needed: <b>{na_nacl_needed:.1f} mmol</b></div>',
            unsafe_allow_html=True
        )
    elif na_from_phos > 0 and na_target == 0:
        st.markdown(
            f'<div class="info-box">ℹ️ Na Phosphate (PO₄ section) will deliver <b>{na_from_phos:.1f} mmol Na⁺</b>. '
            f'Set a Na⁺ target above to see the full breakdown.</div>',
            unsafe_allow_html=True
        )

    na_vol = (na_nacl_needed / 0.51335) if na_target > 0 else 0.0
    st.metric("→ Volume of NaCl 3% to add (mL)", f"{na_vol:.1f}" if na_target > 0 else "—")

# ── POTASSIUM ─────────────────────────────────────────────────────────────────
with st.expander("🟨 Potassium — K⁺", expanded=True):
    ks1, ks2, ks3, ks4 = st.columns(4)
    k_target = ks1.number_input("Target K⁺ (mmol/day)", min_value=0.0, value=0.0, step=5.0)
    ks2.markdown(f'<div class="from-aa">🟡 From AA: <b>{aa_K:.1f} mmol</b></div>', unsafe_allow_html=True)
    k_needed = max(0.0, k_target - aa_K) if k_target > 0 else 0.0
    ks3.metric("Still needed after AA (mmol)", f"{k_needed:.1f}" if k_target > 0 else "—")
    k_src = ks4.selectbox("KCl Source", ["KCl 1:1 (1 mmol K⁺/mL)", "KCl 2:1 (2 mmol K⁺/mL)"])
    k_conc = 1.0 if "1:1" in k_src else 2.0

    k_kcl_needed = max(0.0, k_needed - k_from_phos) if k_target > 0 else 0.0

    if k_from_phos > 0 and k_target > 0:
        st.markdown(
            f'<div class="info-box">ℹ️ <b>K Phosphate (PO₄ section) co-delivers {k_from_phos:.1f} mmol K⁺</b> '
            f'→ KCl still needed: <b>{k_kcl_needed:.1f} mmol</b></div>',
            unsafe_allow_html=True
        )
    elif k_from_phos > 0 and k_target == 0:
        st.markdown(
            f'<div class="info-box">ℹ️ K Phosphate (PO₄ section) will deliver <b>{k_from_phos:.1f} mmol K⁺</b>. '
            f'Set a K⁺ target above to see the full breakdown.</div>',
            unsafe_allow_html=True
        )

    k_vol             = k_kcl_needed / k_conc if k_target > 0 else 0.0
    k_cl_contribution = k_kcl_needed
    st.metric("→ Volume of KCl to add (mL)", f"{k_vol:.1f}" if k_target > 0 else "—")
    if k_target > 0:
        st.markdown(
            f'<span class="result-pill">K⁺: <b>{k_kcl_needed:.1f} mmol</b></span>'
            f'<span class="result-pill">Cl⁻ from KCl: <b>{k_cl_contribution:.1f} mmol</b></span>',
            unsafe_allow_html=True
        )

# ── MAGNESIUM ─────────────────────────────────────────────────────────────────
MG_MEQ_PER_ML  = 0.81
MG_MMOL_PER_ML = 0.405
MG_VIAL_ML     = 10

with st.expander("🟩 Magnesium — Mg²⁺", expanded=True):
    st.markdown(
        f'<div class="info-box">MgSO₄: <b>8.1 mEq / 10 mL</b> ({MG_MEQ_PER_ML} mEq/mL = {MG_MMOL_PER_ML} mmol/mL). '
        f'Mg²⁺ is divalent → <b>1 mmol = 2 mEq</b>. '
        f'Enter target in <b>mEq</b> — converted to mmol internally (÷ 2) for volume and osmolarity.</div>',
        unsafe_allow_html=True
    )
    ms1, ms2, ms3, ms4 = st.columns(4)
    mg_target_meq = ms1.number_input("Target Mg²⁺ (mEq/day)", min_value=0.0, value=0.0, step=1.0)
    mg_target     = mg_target_meq / 2
    aa_Mg_meq     = aa_Mg * 2
    ms2.markdown(f'<div class="from-aa">🟡 From AA: <b>{aa_Mg_meq:.1f} mEq</b> ({aa_Mg:.2f} mmol)</div>', unsafe_allow_html=True)
    mg_needed     = max(0.0, mg_target - aa_Mg) if mg_target_meq > 0 else 0.0
    mg_needed_meq = mg_needed * 2
    ms3.metric("Still needed (mEq)", f"{mg_needed_meq:.1f}" if mg_target_meq > 0 else "—")
    mg_vol   = mg_needed / MG_MMOL_PER_ML if mg_target_meq > 0 else 0.0
    mg_vials = mg_vol / MG_VIAL_ML
    ms4.metric("Vials (10 mL each)", f"{mg_vials:.1f}" if mg_target_meq > 0 else "—")
    st.metric("→ Volume of MgSO₄ to add (mL)", f"{mg_vol:.1f}" if mg_target_meq > 0 else "—")
    if mg_target_meq > 0:
        st.markdown(
            f'<span class="result-pill">Target: <b>{mg_target_meq:.1f} mEq</b> = <b>{mg_target:.2f} mmol</b></span>'
            f'<span class="result-pill">To add: <b>{mg_needed_meq:.1f} mEq</b> = <b>{mg_needed:.2f} mmol</b></span>',
            unsafe_allow_html=True
        )

# ── PHOSPHATE ─────────────────────────────────────────────────────────────────
with st.expander("🟦 Phosphate — PO₄³⁻", expanded=True):
    st.markdown('<div class="info-box">⚠️ <b>K Phosphate</b> also delivers <b>1 mmol K⁺ per mL</b> — credited in the K⁺ section, reducing KCl needed.<br>⚠️ <b>Na Phosphate</b> also delivers <b>1 mmol Na⁺ per mL</b> — credited in the Na⁺ section, reducing NaCl 3% needed.</div>', unsafe_allow_html=True)
    ps1, ps2, ps3, ps4 = st.columns(4)
    phos_target = ps1.number_input("Target PO₄³⁻ (mmol/day)", min_value=0.0, value=0.0, step=2.0,
                                    key="phos_target_pre")
    ps2.markdown(f'<div class="from-aa">🟡 From AA: <b>{aa_Phos:.1f} mmol</b></div>', unsafe_allow_html=True)
    phos_needed = max(0.0, phos_target - aa_Phos) if phos_target > 0 else 0.0
    ps3.metric("Still needed (mmol)", f"{phos_needed:.1f}" if phos_target > 0 else "—")
    phos_src = ps4.selectbox("Source", ["K Phosphate B.Braun (0.6 mmol/mL PO₄)", "Na Phosphate Braun (0.6 mmol/mL PO₄)"],
                              key="phos_src_pre")

    phos_vol = phos_needed / 0.6 if phos_target > 0 else 0.0
    st.metric("→ Volume of PO₄ source to add (mL)", f"{phos_vol:.1f}" if phos_target > 0 else "—")

    k_from_phos  = phos_vol if (phos_target > 0 and "K Phosphate" in phos_src) else 0.0
    na_from_phos = phos_vol if (phos_target > 0 and "Na Phosphate" in phos_src) else 0.0
    if k_from_phos > 0:
        st.markdown(
            f'<div class="info-box">✅ K Phosphate delivers <b>{k_from_phos:.1f} mmol K⁺</b> '
            f'(= {phos_vol:.1f} mL × 1 mmol/mL). Credited in the K⁺ section — KCl reduced accordingly.</div>',
            unsafe_allow_html=True
        )
    if na_from_phos > 0:
        st.markdown(
            f'<div class="info-box">✅ Na Phosphate delivers <b>{na_from_phos:.1f} mmol Na⁺</b> '
            f'(= {phos_vol:.1f} mL × 1 mmol/mL). Credited in the Na⁺ section — NaCl 3% reduced accordingly.</div>',
            unsafe_allow_html=True
        )

st.markdown("---")

# ── SODIUM ACETATE ────────────────────────────────────────────────────────────
with st.expander("🧂 Sodium Acetate", expanded=False):
    st.markdown('<div class="info-box"><b>Sodium Acetate:</b> 2 mEq/mL (provides Na⁺ and acetate). Osmolarity: 4 mOsm/mL</div>', unsafe_allow_html=True)
    saa1, saa2, saa3 = st.columns(3)
    sa_target = saa1.number_input("Target Sodium Acetate (mEq/day)", min_value=0.0, value=0.0, step=5.0)
    sa_vol = (sa_target / 2.0) if sa_target > 0 else 0.0
    saa2.metric("→ Volume (mL)", f"{sa_vol:.1f}" if sa_target > 0 else "—")
    
    if sa_target > 0:
        st.markdown(
            f'<span class="result-pill">Na⁺ from Acetate: <b>{sa_target:.1f} mEq</b></span>'
            f'<span class="result-pill">Acetate: <b>{sa_target:.1f} mEq</b></span>',
            unsafe_allow_html=True
        )

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
#  LIPID EMULSION 20%
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("### 🫧 Lipid Emulsion 20% *(Separate Infusion)*")
st.markdown('<div class="info-box">Lipid 20% is infused separately — <b>not included</b> in TPN total volume or osmolarity calculation.<br><b>Per litre:</b> 200 g fat · 2000 kcal · Osmolarity ≈ 350 mOsm/L (isotonic, peripheral safe)</div>', unsafe_allow_html=True)

lp1, lp2, lp3, lp4 = st.columns(4)
lipid_gkg = lp1.number_input("Dose (g/kg/day)", min_value=0.0, max_value=5.0, value=0.0, step=0.5)
if lipid_gkg > 0:
    lipid_grams = weight * lipid_gkg
else:
    lipid_grams = lp2.number_input("Lipid (grams)", min_value=0.0, max_value=500.0, value=0.0, step=5.0)

lipid_vit_vol    = lp3.number_input("Lipid Vitamin Vol (mL)", min_value=0.0, max_value=50.0, value=0.0, step=1.0)
lipid_infuse_hrs = lp4.number_input("Infuse Over (hours)", min_value=1, max_value=24, value=12, step=1)

lipid_base_vol = (lipid_grams / 200) * 1000 if lipid_grams > 0 else 0.0
lipid_vol      = lipid_base_vol + lipid_vit_vol
lipid_kcal     = lipid_grams * 9
lipid_rate     = lipid_vol / lipid_infuse_hrs if lipid_vol > 0 else 0.0

lv1, lv2, lv3 = st.columns(3)
lv1.metric("Lipid Base Vol (mL)", f"{lipid_base_vol:.1f}" if lipid_grams > 0 else "—")
lv2.metric("Total Bag Vol (mL)", f"{lipid_vol:.1f}" if lipid_vol > 0 else "—")
lv3.metric("→ Rate (mL/hr)", f"{lipid_rate:.1f}" if lipid_vol > 0 else "—")

if lipid_grams > 0:
    st.markdown(
        f'<span class="result-pill">Fat: <b>{lipid_grams:.1f} g</b></span>'
        f'<span class="result-pill">/kg: <b>{lipid_grams/weight:.2f} g/kg</b></span>'
        f'<span class="result-pill">Energy: <b>{lipid_kcal:.0f} kcal</b></span>'
        f'<span class="result-pill">Over: <b>{lipid_infuse_hrs} hrs</b></span>'
        f'<span class="result-pill">Osmolarity: <b>~350 mOsm/L (isotonic)</b></span>',
        unsafe_allow_html=True
    )

st.markdown("---")


# ══════════════════════════════════════════════════════════════════════════════
#  WFI
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("### 💧 Water for Injection / Diluent")
used_so_far = dex_vol + aa_vol + na_vol + k_vol + mg_vol + phos_vol + sa_vol + extra_nacl3 + trace_vol + mv_vol
auto_wfi    = max(0.0, goal_vol - used_so_far)
wa1, wa2 = st.columns([2, 1])
wfi_vol = wa1.number_input("WFI Volume (mL)", min_value=0.0, value=0.0, step=10.0)
wa2.markdown(f"**Auto-fill suggestion:** `{auto_wfi:.1f} mL`  \n*(to reach {goal_vol} mL goal)*")

st.markdown("---")


# ══════════════════════════════════════════════════════════════════════════════
#  CALCULATIONS
# ══════════════════════════════════════════════════════════════════════════════
total_vol  = dex_vol + aa_vol + na_vol + k_vol + mg_vol + phos_vol + sa_vol + extra_nacl3 + trace_vol + mv_vol + wfi_vol
total_kcal = dex_kcal + aa_kcal
total_kcal_with_lipid = total_kcal + lipid_kcal

# ── Final glucose concentration in the TPN bag ────────────────────────────────
final_dex_conc = (dex_grams / total_vol * 100) if (total_vol > 0 and dex_grams > 0) else 0.0

# ── Electrolyte totals ────────────────────────────────────────────────────────
tot_Na           = aa_Na + (na_nacl_needed if na_target > 0 else 0) + na_from_phos + (sa_target if sa_target > 0 else 0)
tot_Phos_from_na = na_from_phos * 0.6
tot_K            = aa_K + (k_kcl_needed if k_target > 0 else 0) + k_from_phos
tot_Mg           = aa_Mg + (mg_needed if mg_target > 0 else 0)
tot_Mg_meq       = tot_Mg * 2
tot_Phos         = aa_Phos + (phos_needed if phos_target > 0 else 0) + tot_Phos_from_na
tot_Cl           = aa_Cl
if na_target > 0:
    tot_Cl += na_nacl_needed
if k_target > 0 and "KCl" in k_src:
    tot_Cl += k_cl_contribution
tot_Cl  += extra_nacl3 * 0.51335
tot_Ace  = aa_Ace + (sa_target if sa_target > 0 else 0)
tot_Na  += extra_nacl3 * 0.51335

# ── OSMOLARITY ────────────────────────────────────────────────────────────────
# Component-specific osmolarity values (mOsm/mL)
OSM_AA = 1.021  # Amino acids 10%
OSM_DEX_25 = 1.39  # Dextrose 25%
OSM_DEX_50 = 2.525  # Dextrose 50%
OSM_NACL_3 = 1.0267  # NaCl 3%
OSM_KCL_1_1 = 2.0  # KCl 1:1
OSM_KCL_2_1 = 4.0  # KCl 2:1
OSM_MG = 4.06  # MgSO₄
OSM_NA_PHOS = 7.0  # Na Phosphate
OSM_K_PHOS = 7.0  # K Phosphate (assuming same as Na Phosphate)
OSM_NA_ACETATE = 4.0  # Sodium Acetate
OSM_LIPID = 0.38  # Lipid 20%

# Determine dextrose osmolarity based on concentration
if dex_conc == 25:
    osm_dex_per_ml = OSM_DEX_25
elif dex_conc == 50:
    osm_dex_per_ml = OSM_DEX_50
else:
    # Linear interpolation for other concentrations
    osm_dex_per_ml = (dex_conc / 25) * OSM_DEX_25 if dex_conc < 25 else ((dex_conc - 25) / 25 * (OSM_DEX_50 - OSM_DEX_25) + OSM_DEX_25)

# Determine phosphate osmolarity based on source
osm_phos_per_ml = OSM_NA_PHOS if "Na Phosphate" in phos_src else OSM_K_PHOS

# Calculate osmolarity contributions (mOsm)
osm_dex_total = dex_vol * osm_dex_per_ml if dex_vol > 0 else 0
osm_aa_total = aa_vol * OSM_AA if aa_vol > 0 else 0
osm_nacl_total = na_vol * OSM_NACL_3 if na_vol > 0 else 0
osm_kcl_total = k_vol * (OSM_KCL_2_1 if "2:1" in k_src else OSM_KCL_1_1) if k_vol > 0 else 0
osm_mg_total = mg_vol * OSM_MG if mg_vol > 0 else 0
osm_phos_total = phos_vol * osm_phos_per_ml if phos_vol > 0 else 0
osm_sa_total = sa_vol * OSM_NA_ACETATE if sa_vol > 0 else 0
osm_extra_nacl_total = extra_nacl3 * OSM_NACL_3 if extra_nacl3 > 0 else 0
osm_trace_total = 0  # Trace elements typically minimal osmolarity
osm_mv_total = 0  # Multivitamin typically minimal osmolarity

# Total osmolarity contribution (mOsm)
total_osm = osm_dex_total + osm_aa_total + osm_nacl_total + osm_kcl_total + osm_mg_total + osm_phos_total + osm_sa_total + osm_extra_nacl_total + osm_trace_total + osm_mv_total

# Final osmolarity (mOsm/L) = total mOsm / total volume in L
osmolarity = round(total_osm / (total_vol / 1000)) if total_vol > 0 else 0


# ══════════════════════════════════════════════════════════════════════════════
#  LIVE SUMMARY
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("## 📊 Results Summary")

if osmolarity > 900:
    st.markdown(f'<div class="osm-central">⚠️ CENTRAL LINE Required — Osmolarity: {osmolarity} mOsm/L (>900)</div>', unsafe_allow_html=True)
else:
    st.markdown(f'<div class="osm-peripheral">✅ Peripheral Line Safe — Osmolarity: {osmolarity} mOsm/L (≤900)</div>', unsafe_allow_html=True)

osm_pct   = min(100, (osmolarity / 1800) * 100)
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

# ── Final glucose concentration banner ───────────────────────────────────────
if dex_grams > 0 and total_vol > 0:
    dex_conc_color = "#ff5c5c" if final_dex_conc > 12.5 else "#ffb347" if final_dex_conc > 10 else "#00c8a0"
    dex_conc_note  = "⚠️ Central line required (>12.5%)" if final_dex_conc > 12.5 else "✅ Peripheral safe (≤10%)" if final_dex_conc <= 10 else "⚠️ Consider central line (>10%)"
    st.markdown(
        f'<div style="background:rgba(255,179,71,0.08);border:1px solid rgba(255,179,71,0.35);'
        f'border-radius:8px;padding:10px 16px;margin-bottom:10px;display:flex;align-items:center;gap:16px;">'
        f'<span style="font-size:1.05rem;color:#7a92b0;">🍬 Final Glucose Concentration in TPN Bag:</span>'
        f'<span style="font-size:1.5rem;font-weight:900;color:{dex_conc_color};">{final_dex_conc:.1f}%</span>'
        f'<span style="font-size:0.85rem;color:{dex_conc_color};font-weight:600;">{dex_conc_note}</span>'
        f'</div>',
        unsafe_allow_html=True
    )

# Stat boxes
actual_rate = total_vol / duration if duration > 0 and total_vol > 0 else 0
sc1, sc2, sc3, sc4, sc5 = st.columns(5)
sc1.metric("TPN Volume (mL)", f"{total_vol:.0f}")
sc2.metric("TPN Rate (mL/hr)", f"{actual_rate:.1f}" if actual_rate > 0 else "—")
sc3.metric("TPN kcal", f"{total_kcal:.0f}")
sc4.metric("Protein (g/kg)", f"{aa_grams/weight:.2f}" if aa_grams > 0 and weight > 0 else "—")
sc5.metric("GIR (mg/kg/min)", f"{dex_gir:.2f}" if dex_grams > 0 else "—")

if lipid_grams > 0:
    sl1, sl2, sl3, sl4, sl5 = st.columns(5)
    sl1.metric("Lipid Total Vol (mL)", f"{lipid_vol:.0f}")
    sl2.metric("Lipid Rate (mL/hr)", f"{lipid_rate:.1f}")
    sl3.metric("Infuse Over (hrs)", f"{lipid_infuse_hrs}")
    sl4.metric("Lipid kcal", f"{lipid_kcal:.0f}")
    sl5.metric("Total kcal (TPN + Lipid)", f"{total_kcal_with_lipid:.0f}")

sc5, sc6, sc7, sc8, sc9, sc10 = st.columns(6)
sc5.metric("Na⁺ total (mmol)", f"{tot_Na:.1f}")
sc6.metric("K⁺ total (mmol)", f"{tot_K:.1f}")
sc7.metric("Mg²⁺ total (mEq)", f"{tot_Mg_meq:.1f}")
sc8.metric("PO₄³⁻ total (mmol)", f"{tot_Phos:.1f}")
sc9.metric("Cl⁻ total (mmol)", f"{tot_Cl:.1f}")
sc10.metric("Acetate total (mmol)", f"{tot_Ace:.1f}")

st.markdown("---")


# ══════════════════════════════════════════════════════════════════════════════
#  OSMOLARITY BREAKDOWN
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("### 📐 Osmolarity Breakdown")
st.markdown(
    f'<div class="info-box">'
    f'<b>Method:</b> Component osmolarity values (mOsm/mL) × volume (mL)<br>'
    f'<b>Components:</b> AA 1.021 | Dex 25% 1.39 | Dex 50% 2.525 | NaCl 3% 1.0267 | KCl 2:1 4.0 | KCl 1:1 2.0 | Mg 4.06 | Na Phos 7.0 | Na Acetate 4.0 mOsm/mL<br>'
    f'<b>Total TPN volume:</b> <b>{total_vol:.0f} mL</b>'
    f'</div>',
    unsafe_allow_html=True
)

import pandas as pd
osm_data = []
if osm_dex_total > 0:
    osm_data.append({"Component": f"Dextrose {dex_conc:.0f}%", "Volume (mL)": round(dex_vol, 1),
                     "mOsm/mL": osm_dex_per_ml, "Total mOsm": round(osm_dex_total, 1)})
if osm_aa_total > 0:
    osm_data.append({"Component": "Amino Acids 10%", "Volume (mL)": round(aa_vol, 1),
                     "mOsm/mL": OSM_AA, "Total mOsm": round(osm_aa_total, 1)})
if osm_nacl_total > 0:
    osm_data.append({"Component": "NaCl 3%", "Volume (mL)": round(na_vol, 1),
                     "mOsm/mL": OSM_NACL_3, "Total mOsm": round(osm_nacl_total, 1)})
if osm_kcl_total > 0:
    kcl_label = "KCl 2:1" if "2:1" in k_src else "KCl 1:1"
    kcl_osm = OSM_KCL_2_1 if "2:1" in k_src else OSM_KCL_1_1
    osm_data.append({"Component": kcl_label, "Volume (mL)": round(k_vol, 1),
                     "mOsm/mL": kcl_osm, "Total mOsm": round(osm_kcl_total, 1)})
if osm_mg_total > 0:
    osm_data.append({"Component": "MgSO₄", "Volume (mL)": round(mg_vol, 1),
                     "mOsm/mL": OSM_MG, "Total mOsm": round(osm_mg_total, 1)})
if osm_phos_total > 0:
    phos_label = "Na Phosphate" if "Na Phosphate" in phos_src else "K Phosphate"
    osm_data.append({"Component": phos_label, "Volume (mL)": round(phos_vol, 1),
                     "mOsm/mL": osm_phos_per_ml, "Total mOsm": round(osm_phos_total, 1)})
if osm_sa_total > 0:
    osm_data.append({"Component": "Sodium Acetate", "Volume (mL)": round(sa_vol, 1),
                     "mOsm/mL": OSM_NA_ACETATE, "Total mOsm": round(osm_sa_total, 1)})
if osm_extra_nacl_total > 0:
    osm_data.append({"Component": "NaCl 3% (extra)", "Volume (mL)": round(extra_nacl3, 1),
                     "mOsm/mL": OSM_NACL_3, "Total mOsm": round(osm_extra_nacl_total, 1)})

osm_data.append({"Component": "TOTAL", "Volume (mL)": round(total_vol, 1),
                 "mOsm/mL": f"{osmolarity/1000:.3f}", "Total mOsm": round(total_osm, 1)})

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
    recipe.append({"Component": "NaCl 3%", "Volume (mL)": round(na_vol, 1),
                   "Details": f"Na⁺ {na_nacl_needed:.1f} mmol + Cl⁻ {na_nacl_needed:.1f} mmol"})
if k_vol > 0:
    k_label = "KCl 1:1" if "1:1" in k_src else "KCl 2:1"
    recipe.append({"Component": k_label, "Volume (mL)": round(k_vol, 1),
                   "Details": f"K⁺ {k_kcl_needed:.1f} mmol + Cl⁻ {k_cl_contribution:.1f} mmol"})
if mg_vol > 0:
    recipe.append({"Component": "MgSO₄ 8.1 mEq/10 mL", "Volume (mL)": round(mg_vol, 1),
                   "Details": f"{mg_vials:.1f} vials × 10 mL | Mg²⁺ {mg_needed_meq:.1f} mEq ({mg_needed:.2f} mmol)"})
if phos_vol > 0:
    p_label = "K Phosphate B.Braun" if "K Phosphate" in phos_src else "Na Phosphate Braun"
    recipe.append({"Component": p_label, "Volume (mL)": round(phos_vol, 1),
                   "Details": f"PO₄³⁻ {phos_needed:.1f} mmol + {'K⁺' if 'K Phosphate' in phos_src else 'Na⁺'} {phos_vol:.1f} mmol"})
if sa_vol > 0:
    recipe.append({"Component": "Sodium Acetate 2 mEq/mL", "Volume (mL)": round(sa_vol, 1),
                   "Details": f"Na⁺ {sa_target:.1f} mEq + Acetate {sa_target:.1f} mEq"})
if extra_nacl3 > 0:
    recipe.append({"Component": "NaCl 3% (extra)", "Volume (mL)": round(extra_nacl3, 1),
                   "Details": f"Na⁺ {extra_nacl3*0.51335:.1f} mmol · Cl⁻ {extra_nacl3*0.51335:.1f} mmol"})
if trace_vol > 0:
    recipe.append({"Component": "Trace Elements", "Volume (mL)": round(trace_vol, 1),
                   "Details": "Fixed additive"})
if mv_vol > 0:
    recipe.append({"Component": "Multivitamin", "Volume (mL)": round(mv_vol, 1),
                   "Details": "Fixed additive"})
if wfi_vol > 0:
    recipe.append({"Component": "Water for Injection", "Volume (mL)": round(wfi_vol, 1), "Details": "Diluent — 0 mOsm"})

if recipe:
    dex_conc_str = f" · Final Glucose: {final_dex_conc:.1f}%" if dex_grams > 0 else ""
    recipe.append({"Component": "── TPN TOTAL ──", "Volume (mL)": round(total_vol, 1),
                   "Details": f"Osmolarity: {osmolarity} mOsm/L · {'⚠️ CENTRAL LINE' if osmolarity > 900 else '✅ Peripheral safe'}{dex_conc_str}"})
    if lipid_grams > 0:
        recipe.append({"Component": "⚡ Lipid Emulsion 20% (separate)", "Volume (mL)": round(lipid_base_vol, 1),
                       "Details": f"{lipid_grams:.1f} g fat · {lipid_kcal:.0f} kcal · NOT included in TPN osmolarity"})
        if lipid_vit_vol > 0:
            recipe.append({"Component": "⚡ Lipid Vitamin Additive (separate)", "Volume (mL)": round(lipid_vit_vol, 1),
                           "Details": f"Added to lipid bag → Total bag: {lipid_vol:.1f} mL · Rate: {lipid_rate:.1f} mL/hr over {lipid_infuse_hrs}h"})
        else:
            recipe.append({"Component": "⚡ Lipid — Infusion Info", "Volume (mL)": "—",
                           "Details": f"Total bag: {lipid_vol:.1f} mL · Rate: {lipid_rate:.1f} mL/hr over {lipid_infuse_hrs}h"})
        recipe.append({"Component": "── GRAND TOTAL kcal ──", "Volume (mL)": "—",
                       "Details": f"TPN {total_kcal:.0f} kcal + Lipid {lipid_kcal:.0f} kcal = {total_kcal_with_lipid:.0f} kcal"})
    df_recipe = pd.DataFrame(recipe)
    st.dataframe(df_recipe, use_container_width=True, hide_index=True)

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
if dex_grams > 0 and final_dex_conc > 12.5:
    warnings.append(f"⚠️ Final glucose concentration {final_dex_conc:.1f}% exceeds 12.5% — Central venous access required.")
elif dex_grams > 0 and final_dex_conc > 10:
    warnings.append(f"⚠️ Final glucose concentration {final_dex_conc:.1f}% exceeds 10% — Consider central line (peripheral limit typically 10–12.5%).")
if na_target > 0 and na_target < aa_Na:
    warnings.append(f"⚠️ Na⁺ target ({na_target} mmol) is less than what AA solution alone provides ({aa_Na:.1f} mmol). Reconsider target or AA volume.")
if k_target > 0 and k_target < aa_K:
    warnings.append(f"⚠️ K⁺ target ({k_target} mmol) is less than what AA solution provides ({aa_K:.1f} mmol).")
if tot_K > weight * 3:
    warnings.append("⚠️ Total K⁺ may exceed safe limit (~3 mmol/kg/day max in TPN).")

gir_max = 12 if is_pediatric else 7
if dex_grams > 0 and dex_gir > gir_max:
    warnings.append(f"⚠️ GIR >{gir_max} mg/kg/min — risk of hyperglycemia. Consider reducing dextrose.")

lipid_max = 3.0 if is_pediatric else 2.5
if lipid_grams > 0 and lipid_grams / weight > lipid_max:
    warnings.append(f"⚠️ Lipid dose ({lipid_grams/weight:.2f} g/kg/day) exceeds recommended max ({lipid_max} g/kg/day for {'pediatric' if is_pediatric else 'adult'}).")

if total_vol > goal_vol * 1.05:
    warnings.append(f"⚠️ Total volume ({total_vol:.0f} mL) exceeds fluid goal ({goal_vol} mL).")

if warnings:
    st.markdown("### ⚠️ Clinical Warnings")
    for w in warnings:
        st.markdown(f'<div class="warn-box">{w}</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("⚗️ TPN Compounding Calculator — For clinical use by trained pharmacy")
