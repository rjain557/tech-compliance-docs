const path = require("path");
const PptxGenJS = require("pptxgenjs");

const pptx = new PptxGenJS();
pptx.layout = "LAYOUT_WIDE";
pptx.author = "Technijian";
pptx.company = "Technijian";
pptx.subject = "AFFG IT Compliance Strategy - Revised Proposal Review";
pptx.title = "AFFG IT Compliance Strategy - Revised Proposal Review";
pptx.lang = "en-US";
pptx.theme = { headFontFace: "Arial", bodyFontFace: "Arial", lang: "en-US" };

const COLORS = {
  blue: "006DB6",
  teal: "1EAAC8",
  orange: "F67D4B",
  dark: "1A1A2E",
  slate: "334155",
  grey: "64748B",
  light: "E9EEF5",
  offWhite: "F8FAFC",
  white: "FFFFFF",
  line: "D8E0EA",
  paleBlue: "EAF4FB",
  paleTeal: "E8F8FB",
  paleOrange: "FFF1EA",
  paleDark: "EEF2F7",
  green: "0F766E",
  red: "B42318",
};

const logoWhite = path.resolve(__dirname, "..", "..", "ampac", "technijian_logo_white_on_dark.png");
const outPath = path.resolve(__dirname, "AFFG_Proposal_Revision_Review_Technijian.pptx");

function hLine(slide, x, y, w, color = COLORS.line, thickness = 0.012) {
  slide.addShape(pptx.ShapeType.rect, {
    x, y, w, h: thickness,
    fill: { color },
    line: { color, transparency: 100 },
  });
}

function addFooter(slide, page) {
  hLine(slide, 0.5, 7.05, 12.35, COLORS.line, 0.012);
  slide.addText("Technijian  |  AFFG IT Compliance Strategy - Revised Proposal Review", {
    x: 0.55, y: 7.1, w: 7.5, h: 0.25,
    fontFace: "Arial", fontSize: 9, color: COLORS.grey, margin: 0,
  });
  slide.addText(String(page), {
    x: 12.2, y: 7.08, w: 0.6, h: 0.25,
    fontFace: "Arial", fontSize: 10, bold: true, align: "right",
    color: COLORS.blue, margin: 0,
  });
}

function addBrandMark(slide, x, y, darkBg = false) {
  const s = 0.09;
  const gap = 0.018;
  const palette = [
    ["64748B", "006DB6", "F67D4B", "64748B"],
    ["64748B", "1EAAC8", "64748B", "1EAAC8"],
    ["94A3AF", "006DB6", "1EAAC8", "64748B"],
  ];
  for (let r = 0; r < 3; r++) {
    for (let c = 0; c < 4; c++) {
      slide.addShape(pptx.ShapeType.roundRect, {
        x: x + c * (s + gap),
        y: y + r * (s + gap),
        w: s, h: s, rectRadius: 0.015,
        fill: { color: palette[r][c] },
        line: { color: palette[r][c], transparency: 100 },
      });
    }
  }
  slide.addText("TECHNIJIAN", {
    x: x + 4 * (s + gap) + 0.1,
    y: y - 0.02,
    w: 1.8, h: 0.36,
    fontFace: "Arial", fontSize: 17, bold: true,
    color: darkBg ? COLORS.white : COLORS.dark,
    charSpace: 1, margin: 0, valign: "mid",
  });
}

function addHeader(slide, eyebrow, title, subtitle, page, accent = COLORS.blue) {
  slide.background = { color: COLORS.offWhite };
  slide.addShape(pptx.ShapeType.rect, {
    x: 0, y: 0, w: 13.33, h: 0.18,
    fill: { color: accent },
    line: { color: accent, transparency: 100 },
  });
  addBrandMark(slide, 0.55, 0.35);
  slide.addText(eyebrow.toUpperCase(), {
    x: 0.55, y: 0.95, w: 6.0, h: 0.28,
    fontFace: "Arial", fontSize: 10, bold: true,
    color: accent, charSpace: 0.5, margin: 0,
  });
  slide.addText(title, {
    x: 0.55, y: 1.2, w: 12.4, h: 0.55,
    fontFace: "Arial", fontSize: 22, bold: true,
    color: COLORS.dark, margin: 0,
  });
  if (subtitle) {
    slide.addText(subtitle, {
      x: 0.55, y: 1.7, w: 12.4, h: 0.35,
      fontFace: "Arial", fontSize: 11, color: COLORS.slate, margin: 0,
    });
  }
  hLine(slide, 0.55, 2.05, 12.25, COLORS.line, 0.01);
  addFooter(slide, page);
}

function addBulletList(slide, items, opts = {}) {
  const { x = 0.7, y = 2.1, w = 5.6, fontSize = 15,
    bulletColor = COLORS.blue, textColor = COLORS.dark, gap = 0.52 } = opts;
  items.forEach((item, index) => {
    const top = y + index * gap;
    slide.addShape(pptx.ShapeType.ellipse, {
      x, y: top + 0.08, w: 0.12, h: 0.12,
      fill: { color: bulletColor },
      line: { color: bulletColor, transparency: 100 },
    });
    slide.addText(item, {
      x: x + 0.22, y: top, w, h: 0.35,
      fontFace: "Arial", fontSize, color: textColor,
      breakLine: false, margin: 0,
    });
  });
}

function addCard(slide, card) {
  slide.addShape(pptx.ShapeType.roundRect, {
    x: card.x, y: card.y, w: card.w, h: card.h,
    rectRadius: 0.08,
    fill: { color: card.fill },
    line: { color: card.line || card.fill, pt: 1 },
  });
  if (card.band) {
    slide.addShape(pptx.ShapeType.rect, {
      x: card.x, y: card.y, w: card.w, h: 0.1,
      fill: { color: card.band },
      line: { color: card.band, transparency: 100 },
    });
  }
  if (card.label) {
    slide.addText(card.label.toUpperCase(), {
      x: card.x + 0.18, y: card.y + 0.2, w: card.w - 0.36, h: 0.22,
      fontFace: "Arial", fontSize: 9, bold: true,
      color: card.labelColor || card.band || COLORS.blue,
      charSpace: 0.4, margin: 0,
    });
  }
  if (card.title) {
    slide.addText(card.title, {
      x: card.x + 0.18, y: card.y + 0.44, w: card.w - 0.36, h: 0.42,
      fontFace: "Arial", fontSize: 16, bold: true,
      color: COLORS.dark, margin: 0,
    });
  }
  if (card.body) {
    const reserveBottom = card.citation ? 0.45 : 0.15;
    slide.addText(card.body, {
      x: card.x + 0.18, y: card.y + 0.86,
      w: card.w - 0.36, h: card.h - 0.86 - reserveBottom,
      fontFace: "Arial", fontSize: 10.5, color: COLORS.slate,
      valign: "top", margin: 0, breakLine: false,
    });
  }
  if (card.citation) {
    slide.addText(card.citation, {
      x: card.x + 0.18, y: card.y + card.h - 0.38,
      w: card.w - 0.36, h: 0.28,
      fontFace: "Arial", fontSize: 9, bold: true, italic: true,
      color: card.band || COLORS.blue, margin: 0,
    });
  }
}

