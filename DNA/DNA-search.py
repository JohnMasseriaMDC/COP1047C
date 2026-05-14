"""
search_dna_substrings.py

Searches a database of known animal DNA sequences for a set of unknown
DNA fragments.  For every fragment the script reports the animals that
contain it, and also lists fragments that were not found in any
known sequence.

Usage
-----
    python search_dna_substrings.py \
        --known known_sequences.txt \
        --unknown unknown_fragments.txt \
        [--output results.txt]      # optional

If `--output` is omitted, the results are printed to stdout.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple


# --------------------------------------------------------------------------- #
# 1.  Command‑line parsing
# --------------------------------------------------------------------------- #
def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Find unknown DNA fragments inside known animal DNA sequences."
    )
    p.add_argument(
        "--known",
        required=True,
        type=Path,
        help="File with known animal DNA sequences (tab‑separated name + seq).",
    )
    p.add_argument(
        "--unknown",
        required=True,
        type=Path,
        help="File with unknown DNA fragments (one per line).",
    )
    p.add_argument(
        "--output",
        type=Path,
        help="Optional file to write results; otherwise prints to stdout.",
    )
    return p.parse_args()


# --------------------------------------------------------------------------- #
# 2.  Load data
# --------------------------------------------------------------------------- #
def load_known_sequences(path: Path) -> Dict[str, str]:
    """Read the known‑sequence file and return a dict {animal: sequence}."""
    known = {}
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                name, seq = line.split(" ", 1)
            except ValueError:
                sys.stderr.write(f"WARNING: Skipping malformed known line: {line!r}\n")
                continue
            known[name.strip()] = seq.strip().upper()
    return known


def load_unknown_fragments(path: Path) -> List[str]:
    """Read the unknown‑fragment file and return a list of fragments (upper‑case)."""
    fragments = []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            frag = line.strip().upper()
            if frag and not frag.startswith("#"):
                fragments.append(frag)
    return fragments


# --------------------------------------------------------------------------- #
# 3.  Search fragments
# --------------------------------------------------------------------------- #
def search_fragments(
    known: Dict[str, str], fragments: List[str]
) -> Tuple[Dict[str, List[str]], List[str]]:
    """
    For each fragment, record the animals whose full sequence contains it.
    Returns
        * results  – {fragment: [animal, …]}
        * unmatched – list of fragments that had **no** matches
    """
    results: Dict[str, List[str]] = defaultdict(list)

    for frag in fragments:
        for animal, seq in known.items():
            if frag in seq:
                results[frag].append(animal)

    unmatched = [f for f in fragments if f not in results or not results[f]]
    return results, unmatched


# --------------------------------------------------------------------------- #
# 4.  Write output
# --------------------------------------------------------------------------- #
def write_results(
    matched: Dict[str, List[str]], unmatched: List[str], out_path: Path | None
) -> None:
    """
    Pretty‑print / write the search results.

    Format
    ------
    MATCHED
        UNKNOWN_FRAGMENT
            - AnimalName
            - AnimalName

    UNMATCHED
        UNKNOWN_FRAGMENT
    """
    lines: List[str] = []

    # -------- matched fragments ------------------------------------------- #
    lines.append("=== FRAGMENTS THAT MATCHED ===")
    lines.append("")
    for frag in sorted(matched):
        animals = sorted(matched[frag])
        lines.append(f"{frag}")
        for a in animals:
            lines.append(f"    - {a}")
        lines.append("")          # blank line for readability

    # -------- unmatched fragments ------------------------------------------ #
    lines.append("=== FRAGMENTS THAT DID NOT MATCH ANY KNOWN SEQUENCE ===")
    lines.append("")
    for frag in sorted(unmatched):
        lines.append(f"{frag}")
    lines.append("")  # final blank line

    out_text = "\n".join(lines)

    if out_path:
        out_path.write_text(out_text, encoding="utf-8")
    else:
        print(out_text)


# --------------------------------------------------------------------------- #
# 5.  Main driver
# --------------------------------------------------------------------------- #
def main() -> None:
    args = parse_args()

    known = load_known_sequences(args.known)
    if not known:
        sys.stderr.write("ERROR: No valid known sequences loaded.\n")
        sys.exit(1)

    fragments = load_unknown_fragments(args.unknown)
    if not fragments:
        sys.stderr.write("ERROR: No valid unknown fragments loaded.\n")
        sys.exit(1)

    matched, unmatched = search_fragments(known, fragments)
    write_results(matched, unmatched, args.output)


if __name__ == "__main__":
    main()