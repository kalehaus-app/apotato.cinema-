#!/usr/bin/env python3
"""Render copy-paste prompt sheets from a film's SHOT_MANIFEST.json.

Usage: python3 offbeat-cinema/tools/render_prompts.py offbeat-cinema/001-great-cake-escape
Writes prompts/IMAGE_PROMPTS.md and prompts/ANIMATION_PROMPTS.md. The manifest is the
source of truth; edit prompts there, then re-run this.
"""
import json
import sys
from pathlib import Path


def fmt_inputs(inputs):
    if isinstance(inputs, dict):
        return "\n".join(f"- `{role}`: `{path}`" for role, path in inputs.items())
    return "\n".join(f"- `{path}`" for path in inputs) or "- (none)"


def main(project_dir):
    root = Path(project_dir)
    m = json.loads((root / "SHOT_MANIFEST.json").read_text())
    title = m["project"]["title"]
    img_defaults = m["defaults"]["image"]
    vid_defaults = m["defaults"]["video"]

    img = [f"# {title} — Image Prompts\n",
           "_Generated from `SHOT_MANIFEST.json` by `tools/render_prompts.py`. Do not edit by hand._\n",
           f"Default model: **{img_defaults['model']}** · params: `{json.dumps(img_defaults['params'])}`\n",
           "Attach every listed reference image. The first reference is the primary one.\n"]
    vid = [f"# {title} — Animation Prompts\n",
           "_Generated from `SHOT_MANIFEST.json` by `tools/render_prompts.py`. Do not edit by hand._\n",
           f"Default model: **{vid_defaults['model']}** · params: `{json.dumps(vid_defaults['params'])}`\n",
           "One shot per generation. Generated length is longer than the used length; trim in the edit.\n"]

    for s in m["shots"]:
        head = f"## {s['id']} — {s['name']} ({s['classification']})"
        meta = f"*{s['act']} · {s['duration_s']} s · {s['purpose']}*"
        i = s["image"]
        if s["classification"] in ("MISSING", "REGENERATE"):
            img += [head, meta, f"\n**Model:** {i.get('model', img_defaults['model'])}",
                    "\n**References:**", fmt_inputs(i["inputs"]),
                    f"\n**Save as:** `{s['video']['inputs'].get('start_image', '')}`",
                    "\n```text", i["prompt"], "```\n"]
        v = s["video"]
        params = {**vid_defaults["params"], **v.get("params", {})}
        vid += [head, meta, f"\n**Params:** `{json.dumps(params)}` · **use:** {v['use_range_s'][0]}–{v['use_range_s'][1]} s",
                "\n**Inputs:**", fmt_inputs(v["inputs"]),
                "\n```text", v["prompt"], "```\n"]

    out = root / "prompts"
    out.mkdir(exist_ok=True)
    (out / "IMAGE_PROMPTS.md").write_text("\n".join(img))
    (out / "ANIMATION_PROMPTS.md").write_text("\n".join(vid))
    print(f"wrote {out / 'IMAGE_PROMPTS.md'} and {out / 'ANIMATION_PROMPTS.md'}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