function addTableHeaders(slide, headers, colX, y, widths, fill = COLORS.blue) {
  slide.addShape(pptx.ShapeType.roundRect, {
    x: colX[0], y,
    w: widths.reduce((s, n) => s + n, 0), h: 0.38, rectRadius: 0.03,
    fill: { color: fill }, line: { color: fill, transparency: 100 },
  });
  headers.forEach((header, idx) => {
    slide.addText(header, {
      x: colX[idx] + 0.08, y: y + 0.08,
      w: widths[idx] - 0.16, h: 0.22,
      fontFace: "Arial", fontSize: 9, bold: true,
      color: COLORS.white, margin: 0,
    });
  });
}

function addTableRow(slide, cols, colX, y, widths, opts = {}) {
  slide.addShape(pptx.ShapeType.rect, {
    x: colX[0], y,
    w: widths.reduce((s, n) => s + n, 0), h: opts.h || 0.58,
    fill: { color: opts.fill || COLORS.white },
    line: { color: opts.line || COLORS.line, pt: 0.75 },
  });
  cols.forEach((text, idx) => {
    slide.addText(text, {
      x: colX[idx] + 0.08, y: y + 0.09,
      w: widths[idx] - 0.16, h: (opts.h || 0.58) - 0.16,
      fontFace: "Arial", fontSize: opts.fontSize || 10,
      color: opts.color || COLORS.slate,
      bold: idx === 0 && !!opts.firstColBold,
      valign: "mid", margin: 0,
    });
  });
}

// ============ SLIDES ============

function coverSlide() {
  const slide = pptx.addSlide();
  slide.background = { color: COLORS.dark };

  slide.addShape(pptx.ShapeType.rect, {
    x: 0, y: 6.95, w: 13.33, h: 0.12,
    fill: { color: COLORS.orange },
    line: { color: COLORS.orange, transparency: 100 },
  });
  slide.addShape(pptx.ShapeType.rect, {
    x: 0, y: 6.82, w: 13.33, h: 0.03,
    fill: { color: COLORS.teal },
    line: { color: COLORS.teal, transparency: 100 },
  });

  addBrandMark(slide, 0.6, 0.5, true);

  slide.addShape(pptx.ShapeType.rect, {
    x: 0.6, y: 1.3, w: 0.9, h: 0.06,
    fill: { color: COLORS.orange },
    line: { color: COLORS.orange, transparency: 100 },
  });
  slide.addText("AFFG IT Compliance Strategy", {
    x: 0.6, y: 1.5, w: 7.5, h: 0.6,
    fontFace: "Arial", fontSize: 30, bold: true,
    color: COLORS.white, margin: 0,
  });
  slide.addText("Revised Proposal Review", {
    x: 0.6, y: 2.1, w: 7.5, h: 0.6,
    fontFace: "Arial", fontSize: 32, bold: true,
    color: COLORS.white, margin: 0,
  });
  slide.addText(
    "Each design choice mapped to the specific FINRA and SEC requirement it satisfies",
    { x: 0.6, y: 2.85, w: 7.4, h: 0.4, fontFace: "Arial", fontSize: 13,
      color: "DCE5F2", margin: 0 }
  );

  slide.addShape(pptx.ShapeType.roundRect, {
    x: 8.2, y: 1.5, w: 4.5, h: 2.8, rectRadius: 0.08,
    fill: { color: "202842" },
    line: { color: "36435E", pt: 1 },
  });
  slide.addText("Regulatory Scope", {
    x: 8.45, y: 1.72, w: 3.0, h: 0.28,
    fontFace: "Arial", fontSize: 11, bold: true,
    color: COLORS.orange, margin: 0,
  });
  addBulletList(slide, [
    "SEC Regulation S-P \u00a7248.30 (Safeguards Rule)",
    "FINRA Rule 3110 (Supervision)",
    "SEC Rule 17a-4 (Records Retention)",
    "FINRA Rule 4511 (Books and Records)",
    "SEC Cybersecurity Risk Mgmt Rules (2023)",
  ], {
    x: 8.45, y: 2.1, w: 4.0, fontSize: 12,
    bulletColor: COLORS.teal, textColor: COLORS.white, gap: 0.38,
  });

  slide.addText("Prepared for AFFG  |  April 15, 2026", {
    x: 0.6, y: 6.45, w: 4.4, h: 0.2,
    fontFace: "Arial", fontSize: 10, color: "BFD0E5", margin: 0,
  });

  slide.addNotes(
    "Open by thanking AFFG for the detailed written response. " +
    "Frame today as a working session: the job is to show each line item maps to a specific FINRA or SEC requirement. " +
    "Set expectation: the revised proposal will be leaner where we can, but there are controls we cannot remove without creating an examination gap. " +
    "Call out the five citations on the right - these are the rulebooks every design decision in this deck traces back to."
  );
}

