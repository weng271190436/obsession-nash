"""
Nash Bargaining Model for Obsession (2025) profit distribution.

The Nash Bargaining Solution maximizes the product of each party's
surplus (payoff minus their outside option / disagreement point).

For a two-party split of surplus S between player A and B:
  A gets: d_A + (b_A / (b_A + b_B)) * S
  B gets: d_B + (b_B / (b_A + b_B)) * S

where d = disagreement point (outside option), b = bargaining power,
and S = total value - sum of all disagreement points.

For N players, we generalize: each player i gets:
  d_i + (b_i / sum(b)) * S

Bargaining power factors we consider:
  - Replaceability (inverse: fewer substitutes = more power)
  - Risk borne (more downside exposure = more power)  
  - Contribution uniqueness (creative vision vs. fungible labor)
"""

import json

# ============================================================
# ACTUAL DATA FROM OBSESSION
# ============================================================

TOTAL_REVENUE = 294_000_000  # worldwide box office
EXHIBITOR_CUT = 0.50         # theaters keep ~50%
STUDIO_REVENUE = TOTAL_REVENUE * (1 - EXHIBITOR_CUT)  # ~$147M to Focus

# Focus paid $14.5M for distribution rights + marketing costs
FOCUS_ACQUISITION = 14_500_000
FOCUS_MARKETING = 30_000_000  # estimated P&A for wide release
FOCUS_TOTAL_COST = FOCUS_ACQUISITION + FOCUS_MARKETING

# Production budget
PRODUCTION_BUDGET = 750_000

# Total value created (simplified: what all parties collectively earned)
# Focus net: studio revenue - their costs
FOCUS_NET = STUDIO_REVENUE - FOCUS_TOTAL_COST
# Producers got the acquisition price
PRODUCER_NET = FOCUS_ACQUISITION - PRODUCTION_BUDGET

TOTAL_SURPLUS_CREATED = STUDIO_REVENUE  # gross pie before costs

# ============================================================
# PARTICIPANTS & OUTSIDE OPTIONS
# ============================================================

participants = {
    # --- ABOVE THE LINE ---
    "Curry Barker (writer/director/editor)": {
        "actual_pay": 100_000,  # estimated (likely kept most of remaining budget after crew)
        "outside_option": 80_000,  # YouTube income + could direct another micro-budget
        "bargaining_power": 10,    # irreplaceable - wrote, directed, edited. THE creative vision
        "days": 180,               # writing + shooting + editing + reshoots (~6 months)
        "category": "above_the_line",
        "notes": "Triple-threat. No film without him. But pre-success, he was a YouTuber.",
    },
    "James Harris (producer)": {
        "actual_pay": 75_000,   # estimated producer fee
        "outside_option": 50_000,  # could produce another indie
        "bargaining_power": 7,     # found Barker, assembled financing, took financial risk
        "days": 240,
        "category": "above_the_line",
        "notes": "Tea Shop Productions. Discovered Barker, initiated the project.",
    },
    "Other Producers (Johnson, Mercuri, Viaris)": {
        "actual_pay": 100_000,  # combined estimated
        "outside_option": 120_000,  # combined outside options (they have other projects)
        "bargaining_power": 5,
        "days": 200,
        "category": "above_the_line",
        "notes": "Capstone Studios, Under the Shell. Financing + production support.",
    },

    # --- CAST (SAG Indie rates) ---
    "Michael Johnston (lead - Bear)": {
        "actual_pay": 25_000,   # estimated, SAG indie lead
        "outside_option": 15_000,  # TV guest spots, other indie offers
        "bargaining_power": 3,     # replaceable at this budget level, but cast chemistry matters
        "days": 26,
        "category": "cast",
        "notes": "Lead role. SAG indie rate.",
    },
    "Inde Navarrette (lead - Nikki)": {
        "actual_pay": 20_000,   # reported ~$20K
        "outside_option": 12_000,  # small TV roles (Superman & Lois ended)
        "bargaining_power": 3,
        "days": 26,
        "category": "cast",
        "notes": "Breakout performance. But at time of hiring, limited credits.",
    },
    "Cooper Tomlinson (supporting - Ian)": {
        "actual_pay": 10_000,
        "outside_option": 8_000,
        "bargaining_power": 1.5,
        "days": 15,
        "category": "cast",
    },
    "Megan Lawless (supporting - Sarah)": {
        "actual_pay": 10_000,
        "outside_option": 8_000,
        "bargaining_power": 1.5,
        "days": 12,
        "category": "cast",
    },
    "Andy Richter (supporting - Carter)": {
        "actual_pay": 15_000,   # more established = slightly higher rate
        "outside_option": 30_000,  # established TV career, lots of options
        "bargaining_power": 2,     # name recognition helps marketing
        "days": 5,
        "category": "cast",
        "notes": "Most established actor. Higher outside option.",
    },

    # --- BELOW THE LINE CREW ---
    "Taylor Clemons (cinematographer)": {
        "actual_pay": 12_000,   # estimated ~$500-600/day x 20-26 days
        "outside_option": 10_000,
        "bargaining_power": 2.5,   # creative role, shapes the look
        "days": 26,
        "category": "crew",
        "notes": "Key creative. Center-composed 'uncomfortable' framing was collaborative.",
    },
    "Sally Choi (art director)": {
        "actual_pay": 6_741,    # confirmed: $300/day, $6741.36 after tax
        "outside_option": 5_000,   # first major credit, one short film before this
        "bargaining_power": 1.5,   # also did set dressing, graphic design, BG acting
        "days": 22,
        "category": "crew",
        "notes": "Multi-role. First major feature. Weak outside option at time.",
    },
    "Vivian Gray (production designer)": {
        "actual_pay": 10_000,   # estimated
        "outside_option": 8_000,
        "bargaining_power": 2,
        "days": 26,
        "category": "crew",
        "notes": "Remodeled Bear's house set in Burbank.",
    },
    "Rock Burwell (composer)": {
        "actual_pay": 8_000,    # estimated indie composer rate
        "outside_option": 6_000,
        "bargaining_power": 1.5,
        "days": 30,             # post-production
        "category": "crew",
    },
    "Volunteer crew (~10 people)": {
        "actual_pay": 2_000,    # gas/mileage only, combined
        "outside_option": 0,    # literally volunteered
        "bargaining_power": 0.5,
        "days": 20,
        "category": "crew",
        "notes": "Paid in gas and mileage. Some not even paid on time.",
    },
    "Other paid crew (~15 people)": {
        "actual_pay": 60_000,   # combined, ~$200-300/day rates
        "outside_option": 45_000,
        "bargaining_power": 1,  # combined, fungible roles
        "days": 20,
        "category": "crew",
        "notes": "Grips, gaffers, sound, makeup, etc.",
    },

    # --- DISTRIBUTION (post-production entrants) ---
    "Focus Features (distributor)": {
        "actual_pay": FOCUS_NET,  # they keep the distribution profit
        "outside_option": 5_000_000,  # could've bought a different TIFF film
        "bargaining_power": 15,   # controls access to theaters, marketing machine
        "days": 365,
        "category": "distribution",
        "notes": "Paid $14.5M acquisition + ~$30M marketing. Massive leverage.",
    },
    "Jason Blum / Blumhouse (exec producer)": {
        "actual_pay": 2_000_000,  # estimated exec producer fee/backend
        "outside_option": 5_000_000,  # Blumhouse has many projects
        "bargaining_power": 4,
        "days": 30,
        "category": "distribution",
        "notes": "Came on AFTER TIFF. Brand value + distribution expertise.",
    },
}


