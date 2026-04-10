#!/usr/bin/env python3
"""Generate .claude-plugin/marketplace.json with individual plugin entries.

Reads YAML frontmatter from every skills/*/SKILL.md file and produces a
marketplace manifest that lists each skill as its own installable plugin,
plus a single 'pm-skills-bundle' entry that installs the entire library.

Usage:
    python scripts/generate-marketplace.py          # write to .claude-plugin/marketplace.json
    python scripts/generate-marketplace.py --check  # exit non-zero if file would change
"""

from __future__ import annotations

import glob
import json
import sys
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SKILLS_GLOB = PROJECT_ROOT / "skills" / "*" / "SKILL.md"
MARKETPLACE_PATH = PROJECT_ROOT / ".claude-plugin" / "marketplace.json"
PLUGIN_PATH = PROJECT_ROOT / ".claude-plugin" / "plugin.json"

# ── Theme-to-tags mapping ────────────────────────────────────────────────────
THEME_TAGS: dict[str, list[str]] = {
    "ai-agents": ["ai", "agents"],
    "career-leadership": ["career", "leadership"],
    "finance-metrics": ["finance", "saas", "metrics"],
    "discovery-research": ["discovery", "research"],
    "workshops-facilitation": ["workshop", "facilitation"],
    "strategy-positioning": ["strategy", "positioning"],
    "pm-artifacts": ["artifacts", "templates"],
}

# ── Keyword-to-tags heuristics (matched against skill name) ──────────────────
NAME_TAG_HINTS: list[tuple[str, list[str]]] = [
    ("finance", ["finance", "saas"]),
    ("saas", ["finance", "saas"]),
    ("pricing", ["finance", "pricing"]),
    ("user-story", ["user-stories", "backlog"]),
    ("epic", ["user-stories", "backlog"]),
    ("discovery", ["discovery", "research"]),
    ("prd", ["prd", "artifacts"]),
    ("roadmap", ["roadmap", "strategy"]),
    ("positioning", ["strategy", "positioning"]),
    ("persona", ["discovery", "research"]),
    ("journey", ["discovery", "ux"]),
    ("workshop", ["workshop", "facilitation"]),
    ("career", ["career", "leadership"]),
    ("director", ["career", "leadership"]),
    ("vp-cpo", ["career", "leadership"]),
    ("executive", ["career", "leadership"]),
    ("onboarding", ["career", "leadership"]),
    ("canvas", ["frameworks"]),
    ("prioritization", ["prioritization"]),
    ("opportunity", ["discovery", "frameworks"]),
    ("jobs-to-be-done", ["discovery", "frameworks"]),
    ("storyboard", ["ux", "artifacts"]),
    ("press-release", ["strategy", "artifacts"]),
    ("pestel", ["strategy", "analysis"]),
    ("tam-sam-som", ["strategy", "market-sizing"]),
    ("eol", ["lifecycle"]),
    ("pol-probe", ["validation", "experiments"]),
    ("lean-ux", ["ux", "frameworks"]),
    ("context-engineering", ["ai", "agents"]),
    ("ai-shaped", ["ai", "agents"]),
    ("company-research", ["research", "analysis"]),
    ("recommendation", ["ai", "frameworks"]),
    ("skill-authoring", ["meta"]),
]


def read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    return yaml.safe_load(parts[1]) or {}


def tags_for_skill(name: str, skill_type: str, theme: str) -> list[str]:
    """Derive a compact tag list for a skill plugin entry."""
    tags: list[str] = ["pm", "product-management"]

    # Skill type tag
    if skill_type:
        tags.append(skill_type)

    # Theme-based tags
    if theme and theme in THEME_TAGS:
        tags.extend(THEME_TAGS[theme])

    # Name-heuristic tags
    for keyword, extra_tags in NAME_TAG_HINTS:
        if keyword in name:
            tags.extend(extra_tags)

    # Deduplicate while preserving order
    seen: set[str] = set()
    unique: list[str] = []
    for tag in tags:
        if tag not in seen:
            seen.add(tag)
            unique.append(tag)
    return unique


def load_version() -> str:
    """Read current version from plugin.json."""
    if PLUGIN_PATH.exists():
        data = json.loads(PLUGIN_PATH.read_text(encoding="utf-8"))
        return data.get("version", "0.75.0")
    return "0.75.0"


def build_marketplace() -> dict:
    """Build the full marketplace manifest."""
    version = load_version()

    # Collect individual skill plugins
    skill_plugins: list[dict] = []
    for raw_path in sorted(glob.glob(str(SKILLS_GLOB))):
        path = Path(raw_path)
        fm = read_frontmatter(path)
        if not fm:
            continue

        name = fm.get("name", "")
        description = fm.get("description", "")
        skill_type = fm.get("type", "")
        theme = fm.get("theme", "")

        if not name or not description:
            continue

        # Truncate description to marketplace limit (200 chars)
        if len(description) > 200:
            description = description[:197] + "..."

        tags = tags_for_skill(name, skill_type, theme)

        skill_plugins.append(
            {
                "name": name,
                "source": f"./skills/{name}/",
                "description": description,
                "category": "product-management",
                "tags": tags,
                "strict": False,
            }
        )

    # Bundle plugin — installs everything at once
    bundle_plugin = {
        "name": "pm-skills-bundle",
        "source": "./",
        "description": f"All {len(skill_plugins)} PM skills at once — discovery, strategy, finance, career, and more.",
        "category": "product-management",
        "tags": [
            "pm",
            "product-management",
            "discovery",
            "strategy",
            "finance",
            "career",
            "prd",
            "user-stories",
            "roadmap",
            "bundle",
        ],
        "strict": False,
    }

    return {
        "name": "pm-skills",
        "owner": {
            "name": "Dean Peters",
            "email": "dean.peters@productside.com",
        },
        "metadata": {
            "description": f"{len(skill_plugins)} battle-tested product management skills for Claude Code — install individually or as a bundle.",
            "version": version,
        },
        "plugins": [bundle_plugin] + skill_plugins,
    }


def main() -> int:
    check_mode = "--check" in sys.argv

    marketplace = build_marketplace()
    new_content = json.dumps(marketplace, indent=2, ensure_ascii=False) + "\n"

    if check_mode:
        if MARKETPLACE_PATH.exists():
            current = MARKETPLACE_PATH.read_text(encoding="utf-8")
            if current == new_content:
                print("marketplace.json is up to date.")
                return 0
        print("marketplace.json is out of date. Run: python scripts/generate-marketplace.py")
        return 1

    MARKETPLACE_PATH.parent.mkdir(parents=True, exist_ok=True)
    MARKETPLACE_PATH.write_text(new_content, encoding="utf-8")

    total_plugins = len(marketplace["plugins"])
    individual = total_plugins - 1  # minus the bundle
    print(f"Generated marketplace.json with {individual} individual plugins + 1 bundle ({total_plugins} total).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