function executiveSummarySlide() {
  const slide = pptx.addSlide();
  addHeader(slide, "Executive Summary",
    "Policy Alone Is Not A Control - Examiners Require Technical Enforcement",
    "Every item in this design closes a gap that a stated policy cannot close on its own.",
    2, COLORS.blue);

  addCard(slide, {
    x: 0.65, y: 2.3, w: 4.0, h: 4.35,
    fill: COLORS.white, line: COLORS.line, band: COLORS.red,
    label: "The Risk", title: "Unenforced Policy",
    body: "\"We don't store client data on personal devices\" is a policy statement. Without technical controls preventing download to C:, copy to USB, or login to OneDrive from a home PC, an examiner sees intent, not enforcement.\n\nSEC exam letters in 2024 have cited firms whose written policies were not backed by technical safeguards.",
  });

  addCard(slide, {
    x: 4.83, y: 2.3, w: 4.0, h: 4.35,
    fill: COLORS.white, line: COLORS.line, band: COLORS.blue,
    label: "The Requirement", title: "Reg S-P Safeguards",
    body: "SEC Regulation S-P \u00a7248.30(a) requires registered investment advisers and broker-dealers to adopt written policies AND reasonably designed administrative, technical, and physical safeguards for customer records.\n\nThe 2024 amendments added explicit incident response and 30-day notification obligations.",
  });

  addCard(slide, {
    x: 9.01, y: 2.3, w: 3.65, h: 4.35,
    fill: COLORS.white, line: COLORS.line, band: COLORS.orange,
    label: "The Design", title: "Layered Enforcement",
    body: "The revised proposal layers Technijian services:\n\n- Technijian Horizon VDI (7 roles)\n- Technijian MyAudit endpoint DLP\n- Technijian SSO/2FA gateway\n- IP whitelist + managed-endpoint access\n- Technijian Veeam tenant backup\n- Technijian monthly assessment\n\nEach layer closes a specific, cite-able gap.",
  });

  slide.addNotes(
    "Key message: \"We don't store client data on personal devices\" is a policy statement, not a control. " +
    "Reg S-P 248.30(a) specifically requires BOTH written policies AND technical safeguards. " +
    "Recent SEC exam deficiency letters (2023-2024) have cited firms whose written policies were not backed by enforceable technical controls. " +
    "Walk through the three cards left-to-right: the risk, the rule, the response. " +
    "This slide reframes the conversation from 'is this tool redundant' to 'which rule does each tool satisfy.'"
  );
}

function regulatoryFrameworkSlide() {
  const slide = pptx.addSlide();
  addHeader(slide, "Regulatory Framework",
    "The Rules That Drive Each Control In This Design",
    "These are the specific citations referenced when mapping every component of the solution.",
    3, COLORS.teal);

  const colX = [0.6, 2.6, 7.0];
  const widths = [2.0, 4.4, 5.7];
  addTableHeaders(slide,
    ["Citation", "What It Requires", "How This Design Satisfies It"],
    colX, 2.25, widths, COLORS.dark);

  const rows = [
    ["Reg S-P \u00a7248.30(a)",
      "Written policies AND administrative, technical, and physical safeguards to protect customer info.",
      "Technijian Horizon VDI, MyAudit DLP, IP whitelist, and SSO/2FA provide the technical safeguards behind the WSP."],
    ["Reg S-P (2024 amend.)",
      "Incident response program, 30-day customer notification, vendor oversight, annual review.",
      "Monthly drift assessments and Veeam recovery support detection, response, and recoverability."],
    ["FINRA 3110(a)",
      "Supervisory system reasonably designed to achieve compliance with securities laws.",
      "Isolated managed workspace creates a supervisable boundary for regulated activity."],
    ["FINRA 3110(c)",
      "Internal inspections of offices and supervisory activity on a documented cadence.",
      "Monthly site and M365 tenant assessments produce the books-and-records inspection evidence."],
    ["SEC Rule 17a-4(b),(f)",
      "Retention of records in non-rewriteable, non-erasable form for specified periods.",
      "Veeam Backup for M365 provides immutable tenant-wide backup (Exchange, SharePoint, OneDrive, Teams)."],
    ["FINRA 4511",
      "Firms must make and preserve books and records as required under FINRA and SEA 17a-3/17a-4.",
      "Audit logging plus Veeam preservation covers creation and retention in one integrated layer."],
    ["SEC Cyber Risk Mgmt",
      "Written cybersecurity policies, incident disclosure, and board oversight for advisers.",
      "Documented control stack, drift monitoring, and IR evidence package aligns with the rule set."],
  ];

  let y = 2.65;
  rows.forEach((row, index) => {
    addTableRow(slide, row, colX, y, widths, {
      fill: index % 2 === 0 ? COLORS.white : COLORS.paleDark,
      firstColBold: true, h: 0.58, fontSize: 9.5,
    });
    y += 0.6;
  });

  slide.addNotes(
    "This is the rulebook slide. Walk through each citation briefly - don't linger. " +
    "Reg S-P 248.30(a): the core safeguards rule for broker-dealers and advisers. " +
    "Reg S-P 2024 amendments: added incident response, 30-day notification, annual review. Phases in 2025-2026. " +
    "FINRA 3110(a) supervisory system; 3110(c) internal inspections - drives the assessment cadence discussion. " +
    "SEC 17a-4(b) and (f): non-rewriteable records - this is the Veeam justification. " +
    "FINRA 4511: books and records; SEC Cyber Risk Management: proposed rules already shaping exam expectations. " +
    "If the client asks for full citation text, offer the appendix after the meeting."
  );
}

