# Obsession Nash Bargaining Model

A Nash Bargaining model that computes the **implied bargaining power** of each participant in the 2025 indie horror film *Obsession*, based on estimated actual payouts. Inspired by art director Sally Choi's viral post about earning $6,741 on a film that grossed $294M.

## The Question

Given how the money *actually* flowed, what does that tell us about each person's real bargaining power? We use the **Nash Bargaining Solution** from cooperative game theory to reverse-engineer the implied power of all 14 participants — from director Curry Barker to the volunteer crew.

## The Model

The pie is **net profit** — revenue minus all real costs (exhibitor cut, production, marketing). Transfers between parties (like the acquisition price) are part of the *distribution*, not costs.

```
Net value = $294M box office - $147M exhibitor cut - $30M marketing - $750K production = $116.25M
```

The Nash Bargaining formula:

```
pay_i = outside_option_i + (bargaining_power_i / total_bargaining_power) × surplus
```

Where:
- **outside_option**: what they'd earn doing something else (their walk-away value)
- **surplus**: net value minus the sum of all outside options

To reverse-engineer implied bargaining power, we simply solve for it:

```
implied_bargaining_power_i = actual_pay_i - outside_option_i
```

This is the surplus each person captured in practice. The ratio between any two people's implied power tells you their relative real-world leverage.

## Key Findings: Implied Bargaining Power

With Sally Choi as the baseline (1x):

