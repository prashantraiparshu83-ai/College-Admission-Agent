"""
Greenfield University — Streamlit Admin & Analytics Dashboard
Powered by IBM Watsonx.ai (Granite Model) · RAG Architecture

Run:  streamlit run streamlit_app.py
"""

import os
import json
import time
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from data.admission_data import (
    INSTITUTION_NAME,
    INSTITUTION_TAGLINE,
    COURSES,
    ADMISSION_DEADLINES,
    SCHOLARSHIPS,
    CONTACT,
    FAQS,
    DASHBOARD_STATS,
    RAG_CONTEXT,
)
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

# ─── Bootstrap ────────────────────────────────────────────────────────────────
load_dotenv()

st.set_page_config(
    page_title=f"{INSTITUTION_NAME} — Admin Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Watsonx Model (cached) ───────────────────────────────────────────────────
@st.cache_resource(show_spinner="Connecting to IBM Watsonx.ai…")
def _init_model():
    api_key   = os.getenv("WATSONX_API_KEY", "")
    project_id = os.getenv("WATSONX_PROJECT_ID", "")
    url        = os.getenv("WATSONX_URL", "https://us-south.ml.cloud.ibm.com")

    if not api_key or api_key.startswith("your_") or not project_id or project_id.startswith("your_"):
        return None

    try:
        creds = Credentials(url=url, api_key=api_key)
        return ModelInference(
            model_id="ibm/granite-13b-instruct-v2",
            credentials=creds,
            project_id=project_id,
            params={
                GenParams.MAX_NEW_TOKENS: 800,
                GenParams.MIN_NEW_TOKENS: 20,
                GenParams.TEMPERATURE: 0.3,
                GenParams.TOP_P: 0.9,
                GenParams.REPETITION_PENALTY: 1.1,
                GenParams.STOP_SEQUENCES: ["\n\nUSER:", "\n\nHUMAN:", "---END---"],
            },
        )
    except Exception as exc:
        st.warning(f"Watsonx init failed: {exc}")
        return None


watsonx_model = _init_model()

SYSTEM_PROMPT = f"""You are an expert College Admission Agent for {INSTITUTION_NAME}.
Answer questions based strictly on the institutional data provided. Be concise and helpful."""


def _ask_watsonx(query: str) -> str:
    prompt = f"""{SYSTEM_PROMPT}

---
CONTEXT:
{RAG_CONTEXT}

USER QUERY:
{query}
---

ADMISSION AGENT RESPONSE:"""
    try:
        result = watsonx_model.generate_text(prompt=prompt)
        return result.strip() if isinstance(result, str) else str(result).strip()
    except Exception as exc:
        return f"⚠️ Model error: {exc}"


def _mock_response(query: str) -> str:
    q = query.lower()
    if any(w in q for w in ["course", "programme", "program"]):
        return "**Available Programmes:**\n" + "\n".join(f"- {c}" for c in COURSES)
    if any(w in q for w in ["deadline", "date"]):
        return "**Key Deadlines:**\n" + "\n".join(f"- **{k}:** {v}" for k, v in list(ADMISSION_DEADLINES.items())[:5])
    if any(w in q for w in ["fee", "cost", "tuition"]):
        return "**Fees:**\n" + "\n".join(f"- **{c}:** {i['annual_fee']}/year" for c, i in list(COURSES.items())[:4])
    if any(w in q for w in ["scholarship"]):
        return "**Scholarships:**\n" + "\n".join(f"- **{s['name']}:** {s['benefit']}" for s in SCHOLARSHIPS)
    if any(w in q for w in ["contact", "phone", "email"]):
        return f"📞 {CONTACT['Admission Office']}\n📧 {CONTACT['Email']}\n🌐 {CONTACT['Website']}"
    return (
        f"Hello! I'm the **{INSTITUTION_NAME}** Admission Assistant.\n\n"
        "Ask me about courses, fees, deadlines, scholarships, or contact info.\n\n"
        "_Note: Live AI requires valid IBM Watsonx credentials in `.env`._"
    )


# ─── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"## 🎓 {INSTITUTION_NAME}")
    st.caption(INSTITUTION_TAGLINE)
    st.divider()

    page = st.radio(
        "Navigation",
        ["💬 AI Chat", "📊 Analytics", "📚 Courses", "📅 Deadlines", "🏆 Scholarships", "❓ FAQ", "📞 Contact"],
        label_visibility="collapsed",
    )

    st.divider()

    # Model status
    if watsonx_model:
        st.success("🟢 IBM Watsonx.ai — Connected")
        st.caption("ibm/granite-13b-instruct-v2")
    else:
        st.warning("🟡 Demo Mode — No credentials")
        st.caption("Add WATSONX_API_KEY & PROJECT_ID in `.env`")

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: AI CHAT
# ─────────────────────────────────────────────────────────────────────────────
if page == "💬 AI Chat":
    st.title("💬 AI Admission Chat")
    st.caption(f"Powered by IBM Watsonx.ai · {INSTITUTION_NAME}")

    # Quick prompt chips
    quick_prompts = [
        "What courses are available?",
        "What are the admission deadlines?",
        "Tell me about scholarships",
        "What is the fee for B.Tech CSE?",
        "What documents are required?",
        "How do I contact the admission office?",
    ]
    cols = st.columns(3)
    for i, qp in enumerate(quick_prompts):
        if cols[i % 3].button(qp, use_container_width=True, key=f"qp_{i}"):
            st.session_state.setdefault("messages", [])
            st.session_state["messages"].append({"role": "user", "content": qp})
            with st.spinner("Thinking…"):
                reply = _ask_watsonx(qp) if watsonx_model else _mock_response(qp)
            st.session_state["messages"].append({"role": "assistant", "content": reply})

    st.divider()

    # Chat history
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    for msg in st.session_state["messages"]:
        with st.chat_message(msg["role"], avatar="🎓" if msg["role"] == "assistant" else "🧑‍🎓"):
            st.markdown(msg["content"])

    # Chat input
    if prompt := st.chat_input("Ask about courses, fees, deadlines, eligibility…"):
        st.session_state["messages"].append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="🧑‍🎓"):
            st.markdown(prompt)

        with st.chat_message("assistant", avatar="🎓"):
            with st.spinner("Generating response…"):
                reply = _ask_watsonx(prompt) if watsonx_model else _mock_response(prompt)
            st.markdown(reply)
            st.session_state["messages"].append({"role": "assistant", "content": reply})

    if st.session_state.get("messages"):
        if st.button("🗑️ Clear Chat", type="secondary"):
            st.session_state["messages"] = []
            st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: ANALYTICS DASHBOARD