function controlMappingSlide() {
  const slide = pptx.addSlide();
  addHeader(slide, "Control-To-Citation Map",
    "Every Component Maps To A Specific FINRA Or SEC Requirement",
    "If a design element cannot be tied to a citation, it is not in the proposal.",
    4, COLORS.blue);

  const colX = [0.55, 3.15, 8.05];
  const widths = [2.6, 4.9, 4.7];
  addTableHeaders(slide,
    ["Design Component", "Control Objective", "Citation(s)"],
    colX, 2.25, widths, COLORS.blue);

  const rows = [
    ["Technijian Horizon VDI (7 roles)",
      "Client financial data is processed only inside a managed, supervised environment.",
      "Reg S-P \u00a7248.30(a)(1)-(3); FINRA 3110(a); NIST SP 800-53 AC-3, SC-7"],
    ["Technijian MyAudit (endpoint DLP)",
      "Block USB, local download, print, clipboard, screen capture on managed devices.",
      "Reg S-P \u00a7248.30(a)(3); NIST AC-19, MP-7, SC-8"],
    ["Technijian SSO / 2FA gateway",
      "Enforced, logged MFA on custodian bank portals, trading platforms, third-party SaaS.",
      "Reg S-P \u00a7248.30 (2024 amend.); FFIEC Auth Guidance; NIST IA-2(1)"],
    ["IP whitelist + managed endpoint",
      "Block M365 and portal access from personal devices and home networks.",
      "Reg S-P \u00a7248.30(a)(3); FINRA 3110(a); NIST AC-3, AC-17"],
    ["Technijian Veeam Backup for M365",
      "Immutable, non-rewriteable backup of full tenant (Exchange, SharePoint, OneDrive, Teams).",
      "SEC Rule 17a-4(b),(f); FINRA 4511; Reg S-P availability"],
    ["Technijian monthly assessment",
      "Detect configuration drift; attested evidence of ongoing control operation.",
      "FINRA 3110(c); FINRA 3120; Reg S-P annual review"],
    ["Audit logging (Technijian + M365)",
      "Records of access, privileged actions, and data movement retained for examination.",
      "SEC 17a-4(b)(4),(e)(7); FINRA 4511; Reg S-P \u00a7248.30(a)"],
  ];

  let y = 2.65;
  rows.forEach((row, index) => {
    addTableRow(slide, row, colX, y, widths, {
      fill: index % 2 === 0 ? COLORS.white : COLORS.paleDark,
      firstColBold: true, h: 0.56, fontSize: 9.5,
    });
    y += 0.58;
  });

  slide.addNotes(
    "This is the centerpiece. Before line-by-line, set the rule: 'Nothing goes in the proposal that doesn't map to a citation on this page.' " +
    "That frames cost conversations as compliance conversations. " +
    "Row 1 (VDI): 'where does regulated data live' - inside a controlled environment. " +
    "Row 2 (MyAudit): 'can a user get data off the device' - USB, download, print, clipboard. M365 does not cover this. " +
    "Row 3 (SSO/2FA): 'is MFA enforced AND logged on non-M365 portals' - most custodian portals fail this on their own. " +
    "Row 4 (IP whitelist + managed endpoint): MFA alone doesn't stop a home-laptop login. " +
    "Row 5 (Veeam): M365 retention is not backup. 17a-4(f) requires non-rewriteable preservation. " +
    "Row 6 (Monthly assessment): FINRA 3110(c) inspections - drift detection. " +
    "Row 7 (Audit logging): the evidence that makes everything else defensible. " +
    "Close with: if the client wants to remove any row, ask which citation they are comfortable not satisfying."
  );
}

function vdiRequiredSlide() {
  const slide = pptx.addSlide();
  addHeader(slide, "Controlled Workspace",
    "Technijian Horizon VDI Is A Compliance Requirement, Not A Design Preference",
    "Dedicated VDI workstations in the Technijian datacenter, scoped to the 7 roles that touch client financial data.",
    5, COLORS.blue);

  slide.addShape(pptx.ShapeType.roundRect, {
    x: 0.75, y: 2.3, w: 3.3, h: 4.2, rectRadius: 0.08,
    fill: { color: COLORS.dark },
    line: { color: COLORS.dark, pt: 1 },
  });
  slide.addText("7", {
    x: 1.0, y: 2.65, w: 1.2, h: 0.9,
    fontFace: "Arial", fontSize: 54, bold: true,
    color: COLORS.orange, margin: 0,
  });
  slide.addText("in-scope users", {
    x: 1.0, y: 3.5, w: 2.2, h: 0.3,
    fontFace: "Arial", fontSize: 14, color: COLORS.white,
    bold: true, margin: 0,
  });
  slide.addText(
    "Only the roles with access to client financial data operate inside Technijian Horizon VDI workstations hosted in the Technijian datacenter. Remaining staff use standard managed endpoints with IP whitelist access to M365.",
    { x: 1.0, y: 3.95, w: 2.8, h: 2.3, fontFace: "Arial", fontSize: 12,
      color: "DCE5F2", margin: 0, valign: "top" }
  );

  addCard(slide, {
    x: 4.35, y: 2.3, w: 8.3, h: 1.3,
    fill: COLORS.paleBlue, line: COLORS.blue, band: COLORS.blue,
    label: "Why Horizon VDI (not just managed laptops)",
    body: "Client data stays in the Technijian datacenter. Even on a stolen or compromised endpoint, no regulated data is resident on the device. This is the cleanest Reg S-P \u00a7248.30(a) technical safeguard posture available.",
  });

  addCard(slide, {
    x: 4.35, y: 3.7, w: 8.3, h: 1.3,
    fill: COLORS.paleTeal, line: COLORS.teal, band: COLORS.teal,
    label: "Why only 7 users",
    body: "Reg S-P and FINRA 3110 obligations attach to users and systems that touch customer info. Scoping Horizon VDI to the 7 roles aligns control cost with risk without weakening the supervisory boundary.",
  });

  addCard(slide, {
    x: 4.35, y: 5.1, w: 8.3, h: 1.4,
    fill: COLORS.paleOrange, line: COLORS.orange, band: COLORS.orange,
    label: "Examiner optic",
    body: "A named Horizon VDI pool in the Technijian datacenter with documented membership, access rules, and session recording produces a clean, defensible answer to \"show us where and how customer records are accessed\" - exactly what Reg S-P exams ask.",
  });

  slide.addNotes(
    "Directly answer the client's pushback: we ARE scoping Technijian Horizon VDI to only 7 users - they were right that firm-wide is unnecessary. " +
    "But Horizon VDI itself for those 7 is not optional; it was compliance-driven in the original proposal and that hasn't changed. " +
    "Three points: " +
    "(1) Data stays in the Technijian datacenter - stolen laptop, ransomware, lost phone - none touches regulated data. " +
    "(2) The 7 users are the people Reg S-P cares about. Everyone else stays on managed endpoints with IP-whitelisted M365 access. " +
    "(3) Examiner POV: a defined Horizon VDI pool hosted by Technijian with documented membership is the cleanest answer to 'show us where customer records are processed.' " +
    "Fallback if client pushes back on VDI entirely: managed endpoints + full MyAudit DLP + IP whitelist - weaker posture, must be noted."
  );
}

