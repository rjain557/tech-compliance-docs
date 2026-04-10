"""
AFFG IT Compliance & Security Strategy — Multi-Page Branded PDF
Design: White-background professional consulting report with Technijian branding
"""

import os
import math
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, Color, white, black
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.utils import ImageReader

# ─── Brand Colors ───────────────────────────────────────────
BLUE = HexColor("#006DB6")
BLUE_DARK = HexColor("#004D80")
BLUE_LIGHT = HexColor("#E6F0FA")
BLUE_LIGHTER = HexColor("#F0F6FC")
ORANGE = HexColor("#F67D4B")
ORANGE_LIGHT = HexColor("#FEF0EB")
TEAL = HexColor("#1EAAC8")
TEAL_LIGHT = HexColor("#E8F7FA")
CHARTREUSE = HexColor("#CBDB2D")
DARK = HexColor("#1A1A2E")
DARK_TEXT = HexColor("#2D3748")
BODY_TEXT = HexColor("#4A5568")
LIGHT_TEXT = HexColor("#718096")
BORDER = HexColor("#E2E8F0")
LIGHT_BG = HexColor("#F7FAFC")
WHITE = white
BLACK = black
RISK_CRITICAL = HexColor("#DC2626")
RISK_CRITICAL_BG = HexColor("#FEF2F2")
RISK_HIGH = HexColor("#EA580C")
RISK_HIGH_BG = HexColor("#FFF7ED")
RISK_MEDIUM = HexColor("#CA8A04")
RISK_MEDIUM_BG = HexColor("#FEFCE8")

W, H = letter  # 612 x 792
MARGIN = 54  # 0.75 inch
CONTENT_W = W - 2 * MARGIN

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "AFFG_IT_Compliance_Strategy.pdf")

# Logo path
LOGO_PATH = r"C:\Users\rjain\OneDrive - Technijian, Inc\Documents - Technijian-SEO Marketing\Logos\Technijian Logo 2.png"


def draw_accent_line(c, x, y, w, h=2.5):
    """Draw the orange-to-teal gradient accent line."""
    steps = 80
    for i in range(steps):
        t = i / float(steps)
        r = ORANGE.red + t * (TEAL.red - ORANGE.red)
        g = ORANGE.green + t * (TEAL.green - ORANGE.green)
        b = ORANGE.blue + t * (TEAL.blue - ORANGE.blue)
        c.setFillColor(Color(r, g, b))
        strip_w = w / steps
        c.rect(x + i * strip_w, y, strip_w + 0.5, h, fill=1, stroke=0)


def draw_blue_bar(c, x, y, w, h=2):
    """Draw a thin blue rule."""
    c.setFillColor(BLUE)
    c.rect(x, y, w, h, fill=1, stroke=0)


def draw_section_header(c, y, title, number=None):
    """Draw a section header — blue left bar + title."""
    # Blue accent bar on left
    c.setFillColor(BLUE)
    c.rect(MARGIN, y - 1, 3, 14, fill=1, stroke=0)

    c.setFillColor(BLUE)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(MARGIN + 12, y, title.upper())

    # Thin rule below
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.5)
    c.line(MARGIN, y - 6, W - MARGIN, y - 6)
    return y - 14


def draw_page_footer(c, page_num, total_pages):
    """Draw footer with page number and branding."""
    # Top border line
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.5)
    c.line(MARGIN, 36, W - MARGIN, 36)

    c.setFillColor(LIGHT_TEXT)
    c.setFont("Helvetica", 6)
    c.drawString(MARGIN, 24, "CONFIDENTIAL — American Fundstars Financial Group LLC")
    c.drawCentredString(W / 2, 24, "Technijian  ·  technology as a solution")
    c.drawRightString(W - MARGIN, 24, f"{page_num} / {total_pages}")


def draw_logo(c, x, y, width=140):
    """Draw the Technijian logo from PNG file."""
    try:
        logo = ImageReader(LOGO_PATH)
        iw, ih = logo.getSize()
        aspect = ih / iw
        c.drawImage(logo, x, y, width=width, height=width * aspect, mask='auto')
        return width * aspect
    except Exception as e:
        # Fallback: text wordmark
        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica-Bold", 14)
        c.drawString(x, y + 4, "TECHNIJIAN")
        c.setFillColor(TEAL)
        c.setFont("Helvetica", 7)
        tw = pdfmetrics.stringWidth("TECHNIJIAN", "Helvetica-Bold", 14)
        c.drawString(x + tw + 6, y + 4, "technology as a solution")
        return 20


