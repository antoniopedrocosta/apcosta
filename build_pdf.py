# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                 HRFlowable, ListFlowable, ListItem)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT

INK = colors.HexColor("#1c2530")
INK_SOFT = colors.HexColor("#4b5563")
ACCENT = colors.HexColor("#1f6f78")
LINE = colors.HexColor("#e2e5e9")

styles = getSampleStyleSheet()

name_style = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=22, textColor=INK, spaceAfter=4, leading=26)
role_style = ParagraphStyle("role", fontName="Helvetica", fontSize=11, textColor=INK_SOFT, spaceAfter=8, leading=14)
tagline_style = ParagraphStyle("tagline", fontName="Helvetica-Oblique", fontSize=9.5, textColor=INK_SOFT, spaceAfter=10, leading=13)
contact_style = ParagraphStyle("contact", fontName="Helvetica", fontSize=9, textColor=INK_SOFT, spaceAfter=14, leading=13)

h2_style = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=11, textColor=ACCENT, spaceBefore=16, spaceAfter=8,
                           letterSpacing=1)
h3_style = ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=10.5, textColor=INK, spaceAfter=1, leading=13)
meta_style = ParagraphStyle("meta", fontName="Helvetica-Oblique", fontSize=8.7, textColor=INK_SOFT, spaceAfter=8, leading=11)
period_style = ParagraphStyle("period", fontName="Helvetica-Bold", fontSize=8.3, textColor=ACCENT, spaceAfter=1, leading=10)
body_style = ParagraphStyle("body", fontName="Helvetica", fontSize=9.3, textColor=INK, spaceAfter=8, leading=13.5, alignment=TA_LEFT)
li_style = ParagraphStyle("li", fontName="Helvetica", fontSize=9, textColor=INK_SOFT, spaceAfter=5, leading=12.5)
pub_style = ParagraphStyle("pub", fontName="Helvetica", fontSize=8.9, textColor=INK_SOFT, spaceAfter=6, leading=12.5)
stat_num = ParagraphStyle("statnum", fontName="Helvetica-Bold", fontSize=15, textColor=ACCENT, leading=17)
stat_lbl = ParagraphStyle("statlbl", fontName="Helvetica", fontSize=7.3, textColor=INK_SOFT, leading=9)

def hr():
    return HRFlowable(width="100%", thickness=0.6, color=LINE, spaceBefore=2, spaceAfter=10)

story = []

story.append(Paragraph("António Pedro Dias da Costa", name_style))
story.append(Paragraph(
    "Investigador Doutorado &middot; Universidade de Aveiro (CIDTFF) &middot; Colaborador LIACC &ndash; Faculdade de Engenharia da Universidade do Porto",
    role_style))
story.append(Paragraph(
    "Investiga&ccedil;&atilde;o Qualitativa, M&eacute;todos Mistos e Colabora&ccedil;&atilde;o Humano-IA aplicadas &agrave; Educa&ccedil;&atilde;o. "
    "Coautor do software webQDA e coordenador do Congresso Ibero-Americano em Investiga&ccedil;&atilde;o Qualitativa (CIAIQ) e da "
    "World Conference on Qualitative Research (WCQR).", tagline_style))
story.append(Paragraph(
    "Oliveira de Azem&eacute;is, Portugal &nbsp;&middot;&nbsp; apcosta@ua.pt &nbsp;&middot;&nbsp; "
    "ORCID: 0000-0002-4644-5879 &nbsp;&middot;&nbsp; Google Scholar &nbsp;&middot;&nbsp; CiênciaVitae &nbsp;&middot;&nbsp; Lattes",
    contact_style))
story.append(hr())

# SOBRE
story.append(Paragraph("SOBRE", h2_style))
story.append(Paragraph(
    "Investigador doutorado da Universidade de Aveiro, integrado no Centro de Investiga&ccedil;&atilde;o em Did&aacute;tica e "
    "Tecnologia na Forma&ccedil;&atilde;o de Formadores (CIDTFF &ndash; DEP), e colaborador do Laborat&oacute;rio de Intelig&ecirc;ncia "
    "Artificial e Ci&ecirc;ncia de Computadores (LIACC) da Faculdade de Engenharia da Universidade do Porto. Desenvolve atividade "
    "cient&iacute;fica h&aacute; mais de duas d&eacute;cadas na intersec&ccedil;&atilde;o entre Educa&ccedil;&atilde;o, tecnologias "
    "digitais e metodologias de investiga&ccedil;&atilde;o, com enfoque recente na utiliza&ccedil;&atilde;o cr&iacute;tica, &eacute;tica "
    "e respons&aacute;vel da intelig&ecirc;ncia artificial &mdash; incluindo grandes modelos de linguagem &mdash; em contextos de "
    "ensino superior e investiga&ccedil;&atilde;o cient&iacute;fica.", body_style))