function desktopComparisonSlide() {
  const slide = pptx.addSlide();
  addHeader(slide, "Desktop Model",
    "Dedicated Technijian Horizon VDI Workstations vs Multi-Session Technijian RDP Server",
    "Both options are Technijian-hosted in the Technijian datacenter. The choice is how users are isolated from each other.",
    6, COLORS.orange);

  const colX = [0.7, 3.1, 7.0];
  const widths = [2.35, 3.8, 5.55];
  addTableHeaders(slide,
    ["Factor", "Dedicated Horizon VDI Workstation (recommended)", "Multi-Session Technijian RDP Server"],
    colX, 2.25, widths, COLORS.dark);

  const rows = [
    ["Hosting",
      "Technijian datacenter - dedicated virtual workstation per user.",
      "Technijian datacenter - one shared Windows Server hosts all 7 sessions."],
    ["Isolation level",
      "Hypervisor-level: one user, one VM, dedicated OS kernel, memory, filesystem.",
      "Logical-only: all 7 users share one Windows Server OS, kernel, memory, and filesystem."],
    ["Compliance posture",
      "Matches the original proposal - \"isolated VDI workstations\" for Reg S-P \u00a7248.30(a).",
      "Weakens isolation for a population where every user handles regulated customer data."],
    ["Blast radius",
      "A compromised session is contained to one VM.",
      "Kernel, RDS, or profile misconfiguration on the host can affect every user at once."],
    ["Cost per user",
      "Higher - one persistent workstation per user (cost delta for 7 users is modest).",
      "Lower - savings come from sharing one OS instance across all users."],
  ];

  let y = 2.65;
  rows.forEach((row, index) => {
    addTableRow(slide, row, colX, y, widths, {
      fill: index % 2 === 0 ? COLORS.white : COLORS.paleDark,
      firstColBold: true, h: 0.66,
    });
    y += 0.68;
  });

  slide.addShape(pptx.ShapeType.roundRect, {
    x: 0.75, y: 6.25, w: 12.1, h: 0.45, rectRadius: 0.04,
    fill: { color: COLORS.paleOrange },
    line: { color: COLORS.orange, pt: 0.8 },
  });
  slide.addText(
    "Recommendation: Dedicated Technijian Horizon VDI workstations for the 7 in-scope roles. Preserves the hypervisor-level isolation the original proposal committed to for Reg S-P \u00a7248.30(a).",
    { x: 0.95, y: 6.36, w: 11.7, h: 0.22, fontFace: "Arial", fontSize: 11,
      color: COLORS.dark, bold: true, margin: 0, align: "center" }
  );

  slide.addNotes(
    "Clarify first: both options are Technijian services hosted in the Technijian datacenter. The choice is how users are isolated from each other inside that environment. " +
    "Option A - Dedicated Technijian Horizon VDI workstation: each user gets their own virtual workstation with its own Windows OS, memory, and filesystem. Hypervisor-level isolation. This is what 'isolated VDI workstations' in the original proposal meant. " +
    "Option B - Multi-session Technijian RDP server: all 7 users log into one Windows Server hosted in the Technijian datacenter and share one OS kernel, one memory space, one filesystem namespace. Isolation between users is enforced by the OS and session boundaries alone - not by the hypervisor. " +
    "For AFFG, every user in scope handles regulated customer data. When every occupant of the environment is in scope for Reg S-P, putting them all on one shared OS is the weaker posture. A single misconfiguration, kernel-level exploit, profile bleed, or admin error on the shared server affects every user simultaneously. " +
    "Dedicated Horizon workstations avoid that entire class of problem: the blast radius is one workstation, one user, one log stream. It is also the cleanest possible answer to an examiner question about isolation between regulated users. " +
    "The original proposal was built on this posture. Switching to the shared RDP server to save cost would walk back the compliance commitment. For 7 users, the cost delta is modest; the compliance delta is not. " +
    "If the client pushes on cost: multi-session Technijian RDP can be offered as a fallback, but the isolation tradeoff must be documented in writing and acknowledged by AFFG."
  );
}

function mfaAndIpWhitelistSlide() {
  const slide = pptx.addSlide();
  addHeader(slide, "Access Boundary",
    "MFA Is Necessary But Not Sufficient - IP Whitelisting Closes The Real Gap",
    "Without conditional access, a user at home on a personal laptop can still MFA into OneDrive or a custodian portal and exfiltrate data.",
    7, COLORS.blue);

  addCard(slide, {
    x: 0.65, y: 2.3, w: 4.0, h: 4.35,
    fill: COLORS.paleBlue, line: COLORS.blue, band: COLORS.blue,
    label: "Layer 1", title: "MFA on Every Portal",
    body: "M365 MFA is in place. The gap is every non-M365 portal: custodian bank platforms, trading systems, CRM, third-party SaaS.\n\nThe SSO/2FA gateway puts every regulated portal behind enforced, logged MFA with auditable session records.",
    citation: "Reg S-P \u00a7248.30 (2024); NIST IA-2(1)",
  });

  addCard(slide, {
    x: 4.83, y: 2.3, w: 4.0, h: 4.35,
    fill: COLORS.paleTeal, line: COLORS.teal, band: COLORS.teal,
    label: "Layer 2", title: "Office-IP Whitelist",
    body: "IP whitelist policy restricts M365, OneDrive, and every custodian portal to the office IP or Horizon VDI egress IP only.\n\nA user at home on a personal laptop cannot reach client data - even with valid credentials and MFA. This closes the personal-device exfiltration vector.",
    citation: "Reg S-P \u00a7248.30(a)(3); NIST AC-3, AC-17",
  });

  addCard(slide, {
    x: 9.01, y: 2.3, w: 3.65, h: 4.35,
    fill: COLORS.paleOrange, line: COLORS.orange, band: COLORS.orange,
    label: "Layer 3", title: "Device Compliance",
    body: "Technijian-managed endpoint with device-compliance policy gates access behind \"managed + compliant device\" checks.\n\nCombined with IP whitelist, access requires: right user + MFA + office network + Technijian-managed device.\n\nThis is the four-factor boundary a Reg S-P examination expects.",
    citation: "Reg S-P \u00a7248.30(a); NIST AC-3, CM-8",
  });

  slide.addNotes(
    "Most important slide in the deck. The client's email claimed MFA is already handled - for M365 they're right. " +
    "But MFA alone does not solve the real exfiltration vector: user at home on personal laptop logs into OneDrive or custodian portal, MFAs successfully, downloads regulated data locally. " +
    "That workflow passes MFA but fails Reg S-P. " +
    "Three layers: " +
    "Layer 1 - MFA on EVERY portal, not just M365. Custodian bank portals typically don't enforce MFA natively with auditable logs; SSO gateway fixes that. " +
    "Layer 2 - Office IP whitelist. Technijian-configured policies restrict M365 + OneDrive + every custodian portal to the office IP or Horizon VDI egress IP. Home laptop cannot reach data even with correct credentials. " +
    "Layer 3 - Device compliance. Technijian-managed and compliant device required. Combined: user + MFA + office network + Technijian-managed device. " +
    "Close: this is the control pattern examiners look for post-2024 Reg S-P amendments."
  );
}

