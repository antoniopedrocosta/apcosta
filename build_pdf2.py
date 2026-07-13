# -*- coding: utf-8 -*-
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                 HRFlowable, ListFlowable, ListItem, Image)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from PIL import Image as PILImage, ImageDraw

INK = colors.HexColor("#1c2530")
INK_SOFT = colors.HexColor("#4b5563")
ACCENT = colors.HexColor("#1f6f78")
LINE = colors.HexColor("#e2e5e9")

OUTDIR = "/sessions/determined-nice-gauss/mnt/outputs"
PHOTO_SRC = os.path.join(OUTDIR, "foto.jpg")
PHOTO_CIRCLE = os.path.join(OUTDIR, "foto_circle.png")


def make_circle_photo(src, dst, size=300):
    im = PILImage.open(src).convert("RGB")
    w, h = im.size
    side = min(w, h)
    left = (w - side) // 2
    top = (h - side) // 2
    im = im.crop((left, top, left + side, top + side)).resize((size, size), PILImage.LANCZOS)
    mask = PILImage.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    out = PILImage.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(im, (0, 0), mask)
    out.save(dst)


CONTENT = {
    "pt": dict(
        title="António Pedro Costa — Curriculum Vitae",
        role="Investigador Doutorado · Faculdade de Psicologia e Ciências da Educação, Universidade do Porto · CIDTFF – Universidade de Aveiro · LIACC – Universidade do Porto",
        tagline="Investigação Qualitativa, Métodos Mistos e Colaboração Humano-IA aplicadas à Educação. Coautor do software webQDA e coordenador do Congresso Ibero-Americano em Investigação Qualitativa (CIAIQ) e da World Conference on Qualitative Research (WCQR).",
        contact="Oliveira de Azeméis, Portugal  ·  apcosta@fpce.up.pt  ·  apcosta@ludomedia.org  ·  ORCID: 0000-0002-4644-5879  ·  Google Scholar  ·  CiênciaVitae",
        h_sobre="SOBRE", h_percurso="PERCURSO PROFISSIONAL", h_formacao="FORMAÇÃO ACADÉMICA",
        h_investigacao="ÁREAS DE INVESTIGAÇÃO", h_publicacoes="PUBLICAÇÕES SELECIONADAS",
        h_docencia="DOCÊNCIA", h_servico="SERVIÇO CIENTÍFICO", h_premios="PRÉMIOS E DISTINÇÕES",
        sobre_p1="Investigador doutorado, atualmente na Faculdade de Psicologia e Ciências da Educação da Universidade do Porto, com ligação de longa data ao Centro de Investigação em Didática e Tecnologia na Formação de Formadores (CIDTFF – Universidade de Aveiro) e ao Laboratório de Inteligência Artificial e Ciência de Computadores (LIACC – Universidade do Porto). Desenvolve atividade científica há mais de duas décadas na intersecção entre Educação, tecnologias digitais e metodologias de investigação, com enfoque recente na utilização crítica, ética e responsável da inteligência artificial — incluindo grandes modelos de linguagem — em contextos de ensino superior e investigação científica.",
        sobre_p2="Doutorado em Multimédia em Educação pela Universidade de Aveiro, com pós-doutoramento em investigação qualitativa aplicada à Educação e formação de base em Engenharia da Comunicação. É autor e editor de mais de 300 publicações científicas. Coordena, desde a sua criação, dois dos principais eventos internacionais na área da investigação qualitativa: o CIAIQ e a WCQR.",
        stats=[("300+", "Publicações"), ("76", "Artigos em revistas"), ("50", "Artigos em conferências"),
               ("44", "Eventos organizados"), ("20+", "Anos de atividade")],
        percurso=[
            ("2026 – presente", "Investigador Doutorado (nível 2), Faculdade de Psicologia e Ciências da Educação, Universidade do Porto", None),
            ("2023 – 2026", "Investigador Doutorado (nível 3), Universidade de Aveiro",
             "Projeto “Collaborative and automated processes for qualitative research in Education” · DOI: 10.54499/CEECINST/00013/2021/CP2779/CT0011"),
            ("2013 – 2026", "Membro integrado e do Conselho Científico, CIDTFF – Universidade de Aveiro",
             "Laboratório de Conteúdos Digitais (LCD), Departamento de Educação e Psicologia"),
            ("2008 – 2026", "Colaborador, LIACC – Faculdade de Engenharia da Universidade do Porto", None),
            ("2004 – presente", "Cofundador, Ludomedia Unipessoal Lda.",
             "Responsável intelectual e pedagógico · Oliveira de Azeméis · www.ludomedia.org"),
            ("2000 – 2006", "Cofundador e Diretor Geral, ArteVirtual",
             "Exploração de Tecnologias de Informação e Comunicação, Oliveira de Azeméis"),
        ],
        formacao=[
            ("2018", "Pós-Doutoramento – Universidade de Aveiro",
             "“Implementação e Avaliação de Instrumentos para Análise Qualitativa na Investigação em Educação” · bolsa SFRH/BPD/104288/2014"),
            ("2012", "Doutoramento em Multimédia em Educação – Universidade de Aveiro",
             "Tese: “Metodologia Híbrida de Desenvolvimento Centrado no Utilizador: aplicada ao Software Educativo”"),
            ("2003", "Curso de Especialização em Multimédia em Educação – Universidade de Aveiro", None),
            ("2002", "Licenciatura em Engenharia da Comunicação (Comunicação e Design) – Universidade Fernando Pessoa", None),
        ],
        formacao_extra="Certificação como Formador pelo Conselho Científico-Pedagógico da Formação Contínua (CCPFC/RFO – 17976/04, desde 2004).",
        areas="Colaboração Humano-IA · Investigação Qualitativa · Métodos Mistos · Análise de Dados Qualitativos · Software webQDA · Métodos Visuais · Design Centrado no Utilizador · Ética e Integridade na Investigação · Tecnologias Educativas",
        areas_p="Participa atualmente em projetos e redes científicas internacionais, entre os quais o Erasmus+ EDUAI, a COST Action CA24121 (Knowledge Graphs in the Era of Large Language Models) e colaborações com a National Academy of Sciences of Ukraine / UNESCO Chair on AI in Education.",
        pubs_intro="Lista completa (300+ trabalhos) disponível no Google Scholar e ORCID.",
        docencia=[
            ("2025/2026", "Universidade de Aveiro",
             "Metodologias de Investigação em Multimédia em Educação · Metodologias de Investigação em Educação (Programas Doutorais)"),
            ("2014 – 2024", "Universidade de Aveiro, Universidade Lusófona do Porto, ISLA, ISVOUGA",
             "Metodologias de Investigação em cursos de mestrado, doutoramento e pós-graduação"),
            ("2001 – 2003", "Instituto Piaget", "Comunicação Educacional Multimédia e Novas Técnicas de Comunicação"),
        ],
        docencia_extra="Desde 2010, coordena a formação em torno do software webQDA, tendo dinamizado dezenas de cursos e workshops em Portugal, Espanha, Brasil, Croácia e Jordânia, entre outros.",
        serv_left_title="Organização de Eventos (seleção)",
        serv_left=[
            "Coorganizador, 9th World Conference on Qualitative Research (WCQR2026), Madrid",
            "Coorganizador, 14º Congresso Ibero-Americano em Investigação Qualitativa, Porto (2025)",
            "Coorganizador, 2º Fórum IA no Espaço Educacional, Universidade de Aveiro (2025)",
            "Coordenador fundador do CIAIQ (14 edições) e da WCQR (9 edições)",
        ],
        serv_right_title="Órgãos e Comissões Científicas",
        serv_right=[
            "Membro do Conselho Científico, CIIE – Universidade do Porto (2026–)",
            "Membro da Comissão Científica, Doutoramento em Educação, ISCED-Huíla, Angola (2025–)",
            "Membro do Conselho Científico, CIDTFF – Universidade de Aveiro (2013–2026)",
            "Membro do Editorial Board, The Qualitative Report (2025–)",
        ],
        premios=[
            "Menção Honrosa, Área de Artes e Humanidades, “Prémio Investigador UA” (2022)",
            "Biannual Book in Spanish or Portuguese, ICQI Award (2016)",
        ],
        footer2="Currículo completo disponível mediante pedido. · Atualizado em 13 de julho de 2026.",
    ),
    "en": dict(
        title="António Pedro Costa — Curriculum Vitae",
        role="Doctoral Researcher · Faculty of Psychology and Educational Sciences, University of Porto · CIDTFF – University of Aveiro · LIACC – University of Porto",
        tagline="Qualitative Research, Mixed Methods and Human-AI Collaboration applied to Education. Co-author of the webQDA software and coordinator of the Ibero-American Congress on Qualitative Research (CIAIQ) and the World Conference on Qualitative Research (WCQR).",
        contact="Oliveira de Azeméis, Portugal  ·  apcosta@fpce.up.pt  ·  apcosta@ludomedia.org  ·  ORCID: 0000-0002-4644-5879  ·  Google Scholar  ·  CiênciaVitae",
        h_sobre="ABOUT", h_percurso="PROFESSIONAL CAREER", h_formacao="ACADEMIC EDUCATION",
        h_investigacao="RESEARCH AREAS", h_publicacoes="SELECTED PUBLICATIONS",
        h_docencia="TEACHING", h_servico="SCIENTIFIC SERVICE", h_premios="AWARDS AND DISTINCTIONS",
        sobre_p1="Doctoral researcher, currently at the Faculty of Psychology and Educational Sciences, University of Porto, with a long-standing link to the Research Centre on Didactics and Technology in the Education of Trainers (CIDTFF – University of Aveiro) and to the Artificial Intelligence and Computer Science Laboratory (LIACC – University of Porto). He has been active in scientific research for over two decades at the intersection of Education, digital technologies and research methodologies, with a recent focus on the critical, ethical and responsible use of artificial intelligence — including large language models — in higher education and scientific research contexts.",
        sobre_p2="PhD in Multimedia in Education from the University of Aveiro, with a postdoctoral fellowship in qualitative research applied to Education and a background in Communication Engineering. He is author and editor of more than 300 scientific publications. He has coordinated, since their creation, two of the leading international events in qualitative research: CIAIQ and WCQR.",
        stats=[("300+", "Publications"), ("76", "Journal articles"), ("50", "Conference papers"),
               ("44", "Events organised"), ("20+", "Years of activity")],
        percurso=[
            ("2026 – present", "Doctoral Researcher (level 2), Faculty of Psychology and Educational Sciences, University of Porto", None),
            ("2023 – 2026", "Doctoral Researcher (level 3), University of Aveiro",
             "Project “Collaborative and automated processes for qualitative research in Education” · DOI: 10.54499/CEECINST/00013/2021/CP2779/CT0011"),
            ("2013 – 2026", "Integrated Member and Scientific Council Member, CIDTFF – University of Aveiro",
             "Digital Content Laboratory (LCD), Department of Education and Psychology"),
            ("2008 – 2026", "Collaborator, LIACC – Faculty of Engineering, University of Porto", None),
            ("2004 – present", "Co-founder, Ludomedia Unipessoal Lda.",
             "Intellectual and pedagogical lead · Oliveira de Azeméis · www.ludomedia.org"),
            ("2000 – 2006", "Co-founder and General Director, ArteVirtual",
             "Information and Communication Technology venture, Oliveira de Azeméis"),
        ],
        formacao=[
            ("2018", "Postdoctoral Fellowship – University of Aveiro",
             "“Implementation and Evaluation of Instruments for Qualitative Analysis in Education Research” · grant SFRH/BPD/104288/2014"),
            ("2012", "PhD in Multimedia in Education – University of Aveiro",
             "Thesis: “Hybrid User-Centred Development Methodology Applied to Educational Software”"),
            ("2003", "Specialisation Course in Multimedia in Education – University of Aveiro", None),
            ("2002", "Bachelor's Degree in Communication Engineering (Communication and Design) – Universidade Fernando Pessoa", None),
        ],
        formacao_extra="Certified Trainer, Scientific-Pedagogical Council for Continuing Education (CCPFC/RFO – 17976/04, since 2004).",
        areas="Human-AI Collaboration · Qualitative Research · Mixed Methods · Qualitative Data Analysis · webQDA Software · Visual Methods · User-Centred Design · Research Ethics and Integrity · Educational Technologies",
        areas_p="Currently involved in international scientific projects and networks, including the Erasmus+ EDUAI project, COST Action CA24121 (Knowledge Graphs in the Era of Large Language Models), and collaborations with the National Academy of Sciences of Ukraine / UNESCO Chair on AI in Education.",
        pubs_intro="Full list (300+ works) available on Google Scholar and ORCID.",
        docencia=[
            ("2025/2026", "University of Aveiro",
             "Research Methodologies in Multimedia in Education · Research Methodologies in Education (Doctoral Programmes)"),
            ("2014 – 2024", "University of Aveiro, Universidade Lusófona do Porto, ISLA, ISVOUGA",
             "Research Methodologies in master's, doctoral and postgraduate programmes"),
            ("2001 – 2003", "Instituto Piaget", "Multimedia Educational Communication and New Communication Techniques"),
        ],
        docencia_extra="Since 2010, he has coordinated training around the webQDA software, having run dozens of courses and workshops in Portugal, Spain, Brazil, Croatia and Jordan, among other countries.",
        serv_left_title="Event Organisation (selection)",
        serv_left=[
            "Co-organiser, 9th World Conference on Qualitative Research (WCQR2026), Madrid",
            "Co-organiser, 14th Ibero-American Congress on Qualitative Research, Porto (2025)",
            "Co-organiser, 2nd AI in Education Forum, University of Aveiro (2025)",
            "Founding coordinator of CIAIQ (14 editions) and WCQR (9 editions)",
        ],
        serv_right_title="Scientific Bodies and Committees",
        serv_right=[
            "Member of the Scientific Council, CIIE – University of Porto (2026–)",
            "Member of the Scientific Committee, PhD in Education, ISCED-Huíla, Angola (2025–)",
            "Member of the Scientific Council, CIDTFF – University of Aveiro (2013–2026)",
            "Member of the Editorial Board, The Qualitative Report (2025–)",
        ],
        premios=[
            "Honourable Mention, Arts and Humanities, “UA Researcher Award” (2022)",
            "Biannual Book in Spanish or Portuguese, ICQI Award (2016)",
        ],
        footer2="Full curriculum vitae available upon request. · Updated July 13, 2026.",
    ),
}