story.append(Paragraph(
    "Doutorado em Multim&eacute;dia em Educa&ccedil;&atilde;o pela Universidade de Aveiro, com p&oacute;s-doutoramento em "
    "investiga&ccedil;&atilde;o qualitativa aplicada &agrave; Educa&ccedil;&atilde;o e forma&ccedil;&atilde;o de base em Engenharia "
    "da Comunica&ccedil;&atilde;o. &Eacute; autor e editor de mais de 300 publica&ccedil;&otilde;es cient&iacute;ficas. Coordena, "
    "desde a sua cria&ccedil;&atilde;o, dois dos principais eventos internacionais na &aacute;rea da investiga&ccedil;&atilde;o "
    "qualitativa: o CIAIQ e a WCQR.", body_style))

stat_data = [
    [Paragraph("300+", stat_num), Paragraph("76", stat_num), Paragraph("50", stat_num), Paragraph("44", stat_num), Paragraph("20+", stat_num)],
    [Paragraph("Publica&ccedil;&otilde;es", stat_lbl), Paragraph("Artigos em revistas", stat_lbl),
     Paragraph("Artigos em confer&ecirc;ncias", stat_lbl), Paragraph("Eventos organizados", stat_lbl), Paragraph("Anos de atividade", stat_lbl)]
]
stat_table = Table(stat_data, colWidths=[95]*5)
stat_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING', (0,0), (-1,-1), 2),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
]))
story.append(Spacer(1, 4))
story.append(stat_table)
story.append(hr())

def entry(period, title, meta=None):
    story.append(Paragraph(period, period_style))
    story.append(Paragraph(title, h3_style))
    if meta:
        story.append(Paragraph(meta, meta_style))
    else:
        story.append(Spacer(1, 6))

# PERCURSO PROFISSIONAL
story.append(Paragraph("PERCURSO PROFISSIONAL", h2_style))
entry("2023 &ndash; presente", "Investigador Doutorado, Universidade de Aveiro",
      "Projeto “Collaborative and automated processes for qualitative research in Education” &middot; DOI: 10.54499/CEECINST/00013/2021/CP2779/CT0011")
entry("2023 &ndash; presente", "Investigador Doutorado, Faculdade de Psicologia e Ci&ecirc;ncias da Educa&ccedil;&atilde;o da Universidade do Porto")
entry("2013 &ndash; presente", "Membro integrado e do Conselho Cient&iacute;fico, CIDTFF &ndash; Universidade de Aveiro",
      "Laborat&oacute;rio de Conte&uacute;dos Digitais (LCD), Departamento de Educa&ccedil;&atilde;o e Psicologia")
entry("2008 &ndash; presente", "Colaborador, LIACC &ndash; Faculdade de Engenharia da Universidade do Porto")
entry("2004 &ndash; presente", "Cofundador, Ludomedia Unipessoal Lda.", "Respons&aacute;vel intelectual e pedag&oacute;gico &middot; Oliveira de Azem&eacute;is &middot; www.ludomedia.org")
entry("2000 &ndash; 2006", "Cofundador e Diretor Geral, ArteVirtual", "Explora&ccedil;&atilde;o de Tecnologias de Informa&ccedil;&atilde;o e Comunica&ccedil;&atilde;o, Oliveira de Azem&eacute;is")
story.append(hr())

# FORMACAO
story.append(Paragraph("FORMA&Ccedil;&Atilde;O ACAD&Eacute;MICA", h2_style))
entry("2018", "P&oacute;s-Doutoramento &ndash; Universidade de Aveiro",
      "“Implementa&ccedil;&atilde;o e Avalia&ccedil;&atilde;o de Instrumentos para An&aacute;lise Qualitativa na Investiga&ccedil;&atilde;o em Educa&ccedil;&atilde;o” &middot; bolsa SFRH/BPD/104288/2014")