function endpointDlpSlide() {
  const slide = pptx.addSlide();
  addHeader(slide, "Endpoint DLP",
    "MyAudit Controls The Device - M365 DLP Controls The Cloud",
    "Complementary layers, not duplicative. Removing either leaves a gap cited in recent SEC exam letters.",
    8, COLORS.teal);

  const colX = [0.55, 4.55, 8.55];
  const widths = [4.0, 4.0, 4.2];
  addTableHeaders(slide,
    ["Data Movement Path", "M365 E3 DLP Coverage", "MyAudit Coverage"],
    colX, 2.25, widths, COLORS.teal);

  const rows = [
    ["Download file to local C: drive", "Not covered", "Blocked / logged"],
    ["Copy file to USB drive", "Not covered", "Blocked / logged"],
    ["Print to local printer", "Not covered", "Blocked / logged"],
    ["Copy to clipboard \u2192 paste elsewhere", "Not covered", "Blocked / logged"],
    ["Screen capture / screenshot", "Not covered", "Blocked / logged"],
    ["Send via Exchange email", "Covered (mail-flow DLP)", "N/A (mail is M365)"],
    ["Share SharePoint / OneDrive externally", "Covered (M365 DLP)", "N/A (tenant-side)"],
    ["Upload to unsanctioned SaaS / browser", "Partial (requires E5 + Defender)", "Blocked / logged"],
  ];

  let y = 2.65;
  rows.forEach((row, index) => {
    addTableRow(slide, row, colX, y, widths, {
      fill: index % 2 === 0 ? COLORS.white : COLORS.paleDark,
      firstColBold: true, h: 0.48, fontSize: 10,
    });
    y += 0.5;
  });

  slide.addShape(pptx.ShapeType.roundRect, {
    x: 0.55, y: 6.75, w: 12.3, h: 0.35, rectRadius: 0.04,
    fill: { color: COLORS.paleBlue },
    line: { color: COLORS.blue, pt: 0.75 },
  });
  slide.addText(
    "Citation: Reg S-P \u00a7248.30(a)(3) - safeguards to prevent unauthorized access or use  |  NIST SP 800-53 AC-19, MP-7, SC-8",
    { x: 0.75, y: 6.81, w: 11.9, h: 0.24, fontFace: "Arial", fontSize: 10,
      bold: true, italic: true, color: COLORS.blue, margin: 0, align: "center" }
  );

  slide.addNotes(
    "MyAudit justification slide. Client's email said MyAudit overlaps with M365 DLP - misunderstanding of what MyAudit does. " +
    "MyAudit is endpoint / device DLP. M365 DLP is cloud / mail-flow DLP. Different layers, different scope. " +
    "Walk the table row-by-row: first five rows all 'Not covered' by M365 E3 DLP. These are the exfiltration paths that matter - USB, local download, print, clipboard, screen capture. " +
    "M365 DLP does cover rows 6-7 (email and SharePoint external sharing). We agree those are M365's job - MyAudit does not duplicate. " +
    "Last row (browser upload): partial coverage only with M365 E5 + Defender for Cloud Apps. On E3, this is a gap MyAudit closes. " +
    "Closing line: the overlap the client worried about does not exist. Complementary layers. " +
    "Alternative if AFFG wants an all-Microsoft stack: E5 + Purview Endpoint DLP - but requires E5 licensing across all covered users plus endpoint enrollment, usually more expensive than Technijian MyAudit included in the managed service."
  );
}

function veeamBackupSlide() {
  const slide = pptx.addSlide();
  addHeader(slide, "Tenant Backup",
    "Veeam Is Full-Tenant Backup - M365 Retention Is Not A Backup",
    "SEC Rule 17a-4(f) requires non-rewriteable, non-erasable preservation. Microsoft native retention does not meet that standard on its own.",
    9, COLORS.blue);

  addCard(slide, {
    x: 0.65, y: 2.3, w: 6.0, h: 4.35,
    fill: COLORS.white, line: COLORS.line, band: COLORS.red,
    label: "What M365 Retention Does NOT Cover",
    body: "- Tenant-level events (malicious admin, account takeover)\n- Ransomware encrypting OneDrive / SharePoint via sync\n- Accidental or malicious mass deletion across the tenant\n- Retention-policy changes that shorten preservation\n- Point-in-time restore at item, folder, or site granularity\n- SharePoint site recovery after structural damage\n- Teams channel, chat, and tab content recovery\n- Independent chain-of-custody outside the tenant\n\nMicrosoft retention is a policy inside the tenant. If the tenant is the attack surface, retention is not a backup.",
    citation: "SEC Rule 17a-4(f); FINRA 4511",
  });

  addCard(slide, {
    x: 6.85, y: 2.3, w: 6.0, h: 4.35,
    fill: COLORS.white, line: COLORS.line, band: COLORS.blue,
    label: "What Veeam Backup for M365 Adds",
    body: "- Full tenant backup: Exchange, SharePoint, OneDrive, Teams\n- Immutable off-tenant storage (WORM-capable)\n- Granular restore to item, folder, mailbox, or site level\n- Point-in-time recovery for ransomware scenarios\n- Independent encryption keys and access controls\n- Restore to alternate tenant for DR\n- Evidence chain suitable for 17a-4(f) attestation\n\nThe $100/month storage line is the backup repository. Not duplicative of M365 retention - it is the control that makes 17a-4(f) defensible.",
    citation: "SEC Rule 17a-4(b),(f); FINRA 4511; Reg S-P availability",
  });

  slide.addNotes(
    "Client's email suggested the $100/mo backup storage might overlap with Veeam pricing or M365 native retention. Address both. " +
    "First: Veeam Backup for M365 is NOT just email backup - it backs up the entire tenant: Exchange, SharePoint, OneDrive, Teams channels and chat. " +
    "Second: M365 native retention is a policy inside the tenant. If the tenant itself is the attack surface - compromised admin, ransomware via sync, retention edited by a bad actor, accidental mass deletion - retention cannot save you. Retention is not backup. " +
    "SEC 17a-4(f) requires non-rewriteable, non-erasable preservation. Microsoft's built-in retention doesn't meet that bar alone; Veeam with immutable storage does. " +
    "The $100/mo storage line is the repository cost. It is not duplicative - it is the control that makes 17a-4(f) compliance defensible. " +
    "Concrete example: 'If a user account is compromised tomorrow and files deleted, M365 recycle bin gives 93 days at best. If retention is edited by the attacker, even less. Veeam gives immutable point-in-time recovery independent of the tenant.'"
  );
}