def wrap_text(text, font_name, font_size, max_width):
    """Simple word-wrap returning list of lines."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip()
        tw = pdfmetrics.stringWidth(test, font_name, font_size)
        if tw > max_width and current:
            lines.append(current)
            current = word
        else:
            current = test
    if current:
        lines.append(current)
    return lines


# ═══════════════════════════════════════════════════════════════
# PAGE 1: COVER
# ═══════════════════════════════════════════════════════════════
def page_cover(c):
    # White background (default)

    # Top dark band
    c.setFillColor(DARK)
    c.rect(0, H - 100, W, 100, fill=1, stroke=0)

    # Logo on dark band
    draw_logo_white(c, MARGIN, H - 75, width=160)

    # CONFIDENTIAL badge on dark band
    c.setFillColor(Color(0.96, 0.49, 0.29, 0.3))
    c.roundRect(W - MARGIN - 90, H - 72, 90, 20, 3, fill=1, stroke=0)
    c.setFillColor(ORANGE)
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(W - MARGIN - 45, H - 66, "CONFIDENTIAL")

    # Accent line below dark band
    draw_accent_line(c, 0, H - 103, W, 3)

    # Main title area
    title_y = H / 2 + 100

    c.setFillColor(DARK_TEXT)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(W / 2, title_y, "IT Compliance &")
    c.drawCentredString(W / 2, title_y - 36, "Security Strategy")

    # Subtitle
    c.setFillColor(BLUE)
    c.setFont("Helvetica", 10)
    c.drawCentredString(W / 2, title_y - 64, "Cloud Access Control  ·  VDI Architecture  ·  Regulatory Alignment")

    # Thin rule
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.5)
    c.line(MARGIN + 80, title_y - 80, W - MARGIN - 80, title_y - 80)

    # Regulatory badges
    badge_y = title_y - 112
    badges = [
        ("SEC Reg S-P", BLUE, BLUE_LIGHT),
        ("FINRA 4370", TEAL, TEAL_LIGHT),
        ("FINRA 3110", TEAL, TEAL_LIGHT),
        ("SEC 17a-4", BLUE, BLUE_LIGHT),
    ]
    badge_w = 108
    total_w = len(badges) * badge_w + (len(badges) - 1) * 10
    start_x = (W - total_w) / 2

    for i, (text, text_color, bg_color) in enumerate(badges):
        bx = start_x + i * (badge_w + 10)
        c.setFillColor(bg_color)
        c.roundRect(bx, badge_y, badge_w, 24, 4, fill=1, stroke=0)
        c.setStrokeColor(text_color)
        c.setLineWidth(0.5)
        c.roundRect(bx, badge_y, badge_w, 24, 4, fill=0, stroke=1)
        c.setFillColor(text_color)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawCentredString(bx + badge_w / 2, badge_y + 8, text)

    # Client info
    info_y = badge_y - 60
    c.setFillColor(LIGHT_TEXT)
    c.setFont("Helvetica", 7.5)
    c.drawCentredString(W / 2, info_y + 20, "PREPARED FOR")
    c.setFillColor(DARK_TEXT)
    c.setFont("Helvetica-Bold", 15)
    c.drawCentredString(W / 2, info_y, "American Fundstars Financial Group LLC")
    c.setFillColor(BODY_TEXT)
    c.setFont("Helvetica", 9)
    c.drawCentredString(W / 2, info_y - 18, "Dually Registered RIA / Broker-Dealer")

    # Bottom section
    # Logo (full color) centered near bottom
    logo_w = 150
    try:
        logo = ImageReader(LOGO_PATH)
        iw, ih = logo.getSize()
        aspect = ih / iw
        logo_h = logo_w * aspect
        c.drawImage(logo, (W - logo_w) / 2, 110, width=logo_w, height=logo_h, mask='auto')
    except:
        pass

    c.setFillColor(LIGHT_TEXT)
    c.setFont("Helvetica", 7.5)
    c.drawCentredString(W / 2, 95, "April 2026  ·  Irvine, California")

    # Bottom accent line
    draw_accent_line(c, MARGIN, 72, CONTENT_W, 2)

    # Reference number
    c.setFillColor(BORDER)
    c.setFont("Helvetica", 5.5)
    c.drawString(MARGIN, 60, "REF: AFFG-CS-2026-04")
    c.drawRightString(W - MARGIN, 60, "REV 1.0")


def draw_logo_white(c, x, y, width=160):
    """Draw white-text logo on dark background. Falls back to text."""
    white_logo = r"C:\Users\rjain\OneDrive - Technijian, Inc\Documents - Technijian-SEO Marketing\Logos\Technijian Logo - white text.png"
    try:
        logo = ImageReader(white_logo)
        iw, ih = logo.getSize()
        aspect = ih / iw
        c.drawImage(logo, x, y, width=width, height=width * aspect, mask='auto')
    except:
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 14)
        c.drawString(x, y + 4, "TECHNIJIAN")
        c.setFillColor(TEAL)
        c.setFont("Helvetica", 7)
        tw = pdfmetrics.stringWidth("TECHNIJIAN", "Helvetica-Bold", 14)
        c.drawString(x + tw + 6, y + 4, "technology as a solution")


# ═══════════════════════════════════════════════════════════════
# PAGE 2: EXECUTIVE SUMMARY
# ═══════════════════════════════════════════════════════════════
def page_executive_summary(c):
    draw_page_header(c, "Executive Summary", "01")
    draw_page_footer(c, 2, 9)

    y = H - 115

    # Key finding callout
    c.setFillColor(BLUE_LIGHT)
    c.roundRect(MARGIN, y - 52, CONTENT_W, 56, 4, fill=1, stroke=0)
    c.setStrokeColor(BLUE)
    c.setLineWidth(1)
    c.line(MARGIN + 3, y - 52, MARGIN + 3, y + 4)
    c.setFillColor(ORANGE)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(MARGIN + 14, y - 8, "KEY FINDING")
    c.setFillColor(DARK_TEXT)
    c.setFont("Helvetica", 8.5)
    c.drawString(MARGIN + 14, y - 23, "VDI alone addresses approximately 40% of compliance requirements. The full Technijian")
    c.drawString(MARGIN + 14, y - 35, "stack (VDI + My Archive + V365 Backup + My Audit + Huntress SAT + policies) achieves 100%.")
    y -= 72

    # Body text
    c.setFillColor(BODY_TEXT)
    c.setFont("Helvetica", 9)
    line_h = 14
    para = 'American Fundstars Financial Group LLC ("AFFG") is a dually registered investment adviser (RIA) and broker-dealer regulated by the Securities and Exchange Commission (SEC) and the Financial Industry Regulatory Authority (FINRA).'
    lines = wrap_text(para, "Helvetica", 9, CONTENT_W - 10)
    for line in lines:
        c.drawString(MARGIN, y, line)
        y -= line_h
    y -= 6

    c.drawString(MARGIN, y, "The firm currently operates with the following technology infrastructure:")
    y -= 20

    # Current systems
    systems = [
        ("Charles Schwab Advisor Services", "advisorservices.schwab.com", BLUE),
        ("Interactive Brokers", "ndcdyn.interactivebrokers.com", BLUE),
        ("Microsoft 365 & OneDrive", "File storage and collaboration", TEAL),
        ("Personal Laptops", "Unmanaged endpoints for daily operations", ORANGE),
    ]
    for name, desc, accent in systems:
        c.setFillColor(accent)
        c.circle(MARGIN + 12, y + 3.5, 3, fill=1, stroke=0)
        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(MARGIN + 22, y, name)
        c.setFillColor(LIGHT_TEXT)
        c.setFont("Helvetica", 7.5)
        c.drawString(MARGIN + 22, y - 12, desc)
        y -= 28

    y -= 8
    c.setFillColor(BODY_TEXT)
    c.setFont("Helvetica", 9)
    overview = "This strategy document outlines a comprehensive compliance approach that goes beyond VDI alone to achieve full regulatory alignment with SEC Reg S-P (2024 Amendments), FINRA Rule 4370, and FINRA Rule 3110. The approach follows a six-pillar framework addressing infrastructure, access control, data protection, archiving, identity management, and continuous monitoring."
    lines = wrap_text(overview, "Helvetica", 9, CONTENT_W - 10)
    for line in lines:
        c.drawString(MARGIN, y, line)
        y -= line_h
    y -= 20

    # Compliance posture projection
    y = draw_section_header(c, y, "COMPLIANCE POSTURE PROJECTION")
    y -= 16

    card_w = (CONTENT_W - 20) / 2

    # Current state card
    cx = MARGIN
    c.setFillColor(RISK_CRITICAL_BG)
    c.roundRect(cx, y - 85, card_w, 88, 5, fill=1, stroke=0)
    c.setStrokeColor(RISK_CRITICAL)
    c.setLineWidth(0.5)
    c.roundRect(cx, y - 85, card_w, 88, 5, fill=0, stroke=1)
    # Orange top bar
    c.setFillColor(ORANGE)
    c.rect(cx + 1, y - 1, card_w - 2, 4, fill=1, stroke=0)
    c.setFillColor(LIGHT_TEXT)
    c.setFont("Helvetica-Bold", 7)
    c.drawString(cx + 14, y - 16, "CURRENT STATE")
    c.setFillColor(RISK_CRITICAL)
    c.setFont("Helvetica-Bold", 34)
    c.drawString(cx + 14, y - 52, "~15%")
    c.setFillColor(BODY_TEXT)
    c.setFont("Helvetica", 7.5)
    c.drawString(cx + 14, y - 68, "Personal laptops · No DLP · No archive or audit")

    # Target state card
    cx = MARGIN + card_w + 20
    c.setFillColor(TEAL_LIGHT)
    c.roundRect(cx, y - 85, card_w, 88, 5, fill=1, stroke=0)
    c.setStrokeColor(TEAL)
    c.setLineWidth(0.5)
    c.roundRect(cx, y - 85, card_w, 88, 5, fill=0, stroke=1)
    c.setFillColor(TEAL)
    c.rect(cx + 1, y - 1, card_w - 2, 4, fill=1, stroke=0)
    c.setFillColor(LIGHT_TEXT)
    c.setFont("Helvetica-Bold", 7)
    c.drawString(cx + 14, y - 16, "POST-IMPLEMENTATION")
    c.setFillColor(TEAL)
    c.setFont("Helvetica-Bold", 34)
    c.drawString(cx + 14, y - 52, "100%")
    c.setFillColor(BODY_TEXT)
    c.setFont("Helvetica", 7.5)
    c.drawString(cx + 14, y - 68, "Full Technijian stack + policies · Exam-ready")


def draw_page_header(c, title, number):
    """Standard page header: logo + accent line + page title."""
    # Logo top left
    try:
        logo = ImageReader(LOGO_PATH)
        iw, ih = logo.getSize()
        aspect = ih / iw
        c.drawImage(logo, MARGIN, H - 42, width=100, height=100 * aspect, mask='auto')
    except:
        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(MARGIN, H - 34, "TECHNIJIAN")

    # Accent line
    draw_accent_line(c, MARGIN, H - 52, CONTENT_W, 2)

    # Page number + title
    y = H - 80
    c.setFillColor(BLUE)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(MARGIN, y + 5, number)
    c.setFillColor(DARK_TEXT)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(MARGIN + 22, y, title)
    return y


# ═══════════════════════════════════════════════════════════════
# PAGE 3: CURRENT STATE ASSESSMENT
# ═══════════════════════════════════════════════════════════════
def page_current_state(c):
    draw_page_header(c, "Current State Assessment", "02")
    draw_page_footer(c, 3, 9)

    y = H - 100
    c.setFillColor(LIGHT_TEXT)
    c.setFont("Helvetica", 8)
    c.drawString(MARGIN + 22, y, "Risk analysis of existing infrastructure against regulatory requirements")
    y -= 24

    risks = [
        ("Device Management", "Personal laptops, no MDM enrollment", "CRITICAL"),
        ("Access Control", "No IP restrictions on Schwab / IBKR portals", "HIGH"),
        ("Data Loss Prevention", "No DLP policies configured in M365", "CRITICAL"),
        ("Email Archiving", "No WORM-compliant archive (SEC 17a-4)", "CRITICAL"),
        ("Multi-Factor Auth", "Partial — platform-dependent, not enforced", "HIGH"),
        ("Audit Logging", "Minimal — no unified log or 7-year retention", "HIGH"),
        ("Endpoint Protection", "Inconsistent across personal devices", "HIGH"),
        ("Communications Capture", "No Teams/email retention for FINRA 3110", "CRITICAL"),
        ("Clipboard / Print Controls", "No isolation between VDI and local device", "HIGH"),
        ("Supervisory Continuity", "No alternate supervisor procedures documented", "MEDIUM"),
    ]

    # Table header
    col_x = [MARGIN, MARGIN + 165, MARGIN + 385]
    c.setFillColor(BLUE)
    c.rect(MARGIN, y - 16, CONTENT_W, 20, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 6.5)
    c.drawString(col_x[0] + 8, y - 10, "RISK AREA")
    c.drawString(col_x[1] + 8, y - 10, "CURRENT STATE")
    c.drawString(col_x[2] + 8, y - 10, "RISK LEVEL")
    y -= 20

    row_h = 26
    for idx, (area, state, level) in enumerate(risks):
        ry = y - row_h
        # Alternating row
        if idx % 2 == 0:
            c.setFillColor(LIGHT_BG)
        else:
            c.setFillColor(WHITE)
        c.rect(MARGIN, ry, CONTENT_W, row_h, fill=1, stroke=0)

        # Border bottom
        c.setStrokeColor(BORDER)
        c.setLineWidth(0.3)
        c.line(MARGIN, ry, W - MARGIN, ry)

        # Risk area
        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(col_x[0] + 8, ry + 9, area)

        # Current state
        c.setFillColor(BODY_TEXT)
        c.setFont("Helvetica", 7.5)
        state_lines = wrap_text(state, "Helvetica", 7.5, 210)
        for li, sl in enumerate(state_lines[:2]):
            c.drawString(col_x[1] + 8, ry + 9 - li * 9, sl)

        # Risk badge
        if level == "CRITICAL":
            badge_color, badge_bg = RISK_CRITICAL, RISK_CRITICAL_BG
        elif level == "HIGH":
            badge_color, badge_bg = RISK_HIGH, RISK_HIGH_BG
        else:
            badge_color, badge_bg = RISK_MEDIUM, RISK_MEDIUM_BG

        bw = pdfmetrics.stringWidth(level, "Helvetica-Bold", 7) + 14
        bx = col_x[2] + 8
        c.setFillColor(badge_bg)
        c.roundRect(bx, ry + 5, bw, 16, 3, fill=1, stroke=0)
        c.setFillColor(badge_color)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(bx + 7, ry + 9, level)
        y -= row_h

    y -= 18

    # Risk distribution
    y = draw_section_header(c, y, "RISK DISTRIBUTION")
    y -= 14

    counts = [("CRITICAL", 4, RISK_CRITICAL, RISK_CRITICAL_BG), ("HIGH", 5, RISK_HIGH, RISK_HIGH_BG), ("MEDIUM", 1, RISK_MEDIUM, RISK_MEDIUM_BG)]
    total_count = 10
    bar_w = CONTENT_W - 90

    for label, count, color, bg in counts:
        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(MARGIN + 5, y, label)
        bar_x = MARGIN + 65
        c.setFillColor(bg)
        c.roundRect(bar_x, y - 3, bar_w, 12, 2, fill=1, stroke=0)
        fill_w = (count / total_count) * bar_w
        c.setFillColor(color)
        c.roundRect(bar_x, y - 3, fill_w, 12, 2, fill=1, stroke=0)
        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(bar_x + fill_w + 6, y, str(count))
        y -= 20

    y -= 10

    # Overall score box
    c.setFillColor(RISK_CRITICAL_BG)
    c.roundRect(MARGIN, y - 46, CONTENT_W, 50, 5, fill=1, stroke=0)
    c.setStrokeColor(RISK_CRITICAL)
    c.setLineWidth(0.7)
    c.roundRect(MARGIN, y - 46, CONTENT_W, 50, 5, fill=0, stroke=1)
    c.setFillColor(LIGHT_TEXT)
    c.setFont("Helvetica-Bold", 7)
    c.drawString(MARGIN + 14, y - 10, "OVERALL CURRENT COMPLIANCE SCORE")
    c.setFillColor(RISK_CRITICAL)
    c.setFont("Helvetica-Bold", 26)
    c.drawString(MARGIN + 14, y - 36, "~15%")
    c.setFillColor(BODY_TEXT)
    c.setFont("Helvetica", 8)
    c.drawString(MARGIN + 90, y - 32, "Significant regulatory exposure requiring immediate remediation")


# ═══════════════════════════════════════════════════════════════
# PAGE 4: VDI ARCHITECTURE RECOMMENDATION
# ═══════════════════════════════════════════════════════════════
def page_vdi_recommendation(c):
    draw_page_header(c, "VDI Architecture Recommendation", "03")
    draw_page_footer(c, 4, 9)

    y = H - 100
    c.setFillColor(LIGHT_TEXT)
    c.setFont("Helvetica", 8)
    c.drawString(MARGIN + 22, y, "Isolated Windows 11 VDI vs. shared RDS sessions — compliance-driven analysis")
    y -= 28

    # Recommendation callout
    c.setFillColor(TEAL_LIGHT)
    c.roundRect(MARGIN, y - 44, CONTENT_W, 48, 4, fill=1, stroke=0)
    c.setStrokeColor(TEAL)
    c.setLineWidth(1)
    c.line(MARGIN + 3, y - 44, MARGIN + 3, y + 4)
    c.setFillColor(TEAL)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(MARGIN + 14, y - 6, "RECOMMENDATION")
    c.setFillColor(DARK_TEXT)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(MARGIN + 14, y - 20, "Azure Virtual Desktop (AVD) with Windows 11 Enterprise personal desktops.")
    c.setFillColor(BODY_TEXT)
    c.setFont("Helvetica", 8)
    c.drawString(MARGIN + 14, y - 34, "Each user receives a dedicated, isolated VM — the strongest compliance posture for a regulated firm.")
    y -= 62

    # Comparison table
    y = draw_section_header(c, y, "ARCHITECTURE COMPARISON")
    y -= 10

    # Table headers
    col_x = [MARGIN, MARGIN + 150, MARGIN + 330]
    col_w = [150, 180, CONTENT_W - 330]

    c.setFillColor(BLUE)
    c.rect(MARGIN, y - 16, CONTENT_W, 20, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 6.5)
    c.drawString(col_x[0] + 8, y - 10, "FACTOR")
    c.drawString(col_x[1] + 8, y - 10, "WINDOWS 11 VDI (PERSONAL)")
    c.drawString(col_x[2] + 8, y - 10, "RDS SHARED SESSIONS")
    y -= 20

    comparisons = [
        ("User Isolation", "Complete — separate VM per user", "Session-based — same OS kernel"),
        ("Cross-User Data Risk", "Zero — no shared resources", "Non-zero — shared memory, temp files"),
        ("FINRA 3110 Accountability", "Clean — 1 user = 1 machine = 1 audit trail", "Muddier — must prove session isolation"),
        ("My Audit Attribution", "1 agent per VM, clean per-user capture", "Session disambiguation required"),
        ("Blast Radius if Compromised", "One user's VM only", "Entire server + all active sessions"),
        ("DLP Granularity", "Per-user, per-VM policies", "Per-session — harder to differentiate"),
        ("App Compatibility", "Full Win 11 — Schwab & IBKR native", "Some financial apps have issues"),
        ("Examiner Optics", "Simple: \"each user has own desktop\"", "Invites follow-up questions"),
        ("Cost per User", "Higher (~$30–50/mo more)", "Lower (10–15 users per server)"),
    ]

    row_h = 24
    for idx, (factor, win11, rds) in enumerate(comparisons):
        ry = y - row_h
        if idx % 2 == 0:
            c.setFillColor(LIGHT_BG)
        else:
            c.setFillColor(WHITE)
        c.rect(MARGIN, ry, CONTENT_W, row_h, fill=1, stroke=0)
        c.setStrokeColor(BORDER)
        c.setLineWidth(0.2)
        c.line(MARGIN, ry, W - MARGIN, ry)

        # Factor
        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(col_x[0] + 8, ry + 9, factor)

        # Win 11 column (green tint for recommended)
        c.setFillColor(HexColor("#047857"))
        c.setFont("Helvetica", 6.5)
        # Wrap text
        lines = wrap_text(win11, "Helvetica", 6.5, col_w[1] - 16)
        for li, sl in enumerate(lines[:2]):
            c.drawString(col_x[1] + 8, ry + 9 - li * 8, sl)

        # RDS column
        c.setFillColor(BODY_TEXT)
        c.setFont("Helvetica", 6.5)
        lines = wrap_text(rds, "Helvetica", 6.5, col_w[2] - 16)
        for li, sl in enumerate(lines[:2]):
            c.drawString(col_x[2] + 8, ry + 9 - li * 8, sl)

        y -= row_h

    y -= 18

    # Why it matters section
    y = draw_section_header(c, y, "WHY THIS MATTERS FOR AFFG")
    y -= 12

    reasons = [
        ("FINRA 3110 — Individual Accountability", "Examiners want each associated person's activity attributable to them and only them. A dedicated VM makes this trivially provable. With RDS, you must explain session isolation to a non-technical examiner — unnecessary risk during an examination.", BLUE),
        ("SEC Reg S-P — Data Safeguards", "The 2024 amendments require preventing unauthorized access to customer information. On a shared RDS server, a privilege escalation in one session theoretically exposes all sessions. Isolated VMs contain the attack surface to a single user.", TEAL),
        ("Technijian My Audit — Clean Attribution", "Screen recording, keystroke logging, and application monitoring are cleanest on a dedicated desktop. In RDS multi-session, My Audit must disambiguate sessions — adding complexity that can create gaps in audit evidence.", ORANGE),
        ("Schwab & IBKR Compatibility", "Schwab Advisor Services and Interactive Brokers TWS assume a standard Windows desktop. Financial applications have known issues with Windows Server multi-session environments, particularly around certificate stores and browser sessions.", BLUE),
    ]

    for title, desc, accent in reasons:
        # Accent bar
        c.setFillColor(accent)
        c.rect(MARGIN + 4, y - 1, 3, 12, fill=1, stroke=0)
        # Title
        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(MARGIN + 14, y, title)
        # Description
        c.setFillColor(BODY_TEXT)
        c.setFont("Helvetica", 7)
        lines = wrap_text(desc, "Helvetica", 7, CONTENT_W - 20)
        for li, sl in enumerate(lines[:3]):
            c.drawString(MARGIN + 14, y - 12 - li * 10, sl)
        y -= 14 + len(lines[:3]) * 10 + 6


# ═══════════════════════════════════════════════════════════════
# PAGE 5: RECOMMENDED ARCHITECTURE
# ═══════════════════════════════════════════════════════════════
def page_architecture(c):
    draw_page_header(c, "Recommended Architecture", "04")
    draw_page_footer(c, 5, 9)

    y = H - 100
    c.setFillColor(LIGHT_TEXT)
    c.setFont("Helvetica", 8)
    c.drawString(MARGIN + 22, y, "Layered security architecture — no client data touches the personal device")
    y -= 30

    # ── ENDPOINT LAYER ──
    layer_h = 46
    c.setFillColor(ORANGE_LIGHT)
    c.roundRect(MARGIN, y - layer_h, CONTENT_W, layer_h, 4, fill=1, stroke=0)
    c.setStrokeColor(ORANGE)
    c.setLineWidth(0.5)
    c.roundRect(MARGIN, y - layer_h, CONTENT_W, layer_h, 4, fill=0, stroke=1)
    c.setFillColor(LIGHT_TEXT)
    c.setFont("Helvetica-Bold", 6)
    c.drawString(MARGIN + 10, y - 12, "ENDPOINT LAYER")
    # Personal Laptop box
    bw, bh = 170, 24
    bx = (W - bw) / 2
    by = y - layer_h + 6
    c.setFillColor(WHITE)
    c.roundRect(bx, by, bw, bh, 3, fill=1, stroke=0)
    c.setStrokeColor(ORANGE)
    c.setLineWidth(0.5)
    c.roundRect(bx, by, bw, bh, 3, fill=0, stroke=1)
    c.setFillColor(DARK_TEXT)
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(W / 2, by + 9, "Personal Laptop")
    c.setFillColor(ORANGE)
    c.setFont("Helvetica", 5.5)
    c.drawCentredString(W / 2, by + 1, "Thin client only — no data stored")

    # Arrow down
    arrow_x = W / 2
    arr_top = y - layer_h
    arr_bot = arr_top - 20
    c.setStrokeColor(BLUE)
    c.setLineWidth(1.2)
    c.setDash(4, 3)
    c.line(arrow_x, arr_top, arrow_x, arr_bot + 4)
    c.setDash()
    # Arrowhead
    c.setFillColor(BLUE)
    p = c.beginPath()
    p.moveTo(arrow_x, arr_bot)
    p.lineTo(arrow_x - 4, arr_bot + 7)
    p.lineTo(arrow_x + 4, arr_bot + 7)
    p.close()
    c.drawPath(p, fill=1, stroke=0)

    y = arr_bot - 4

    # ── VDI SECURITY BOUNDARY ──
    vdi_h = 175
    vdi_y = y - vdi_h

    c.setFillColor(BLUE_LIGHTER)
    c.roundRect(MARGIN, vdi_y, CONTENT_W, vdi_h, 6, fill=1, stroke=0)
    c.setStrokeColor(BLUE)
    c.setLineWidth(1)
    c.setDash(6, 3)
    c.roundRect(MARGIN, vdi_y, CONTENT_W, vdi_h, 6, fill=0, stroke=1)
    c.setDash()

    c.setFillColor(BLUE)
    c.setFont("Helvetica-Bold", 6.5)
    c.drawString(MARGIN + 10, vdi_y + vdi_h - 14, "TECHNIJIAN VDI ENVIRONMENT — SECURITY BOUNDARY")

    # VDI central box
    vdi_bw, vdi_bh = 160, 30
    vdi_bx = (W - vdi_bw) / 2
    vdi_by = vdi_y + vdi_h - 48
    c.setFillColor(BLUE)
    c.roundRect(vdi_bx, vdi_by, vdi_bw, vdi_bh, 4, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(W / 2, vdi_by + 12, "Technijian VDI")
    c.setFont("Helvetica", 5.5)
    c.drawCentredString(W / 2, vdi_by + 3, "AVD · Windows 11 · Personal Desktops")

    # Service boxes
    services = [
        ("Microsoft 365 /\nOneDrive", "Entra Conditional\nAccess: VDI-only", TEAL, TEAL_LIGHT),
        ("Schwab Advisor\nServices", "IP allowlisted to\nVDI egress", BLUE, BLUE_LIGHT),
        ("Interactive\nBrokers", "IP allowlisted to\nVDI egress", BLUE, BLUE_LIGHT),
    ]
    svc_w = (CONTENT_W - 60) / 3
    svc_h = 42
    svc_y = vdi_by - 56
    svc_start_x = MARGIN + 15

    for i, (name, desc, accent, bg) in enumerate(services):
        sx = svc_start_x + i * (svc_w + 10)
        c.setFillColor(WHITE)
        c.roundRect(sx, svc_y, svc_w, svc_h, 3, fill=1, stroke=0)
        c.setStrokeColor(accent)
        c.setLineWidth(0.5)
        c.roundRect(sx, svc_y, svc_w, svc_h, 3, fill=0, stroke=1)
        # Top accent
        c.setFillColor(accent)
        c.rect(sx + 1, svc_y + svc_h - 3, svc_w - 2, 3, fill=1, stroke=0)
        # Name
        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica-Bold", 7)
        for li, nl in enumerate(name.split("\n")):
            c.drawCentredString(sx + svc_w / 2, svc_y + svc_h - 16 - li * 9, nl)
        # Desc
        c.setFillColor(LIGHT_TEXT)
        c.setFont("Helvetica", 5.5)
        for li, dl in enumerate(desc.split("\n")):
            c.drawCentredString(sx + svc_w / 2, svc_y + 8 - li * 7, dl)
        # Connector
        c.setStrokeColor(BORDER)
        c.setLineWidth(0.5)
        c.line(sx + svc_w / 2, vdi_by, sx + svc_w / 2, svc_y + svc_h)

    # Support systems row
    support = [
        ("Technijian My Archive", "Email Archiving", ORANGE, ORANGE_LIGHT),
        ("Technijian V365 Backup", "M365 Backup & Retention", ORANGE, ORANGE_LIGHT),
        ("Technijian My Audit", "User Monitoring & Audit", TEAL, TEAL_LIGHT),
    ]
    sup_y = svc_y - 44
    for i, (name, desc, accent, bg) in enumerate(support):
        sx = svc_start_x + i * (svc_w + 10)
        c.setFillColor(bg)
        c.roundRect(sx, sup_y, svc_w, 34, 3, fill=1, stroke=0)
        c.setStrokeColor(accent)
        c.setLineWidth(0.4)
        c.roundRect(sx, sup_y, svc_w, 34, 3, fill=0, stroke=1)
        c.setFillColor(accent)
        c.rect(sx + 1, sup_y + 31, svc_w - 2, 3, fill=1, stroke=0)
        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica-Bold", 7)
        c.drawCentredString(sx + svc_w / 2, sup_y + 17, name)
        c.setFillColor(LIGHT_TEXT)
        c.setFont("Helvetica", 5.5)
        c.drawCentredString(sx + svc_w / 2, sup_y + 6, desc)
        # Dashed connector
        c.setStrokeColor(BORDER)
        c.setLineWidth(0.3)
        c.setDash(2, 2)
        c.line(sx + svc_w / 2, svc_y, sx + svc_w / 2, sup_y + 34)
        c.setDash()

    y = sup_y - 24

    # Core principle callout
    c.setFillColor(TEAL_LIGHT)
    c.roundRect(MARGIN, y - 36, CONTENT_W, 40, 4, fill=1, stroke=0)
    c.setStrokeColor(TEAL)
    c.setLineWidth(0.7)
    c.line(MARGIN + 3, y - 36, MARGIN + 3, y + 4)
    c.setFillColor(TEAL)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(MARGIN + 14, y - 8, "CORE DESIGN PRINCIPLE")
    c.setFillColor(DARK_TEXT)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(MARGIN + 14, y - 23, "No client data touches the personal device. The VDI is the security boundary.")

    y -= 54

    # VDI Session Controls
    y = draw_section_header(c, y, "VDI SESSION CONTROLS")
    y -= 12

    controls = [
        "Clipboard redirection — disabled",
        "Local drive mapping — disabled",
        "USB / external storage — blocked",
        "Print-to-local — disabled or audited",
        "Session auto-lock — 15 min inactivity",
        "Watermarking — screen capture deterrence",
    ]
    col_w_ctrl = CONTENT_W / 2
    for i, ctrl in enumerate(controls):
        col = i % 2
        row = i // 2
        cx = MARGIN + col * col_w_ctrl + 8
        cy = y - row * 15
        c.setFillColor(TEAL)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(cx, cy, "✓")
        c.setFillColor(BODY_TEXT)
        c.setFont("Helvetica", 7.5)
        c.drawString(cx + 12, cy, ctrl)


# ═══════════════════════════════════════════════════════════════
# PAGE 5: SIX-PILLAR STRATEGY
# ═══════════════════════════════════════════════════════════════
def page_six_pillars(c):
    draw_page_header(c, "Six-Pillar Compliance Strategy", "05")
    draw_page_footer(c, 6, 9)

    y = H - 110

    pillars = [
        {
            "title": "VDI as Security Boundary",
            "accent": BLUE, "bg": BLUE_LIGHT,
            "items": [
                "All operations within Technijian VDI",
                "No local data on personal devices",
                "Clipboard & drive mapping disabled",
                "USB/external storage blocked",
                "Session auto-lock: 15 min",
            ],
        },
        {
            "title": "Conditional Access & IP Lockdown",
            "accent": TEAL, "bg": TEAL_LIGHT,
            "items": [
                "Entra ID: M365 sign-ins from VDI only",
                "Schwab: IP allowlisted to VDI egress",
                "IBKR: IP restricted to VDI egress",
                "Legacy auth protocols blocked",
                "Geo-fencing to approved locations",
            ],
        },
        {
            "title": "Data Loss Prevention",
            "accent": ORANGE, "bg": ORANGE_LIGHT,
            "items": [
                "M365 DLP for SSN, account #s, PII",
                "External sharing blocked in OneDrive",
                "Email DLP: no client data to personal",
                "Financial SITs configured",
                "Quarterly policy review cycle",
            ],
        },
        {
            "title": "Email & Comms Archiving",
            "accent": BLUE, "bg": BLUE_LIGHT,
            "items": [
                "Technijian My Archive (SEC 17a-4)",
                "WORM-compliant email retention",
                "Technijian V365 Backup for M365 data",
                "7-year retention with immutability",
                "eDiscovery-ready search & export",
            ],
        },
        {
            "title": "Authentication & Identity",
            "accent": TEAL, "bg": TEAL_LIGHT,
            "items": [
                "MFA on all: VDI, M365, Schwab, IBKR",
                "Named accounts (FINRA 3110)",
                "14+ character password policy",
                "Privileged access management",
                "Annual access reviews",
            ],
        },
        {
            "title": "Audit, Monitoring & Reporting",
            "accent": ORANGE, "bg": ORANGE_LIGHT,
            "items": [
                "Technijian My Audit: user monitoring",
                "VDI session logging with attribution",
                "Real-time anomaly & insider threat alerting",
                "Monthly compliance dashboards",
                "Supervisory audit trail (FINRA 3110)",
            ],
        },
    ]

    card_w = (CONTENT_W - 16) / 2
    card_h = 112
    gap_x = 16
    gap_y = 12

    for idx, pillar in enumerate(pillars):
        col = idx % 2
        row = idx // 2
        cx = MARGIN + col * (card_w + gap_x)
        cy = y - row * (card_h + gap_y)

        # Card
        c.setFillColor(pillar["bg"])
        c.roundRect(cx, cy - card_h, card_w, card_h, 5, fill=1, stroke=0)
        c.setStrokeColor(pillar["accent"])
        c.setLineWidth(0.5)
        c.roundRect(cx, cy - card_h, card_w, card_h, 5, fill=0, stroke=1)

        # Top accent bar
        c.setFillColor(pillar["accent"])
        c.rect(cx + 1, cy - 3, card_w - 2, 3, fill=1, stroke=0)

        # Number
        c.setFillColor(pillar["accent"])
        c.setFont("Helvetica-Bold", 18)
        c.drawString(cx + 12, cy - 26, f"0{idx + 1}")

        # Title
        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(cx + 42, cy - 20, pillar["title"])

        # Rule
        c.setStrokeColor(pillar["accent"])
        c.setLineWidth(0.3)
        c.line(cx + 12, cy - 33, cx + card_w - 12, cy - 33)

        # Items
        item_y = cy - 46
        for item in pillar["items"]:
            c.setFillColor(pillar["accent"])
            c.setFont("Helvetica-Bold", 7)
            c.drawString(cx + 16, item_y, "✓")
            c.setFillColor(BODY_TEXT)
            c.setFont("Helvetica", 7.5)
            max_tw = card_w - 46
            display = item
            while pdfmetrics.stringWidth(display, "Helvetica", 7.5) > max_tw and len(display) > 10:
                display = display[:-1]
            if display != item:
                display = display.rstrip() + "…"
            c.drawString(cx + 28, item_y, display)
            item_y -= 13


# ═══════════════════════════════════════════════════════════════
# PAGE 6: REGULATORY MAPPING
# ═══════════════════════════════════════════════════════════════
def page_regulatory_mapping(c):
    draw_page_header(c, "Regulatory Control Mapping", "06")
    draw_page_footer(c, 7, 9)

    y = H - 100
    c.setFillColor(LIGHT_TEXT)
    c.setFont("Helvetica", 8)
    c.drawString(MARGIN + 22, y, "Each control mapped to the specific regulation it satisfies")
    y -= 24

    headers = ["CONTROL", "SEC REG S-P", "FINRA 4370", "FINRA 3110", "SEC 17a-4"]
    col_widths = [155, 95, 90, 90, 74]
    col_starts = []
    cx = MARGIN
    for w in col_widths:
        col_starts.append(cx)
        cx += w

    # Header row
    c.setFillColor(BLUE)
    c.rect(MARGIN, y - 16, CONTENT_W, 20, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 6.5)
    for i, h in enumerate(headers):
        c.drawString(col_starts[i] + 6, y - 10, h)
    y -= 20

    rows = [
        ("VDI Environment", "Safeguards", "Alt Location", "", ""),
        ("Conditional Access", "Access Control", "", "", ""),
        ("IP Allowlisting", "Access Control", "", "", ""),
        ("DLP Policies", "Data Protection", "", "", ""),
        ("My Archive", "", "", "", "Records"),
        ("Comms Capture", "", "", "Supervision", "Records"),
        ("MFA", "Authentication", "", "", ""),
        ("Named Accounts", "", "", "Accountability", ""),
        ("My Audit", "Monitoring", "", "Supervision", "Records"),
        ("Incident Response", "Required", "BCP Integration", "", ""),
        ("Breach Notification", "30-day Required", "", "", ""),
        ("Vendor Oversight", "72-hr Required", "", "", ""),
        ("Session Controls", "Safeguards", "", "", ""),
        ("Disposal Procedures", "Required", "", "", ""),
    ]

    row_h = 21
    for idx, row_data in enumerate(rows):
        ry = y - row_h
        if idx % 2 == 0:
            c.setFillColor(LIGHT_BG)
        else:
            c.setFillColor(WHITE)
        c.rect(MARGIN, ry, CONTENT_W, row_h, fill=1, stroke=0)
        c.setStrokeColor(BORDER)
        c.setLineWidth(0.2)
        c.line(MARGIN, ry, W - MARGIN, ry)

        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(col_starts[0] + 6, ry + 7, row_data[0])

        for ci in range(1, 5):
            val = row_data[ci]
            if val:
                c.setFillColor(TEAL)
                c.setFont("Helvetica-Bold", 7)
                c.drawString(col_starts[ci] + 6, ry + 7, "✓")
                c.setFillColor(BODY_TEXT)
                c.setFont("Helvetica", 6.5)
                c.drawString(col_starts[ci] + 16, ry + 7, val)
            else:
                c.setFillColor(BORDER)
                c.setFont("Helvetica", 7)
                c.drawString(col_starts[ci] + 6, ry + 7, "—")
        y -= row_h

    y -= 18

    # Coverage summary
    y = draw_section_header(c, y, "REGULATORY COVERAGE SUMMARY")
    y -= 14

    regs = [
        ("SEC Reg S-P (2024 Amendments)", "10 of 10 requirements addressed", BLUE, BLUE_LIGHT),
        ("FINRA Rule 4370", "2 of 2 technical controls mapped", TEAL, TEAL_LIGHT),
        ("FINRA Rule 3110", "3 of 3 supervisory provisions covered", TEAL, TEAL_LIGHT),
        ("SEC Rule 17a-4", "3 of 3 recordkeeping requirements met", ORANGE, ORANGE_LIGHT),
    ]

    for label, desc, color, bg in regs:
        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(MARGIN + 8, y, label)
        c.setFillColor(LIGHT_TEXT)
        c.setFont("Helvetica", 7)
        c.drawString(MARGIN + 8, y - 12, desc)

        bar_x = W - MARGIN - 155
        bar_w = 135
        c.setFillColor(bg)
        c.roundRect(bar_x, y - 5, bar_w, 10, 2, fill=1, stroke=0)
        c.setFillColor(color)
        c.roundRect(bar_x, y - 5, bar_w, 10, 2, fill=1, stroke=0)
        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica-Bold", 7)
        c.drawRightString(bar_x - 6, y - 2, "100%")
        y -= 28


# ═══════════════════════════════════════════════════════════════
# PAGE 7: IMPLEMENTATION ROADMAP
# ═══════════════════════════════════════════════════════════════
def page_roadmap(c):
    draw_page_header(c, "Implementation Roadmap", "07")
    draw_page_footer(c, 8, 9)

    y = H - 100
    c.setFillColor(LIGHT_TEXT)
    c.setFont("Helvetica", 8)
    c.drawString(MARGIN + 22, y, "18-week phased deployment with overlapping workstreams")
    y -= 24

    phases = [
        {
            "num": "01", "title": "Foundation", "weeks": "Weeks 1–4", "accent": BLUE, "bg": BLUE_LIGHT,
            "items": ["Deploy Technijian VDI environment", "Configure VDI security policies (clipboard, drives, USB, print)", "Enroll users in VDI with MFA", "Configure Entra ID Conditional Access for M365"],
            "cost": "Included in VDI subscription",
        },
        {
            "num": "02", "title": "Access Lockdown", "weeks": "Weeks 3–6", "accent": TEAL, "bg": TEAL_LIGHT,
            "items": ["IP allowlist Schwab Advisor Services to VDI egress", "IP allowlist Interactive Brokers to VDI egress", "Block legacy authentication in Entra ID", "Deploy endpoint protection within VDI"],
            "cost": "Included in M365 licensing",
        },
        {
            "num": "03", "title": "Data Protection", "weeks": "Weeks 5–8", "accent": ORANGE, "bg": ORANGE_LIGHT,
            "items": ["Configure M365 DLP policies for financial PII", "Enable OneDrive sharing restrictions", "Deploy email DLP rules", "Configure sensitive information types (SITs)"],
            "cost": "M365 E5 Compliance add-on",
        },
        {
            "num": "04", "title": "Archiving & Records", "weeks": "Weeks 7–10", "accent": BLUE, "bg": BLUE_LIGHT,
            "items": ["Deploy Technijian My Archive for email", "Deploy Technijian V365 Backup for M365", "Enable 7-year retention with immutability", "Set up eDiscovery workspace"],
            "cost": "My Archive + V365 Backup license",
        },
        {
            "num": "05", "title": "Monitoring & Audit", "weeks": "Weeks 9–12", "accent": TEAL, "bg": TEAL_LIGHT,
            "items": ["Deploy Technijian My Audit (user monitoring)", "Configure VDI session logging", "Set up insider threat & anomaly alerting", "Build compliance dashboard"],
            "cost": "My Audit license",
        },
        {
            "num": "06", "title": "Validation & Testing", "weeks": "Weeks 11–14", "accent": ORANGE, "bg": ORANGE_LIGHT,
            "items": ["Penetration testing of VDI environment", "Post-implementation compliance gap assessment", "Deploy Huntress SAT for security training", "Phishing simulations & training completion tracking"],
            "cost": "Huntress SAT license",
        },
        {
            "num": "07", "title": "Policy & Compliance Docs", "weeks": "Weeks 13–18", "accent": BLUE, "bg": BLUE_LIGHT,
            "items": ["Written Incident Response Plan (IRP)", "Breach notification procedures & templates", "Service provider oversight policy (72-hr clause)", "BCP customer disclosure + info disposal + annual sign-off"],
            "cost": "Technijian consulting",
        },
    ]

    card_h = 66
    gap = 5

    for idx, phase in enumerate(phases):
        if y - card_h < 42:
            break

        # Card
        c.setFillColor(phase["bg"])
        c.roundRect(MARGIN, y - card_h, CONTENT_W, card_h, 4, fill=1, stroke=0)
        c.setStrokeColor(phase["accent"])
        c.setLineWidth(0.4)
        c.roundRect(MARGIN, y - card_h, CONTENT_W, card_h, 4, fill=0, stroke=1)

        # Left accent bar
        c.setFillColor(phase["accent"])
        c.rect(MARGIN + 1, y - card_h + 1, 3, card_h - 2, fill=1, stroke=0)

        # Phase number
        c.setFillColor(phase["accent"])
        c.setFont("Helvetica-Bold", 12)
        c.drawString(MARGIN + 12, y - 16, phase["num"])

        # Title and weeks
        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(MARGIN + 34, y - 12, phase["title"])
        c.setFillColor(LIGHT_TEXT)
        c.setFont("Helvetica", 6)
        c.drawString(MARGIN + 34, y - 21, phase["weeks"])

        # Cost badge
        cost_text = phase["cost"]
        cost_w = pdfmetrics.stringWidth(cost_text, "Helvetica", 5.5) + 12
        c.setFillColor(WHITE)
        c.roundRect(W - MARGIN - cost_w - 8, y - 18, cost_w, 13, 2, fill=1, stroke=0)
        c.setFillColor(LIGHT_TEXT)
        c.setFont("Helvetica", 5.5)
        c.drawString(W - MARGIN - cost_w - 2, y - 14, cost_text)

        # Items (two columns)
        items = phase["items"]
        col_w_item = (CONTENT_W - 50) / 2
        for ii, item in enumerate(items):
            col = ii % 2
            row = ii // 2
            ix = MARGIN + 14 + col * col_w_item
            iy = y - 32 - row * 12
            c.setFillColor(phase["accent"])
            c.setFont("Helvetica", 6.5)
            c.drawString(ix, iy, "›")
            c.setFillColor(BODY_TEXT)
            c.setFont("Helvetica", 7)
            display = item
            max_tw = col_w_item - 18
            while pdfmetrics.stringWidth(display, "Helvetica", 7) > max_tw and len(display) > 10:
                display = display[:-1]
            if display != item:
                display = display.rstrip() + "…"
            c.drawString(ix + 8, iy, display)

        y -= card_h + gap


# ═══════════════════════════════════════════════════════════════
# PAGE 8: COST-BENEFIT & CTA
# ═══════════════════════════════════════════════════════════════
def page_cta(c):
    draw_page_header(c, "Cost-Benefit Analysis", "08")
    draw_page_footer(c, 9, 9)

    y = H - 115

    card_w = (CONTENT_W - 20) / 2
    card_h = 176

    # ── VDI Only card ──
    cx = MARGIN
    c.setFillColor(RISK_CRITICAL_BG)
    c.roundRect(cx, y - card_h, card_w, card_h, 5, fill=1, stroke=0)
    c.setStrokeColor(RISK_CRITICAL)
    c.setLineWidth(0.5)
    c.roundRect(cx, y - card_h, card_w, card_h, 5, fill=0, stroke=1)
    c.setFillColor(ORANGE)
    c.rect(cx + 1, y - 3, card_w - 2, 3, fill=1, stroke=0)

    c.setFillColor(LIGHT_TEXT)
    c.setFont("Helvetica-Bold", 7)
    c.drawString(cx + 14, y - 18, "VDI ALONE")
    c.setFillColor(ORANGE)
    c.setFont("Helvetica-Bold", 30)
    c.drawString(cx + 14, y - 50, "~40%")
    c.setFillColor(BODY_TEXT)
    c.setFont("Helvetica", 7)
    c.drawString(cx + 14, y - 62, "Compliance coverage")

    vdi_items = [
        ("✓", "Managed environment", TEAL),
        ("✓", "No local data storage", TEAL),
        ("✓", "Session controls", TEAL),
        ("✗", "No access lockdown", RISK_CRITICAL),
        ("✗", "No DLP policies", RISK_CRITICAL),
        ("✗", "No email archive (My Archive)", RISK_CRITICAL),
        ("✗", "No user monitoring (My Audit)", RISK_CRITICAL),
    ]
    iy = y - 80
    for mark, text, clr in vdi_items:
        c.setFillColor(clr)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(cx + 14, iy, mark)
        c.setFillColor(BODY_TEXT)
        c.setFont("Helvetica", 7.5)
        c.drawString(cx + 28, iy, text)
        iy -= 13

    # ── Full Strategy card ──
    cx = MARGIN + card_w + 20
    c.setFillColor(TEAL_LIGHT)
    c.roundRect(cx, y - card_h, card_w, card_h, 5, fill=1, stroke=0)
    c.setStrokeColor(TEAL)
    c.setLineWidth(0.5)
    c.roundRect(cx, y - card_h, card_w, card_h, 5, fill=0, stroke=1)
    c.setFillColor(TEAL)
    c.rect(cx + 1, y - 3, card_w - 2, 3, fill=1, stroke=0)

    c.setFillColor(LIGHT_TEXT)
    c.setFont("Helvetica-Bold", 7)
    c.drawString(cx + 14, y - 18, "FULL STRATEGY")
    c.setFillColor(TEAL)
    c.setFont("Helvetica-Bold", 30)
    c.drawString(cx + 14, y - 50, "100%")
    c.setFillColor(BODY_TEXT)
    c.setFont("Helvetica", 7)
    c.drawString(cx + 14, y - 62, "Compliance coverage")

    full_items = [
        ("✓", "All SEC Reg S-P requirements", TEAL),
        ("✓", "All FINRA 4370 technical controls", TEAL),
        ("✓", "FINRA 3110 supervisory continuity", TEAL),
        ("✓", "SEC 17a-4 recordkeeping", TEAL),
        ("✓", "Examination-ready documentation", TEAL),
        ("✓", "My Audit continuous monitoring", TEAL),
        ("✓", "V365 Backup complete data protection", TEAL),
    ]
    iy = y - 80
    for mark, text, clr in full_items:
        c.setFillColor(clr)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(cx + 14, iy, mark)
        c.setFillColor(BODY_TEXT)
        c.setFont("Helvetica", 7.5)
        c.drawString(cx + 28, iy, text)
        iy -= 13

    y -= card_h + 22

    # Risk of Inaction
    y = draw_section_header(c, y, "RISK OF INACTION")
    y -= 14

    risks = [
        ("SEC enforcement actions and monetary fines", RISK_CRITICAL),
        ("FINRA examination deficiency letters", RISK_HIGH),
        ("Customer data breach liability and litigation", RISK_CRITICAL),
        ("Reputational damage and client attrition", RISK_HIGH),
    ]
    for text, color in risks:
        c.setFillColor(color)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(MARGIN + 8, y, "▸")
        c.setFillColor(BODY_TEXT)
        c.setFont("Helvetica", 8)
        c.drawString(MARGIN + 22, y, text)
        y -= 15

    y -= 22

    # Next Steps section (replaces sales CTA — this is an existing client)
    y = draw_section_header(c, y, "NEXT STEPS")
    y -= 14

    next_steps = [
        "Review this strategy document and confirm scope alignment",
        "Technijian to schedule kickoff for Phase 1 (VDI deployment)",
        "AFFG to designate registered principal for policy sign-off",
        "Technijian to begin policy drafting in parallel with technical deployment",
    ]
    for i, step in enumerate(next_steps):
        c.setFillColor(BLUE)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(MARGIN + 8, y, f"{i + 1}.")
        c.setFillColor(BODY_TEXT)
        c.setFont("Helvetica", 8)
        c.drawString(MARGIN + 24, y, step)
        y -= 15

    y -= 16

    # Technijian solution stack summary
    y = draw_section_header(c, y, "TECHNIJIAN SOLUTION STACK")
    y -= 14

    solutions = [
        ("Technijian VDI", "Managed virtual desktop environment", BLUE),
        ("Technijian My Archive", "WORM-compliant email archiving (SEC 17a-4)", BLUE),
        ("Technijian V365 Backup", "Microsoft 365 backup and retention", TEAL),
        ("Technijian My Audit", "User activity monitoring and insider threat detection", TEAL),
        ("Huntress SAT", "Security awareness training and phishing simulations", ORANGE),
    ]
    for name, desc, accent in solutions:
        c.setFillColor(accent)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(MARGIN + 8, y, "▸")
        c.setFillColor(DARK_TEXT)
        c.drawString(MARGIN + 22, y, name)
        c.setFillColor(LIGHT_TEXT)
        c.setFont("Helvetica", 7)
        c.drawString(MARGIN + 22, y - 11, desc)
        y -= 26


# ═══════════════════════════════════════════════════════════════
# GENERATE
# ═══════════════════════════════════════════════════════════════
def generate():
    c_pdf = canvas.Canvas(OUTPUT_PATH, pagesize=letter)
    c_pdf.setTitle("AFFG IT Compliance & Security Strategy — Technijian")
    c_pdf.setAuthor("Technijian")
    c_pdf.setSubject("IT Compliance & Security Strategy for American Fundstars Financial Group LLC")

    page_cover(c_pdf)
    c_pdf.showPage()

    page_executive_summary(c_pdf)
    c_pdf.showPage()

    page_current_state(c_pdf)
    c_pdf.showPage()

    page_vdi_recommendation(c_pdf)
    c_pdf.showPage()

    page_architecture(c_pdf)
    c_pdf.showPage()

    page_six_pillars(c_pdf)
    c_pdf.showPage()

    page_regulatory_mapping(c_pdf)
    c_pdf.showPage()

    page_roadmap(c_pdf)
    c_pdf.showPage()

    page_cta(c_pdf)
    c_pdf.showPage()

    c_pdf.save()
    print(f"PDF generated: {OUTPUT_PATH}")


if __name__ == "__main__":
    generate()
