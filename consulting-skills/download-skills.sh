#!/usr/bin/env bash
# download-skills.sh — fetch all recommended consulting skills to your machine.
# Run locally (requires git + internet). Safe to re-run; existing clones are updated.
#
# Usage:
#   ./download-skills.sh              # download everything into ./consulting-ai-skills
#   ./download-skills.sh ~/skills    # custom destination
#
# After download, skills are staged under <dest>/_claude-skills/ ready to copy into:
#   ~/.claude/skills/        (Claude Code, global)
#   .claude/skills/          (Claude Code, per-project)
# or zip any staged folder and upload at claude.ai -> Settings -> Capabilities -> Skills.
#
# The two Anthropic plugin marketplaces are best installed from inside Claude Code instead:
#   claude plugin marketplace add anthropics/financial-services
#   claude plugin marketplace add anthropics/skills

set -euo pipefail

DEST="${1:-./consulting-ai-skills}"
mkdir -p "$DEST"
cd "$DEST"
DEST="$(pwd)"

REPOS=(
  "DogInfantry/claude-skill-management-consultant-B1"   # MBB consultant, 118 reference modules
  "gcamilo/management-consulting"                       # 42 frameworks, evidence labeling, eval-backed
  "sruthir28/enterprise-ai-skills"                      # ex-McKinsey: issue trees, decks, mckinsey-critic
  "aapersh/strategy-skills-for-claude"                  # 21 strategy skills, 6 domains
  "yoichiojima-2/consultant"                            # 50+ frameworks, case practice
  "alirezarezvani/claude-skills"                        # 354-skill enterprise library (market research, C-level)
  "ishwarjha/claude-marketing-research-skill"           # customer/competitor research system
  "OctagonAI/skills"                                    # real-data SEC/earnings research (free API key)
  "JoelLewis/finance_skills"                            # 81 financial-services skills
  "anthropics/skills"                                   # official: pptx/xlsx/docx/pdf + skill spec
  "anthropics/financial-services"                       # official: comps/DCF/LBO/CIM/IC-memo suite
)

echo "==> Downloading ${#REPOS[@]} repositories into $DEST"
for repo in "${REPOS[@]}"; do
  dir="${repo##*/}"
  if [ -d "$dir/.git" ]; then
    echo "--> Updating $repo"
    git -C "$dir" pull --ff-only || echo "    (pull failed; keeping existing copy)"
  else
    echo "--> Cloning $repo"
    git clone --depth 1 "https://github.com/$repo.git" "$dir"
  fi
done

# Stage every folder that contains a SKILL.md so it can be dropped into ~/.claude/skills/
STAGE="$DEST/_claude-skills"
mkdir -p "$STAGE"
echo "==> Staging skill folders into $STAGE"
for repo in "${REPOS[@]}"; do
  dir="${repo##*/}"
  find "$DEST/$dir" -name 'SKILL.md' -not -path '*/node_modules/*' | while read -r f; do
    src="$(dirname "$f")"
    name="$(basename "$src")"
    # Root-level SKILL.md -> use the repo name as the skill name
    if [ "$src" = "$DEST/$dir" ]; then name="$dir"; fi
    target="$STAGE/${dir}__${name}"
    rm -rf "$target"
    cp -R "$src" "$target"
  done
done

count="$(find "$STAGE" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')"
echo ""
echo "Done. $count skill folders staged in: $STAGE"
echo "Install into Claude Code:   cp -R \"$STAGE\"/<skill> ~/.claude/skills/<skill>"
echo "Install into claude.ai:     zip a staged folder and upload via Settings > Capabilities > Skills"
echo "See consulting-skills/PROMPT_PLAYBOOK.md for the optimal prompts per skill."