| Participant | Actual Pay | Implied Power | Relative to Sally | Why |
|---|---|---|---|---|
| Focus Features (distributor) | $102,500,000 | 97,500,000 | 24,375x | Monopoly on wide theatrical distribution. Only path to mass audience. Entered after film was proven at TIFF — zero creative risk, pure market leverage. |
| Curry Barker (writer/director/editor) | $5,000,000 | 4,920,000 | 1,230x | Irreplaceable creative — wrote, directed, AND edited. The film is his vision. But power only materialized after success; pre-TIFF he was a YouTuber with no leverage. |
| James Harris (producer) | $5,000,000 | 4,700,000 | 1,175x | Discovered Barker, initiated the project, assembled financing. Owns the IP rights that Focus paid $14.5M for. Without him there's no deal. |
| Other Producers (Johnson, Mercuri, Viaris) | $3,750,000 | 2,950,000 | 738x | Financing + production infrastructure. Mercuri's Capstone provided capital access; capital is scarce in indie film. They bore real financial downside risk. |
| Other paid crew (~15 people) | $60,000 | 15,000 | 3.8x | Collective bargaining of 15 bodies — more people = slightly more leverage than any individual crew member alone. But each is individually replaceable. |
| Michael Johnston (lead - Bear) | $25,000 | 10,000 | 2.5x | Lead actor in a character-driven horror. Slightly less fungible than crew — his face is the film — but at SAG indie level, many actors would take the role. |
| Inde Navarrette (lead - Nikki) | $20,000 | 8,000 | 2.0x | Supporting lead. Breakout performance, but at time of hiring had limited credits and weak alternatives. |
| Sally Choi (art director) | $9,000 | 4,000 | 1.0x | First major feature credit. Also did set dressing, graphic design, and BG acting (multi-role, underpaid even for scope). Weak outside option = zero leverage. |
| Taylor Clemons (cinematographer) | $12,000 | 2,000 | 0.5x | Creative role (shapes visual language), but many indie DPs available at this budget. Slightly above Sally in pay but similar powerlessness. |
| Vivian Gray (production designer) | $10,000 | 2,000 | 0.5x | Designed the key set (Bear's house). Important work, but replaceable at $750K budget level. |
| Rock Burwell (composer) | $8,000 | 2,000 | 0.5x | Score matters for horror, but composers are hired in post — film already exists, reducing their leverage to near zero. |
| Cooper Tomlinson (supporting - Ian) | $10,000 | 2,000 | 0.5x | Small supporting role. Highly replaceable at indie level. |
| Megan Lawless (supporting - Sarah) | $10,000 | 2,000 | 0.5x | Small supporting role. Highly replaceable at indie level. |
| Volunteer crew (~10 people) | $2,000 | 2,000 | 0.5x | Literally volunteered — they had zero leverage by choice (traded labor for credit/experience). |
| Andy Richter (supporting - Carter) | $15,000 | 0 | 0x | His outside option ($30K) exceeds his pay. Likely did it for fun/relationships. Implies negative surplus — he subsidized the film. |
| Jason Blum / Blumhouse (exec producer) | $2,000,000 | 0 | 0x | Came on post-TIFF. His outside option ($5M+ from Blumhouse slate) exceeds his fee. Attached his name for brand/relationship value, not money. |

### The Power Gap

- Focus is **24,375x** Sally's bargaining power
- Focus is **7.7x** everyone else *combined*
- Focus captures **92.9%** of all surplus
- All crew combined capture **0.02%** of surplus

That's the distribution bottleneck quantified. The single entity that controls access to theaters has more power than every creative contributor combined.

## Why It's Extreme

The gap comes from **sequential bargaining**: everyone negotiated flat rates *before* the value was known, and Focus captured the surplus *after* (buying at TIFF when the film was already proven).

## Sensitivity Scenarios

What if bargaining power were distributed differently?

- **Equal power** (everyone = 1): Sally gets $6.6M, Focus gets $11.6M
- **Power = days worked** (labor theory): Sally gets $1.9M, Focus gets $36M

Sally is underpaid in every scenario.

## Risk-Adjusted Returns

A common defense: "Sally didn't take risk, so she doesn't deserve more." We can test this by quantifying risk in dollars.

**Risk = P(failure) × amount at stake**

- Pre-TIFF participants face ~85% failure rate (typical indie horror)
- Post-TIFF participants (Focus, Blum) face ~15% failure rate (film already proven)

| Participant | Amount at Stake | P(failure) | Expected Loss | Surplus Captured | Return per $1 Risked |
|---|---|---|---|---|---|
| Curry Barker | $80,000 (opportunity cost) | 85% | $68,000 | $4,920,000 | **$72.35** |
| Focus Features | $44,500,000 (acquisition + P&A) | 15% | $6,675,000 | $97,500,000 | **$14.61** |
| James Harris | $750,000 (capital invested) | 85% | $637,500 | $4,700,000 | **$7.37** |
| Other Producers | $750,000 (capital invested) | 85% | $637,500 | $2,950,000 | **$4.63** |
| Sally Choi | $5,000 (opportunity cost) | 85% | $4,250 | $4,000 | **$0.94** |
| Michael Johnston | $15,000 (opportunity cost) | 85% | $12,750 | $10,000 | **$0.78** |
| Andy Richter | $30,000 (opportunity cost) | 85% | $25,500 | $0 | **$0.00** |
| Volunteer crew | $0 | — | $0 | $2,000 | N/A |

### What this shows

1. **Barker** got the best risk-adjusted return ($72/\$1) — but he was genuinely irreplaceable
2. **Focus** got $14.61/\$1 while taking the *least* risk (entered post-proof)
3. **Harris** (the actual risk-taker who bet $750K) got only $7.37/\$1 — half of Focus's return
4. **Sally** got **$0.94 per $1 risked** — she literally didn't break even on a risk-adjusted basis

If risk justified reward, everyone's return-per-dollar would be similar. Instead:
- Sally's return-on-risk is **77x worse** than Barker's
- The producers took the biggest gamble and got **half** Focus's risk-adjusted return
- The "she didn't take risk" argument explains maybe a 2-3x gap, not 24,375x

**The real driver isn't risk — it's bottleneck control.** Who sits between the product and the money? That's who gets paid.

## Run It

```bash
python model.py
```

Pure Python, no dependencies.

## Data Sources & Estimates

- Film budget: $750,000 (widely reported, confirmed by Barker)
- Box office: $294M worldwide (Box Office Mojo)
- Focus Features acquisition: $14.5M at TIFF (Variety, Wikipedia)
- Marketing spend: ~$30M (estimated, typical for wide release)
- Sally Choi pay: $300/day, ~$9,000 pretax (her Instagram post)
- Producer/cast/crew pay: estimated based on indie rate norms
- Outside options: estimated based on each person's career stage at time of hiring

The implied bargaining power calculation is exact given the inputs — the uncertainty is in the estimated actual payouts.

### Input Assumptions

| Participant | Actual Pay | Outside Option | Justification |
|---|---|---|---|
| **ABOVE THE LINE** | | | |
| Curry Barker (writer/director/editor) | $5,000,000 | $80,000 | Actual: estimated largest share of $14.5M acquisition. Outside: was a YouTuber with no film credits pre-Obsession. |
| James Harris (producer) | $5,000,000 | $300,000 | Actual: estimated share of acquisition. Outside: established indie producer at Tea Shop Productions, active slate. |
| Other Producers (Johnson, Mercuri, Viaris) | $3,750,000 | $800,000 | Actual: remainder of acquisition minus production costs. Outside: Mercuri runs Capstone (finances 4-5 films/yr), Viaris runs Under the Shell. Industry veterans with deal flow. |
| **CAST** | | | |
| Michael Johnston (lead - Bear) | $25,000 | $15,000 | Actual: SAG indie lead rate ~$1,000/day × 26 days. Outside: TV guest spots (Teen Wolf alumni, limited recent credits). |
| Inde Navarrette (lead - Nikki) | $20,000 | $12,000 | Actual: reported ~$20K. Outside: Superman & Lois ended, limited pipeline. |
| Cooper Tomlinson (supporting - Ian) | $10,000 | $8,000 | Actual: SAG indie supporting rate. Outside: early-career, few credits. |
| Megan Lawless (supporting - Sarah) | $10,000 | $8,000 | Actual: SAG indie supporting rate. Outside: early-career, few credits. |
| Andy Richter (supporting - Carter) | $15,000 | $30,000 | Actual: likely did it as a favor / for fun. Outside: established TV career (Conan), many options. |
| **CREW** | | | |
| Taylor Clemons (cinematographer) | $12,000 | $10,000 | Actual: ~$500/day × 26 days. Outside: could DP another indie at similar rate. |
| Sally Choi (art director) | $9,000 | $5,000 | Actual: confirmed $300/day × ~22 days pretax. Outside: first major feature, one short film prior. Very weak alternative. |
| Vivian Gray (production designer) | $10,000 | $8,000 | Actual: estimated indie PD rate. Outside: similar gigs available. |
| Rock Burwell (composer) | $8,000 | $6,000 | Actual: estimated indie composer flat fee. Outside: other indie scoring work. |
| Other paid crew (~15 people) | $60,000 | $45,000 | Actual: combined ~$200-300/day rates. Outside: fungible roles, always other indie gigs. |
| Volunteer crew (~10 people) | $2,000 | $0 | Actual: gas/mileage only. Outside: literally volunteered for experience/credit. |
| **DISTRIBUTION** | | | |
| Focus Features (distributor) | $102,500,000 | $5,000,000 | Actual: $147M studio rev - $14.5M acquisition - $30M marketing. Outside: could've acquired a different TIFF film with similar expected return. |
| Jason Blum / Blumhouse (exec producer) | $2,000,000 | $5,000,000 | Actual: estimated exec producer fee. Outside: Blumhouse has 10+ projects/year, opportunity cost exceeds fee (came on for brand/relationship reasons). |

## License

MIT
