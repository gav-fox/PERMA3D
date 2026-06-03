# PERMA3D Roadmap

> **Google Earth for regenerative land design.**  
> From a 5 acre homestead to all the farmland in southern Spain.  
> Open source. AGPLv3. github.com/gav-fox/PERMA3D

---

## The Problem

The knowledge of how to regenerate land exists. It lives in permaculture design courses, in the heads of a few thousand practitioners, in scattered academic experiments, in the hands of farmers who've spent decades reading their land. It is not at scale. It is not connected. It is not computable.

Meanwhile:
- Approximately 40% of Earth's agricultural land is degraded
- Industrial agriculture depends on inputs that are themselves climate-dependent
- Regenerative practice remains artisanal — site-specific, expert-dependent, slow to spread
- There is no shared data infrastructure for what actually works, where, and why
- There is no cultural mechanism pulling people toward land stewardship at the scale required

The permaculture design consultation model — one expert, one site, one report — cannot move fast enough. The climate and food crises are not waiting.

What's missing is infrastructure. A shared spatial intelligence layer for regenerative land use, at every scale simultaneously, accumulating evidence from every site that uses it. And a cultural engine that makes regeneration aspirational.

That's what PERMA3D is.

---

## The Vision

A planetary land intelligence platform with regenerative design as its native language.

**At the small scale:** A farmer with 5 acres and no GIS experience opens PERMA3D, drops a pin, draws a boundary, and gets an accurate analysis of their land — slope, solar exposure, water flow, frost risk, microclimate zones. They design their system with spatial tools that give them real feedback. They place elements and the tool tells them what the sun does there in December, where the water goes in a heavy rain, which corner is most sheltered. They make better decisions. Their land improves.

**At the large scale:** A land restoration project maps thousands of hectares, models intervention scenarios, tracks outcomes over years. A research team applies PERMA3D to all the farmland in southern Spain and models what happens to European climate if 30% of it converts to agroforestry. A government evaluates land use policy at national scale.

**Both scales run on the same platform.** The data flows both ways. The 5 acre homestead contributes to the planetary dataset. The planetary dataset makes the 5 acre tool smarter.

---

## The Data Problem is the Real Problem

No solver, however sophisticated, produces useful outputs without a foundation of real-world evidence. What does regenerative land management actually produce? Under what soil conditions? What climate? What topography? Over what timescale?

That dataset does not exist at useful scale today.

PERMA3D generates it as a side effect of people using it. Every site analysed, every design decision recorded, every intervention placed and tracked over time adds to an open commons. Scientists, farmers, designers, and eventually game players all contribute to the same growing body of spatial evidence.

