#!/usr/bin/env bash
# ==============================================================================
# Skrypt do generowania pracy końcowej w formacie DOCX przy użyciu Pandoc.
# Zgodny z wymogami studiów podyplomowych Data Science (PWr).
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_FILE="${SCRIPT_DIR}/praca_koncowa.docx"
BIB_FILE="${SCRIPT_DIR}/references.bib"
CHAPTERS_DIR="${SCRIPT_DIR}/chapters"
TEMPLATE_FILE="${SCRIPT_DIR}/reference.docx"

echo "==> Sprawdzanie dostępności Pandoc..."
if ! command -v pandoc &> /dev/null; then
    echo "BŁĄD: Pandoc nie jest zainstalowany w Twoim systemie."
    echo "Aby go zainstalować w systemie Linux (Ubuntu/Debian):"
    echo "  sudo apt-get update && sudo apt-get install -y pandoc"
    echo ""
    echo "Jeśli używasz środowiska conda / mamba:"
    echo "  conda install -c conda-forge pandoc"
    exit 1
fi

echo "==> Budowanie pracy końcowej: ${OUTPUT_FILE}..."

PANDOC_ARGS=(
    --from=markdown+pipe_tables+implicit_figures+raw_tex
    --to=docx
    --output="${OUTPUT_FILE}"
    --bibliography="${BIB_FILE}"
    --citeproc
    --toc
    --toc-depth=3
)

# Jeśli istnieje plik szablonu reference.docx, użyj go
if [ -f "${TEMPLATE_FILE}" ]; then
    echo "--> Używam stylów z szablonu: ${TEMPLATE_FILE}"
    PANDOC_ARGS+=(--reference-doc="${TEMPLATE_FILE}")
else
    echo "--> Brak własnego szablonu reference.docx – używam domyślnych stylów Pandoc."
    echo "    (Aby dostosować czcionkę 11pt i interlinię 1.15, zobacz instrukcję w README.md)"
fi

# Zbieranie rozdziałów w odpowiedniej kolejności alfabetycznej/numerycznej
CHAPTER_FILES=($(ls "${CHAPTERS_DIR}"/*.md | sort))

echo "--> Składanie rozdziałów:"
for file in "${CHAPTER_FILES[@]}"; do
    echo "    - $(basename "$file")"
done

pandoc "${PANDOC_ARGS[@]}" "${CHAPTER_FILES[@]}"

echo "==> Sukces! Wygenerowano plik: ${OUTPUT_FILE}"
