#!/usr/bin/env python3
"""Aplica os ajustes do portfólio em index.html (idempotente).
Uso (na raiz do repositório):  python3 apply_changes.py [caminho/index.html]
"""
import re, sys, pathlib

path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "index.html")
src = path.read_text(encoding="utf-8")
out = src
report = []

MARKERS = ["[UPDATE WHEN DATA IS IN]", "[ATUALIZAR QUANDO OS DADOS FECHAREM]"]

# 1) Remove o parágrafo-placeholder do case 04 (qualquer idioma)
pat_p = re.compile(r'[ \t]*<p\b[^>]*>[^<]*(?:%s)[^<]*</p>[ \t]*\n?' % "|".join(re.escape(m) for m in MARKERS))
out, n = pat_p.subn("", out)
report.append(f"placeholder <p> removido: {n}")

# 2) Remove a entrada correspondente do dicionário PT->EN (e a vírgula da linha anterior, se for a última)
lines = out.split("\n")
new, removed = [], 0
for i, line in enumerate(lines):
    if any(m in line for m in MARKERS) and line.lstrip().startswith('"'):
        removed += 1
        if not line.rstrip().endswith(",") and new and new[-1].rstrip().endswith(","):
            new[-1] = new[-1].rstrip()[:-1]
        continue
    new.append(line)
out = "\n".join(new)
report.append(f"entradas de dicionário removidas: {removed}")

left = [m for m in MARKERS if m in out]
if left:
    print("ATENÇÃO: ainda restam marcadores:", left)
    sys.exit(1)

if out != src:
    path.write_text(out, encoding="utf-8")
    print("index.html atualizado.")
else:
    print("Nada a alterar (já aplicado).")
print("\n".join(report))
