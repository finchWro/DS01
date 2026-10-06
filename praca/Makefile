.PHONY: all docx clean help

OUTPUT = praca_koncowa.docx
SCRIPT = ./build.sh

all: docx

docx:
	@chmod +x $(SCRIPT)
	@$(SCRIPT)

clean:
	@rm -f $(OUTPUT)
	@echo "Usunięto $(OUTPUT)"

help:
	@echo "Dostępne polecenia:"
	@echo "  make        - generuje plik praca_koncowa.docx za pomocą Pandoc"
	@echo "  make clean  - usuwa wygenerowany plik praca_koncowa.docx"
