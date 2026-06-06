import time

def separator():
    print("\n" + "="*60 + "\n")

# ── SCOUT AGENT ──
def scout_agent(member):
    print("🟢 SCOUT AGENT — Financial Literacy Coach")
    print(f"Analysing message from {member['name']}...")
    time.sleep(1)
    
    stress_keywords = ["no money", "school fees", "debt", "loan shark"]
    stress_detected = any(kw in member['message'].lower() for kw in stress_keywords)
    
    if stress_detected:
        print(f"⚠️  Stress flag detected: '{member['message']}'")
        print(f"📋 Preparing referral for Guardian Agent...")
        referral = {
            "member_id":     member['id'],
            "name":          member['name'],
            "age":           member['age'],
            "occupation":    member['occupation'],
            "harvest_month": member['harvest_month'],
            "children":      member['children'],
            "savings_kes":   member['savings_kes'],
            "stress_flag":   "YES",
            "referred_by":   "Scout Agent"
        }
        print(f"✅ Referral ready. Handing off to Guardian Agent.")
        return referral
    else:
        print(f"✅ No stress detected. No handoff needed.")
        return None

separator()

# ── GUARDIAN AGENT ──
def guardian_agent(referral, loan_amount):
    print("🟣 GUARDIAN AGENT — Loan Triage Officer")
    print(f"Received referral for {referral['name']} from {referral['referred_by']}")
    time.sleep(1)
    
    print(f"\nScreening application:")
    print(f"  Member     : {referral['name']}, {referral['age']} yrs, {referral['occupation']}")
    print(f"  Children   : {referral['children']}")
    print(f"  Savings    : KES {referral['savings_kes']:,}")
    print(f"  Harvest    : {referral['harvest_month']}")
    print(f"  Loan asked : KES {loan_amount:,}")
    
    risk_flags = 0
    if loan_amount > 15000:
        print(f"\n⚠️  Loan amount KES {loan_amount:,} exceeds KES 15,000 limit.")
        print("📋 Escalating to Hunter Agent with full risk assessment...")
        escalation = {
            **referral,
            "loan_amount":         loan_amount,
            "income_variance":     f"Seasonal — peaks {referral['harvest_month']}",
            "risk_flags":          risk_flags,
            "repayment_capacity":  "Strong during harvest season",
            "cultural_flags":      "School fee cycle aligns with off-harvest season",
            "escalated_by":        "Guardian Agent"
        }
        print("✅ Escalation ready. Handing off to Hunter Agent.")
        return escalation
    elif risk_flags >= 3:
        print("❌ Application denied — 3 or more risk flags.")
        return None
    else:
        print("✅ Application approved by Guardian Agent.")
        return None

separator()

# ── HUNTER AGENT ──
def hunter_agent(escalation):
    print("🔴 HUNTER AGENT — Human-in-Loop Coordinator")
    print(f"Received escalation for {escalation['name']} from {escalation['escalated_by']}")
    time.sleep(1)
    
    print(f"\n{'='*60}")
    print(f"  BRIEFING PACKET FOR HUMAN LOAN OFFICER")
    print(f"{'='*60}")
    print(f"  Applicant   : {escalation['name']}, {escalation['age']}")
    print(f"  Occupation  : {escalation['occupation']}")
    print(f"  Location    : Kakamega")
    print(f"  Children    : {escalation['children']} (ages 6, 9, 14)")
    print(f"  Loan request: KES {escalation['loan_amount']:,} for school fees")
    print(f"  Risk flags  : {escalation['risk_flags']} — NONE")
    print(f"  Income      : {escalation['income_variance']}")
    print(f"  Repayment   : {escalation['repayment_capacity']}")
    print(f"  Note        : {escalation['cultural_flags']}")
    print(f"  Cross-sell  : Consider drought insurance")
    print(f"{'='*60}")
    print(f"\n⚠️  REMINDER: This agent does NOT approve or deny.")
    print(f"✅ Briefing packet ready. Awaiting human officer decision.")

# ── RUN THE PROTOTYPE ──
separator()
print("  UJIMA SACCO — AGENT PRIDE LIVE PROTOTYPE")
print("  Scout → Guardian → Hunter Handoff Demo")
separator()

member = {
    "id":            "UJ001",
    "name":          "Grace Achieng",
    "age":           42,
    "occupation":    "Maize farmer",
    "harvest_month": "October/November",
    "children":      3,
    "savings_kes":   4200,
    "message":       "No money for school fees"
}

loan_amount = 28000

referral   = scout_agent(member)
separator()

if referral:
    escalation = guardian_agent(referral, loan_amount)
    separator()
    if escalation:
        hunter_agent(escalation)

separator()
print("  END OF PROTOTYPE RUN")
separator()