function assessmentCadenceSlide() {
  const slide = pptx.addSlide();
  addHeader(slide, "Drift Detection",
    "Monthly Site And M365 Assessment - Why Monthly For A Regulated Firm",
    "FINRA 3110(c) requires internal inspections. Cadence should reflect how quickly configuration can drift.",
    10, COLORS.teal);

  addCard(slide, {
    x: 0.65, y: 2.3, w: 4.0, h: 4.0,
    fill: COLORS.paleTeal, line: COLORS.teal, band: COLORS.teal,
    label: "Recommended", title: "$50 / month",
    body: "Monthly Technijian assessment of physical site controls and M365 tenant settings.\n\nCovers: DLP policy state, IP whitelist rules, MFA enforcement, managed-endpoint compliance, audit log retention, backup job health, privileged role membership.\n\nMonthly evidence packet is the cleanest answer to a FINRA 3110(c) internal-inspection request.",
    citation: "FINRA 3110(c); FINRA 3120",
  });

  addCard(slide, {
    x: 4.83, y: 2.3, w: 4.0, h: 4.0,
    fill: COLORS.paleOrange, line: COLORS.orange, band: COLORS.orange,
    label: "Alternative", title: "$250 / quarter",
    body: "Quarterly cadence if AFFG prefers lower steady-state cost.\n\nPricing reflects the full labor cycle each quarter: install assessment tooling, scan, review findings, produce evidence packet, uninstall.\n\nQuarterly pricing is not 3x monthly because each cycle is a full engagement rather than an incremental checkpoint.",
    citation: "FINRA 3110(c) (minimum cadence)",
  });

  addCard(slide, {
    x: 9.01, y: 2.3, w: 3.65, h: 4.0,
    fill: COLORS.white, line: COLORS.line, band: COLORS.blue,
    label: "Why Not Skip It", title: "Drift Is The Risk",
    body: "Configuration drift between checkpoints is where examiner findings originate.\n\nAn MFA rule disabled three months ago, a DLP policy accidentally edited, an IP whitelist exception never removed - these are typically found only by periodic attested review.\n\nContinuous tooling detects; the assessment attests.",
  });

  slide.addNotes(
    "Clarify: the assessment is a MONTHLY compliance review of physical site AND M365 tenant configuration to detect drift and produce attested evidence. " +
    "Not automated monitoring - human-led review producing a signed evidence packet suitable for FINRA 3110(c) inspection. " +
    "Labor justification: each cycle deploys assessment tooling, scans site and tenant, reviews findings, produces evidence packet, decommissions tooling. That's why $250/qtr is not 3x $50/mo - each quarterly cycle is a full engagement. " +
    "Recommendation: MONTHLY at $50. Configuration drift between quarters is a common source of findings - an IP whitelist exception added and never removed, an MFA policy scoped wrong, a retention policy shortened. Monthly catches these. " +
    "If client insists on lower cadence: offer $250/qtr but document that monthly was recommended. " +
    "2024 Reg S-P amendments made annual program review explicit. Monthly assessment makes annual review trivial."
  );
}

function noDuplicationSlide() {
  const slide = pptx.addSlide();
  addHeader(slide, "No Duplication",
    "How The Stack Fits Together - Each Layer Solves A Distinct Problem",
    "If any layer is removed, a specific regulatory requirement becomes unenforced by technical means.",
    11, COLORS.blue);

  const colX = [0.55, 3.05, 7.6];
  const widths = [2.5, 4.55, 5.15];
  addTableHeaders(slide,
    ["Layer", "Unique Control Provided", "If Removed..."],
    colX, 2.25, widths, COLORS.blue);

  const rows = [
    ["Technijian Horizon VDI (7 roles)",
      "Client data stays in Technijian datacenter; supervised session boundary.",
      "Endpoint loss / compromise exposes regulated data. Reg S-P \u00a7248.30(a) safeguard weakens."],
    ["Technijian MyAudit (endpoint DLP)",
      "Blocks USB, local download, print, clipboard, screenshot on managed device.",
      "User can exfiltrate via USB or local download. M365 DLP does not cover this."],
    ["Technijian SSO / 2FA gateway",
      "Enforced, logged MFA on non-M365 portals with unified auditing.",
      "Custodian portal MFA is self-enabled, unauditable. Reg S-P 2024 gap."],
    ["IP whitelist + managed endpoint",
      "Blocks all access from personal devices or home networks.",
      "User MFAs into OneDrive / custodian from home PC and downloads locally."],
    ["Technijian Veeam Backup for M365",
      "Immutable full-tenant backup with granular restore.",
      "Ransomware, malicious admin, or mass deletion becomes unrecoverable. 17a-4(f) gap."],
    ["M365 native DLP + retention",
      "In-cloud data handling controls and mail-flow DLP.",
      "External sharing and mail exfiltration lose tenant-side controls."],
    ["Technijian monthly assessment",
      "Attested evidence that all above controls are operating as designed.",
      "Drift goes undetected. FINRA 3110(c) inspection obligation harder to evidence."],
  ];

  let y = 2.65;
  rows.forEach((row, index) => {
    addTableRow(slide, row, colX, y, widths, {
      fill: index % 2 === 0 ? COLORS.white : COLORS.paleDark,
      firstColBold: true, h: 0.58, fontSize: 9.5,
    });
    y += 0.6;
  });

  slide.addNotes(
    "The 'what if we removed this' slide - direct answer to the client's cost-reduction instinct. " +
    "Read down the rightmost column aloud: each row describes the specific regulatory gap that opens if that layer is removed. " +
    "The design is not maximalist; it is minimal given the compliance footprint. Every layer is present because of a distinct requirement. " +
    "Emphasize two rows: " +
    "SSO/2FA gateway - without this, MFA enforcement on custodian portals is self-service and unauditable, exactly what 2024 Reg S-P amendments address. " +
    "IP whitelist + managed endpoint - without this, a user at home on personal laptop is indistinguishable from a user at the office. MFA succeeds, data flows out. " +
    "Framing if client asks to trim further: 'Which row are you comfortable telling an examiner is not technically enforced?' Usually ends the line-by-line cost challenge."
  );
}

