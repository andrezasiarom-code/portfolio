# Pacote de ajustes do portfólio (vaga Sr. Staff Product Designer, QuintoAndar)

## Conteúdo
| Arquivo | O que faz |
|---|---|
| `Andy-Morais-Curriculo.pdf` | Currículo PT-BR adaptado à vaga (2 páginas). Substitui o arquivo de mesmo nome. |
| `Andy-Morais-Resume.pdf` | Currículo EN adaptado à vaga (2 páginas). Substitui o arquivo de mesmo nome. |
| `apply_changes.py` | Ajusta o `index.html` (remove o placeholder do case 04). Idempotente. |

Os nomes dos PDFs são os mesmos que o site já usa (botões "Baixar currículo" em PT/EN), então não há mudança de link.

## Mudanças

### Currículos (PT e EN)
- Resumo reescrito para abrir como **Staff, hands-on, referência técnica** e com o uso de **IA no fluxo de design** em destaque, que é o ponto central da vaga.
- Novo bullet no Trio com o case de Payments (4 jornadas + link externo em 1 semana vs 3+, 144 interações, 1.541 camadas, animação em código testado), que antes só existia no portfólio.
- Competências reordenadas para espelhar a vaga: Product & Interaction Design, Prototipação e IA, Liderança, Discovery/Workshops, Design Systems.
- Ateliware condensado (bullet duplicado e frase quebrada corrigidos); Miro incluído em Ferramentas (já constava na experiência Big Brain).
- Só foram usados fatos já presentes no seu currículo e portfólio. Nada novo foi inventado.

### Site (`index.html`)
- Remove o texto **"[ATUALIZAR QUANDO OS DADOS FECHAREM] / [UPDATE WHEN DATA IS IN]"** do case 04 (parágrafo e entrada do dicionário PT→EN). Se você já tiver as métricas de uso, em vez de remover, troque por uma linha de resultado.

## Como aplicar (na raiz do repositório do site)
```bash
git checkout -b ajustes-vaga-quintoandar
cp /caminho/do/pacote/Andy-Morais-Curriculo.pdf .
cp /caminho/do/pacote/Andy-Morais-Resume.pdf .
python3 /caminho/do/pacote/apply_changes.py index.html
git diff --stat            # deve mostrar 2 PDFs + index.html
git add Andy-Morais-Curriculo.pdf Andy-Morais-Resume.pdf index.html
git commit -m "Atualiza currículos (PT/EN) e remove placeholder do case Payments"
git push -u origin ajustes-vaga-quintoandar
# abra o Pull Request; se o deploy for na Vercel, o preview sai automaticamente
```
Se os PDFs ficarem em outra pasta no repositório, copie para lá.

## Pendências que dependem de você (não foram inseridas por falta de informação)
Se forem verdade, vale acrescentar ao currículo e ao portfólio, porque a vaga pede:
1. **App mobile lançado** (nome, o que você fez, resultado). Maior lacuna hoje.
2. **Mentoria** de designers (quantas pessoas, por quanto tempo, resultado).
3. **Apresentações a C-level/diretoria** (onde e sobre o quê).
4. **Métricas de uso/negócio** do case Payments e do design system além dos −80%.
5. **Nível de inglês:** o currículo diz "Avançado / Proficiência profissional" e a vaga exige "fluente". Se você é fluente, ajuste a linha de Idiomas.