def compute_nash_bargaining(participants, total_pie):
    """
    Compute Nash Bargaining Solution for N players.
    
    Each player gets: outside_option + (power_share * surplus)
    where surplus = total_pie - sum(outside_options)
    and power_share = player_power / sum(all_powers)
    """
    total_outside = sum(p["outside_option"] for p in participants.values())
    total_power = sum(p["bargaining_power"] for p in participants.values())
    surplus = total_pie - total_outside
    
    results = {}
    for name, p in participants.items():
        power_share = p["bargaining_power"] / total_power
        nash_pay = p["outside_option"] + power_share * surplus
        results[name] = {
            "actual_pay": p["actual_pay"],
            "outside_option": p["outside_option"],
            "bargaining_power": p["bargaining_power"],
            "power_share_pct": power_share * 100,
            "nash_pay": nash_pay,
            "surplus_share": power_share * surplus,
            "ratio_nash_vs_actual": nash_pay / p["actual_pay"] if p["actual_pay"] > 0 else float('inf'),
            "category": p["category"],
        }
    return results, surplus, total_outside


def print_results(results, surplus, total_outside, total_pie):
    print("=" * 100)
    print(f"NASH BARGAINING MODEL: OBSESSION (2025)")
    print(f"=" * 100)
    print(f"\nTotal pie (studio revenue after exhibitor cut): ${total_pie:,.0f}")
    print(f"Sum of all outside options:                      ${total_outside:,.0f}")
    print(f"Surplus to distribute:                           ${surplus:,.0f}")
    print()
    
    # Group by category
    categories = ["above_the_line", "cast", "crew", "distribution"]
    cat_labels = {
        "above_the_line": "ABOVE THE LINE",
        "cast": "CAST",
        "crew": "CREW",
        "distribution": "DISTRIBUTION",
    }
    
    for cat in categories:
        print(f"\n{'─' * 100}")
        print(f"  {cat_labels[cat]}")
        print(f"{'─' * 100}")
        print(f"  {'Name':<45} {'Actual':>12} {'Nash Fair':>12} {'Ratio':>8} {'Power%':>8}")
        print(f"  {'─'*45} {'─'*12} {'─'*12} {'─'*8} {'─'*8}")
        
        cat_actual = 0
        cat_nash = 0
        for name, r in sorted(results.items(), key=lambda x: -x[1]["nash_pay"]):
            if r["category"] != cat:
                continue
            ratio_str = f"{r['ratio_nash_vs_actual']:.1f}x"
            print(f"  {name:<45} ${r['actual_pay']:>11,.0f} ${r['nash_pay']:>11,.0f} {ratio_str:>8} {r['power_share_pct']:>7.1f}%")
            cat_actual += r["actual_pay"]
            cat_nash += r["nash_pay"]
        
        print(f"  {'SUBTOTAL':<45} ${cat_actual:>11,.0f} ${cat_nash:>11,.0f}")
    
    # Summary
    total_actual = sum(r["actual_pay"] for r in results.values())
    total_nash = sum(r["nash_pay"] for r in results.values())
    
    print(f"\n{'=' * 100}")
    print(f"  {'TOTAL':<45} ${total_actual:>11,.0f} ${total_nash:>11,.0f}")
    print(f"{'=' * 100}")
    
    # Sally Choi spotlight
    sally = results["Sally Choi (art director)"]
    print(f"\n📌 SALLY CHOI SPOTLIGHT:")
    print(f"   Actual pay:           ${sally['actual_pay']:>12,.0f}")
    print(f"   Outside option:       ${sally['outside_option']:>12,.0f}")
    print(f"   Nash fair share:      ${sally['nash_pay']:>12,.0f}")
    print(f"   She 'deserves' {sally['ratio_nash_vs_actual']:.0f}x what she got (by Nash bargaining)")
    print(f"   Her power share:      {sally['power_share_pct']:.2f}% of surplus")
    print(f"   Surplus allocated:    ${sally['surplus_share']:>12,.0f}")
    
    # Focus spotlight  
    focus = results["Focus Features (distributor)"]
    print(f"\n📌 FOCUS FEATURES SPOTLIGHT:")
    print(f"   Actual net:           ${focus['actual_pay']:>12,.0f}")
    print(f"   Nash fair share:      ${focus['nash_pay']:>12,.0f}")
    print(f"   Their power share:    {focus['power_share_pct']:.2f}% of surplus")
    
    # The gap
    print(f"\n📌 THE INEQUALITY:")
    crew_actual = sum(r["actual_pay"] for r in results.values() if r["category"] == "crew")
    crew_nash = sum(r["nash_pay"] for r in results.values() if r["category"] == "crew")
    dist_actual = sum(r["actual_pay"] for r in results.values() if r["category"] == "distribution")
    dist_nash = sum(r["nash_pay"] for r in results.values() if r["category"] == "distribution")
    
    print(f"   All crew actual:      ${crew_actual:>12,.0f}  →  Nash: ${crew_nash:>12,.0f}  ({crew_nash/crew_actual:.0f}x more)")
    print(f"   Distribution actual:  ${dist_actual:>12,.0f}  →  Nash: ${dist_nash:>12,.0f}  ({dist_nash/dist_actual:.1f}x)")