Over time this becomes something genuinely new: a quantitative, spatially explicit, globally distributed dataset of regenerative land use outcomes. The kind of dataset that changes what questions are even askable — including questions that have never been asked because the data to answer them didn't exist.

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                    INTERFACES                        │
│  Land CAD Tool │ Farmer Tool │ Game │ Research API   │
└────────────────────────┬────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────┐
│                   DESIGN ENGINE                      │
│     Manual tools │ Analysis layers │ Solver          │
└────────────────────────┬────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────┐
│                   SITE MODEL                         │
│         Terrain + Climate + Boundary + Data          │
└────────────────────────┬────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────┐
│                    ADAPTERS                          │
│   DEM │ LIDAR │ EPW │ PVGIS │ Soil │ Boundary │ ...  │
└────────────────────────┬────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────┐
│                  DATA SOURCES                        │
│  OS / EA / NASA / EU JRC / OpenStreetMap / User      │
└─────────────────────────────────────────────────────┘
```

The stack is modular at every layer. New data sources slot in as adapters. New analysis methods slot in as modules. New interfaces sit on top of the same engine. The solver improves without changing the tool. Everything is a plugin until it proves it belongs in the core.

---

## The Four Stages

### Stage 1 — Tool
*Make something genuinely useful on day one.*

A land CAD environment. You see your site. You see real analysis layers — slope, aspect, solar exposure, water accumulation, frost risk, microclimate zones. You design manually. The tool gives you accurate spatial feedback as you work.

No AI required. No accumulated data required. Useful to a permaculture designer or a farmer today.

The tool must work without the solver. The solver is an enhancement, not a dependency. Build the tool until the engine is honest. Then add everything else.

### Stage 2 — Platform
*Connect the sites.*

Designs and outcomes become optionally shareable. An open dataset accumulates. Projects can be public — a farm in Portugal, a restoration project in Rajasthan, a community garden in Detroit — visible on the platform, their data contributing to the commons.

The solver starts making suggestions grounded in evidence from comparable sites, not just encoded rules. Scientists and researchers access the dataset. The feedback loop begins.

### Stage 3 — Intelligence
*The solver gets interesting.*

With enough data the solver stops being a rule engine and becomes a pattern finder. It surfaces things human designers wouldn't:
- Combinations of interventions that consistently outperform on degraded clay soils
- Microclimatic factors that predict establishment success for specific guilds
- Novel polyculture configurations that emerge from outcome data rather than design theory
- Regional climate effects of land use change at watershed and landscape scale

The questions get bigger. What happens to the water table across this valley if every farm installs swales? How does converting 20% of Andalusian farmland to agroforestry affect summer temperatures in France? What is the maximum food yield from 5 acres in this climate without external inputs? These are answerable questions. They need the data infrastructure to exist first.

### Stage 4 — Game
*Open the problem to everyone.*

The game is built last. It runs on the same engine — same adapters, same analysis, same solver. The difference is the interface and the framing. The terrain is real. The climate is real. The scoring is real ecology. The game part is that it's structured as missions with progression and stakes made legible and emotional.

The game is not a distraction from the tool. It is how the tool gets the data, the users, and the cultural weight it needs to matter at scale.

---

## The Solver and Humans Are Partners

The algorithm will eventually out-design any individual human. It can test millions of variations, track thousands of simultaneous interactions, find non-obvious patterns across vast datasets, and optimise for multiple objectives simultaneously. It never gets tired.

But the algorithm needs humans. Not as a workaround for its limitations — as genuine partners.

**What humans bring:**
- Creative leaps the algorithm would never explore — a player tries a bizarre guild pattern because it looks interesting, the simulation shows it works, the algorithm learns from the experiment
- Local and cultural knowledge the training data doesn't contain
- Judgment about when optimisation should stop
- Values the algorithm can't encode — beauty, community, meaning
- Caring — the algorithm doesn't care if the land heals; humans do, and that caring is what gets trees in the ground

**What the algorithm brings:**
- Exhaustive search across possibilities no human has time to explore
- Pattern recognition across thousands of designs in similar conditions
- Rigorous testing against drought years, flood years, late frosts
- Honest scoring that doesn't flatter bad designs

The game is where this partnership plays out at scale. Millions of humans providing sparks. The algorithm providing rigour. Each cycle — human proposes, algorithm refines, human evaluates, algorithm learns — improves both. The result is designs neither could produce alone.

---

## Interfaces

### Land CAD Tool
*For permaculture designers, land managers, restoration ecologists, planners.*

Full spatial toolset. Import any boundary. Work with all analysis layers simultaneously. Place and annotate design elements. Run bounded solver queries — optimal water harvesting points, candidate locations for specific interventions, contour alignments. Export to GIS, CAD, report formats. Plugin architecture for specialist modules.

The professional tool. Replaces the site visit notebook and hand-drawn plan with something spatially accurate and computationally informed.

### Farmer Tool
*For anyone with land, regardless of technical background.*

Zero barrier. Drop a pin. Draw your boundary. Get a plain-language site report and design suggestions with spatial context. No GIS knowledge. No jargon. Available on a phone.

Output: *"Your coldest corner is the northeast — avoid frost-sensitive crops there. Water naturally collects here and here — these are your best pond sites. Your south-facing slope gets 6.2 hours of winter sun — that's where your greenhouse goes."* Actionable. Specific. Free.

### Research & Policy API
*For scientists, NGOs, governments, climate modellers.*

Programmatic access to the platform. Run analysis at regional or national scale. Query the open dataset. Model land use intervention scenarios. Feed outputs into climate models, food security models, carbon accounting systems.

### The Game
*For everyone. Built last. Changes the scale of everything.*

See below.

---

## Modularity & Plugins

Core ships lean: terrain analysis, climate analysis, solar analysis, water flow, basic design tools.

Everything else is a module — plant database, livestock integration, soil biology, biochar and carbon systems, specific crop models, agroforestry configurations, water harvesting, building energy integration. Modules are community-contributed. A soil scientist builds a soil module. A hydrologist builds a watershed model. The platform grows without the core team having to know everything.

Data is the same. Users bring their own site data — soil tests, yield records, rainfall gauges, phenology observations. The platform schema accepts it. It joins the commons if the user chooses to share.

---

## Data Sources

| Data | Source | Resolution | Scale |
|---|---|---|---|
| OS Terrain 50 DEM | Ordnance Survey | 50m | UK bootstrap |
| EA LIDAR DTM/DSM | Environment Agency | 1–2m | England |
| Copernicus DEM | ESA | 30m | Global |
| EPW climate | climate.onebuilding.org | Regional | Global |
| PVGIS solar | EU Joint Research Centre | ~3km | Europe+ |
| NASA POWER | NASA | ~50km | Global |
| SoilGrids | ISRIC | 250m | Global |
| OpenStreetMap | OSM | Variable | Global |
| User-contributed | Field measurements | Exact | Site |

Global coverage from day one is achievable with open data. Resolution improves as better sources are added per region.

---

## Build Sequence

### Now — Foundation
- `Site` object: terrain + climate + boundary
- Terrain analysis: slope, aspect
- First visualisation: real output for a real site
- LIDAR adapter: replace OS Terrain 50 with 1m EA data

### Next — Analysis
- Solar analysis: radiation per cell, seasonal variation, shadow casting
- Water flow: accumulation, catchment, frost hollows, intervention points
- Microclimate zones: composite of all layers
- Site report: plain-language summary of findings

### Then — Design Tools
- Element placement: annotate the map with design decisions
- Spatial feedback: what does each placement mean
- Bounded solver queries: *"where are the valid locations for X"*
- Export: GeoJSON, DXF, PDF report

### Later — Platform
- Shared dataset schema: design decisions + outcomes over time
- Open project layer: public sites on the platform
- Solver trained on accumulated data
- API for researchers

### Eventually — Game
- Built on top of a solver rigorous enough to be an honest judge
- Mechanic designed around what the solver needs from human creativity
- Transparent: players know they're doing real ecological work

---

## The Game

### Why It Exists

The game solves three problems at once.

**Data at scale.** The solver needs training data. The game generates it faster than any research programme. Every design placed — even on a fictional mission — is a real experiment evaluated by real physics. Players stress-test the solver in ways no QA team could, finding edge cases and degenerate solutions because they're trying to win, not trying to be helpful.

**Distribution.** A professional land CAD tool has a ceiling on users. A game has no ceiling. People who would never open a GIS tool will spend hundreds of hours designing regenerative systems if the context is right. The game is a PDC disguised as entertainment — 200 hours of play teaches water flow, soil building, guild design, and succession planning without a textbook.

**Culture.** The food system needs people to return to land — not as a backward step but as skilled, respected, technologically-augmented stewards. The current culture pushes people away from land. The game pulls them toward it. Not through argument. Through play, beauty, and the quiet satisfaction of watching a valley heal because you designed it that way. The Regenerator is the hero. That identity is what shifts culture.

The funnel:

```
GAME (millions)
Players. Gamers. Students. People who've never touched soil.
They play because it's compelling. They learn ecology through play.
    ↓
