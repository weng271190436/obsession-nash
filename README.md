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

| Participant | Actual Pay | Implied Power | Relative to Sally |
|---|---|---|---|
| Focus Features (distributor) | $102,500,000 | 97,500,000 | 24,375x |
| James Harris (producer) | $5,000,000 | 4,950,000 | 1,238x |
| Curry Barker (writer/director/editor) | $5,000,000 | 4,920,000 | 1,230x |
| Other Producers | $3,750,000 | 3,630,000 | 908x |
| Sally Choi (art director) | $9,000 | 4,000 | 1x |
| Inde Navarrette (lead actress) | $20,000 | 8,000 | 2x |
| Volunteer crew (~10 people) | $2,000 | 2,000 | 0.5x |

### The Power Gap

- Focus is **24,375x** Sally's bargaining power
- Focus is **7.2x** everyone else *combined*
- Focus captures **92.1%** of all surplus
- All crew combined capture **0.02%** of surplus

That's the distribution bottleneck quantified. The single entity that controls access to theaters has more power than every creative contributor combined.

## Why It's Extreme

The gap comes from **sequential bargaining**: everyone negotiated flat rates *before* the value was known, and Focus captured the surplus *after* (buying at TIFF when the film was already proven).

## Sensitivity Scenarios

What if bargaining power were distributed differently?

- **Equal power** (everyone = 1): Sally gets $6.6M, Focus gets $11.6M
- **Power = days worked** (labor theory): Sally gets $1.9M, Focus gets $36M

Sally is underpaid in every scenario.

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

## License

MIT