PUBS = [
    "2025 – Costa, A. P., Bryda, G., Christou, P. A., & Kasperiuniene, J. AI as a Co-researcher in the Qualitative Research Workflow. <i>International Journal of Qualitative Methods</i>, 24.",
    "2025 – Costa, A. P., Burneo, P., & Kasperiuniene, J. Mixed-methods & AI for Methodological Literature Reviews. <i>The Qualitative Report</i>, 30(10), 4515–4540.",
    "2025 – Pinho, I., Costa, A. P., & Pinho, C. Generative AI Governance Model in Educational Research. <i>Frontiers in Education</i>, 10.",
    "2024 – Petre, G.-E., & Costa, A. P. Advancing Qualitative Research: Insights from the 7th World Conference on Qualitative Research. <i>Social Sciences</i>, 13(1).",
    "2023 – Bryda, G., & Costa, A. P. Qualitative Research in Digital Era: Innovations, Methodologies and Collaborations. <i>Social Sciences</i>, 12(10), 570.",
    "2023 – Costa, A. P. Qualitative Research Methods: do digital tools open promising trends? <i>Revista Lusófona de Educação</i>, 59(59), 67–76.",
    "2020 – Brandão, C., & Costa, A. P. Reflecting on CAQDAS and Ethics. <i>The Qualitative Report</i>, 25(13), 1–5.",
    "2019 – Costa, A. P., & Moreira, A. Technology ethics in qualitative research: How to be. <i>The Qualitative Report</i>, 24(13).",
    "2019 – Costa, A. P., & Minayo, M. C. de S. Building criteria to evaluate qualitative research papers. <i>Revista da Escola de Enfermagem da USP</i>, 53, 1–7.",
]