OBSERVERS (thousands)
They download the app. They walk real land. They log species.
Virtual skills become real curiosity.
    ↓
PRACTITIONERS (hundreds → growing)
They apprentice, study, find land, design real farms.
The game gave them the vision. They gave themselves the life.

Every stage feeds the platform.
The gamer who never plants a tree still trains the AI.
The observer who logs one species still calibrates the model.
The practitioner who designs a real farm validates everything.
```

The game is not secretly feeding the tool. It openly, proudly feeds the tool. Players are told: you are doing real ecological design work. That dignity is more motivating than finding out later you were a training set.

### The Premise

```
EARTH, 2047.

The collapse didn't come as one event. It came as a million
small failures. Soils turned to dust. Harvests thinned.
Rivers ran dry.

The old maps don't work anymore. The old methods are dead.
But the land remembers what it was.

You are a Regenerator. You carry the PERMA3D engine.
Go where the land is dying. Read it. Design its regeneration.
Prove it works.

The planet is waiting.
```

Real terrain. Real climate. Real ecology. The fiction is the framing. The design work underneath is not fiction.

### The Core Loop

```
ARRIVE   → degraded real landscape, real data, real urgency
READ     → observe slope, water, frost, what still grows
DESIGN   → place ponds, swales, guilds, corridors
SIMULATE → run the clock 5, 10, 50 years
SCORE    → calories, habitat, resilience, carbon, water
MOVE ON  → the valley stabilises, you're needed elsewhere
```

### Scoring — Outcomes Only

Points for what the land actually does. Not aesthetics.

- **Calories** — does this design feed people, how many, starting when, is nutrition diverse and year-round
- **Habitat** — species supported, threatened species returned, ecological corridors
- **Resilience** — survives drought year, flood year, late frost, self-regulates vs needs constant intervention
- **Carbon** — stored in soil and biomass, still accumulating at year 50
- **Water** — captured and stored, released slowly through dry season, downstream communities benefit

A beautiful forest that feeds no one is a failure. A productive farm that's an ecological desert is a failure. The simulation is the judge.

### The Solver IS the Game Engine

The solver is not a feature players consult. It is the physics. The scoring. The time machine. Every element placed triggers instant feedback — water flows, trees grow, scores update. The game feels alive because the solver makes every choice have consequences.

A player places a swale on a steep slope. The solver runs the physics. Erosion. Score drops. The player sees soil wash away in the simulation and learns a permaculture principle without a tutorial. The solver is the teacher. The game is the classroom.

A player tries a bizarre guild combination. The solver runs 50 years. Unexpected facilitation. Score 91. Pattern flagged. The solver learned something from a player just messing around.

This is why the solver and the game cannot be separate. Separate means no immediacy, no feedback loop, no learning. The solver as engine means the game is alive, educational, and generating training data at the speed of play.

### The Hero Moment

```
You've been working a degraded valley for weeks.
Designing. Simulating. Failing. Iterating.
Finally, a design scores 94%. You run the 50-year sim.

