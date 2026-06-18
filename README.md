# Obsession Nash Bargaining Model

A Nash Bargaining model analyzing the profit distribution of the 2025 indie horror film *Obsession*, inspired by art director Sally Choi's viral post about earning $6,741 on a film that grossed $294M.

## The Question

When an indie film becomes a massive hit, how *should* the money be split? We use the **Nash Bargaining Solution** from cooperative game theory to compute "fair" payouts for all 14 participants — from director Curry Barker to the volunteer crew.

## The Model

Each participant gets:

```
pay_i = outside_option_i + (power_i / total_power) × surplus
```

Where:
- **outside_option**: what they'd earn doing something else (their walk-away value)
- **power**: bargaining weight based on replaceability, risk borne, and contribution uniqueness
- **surplus**: total pie minus the sum of all outside options

## Key Findings

| Participant | Actual Pay | Nash Fair Pay | Ratio |
|---|---|---|---|
| Sally Choi (art director) | $9,000 | $1,280,075 | 142x underpaid |
| Inde Navarrette (lead actress) | $20,000 | $2,562,149 | 128x underpaid |
| Curry Barker (writer/director/editor) | $100,000 | $8,580,498 | 86x underpaid |
| All crew combined | $101,000 | $7,724,448 | 76x underpaid |
| Focus Features (distributor) | $102,500,000 | $102,500,710 | 1.0x — matches |

### Implied Bargaining Power

Focus's bargaining power is set to **114.7** (reverse-engineered from actual outcome) vs everyone else combined at **46**.

- Focus is **76x** Sally's power
- Focus is **11x** Barker's power (the guy who wrote, directed, and edited it)
- Focus captures **71.4%** of all surplus

That's the distribution bottleneck quantified.

Even in the *market-based* model (not a "fairness" model), the current distribution is extreme. The gap comes from **sequential bargaining**: everyone negotiated flat rates *before* the value was known, and Focus captured the surplus *after*.

## Sensitivity Scenarios

- **Equal power** (everyone = 1): Sally gets $8.5M
- **Power = days worked** (labor theory): Sally gets $2.4M
- **Default model** (weighted by replaceability/risk): Sally gets $3.4M

She's underpaid in every scenario.

## Run It

```bash
python model.py
```

Pure Python, no dependencies.

## Context

- Film budget: $750,000
- Box office: $294M worldwide
- Focus Features acquired distribution at TIFF for $14.5M
- Sally Choi was paid $300/day (~$9,000 pretax) as art director
- Some crew were volunteers paid only gas/mileage

## License

MIT
