#!/usr/bin/env bash
set -euo pipefail

# Convert all notebooks/*.ipynb to Markdown into markdowns/
if ! command -v jupyter >/dev/null 2>&1; then
  echo "Error: jupyter is not installed or not on PATH" >&2
  exit 1
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
NOTEBOOK_DIR="${ROOT_DIR}/notebooks"
OUTPUT_DIR="${ROOT_DIR}/markdowns"

mkdir -p "${OUTPUT_DIR}"
shopt -s nullglob
notebooks=("${NOTEBOOK_DIR}"/*.ipynb)
if [[ ${#notebooks[@]} -eq 0 ]]; then
  echo "No .ipynb files found in ${NOTEBOOK_DIR}" >&2
  exit 1
fi

for nb in "${notebooks[@]}"; do
  echo "Converting ${nb} to Markdown..."
  jupyter nbconvert --to markdown "${nb}" --output-dir "${OUTPUT_DIR}"
done

count=$(ls -1q "${OUTPUT_DIR}"/*.md | wc -l)
echo "Converted ${count} notebooks to Markdown format in ${OUTPUT_DIR} folder."
echo "All done!"