Year 1:  Bare soil. Tiny trees. Hope.
Year 10: Guilds establishing. Pond full. Soil darkening.
Year 20: Forest. Species you didn't plant have arrived.
Year 50: You barely recognise it.

A notification arrives:
"Your design has been selected by a restoration project
in this valley. Implementation begins next spring."

You didn't just play a game.
You designed a future for a real place.
And someone is going to build it.
```

### The Real-World Bridge

Exceptional designs get ecologically validated, matched with real landowners who've opted in, implemented. Players receive satellite imagery and ground photos.

```
REAL-WORLD IMPACT:
🌳 127 trees planted from your designs
🌍 3 farms using your patterns
📸 Latest ground photo: Almond guild, Year 4

"Your ridge pond design was adapted for a farm in Rajasthan.
The farmer reports 40% more soil moisture."
```

That's the flex. Not skins. Not ranks. *"127 trees exist because I played this game."*

### What the Game Requires

The game cannot exist until the engine is honest. A simulation that flatters bad designs destroys trust within days — players find the exploits and the ecological validity collapses. Build the tool until the engine deserves to be the judge. Then add the game fascia.

---

## What This Is Not

- Not a replacement for site visits and local knowledge
- Not a tool that tells farmers what to do
- Not a closed platform — AGPLv3, forever
- Not finished — the solver gets better as long as land is being regenerated and data flows back

---

## The Stakes

If regenerative land management is applied at scale — and the evidence increasingly suggests it must be — someone will build the data infrastructure for it. That infrastructure will shape how the transition happens: who has access to the knowledge, who owns the data, what design approaches get validated and spread.

PERMA3D is a bet that this infrastructure should be open. That the data should belong to the commons. That the people closest to the land — farmers, communities, restoration practitioners — should be full participants in building it, not subjects of someone else's platform.

The tool is the entry point. The dataset is the goal. The game is how it scales. The land is what it's for.