function revisedPathSlide() {
  const slide = pptx.addSlide();
  addHeader(slide, "Revised Path",
    "What The Revised Proposal Will Say",
    "Leaner where we can, firm where compliance requires it.",
    12, COLORS.blue);

  addBulletList(slide, [
    "Technijian Horizon VDI - dedicated per-user workstations in the Technijian datacenter, scoped to the 7 in-scope roles.",
    "Technijian MyAudit endpoint DLP retained - complementary to M365 DLP, not duplicative.",
    "Technijian SSO/2FA gateway retained to enforce MFA on custodian bank portals and all non-M365 systems.",
    "IP whitelist added for M365, OneDrive, and every custodian portal (office IP and Horizon VDI egress only).",
    "Technijian-managed endpoint compliance required for all access to regulated systems.",
    "Technijian Veeam Backup for M365 retained - full tenant backup (not duplicative of M365 retention).",
    "Technijian monthly site + M365 assessment retained at $50/mo (or $250/qtr alternative).",
    "Side-by-side control-to-citation map included as appendix to the revised proposal.",
    "One-time implementation fee reduced to reflect the 7-user Horizon VDI scope.",
  ], {
    x: 0.95, y: 2.35, w: 11.6, fontSize: 14,
    bulletColor: COLORS.teal, textColor: COLORS.dark, gap: 0.47,
  });

  slide.addNotes(
    "The commit slide - what will actually change in the revised proposal. " +
    "Frame: 'Here is what we heard, and here is what the revised proposal will say.' " +
    "Concessions: VDI scoped to 7 users (cost down), one-time implementation fee reduced, quarterly assessment offered as alternative to monthly. " +
    "Held firm: dedicated Technijian Horizon VDI workstations (not multi-session Technijian RDP - preserves the isolation posture in the original proposal), MyAudit retained (complementary, not duplicative), SSO/2FA retained (portal MFA gap), IP whitelist added (new and important), Veeam retained (tenant backup). " +
    "Ask for consent before leaving the meeting on: (a) 7-user dedicated VDI scope, (b) IP whitelist on M365 and custodian portals, (c) endpoint DLP via MyAudit, (d) assessment cadence. " +
    "Commit to delivering the revised proposal PDF within 3-5 business days with the control-to-citation appendix attached."
  );
}

function closingSlide() {
  const slide = pptx.addSlide();
  slide.background = { color: COLORS.dark };

  slide.addShape(pptx.ShapeType.rect, {
    x: 0, y: 6.95, w: 13.33, h: 0.12,
    fill: { color: COLORS.orange },
    line: { color: COLORS.orange, transparency: 100 },
  });

  addBrandMark(slide, 0.6, 0.5, true);

  slide.addShape(pptx.ShapeType.rect, {
    x: 0.6, y: 1.3, w: 0.9, h: 0.06,
    fill: { color: COLORS.orange },
    line: { color: COLORS.orange, transparency: 100 },
  });
  slide.addText("The Bottom Line", {
    x: 0.6, y: 1.55, w: 12.0, h: 0.6,
    fontFace: "Arial", fontSize: 32, bold: true,
    color: COLORS.white, margin: 0,
  });
  slide.addText(
    "A policy that says \"we don't store client data on personal devices\" is not a control. Reg S-P, FINRA 3110, and SEC 17a-4 require technical enforcement - and each layer in this design maps to a specific, cite-able requirement.",
    { x: 0.6, y: 2.35, w: 12.0, h: 1.4, fontFace: "Arial", fontSize: 16,
      color: "DCE5F2", margin: 0 }
  );

  addBulletList(slide, [
    "Scope is right-sized: 7 users in VDI, not firm-wide.",
    "No duplication: every layer solves a distinct regulatory obligation.",
    "Cost is reduced where possible without weakening the compliance posture.",
    "Every control maps to a specific FINRA or SEC citation.",
  ], {
    x: 0.9, y: 3.9, w: 11.5, fontSize: 16,
    bulletColor: COLORS.teal, textColor: COLORS.white, gap: 0.55,
  });

  slide.addText("Technijian  |  AFFG IT Compliance Strategy  |  April 15, 2026", {
    x: 0.6, y: 6.45, w: 8.0, h: 0.25,
    fontFace: "Arial", fontSize: 10, color: "BFD0E5", margin: 0,
  });

  slide.addNotes(
    "Close the meeting. Re-state the headline: policy is not a control, and every layer maps to a specific citation. " +
    "Confirm decisions captured: VDI scope (7 users), desktop model (dedicated VDI workstations), portal MFA approach, IP whitelist scope, assessment cadence. " +
    "Next steps: revised proposal PDF within 3-5 business days, includes control-to-citation appendix, reflects today's decisions. " +
    "Offer a follow-up call after AFFG's internal review for any remaining questions before signature. " +
    "Thank the client for the thoroughness of their written response - this engagement level is what makes the partnership successful."
  );
}

coverSlide();
executiveSummarySlide();
regulatoryFrameworkSlide();
controlMappingSlide();
vdiRequiredSlide();
desktopComparisonSlide();
mfaAndIpWhitelistSlide();
endpointDlpSlide();
veeamBackupSlide();
assessmentCadenceSlide();
noDuplicationSlide();
revisedPathSlide();
closingSlide();

pptx.writeFile({ fileName: outPath });
console.log(`Presentation generated: ${outPath}`);