if __name__ == "__main__":
    # The "pie" we're splitting is the studio revenue (after theaters take their cut)
    # This is what Focus Features + producers + everyone shares
    total_pie = STUDIO_REVENUE
    
    results, surplus, total_outside = compute_nash_bargaining(participants, total_pie)
    print_results(results, surplus, total_outside, total_pie)
    
    print("\n\n")
    print("=" * 100)
    print("SENSITIVITY: What if we weight bargaining power differently?")
    print("=" * 100)
    
    # Scenario 2: Equal power (pure Shapley-like, everyone matters equally)
    print("\n--- Scenario: EQUAL BARGAINING POWER (everyone = 1) ---")
    equal_participants = {k: {**v, "bargaining_power": 1} for k, v in participants.items()}
    results2, surplus2, total_outside2 = compute_nash_bargaining(equal_participants, total_pie)
    sally2 = results2["Sally Choi (art director)"]
    focus2 = results2["Focus Features (distributor)"]
    print(f"   Sally would get:  ${sally2['nash_pay']:>12,.0f} (vs actual ${sally2['actual_pay']:,.0f})")
    print(f"   Focus would get:  ${focus2['nash_pay']:>12,.0f} (vs actual ${focus2['actual_pay']:,.0f})")
    
    # Scenario 3: Power proportional to days worked
    print("\n--- Scenario: POWER = DAYS WORKED (labor theory) ---")
    labor_participants = {k: {**v, "bargaining_power": v["days"]} for k, v in participants.items()}
    results3, surplus3, total_outside3 = compute_nash_bargaining(labor_participants, total_pie)
    sally3 = results3["Sally Choi (art director)"]
    focus3 = results3["Focus Features (distributor)"]
    print(f"   Sally would get:  ${sally3['nash_pay']:>12,.0f} (vs actual ${sally3['actual_pay']:,.0f})")
    print(f"   Focus would get:  ${focus3['nash_pay']:>12,.0f} (vs actual ${focus3['actual_pay']:,.0f})")