def build_pdf(lang, out_path, photo_path=None):
    c = CONTENT[lang]

    name_style = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=20, textColor=INK, spaceAfter=4, leading=24)
    role_style = ParagraphStyle("role", fontName="Helvetica", fontSize=10.5, textColor=INK_SOFT, spaceAfter=8, leading=13)
    tagline_style = ParagraphStyle("tagline", fontName="Helvetica-Oblique", fontSize=9, textColor=INK_SOFT, spaceAfter=8, leading=12)
    contact_style = ParagraphStyle("contact", fontName="Helvetica", fontSize=8.5, textColor=INK_SOFT, spaceAfter=4, leading=12)

    h2_style = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=11, textColor=ACCENT, spaceBefore=16, spaceAfter=8)
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

    def entry(story, period, title, meta=None):
        story.append(Paragraph(period, period_style))
        story.append(Paragraph(title, h3_style))
        if meta:
            story.append(Paragraph(meta, meta_style))
        else:
            story.append(Spacer(1, 6))

    story = []

    header_text = []
    header_text.append(Paragraph("António Pedro Dias da Costa", name_style))
    header_text.append(Paragraph(c["role"], role_style))
    header_text.append(Paragraph(c["tagline"], tagline_style))
    header_text.append(Paragraph(c["contact"], contact_style))

    if photo_path and os.path.exists(photo_path):
        img = Image(photo_path, width=26 * mm, height=26 * mm)
        header_table = Table([[img, header_text]], colWidths=[30 * mm, 155 * mm])
        header_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (0, 0), 0),
            ('RIGHTPADDING', (0, 0), (0, 0), 0),
        ]))
        story.append(header_table)
    else:
        story.extend(header_text)

    story.append(Spacer(1, 4))
    story.append(hr())

    story.append(Paragraph(c["h_sobre"], h2_style))
    story.append(Paragraph(c["sobre_p1"], body_style))
    story.append(Paragraph(c["sobre_p2"], body_style))

    stat_data = [[Paragraph(n, stat_num) for n, _ in c["stats"]],
                 [Paragraph(l, stat_lbl) for _, l in c["stats"]]]
    stat_table = Table(stat_data, colWidths=[95] * 5)
    stat_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(Spacer(1, 4))
    story.append(stat_table)
    story.append(hr())

    story.append(Paragraph(c["h_percurso"], h2_style))
    for period, title, meta in c["percurso"]:
        entry(story, period, title, meta)
    story.append(hr())

    story.append(Paragraph(c["h_formacao"], h2_style))
    for period, title, meta in c["formacao"]:
        entry(story, period, title, meta)
    story.append(Paragraph(c["formacao_extra"], meta_style))
    story.append(hr())

    story.append(Paragraph(c["h_investigacao"], h2_style))
    story.append(Paragraph(c["areas"], body_style))
    story.append(Paragraph(c["areas_p"], body_style))
    story.append(hr())

    story.append(Paragraph(c["h_publicacoes"], h2_style))
    story.append(Paragraph(c["pubs_intro"], meta_style))
    for p in PUBS:
        story.append(Paragraph(p, pub_style))
    story.append(hr())

    story.append(Paragraph(c["h_docencia"], h2_style))
    for period, title, meta in c["docencia"]:
        entry(story, period, title, meta)
    story.append(Paragraph(c["docencia_extra"], body_style))
    story.append(hr())

    story.append(Paragraph(c["h_servico"], h2_style))
    left_flow = [Paragraph(c["serv_left_title"], h3_style), Spacer(1, 4)]
    left_flow.append(ListFlowable([ListItem(Paragraph(t, li_style)) for t in c["serv_left"]],
                                   bulletType='bullet', start='-', leftIndent=10))
    right_flow = [Paragraph(c["serv_right_title"], h3_style), Spacer(1, 4)]
    right_flow.append(ListFlowable([ListItem(Paragraph(t, li_style)) for t in c["serv_right"]],
                                    bulletType='bullet', start='-', leftIndent=10))
    serv_table = Table([[left_flow, right_flow]], colWidths=[255, 255])
    serv_table.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP')]))
    story.append(serv_table)
    story.append(hr())

    story.append(Paragraph(c["h_premios"], h2_style))
    for p in c["premios"]:
        story.append(Paragraph("· " + p, li_style))

    doc = SimpleDocTemplate(
        out_path,
        pagesize=A4,
        leftMargin=20 * mm, rightMargin=20 * mm, topMargin=16 * mm, bottomMargin=16 * mm,
        title=c["title"]
    )
    doc.build(story)
    print("PDF gerado:", out_path)


if __name__ == "__main__":
    photo = None
    if os.path.exists(PHOTO_SRC):
        make_circle_photo(PHOTO_SRC, PHOTO_CIRCLE)
        photo = PHOTO_CIRCLE
    build_pdf("pt", os.path.join(OUTDIR, "Antonio_Pedro_Costa_CV_PT.pdf"), photo)
    build_pdf("en", os.path.join(OUTDIR, "Antonio_Pedro_Costa_CV_EN.pdf"), photo)