entry("2012", "Doutoramento em Multim&eacute;dia em Educa&ccedil;&atilde;o &ndash; Universidade de Aveiro",
      "Tese: “Metodologia H&iacute;brida de Desenvolvimento Centrado no Utilizador: aplicada ao Software Educativo”")
entry("2003", "Curso de Especializa&ccedil;&atilde;o em Multim&eacute;dia em Educa&ccedil;&atilde;o &ndash; Universidade de Aveiro")
entry("2002", "Licenciatura em Engenharia da Comunica&ccedil;&atilde;o (Comunica&ccedil;&atilde;o e Design) &ndash; Universidade Fernando Pessoa")
story.append(Paragraph(
    "Certifica&ccedil;&atilde;o como Formador pelo Conselho Cient&iacute;fico-Pedag&oacute;gico da Forma&ccedil;&atilde;o Cont&iacute;nua "
    "(CCPFC/RFO &ndash; 17976/04, desde 2004).", meta_style))
story.append(hr())

# INVESTIGACAO
story.append(Paragraph("&Aacute;REAS DE INVESTIGA&Ccedil;&Atilde;O", h2_style))
areas = ("Colabora&ccedil;&atilde;o Humano-IA &middot; Investiga&ccedil;&atilde;o Qualitativa &middot; M&eacute;todos Mistos &middot; "
         "An&aacute;lise de Dados Qualitativos &middot; Software webQDA &middot; M&eacute;todos Visuais &middot; "
         "Design Centrado no Utilizador &middot; &Eacute;tica e Integridade na Investiga&ccedil;&atilde;o &middot; Tecnologias Educativas")
story.append(Paragraph(areas, body_style))
story.append(Paragraph(
    "Participa atualmente em projetos e redes cient&iacute;ficas internacionais, entre os quais o Erasmus+ EDUAI, a COST Action "
    "CA24121 (Knowledge Graphs in the Era of Large Language Models) e colabora&ccedil;&otilde;es com a National Academy of Sciences "
    "of Ukraine / UNESCO Chair on AI in Education.", body_style))
story.append(hr())

# PUBLICACOES
story.append(Paragraph("PUBLICA&Ccedil;&Otilde;ES SELECIONADAS", h2_style))
story.append(Paragraph("Lista completa (300+ trabalhos) dispon&iacute;vel no Google Scholar e ORCID.", meta_style))
pubs = [
 "2025 &ndash; Costa, A. P., Bryda, G., Christou, P. A., &amp; Kasperiuniene, J. AI as a Co-researcher in the Qualitative Research Workflow. <i>International Journal of Qualitative Methods</i>, 24.",
 "2025 &ndash; Costa, A. P., Burneo, P., &amp; Kasperiuniene, J. Mixed-methods &amp; AI for Methodological Literature Reviews. <i>The Qualitative Report</i>, 30(10), 4515&ndash;4540.",
 "2025 &ndash; Pinho, I., Costa, A. P., &amp; Pinho, C. Generative AI Governance Model in Educational Research. <i>Frontiers in Education</i>, 10.",
 "2024 &ndash; Petre, G.-E., &amp; Costa, A. P. Advancing Qualitative Research: Insights from the 7th World Conference on Qualitative Research. <i>Social Sciences</i>, 13(1).",
 "2023 &ndash; Bryda, G., &amp; Costa, A. P. Qualitative Research in Digital Era: Innovations, Methodologies and Collaborations. <i>Social Sciences</i>, 12(10), 570.",
 "2023 &ndash; Costa, A. P. Qualitative Research Methods: do digital tools open promising trends? <i>Revista Lusófona de Educa&ccedil;&atilde;o</i>, 59(59), 67&ndash;76.",
 "2020 &ndash; Brand&atilde;o, C., &amp; Costa, A. P. Reflecting on CAQDAS and Ethics. <i>The Qualitative Report</i>, 25(13), 1&ndash;5.",
 "2019 &ndash; Costa, A. P., &amp; Moreira, A. Technology ethics in qualitative research: How to be. <i>The Qualitative Report</i>, 24(13).",
 "2019 &ndash; Costa, A. P., &amp; Minayo, M. C. de S. Building criteria to evaluate qualitative research papers. <i>Revista da Escola de Enfermagem da USP</i>, 53, 1&ndash;7.",
]
for p in pubs:
    story.append(Paragraph(p, pub_style))