# ─────────────────────────────────────────────────────────────────────────────
elif page == "📊 Analytics":
    st.title("📊 Analytics Dashboard")
    st.caption("Live institutional data — placements, applications, and seat distribution")

    # KPI row
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Placement Rate 2024", "94%", "+1% vs 2023")
    kpi2.metric("Applications 2024", "8,400+", "+1,600 vs 2023")
    kpi3.metric("Highest Package", "₹55 LPA", "M.Tech CS")
    kpi4.metric("Recruiting Companies", "300+", "")

    st.divider()

    stats = DASHBOARD_STATS

    # Row 1: Placement trend + Category distribution
    col1, col2 = st.columns([3, 2])

    with col1:
        st.subheader("📈 Placement Trend (2020–2024)")
        df_place = pd.DataFrame({
            "Year": stats["placement_by_year"]["labels"],
            "Avg Package (LPA)": stats["placement_by_year"]["avg_package"],
            "Placement Rate (%)": stats["placement_by_year"]["placement_rate"],
        }).set_index("Year")
        tab_a, tab_b = st.tabs(["Average Package", "Placement Rate"])
        with tab_a:
            st.line_chart(df_place[["Avg Package (LPA)"]], use_container_width=True)
        with tab_b:
            st.area_chart(df_place[["Placement Rate (%)"]], use_container_width=True)

    with col2:
        st.subheader("🥧 Seat Category Distribution")
        df_cat = pd.DataFrame({
            "Category": stats["category_distribution"]["labels"],
            "Percentage": stats["category_distribution"]["values"],
        }).set_index("Category")
        st.bar_chart(df_cat, use_container_width=True)

    st.divider()

    # Row 2: Applications trend + Seats per programme
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("📋 Applications Received (2020–2024)")
        df_apps = pd.DataFrame({
            "Year": stats["applications_trend"]["labels"],
            "Applications": stats["applications_trend"]["applications"],
        }).set_index("Year")
        st.bar_chart(df_apps, use_container_width=True)

    with col4:
        st.subheader("🪑 Seats by Programme 2025")
        df_seats = pd.DataFrame({
            "Programme": stats["seats_by_course"]["labels"],
            "Seats": stats["seats_by_course"]["seats"],
        }).set_index("Programme")
        st.bar_chart(df_seats, use_container_width=True)

    # Highest packages table
    st.divider()
    st.subheader("🏆 Highest Packages by Programme")
    df_pkg = pd.DataFrame([
        {"Programme": name, "Avg Package": info["placement_avg"], "Highest Package": info["placement_highest"],
         "Annual Fee": info["annual_fee"], "Seats": info["seats"]}
        for name, info in COURSES.items()
    ])
    st.dataframe(df_pkg, use_container_width=True, hide_index=True)

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: COURSES
# ─────────────────────────────────────────────────────────────────────────────
elif page == "📚 Courses":
    st.title("📚 Course Cutoff Dashboard")
    st.caption(f"Eligibility cutoffs by category — {INSTITUTION_NAME}")

    # Search & filter
    search = st.text_input("🔍 Search programmes", placeholder="e.g. B.Tech, MBA, Data Science")

    df_courses = pd.DataFrame([
        {
            "Programme": name,
            "Duration": info["duration"],
            "Seats": info["seats"],
            "General %": info["cutoff_general"],
            "OBC %": info["cutoff_obc"],
            "SC/ST %": info["cutoff_sc_st"],
            "Annual Fee": info["annual_fee"],
            "Avg Package": info["placement_avg"],
            "Highest Package": info["placement_highest"],
        }
        for name, info in COURSES.items()
    ])

    if search:
        df_courses = df_courses[df_courses["Programme"].str.contains(search, case=False, na=False)]

    st.dataframe(
        df_courses,
        use_container_width=True,
        hide_index=True,
        column_config={
            "General %": st.column_config.ProgressColumn("General %", min_value=0, max_value=100, format="%d%%"),
            "OBC %":     st.column_config.ProgressColumn("OBC %",     min_value=0, max_value=100, format="%d%%"),
            "SC/ST %":   st.column_config.ProgressColumn("SC/ST %",   min_value=0, max_value=100, format="%d%%"),
        },
    )

    st.divider()

    # Expandable course detail cards
    st.subheader("Programme Details")
    for name, info in COURSES.items():
        if search and search.lower() not in name.lower():
            continue
        with st.expander(f"📖 {name}"):
            c1, c2, c3 = st.columns(3)
            c1.metric("Duration", info["duration"])
            c2.metric("Total Seats", info["seats"])
            c3.metric("Annual Fee", info["annual_fee"])
            c1.metric("Avg Package", info["placement_avg"])
            c2.metric("Highest Package", info["placement_highest"])
            c3.metric("Hostel Fee", info["hostel_fee"])
            st.markdown(f"**Eligibility:** {info['eligibility']}")
            st.markdown(f"**Specializations:** {', '.join(info['specializations'])}")
            st.markdown(
                f"**Cutoffs** — General: `{info['cutoff_general']}%` · "
                f"OBC: `{info['cutoff_obc']}%` · SC/ST: `{info['cutoff_sc_st']}%`"
            )

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: DEADLINES
# ─────────────────────────────────────────────────────────────────────────────
elif page == "📅 Deadlines":
    st.title("📅 Admission Deadlines")
    st.caption("Key dates for the 2025 admission cycle")

    df_dead = pd.DataFrame(
        [{"Event": k, "Date": v} for k, v in ADMISSION_DEADLINES.items()]
    )
    st.dataframe(df_dead, use_container_width=True, hide_index=True)

    st.divider()
    st.subheader("Timeline")
    for i, (event, date) in enumerate(ADMISSION_DEADLINES.items()):
        icon = "🟢" if i < 3 else ("🟡" if i < 7 else "🔵")
        st.markdown(f"{icon} **{event}** — `{date}`")

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: SCHOLARSHIPS
# ─────────────────────────────────────────────────────────────────────────────
elif page == "🏆 Scholarships":
    st.title("🏆 Scholarships & Financial Aid")
    st.caption(f"{INSTITUTION_NAME} — financial barriers should never stop talent")

    for s in SCHOLARSHIPS:
        with st.container(border=True):
            st.subheader(f"🎖️ {s['name']}")
            col_a, col_b = st.columns(2)
            col_a.info(f"✅ **Benefit:** {s['benefit']}")
            col_b.success(f"👤 **Eligibility:** {s['eligibility']}")
            st.caption(f"Available Seats: {s['seats']}")

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: FAQ
# ─────────────────────────────────────────────────────────────────────────────
elif page == "❓ FAQ":
    st.title("❓ Frequently Asked Questions")
    st.caption(f"Everything about joining {INSTITUTION_NAME}")

    search_faq = st.text_input("🔍 Search questions", placeholder="e.g. JEE, scholarship, hostel, fee")

    for cat in FAQS:
        matching = [
            item for item in cat["questions"]
            if not search_faq
            or search_faq.lower() in item["q"].lower()
            or search_faq.lower() in item["a"].lower()
        ]
        if not matching:
            continue
        st.subheader(f"{cat['category']}  ({len(matching)} questions)")
        for item in matching:
            with st.expander(item["q"]):
                st.markdown(item["a"])

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: CONTACT
# ─────────────────────────────────────────────────────────────────────────────
elif page == "📞 Contact":
    st.title("📞 Contact Information")
    st.caption(f"{INSTITUTION_NAME} — Admission Office")

    icons = {
        "Admission Office": "📞",
        "Email": "📧",
        "Website": "🌐",
        "Address": "📍",
        "Office Hours": "🕘",
        "WhatsApp Helpline": "💬",
    }

    for key, val in CONTACT.items():
        icon = icons.get(key, "ℹ️")
        with st.container(border=True):
            col_k, col_v = st.columns([1, 3])
            col_k.markdown(f"**{icon} {key}**")
            if key == "Email":
                col_v.markdown(f"[{val}](mailto:{val})")
            elif key == "Website":
                col_v.markdown(f"[{val}](https://{val})")
            elif key in ("Admission Office", "WhatsApp Helpline"):
                clean = val.replace(" ", "").replace("-", "")
                col_v.markdown(f"[{val}](tel:{clean})")
            else:
                col_v.markdown(val)

    st.divider()
    st.info(
        f"🕘 **Office Hours:** {CONTACT['Office Hours']}\n\n"
        f"For urgent queries, WhatsApp us at **{CONTACT['WhatsApp Helpline']}**"
    )