story.append(hr())

# DOCENCIA
story.append(Paragraph("DOC&Ecirc;NCIA", h2_style))
entry("2025/2026", "Universidade de Aveiro",
      "Metodologias de Investiga&ccedil;&atilde;o em Multim&eacute;dia em Educa&ccedil;&atilde;o &middot; Metodologias de Investiga&ccedil;&atilde;o em Educa&ccedil;&atilde;o (Programas Doutorais)")
entry("2014 &ndash; 2024", "Universidade de Aveiro, Universidade Lus&oacute;fona do Porto, ISLA, ISVOUGA",
      "Metodologias de Investiga&ccedil;&atilde;o em cursos de mestrado, doutoramento e p&oacute;s-gradua&ccedil;&atilde;o")
entry("2001 &ndash; 2003", "Instituto Piaget", "Comunica&ccedil;&atilde;o Educacional Multim&eacute;dia e Novas T&eacute;cnicas de Comunica&ccedil;&atilde;o")
story.append(Paragraph(
    "Desde 2010, coordena a forma&ccedil;&atilde;o em torno do software webQDA, tendo dinamizado dezenas de cursos e workshops "
    "em Portugal, Espanha, Brasil, Cro&aacute;cia e Jord&acirc;nia, entre outros.", body_style))
story.append(hr())

# SERVICO
story.append(Paragraph("SERVI&Ccedil;O CIENT&Iacute;FICO", h2_style))
serv_left = [
 "Coorganizador, 9th World Conference on Qualitative Research (WCQR2026), Madrid",
 "Coorganizador, 14&ordm; Congresso Ibero-Americano em Investiga&ccedil;&atilde;o Qualitativa, Porto (2025)",
 "Coorganizador, 2&ordm; F&oacute;rum IA no Espa&ccedil;o Educacional, Universidade de Aveiro (2025)",
 "Coordenador fundador do CIAIQ (14 edi&ccedil;&otilde;es) e da WCQR (9 edi&ccedil;&otilde;es)",
]
serv_right = [
 "Membro do Conselho Cient&iacute;fico, CIIE &ndash; Universidade do Porto (2026&ndash;)",
 "Membro da Comiss&atilde;o Cient&iacute;fica, Doutoramento em Educa&ccedil;&atilde;o, ISCED-Hu&iacute;la, Angola (2025&ndash;)",
 "Membro do Conselho Cient&iacute;fico, CIDTFF &ndash; Universidade de Aveiro (2013&ndash;)",
 "Membro do Editorial Board, <i>The Qualitative Report</i> (2025&ndash;)",
]
serv_table_data = [[
    ListFlowable([ListItem(Paragraph(t, li_style)) for t in serv_left], bulletType='bullet', start='-', leftIndent=10),
    ListFlowable([ListItem(Paragraph(t, li_style)) for t in serv_right], bulletType='bullet', start='-', leftIndent=10),
]]
serv_table = Table(serv_table_data, colWidths=[255, 255])
serv_table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
story.append(serv_table)
story.append(hr())

# PREMIOS
story.append(Paragraph("PR&Eacute;MIOS E DISTIN&Ccedil;&Otilde;ES", h2_style))
story.append(Paragraph("&middot; Men&ccedil;&atilde;o Honrosa, &Aacute;rea de Artes e Humanidades, “Pr&eacute;mio Investigador UA” (2022)", li_style))
story.append(Paragraph("&middot; Biannual Book in Spanish or Portuguese, ICQI Award (2016)", li_style))

doc = SimpleDocTemplate(
    "/sessions/determined-nice-gauss/mnt/outputs/Antonio_Pedro_Costa_CV.pdf",
    pagesize=A4,
    leftMargin=20*mm, rightMargin=20*mm, topMargin=16*mm, bottomMargin=16*mm,
    title="António Pedro Costa — Curriculum Vitae"
)
doc.build(story)
print("PDF gerado com sucesso")
