# COMPLIANCE REVIEW

## Business Continuity Plan

**American Fundstars Financial Group LLC**

**Prepared for:** Dually Registered RIA / Broker-Dealer

**Regulatory Framework:** SEC Reg S-P (2024 Amendments) | FINRA Rule 4370 | FINRA Rule 3110

**Date:** March 6, 2026

**Prepared by:** Technijian

**CONFIDENTIAL**

---

# 1. Executive Summary

This report presents a comprehensive compliance review of the Business Continuity Plan (BCP) for American Fundstars Financial Group LLC ("AFS"), a dually registered investment adviser (RIA) and broker-dealer regulated by the Securities and Exchange Commission (SEC) and the Financial Industry Regulatory Authority (FINRA).

The review was conducted against the following regulatory requirements:

- SEC Regulation S-P (as amended May 2024) -- Privacy of Consumer Financial Information and Safeguarding Customer Information, with compliance now mandatory for covered institutions
- FINRA Rule 4370 -- Business Continuity Plans and Emergency Contact Information
- FINRA Rule 3110 -- Supervision (as it relates to supervisory continuity during disruptions)

**Important Regulatory Note Regarding the SEC Cybersecurity Risk Management Rule:**

The SEC's proposed Cybersecurity Risk Management Rule for Investment Advisers (originally proposed in February 2022) was formally withdrawn on June 12, 2025, as part of 14 rule proposals withdrawn by the current SEC administration. This means there is no standalone SEC cybersecurity rule for RIAs/funds. However, the 2024 amendments to Regulation S-P remain in full effect and impose substantial cybersecurity-related obligations, including mandatory incident response programs, breach notification, and service provider oversight. Additionally, the SEC continues to examine cybersecurity practices as part of its regulatory oversight.

## Overall Assessment

The BCP in its current form has significant compliance gaps that require immediate remediation. While the plan provides a general framework for business continuity, it falls materially short of current regulatory requirements, particularly in light of the 2024 Reg S-P amendments that imposed new incident response, notification, service provider oversight, and recordkeeping obligations.

## Findings Summary

| Severity | Count | Description |
|----------|-------|-------------|
| CRITICAL | 3 | Must be remediated immediately -- represents direct regulatory violations |
| HIGH | 7 | Should be remediated within 30-60 days -- significant gaps likely to draw examination scrutiny |
| MEDIUM | 9 | Should be remediated within 90 days -- deficiencies that should be addressed proactively |
| LOW | 1 | Best practice enhancements for improved operational resilience |

---

# 2. Detailed Findings

## 2.1 Critical Findings -- Immediate Remediation Required

These findings represent direct regulatory violations under the amended Reg S-P framework. Non-compliance exposes the firm to enforcement action, examination deficiency letters, and potential fines.

### Finding 1: Incident Response Program

**Applicable Rule:** SEC Reg S-P (2024 Amendments)

**Finding:** BCP has no written incident response program for data breaches or unauthorized access to customer information. The 2024 Reg S-P amendments require covered institutions to develop, implement, and maintain written policies and procedures for detecting, responding to, and recovering from unauthorized access to customer information.

**Recommendation:** Create a standalone Incident Response Plan (IRP) or integrate a comprehensive incident response section into the BCP covering: detection procedures, containment protocols, forensic investigation steps, escalation matrix, evidence preservation, and recovery procedures.

### Finding 2: Customer Breach Notification

**Applicable Rule:** SEC Reg S-P (2024 Amendments)

**Finding:** No procedures exist for notifying affected individuals within 30 days of determining that sensitive customer information was, or is reasonably likely to have been, accessed or used without authorization. This is now a mandatory regulatory obligation.

**Recommendation:** Add a Breach Notification section specifying: criteria for determining when notification is required, 30-day notification timeline, content requirements for notification letters, process for determining scope of affected individuals, and template notification letters.

### Finding 3: Service Provider Oversight

**Applicable Rule:** SEC Reg S-P (2024 Amendments)

**Finding:** The BCP references third-party vendors (AT&T, RingCentral, AWS, Microsoft 365, Synology) but contains no service provider oversight framework. Amended Reg S-P requires written policies for engaging in oversight of service providers to ensure they protect against unauthorized access, including requiring 72-hour breach notification from service providers.

**Recommendation:** Add a Service Provider Management section covering: due diligence procedures for vendor selection, contractual requirements for 72-hour breach notification, ongoing monitoring of service provider security posture, and inventory of all service providers with access to customer information.

## 2.2 High-Priority Findings -- 30-60 Day Remediation

These findings represent significant compliance gaps that are likely to be identified during SEC or FINRA examinations and should be addressed promptly.

### Finding 4: Recordkeeping

**Applicable Rule:** SEC Reg S-P (2024 Amendments)

**Finding:** No recordkeeping provisions for compliance with Reg S-P requirements. The amendments require maintenance of written records documenting compliance, including copies of policies and procedures, incident reports, and notifications provided to affected individuals. Records must be retained for five years.

**Recommendation:** Add recordkeeping requirements specifying: types of records to be maintained (policies, incident reports, notifications, testing results), five-year retention period, storage location and format, and designated custodian of records.

### Finding 5: Data Backup & Recovery

**Applicable Rule:** FINRA Rule 4370(c)(1)

**Finding:** Data backup descriptions are vague and incomplete. References to 'Synology 2 Bay NAS DiskStation' and 'Cloud facilities' lack specifics on backup frequency, RPO/RTO for data specifically, encryption standards, geographic separation requirements, and restoration testing procedures. Hard copy backup procedures are not addressed at all.

**Recommendation:** Expand data backup section to specify: backup frequency and schedule, RPO and RTO for each data category, encryption standards (at rest and in transit), geographic separation of backup sites, hard copy document backup procedures, and regular restoration testing with documented results.

### Finding 6: Mission Critical Systems

**Applicable Rule:** FINRA Rule 4370(c)(2)

**Finding:** The BCP does not identify or define 'mission critical systems' as required. FINRA defines these as systems necessary for prompt and accurate processing of securities transactions, including order taking, execution, clearance and settlement, customer account maintenance, and delivery of funds and securities. The plan references general systems but does not map them to mission-critical functions.

**Recommendation:** Create a Mission Critical Systems Inventory that maps each system to its business function, identifies the owner, documents dependencies, specifies RTO/RPO, and identifies alternate processing capabilities. Include systems for: order management, trade execution, clearing/settlement, customer account access, and fund/securities delivery.

### Finding 7: Financial & Operational Assessment

**Applicable Rule:** FINRA Rule 4370(c)(3)

**Finding:** The BCP contains no written procedures for conducting financial and operational assessments following an SBD. FINRA requires a set of written procedures that allow a member to identify changes in its operational, financial, and credit risk exposures.

**Recommendation:** Add a Financial & Operational Assessment section with procedures for: assessing the firm's ability to fund operations during disruption, evaluating changes to credit risk exposure, determining the firm's ability to meet margin/capital requirements, and establishing decision criteria for continuing or suspending operations.

### Finding 8: Customer Access to Funds & Securities

**Applicable Rule:** FINRA Rule 4370(c)(10)

**Finding:** The BCP states customers should have access to available funds and that 'orders and requests for funds or securities could be delayed during this period,' but provides no specific procedures for ensuring prompt access to funds and securities if the firm cannot continue business. This is a core FINRA 4370 requirement.

**Recommendation:** Add detailed procedures for: how customer accounts will be transferred or made accessible, arrangements with carrying/clearing firms for direct customer access, specific timelines for restoring customer access, and procedures if the firm determines it cannot continue business (including SIPC notification).

### Finding 15: Supervisory Continuity

**Applicable Rule:** FINRA Rule 3110

**Finding:** The BCP does not address how supervisory functions, including Written Supervisory Procedures (WSPs), will be maintained during a disruption. Rule 3110 requires ongoing supervision of associated persons, communications review, and customer account monitoring. A BCP that does not address continuity of these functions creates a supervision gap.

**Recommendation:** Add a Supervisory Continuity section addressing: designation of alternate supervisory personnel, procedures for maintaining communications review during disruption, customer account monitoring continuity, trade supervision procedures at alternate locations, and documentation of supervisory activities during disruption.

### Finding 17: Cybersecurity Integration

**Applicable Rule:** SEC Reg S-P / FINRA Best Practices

**Finding:** The 'Unauthorized Access' subsection is only two bullet points with extremely vague language ('Questionable activity will be monitored until resolution'). There are no references to cybersecurity controls, intrusion detection, endpoint protection, multi-factor authentication, network segmentation, or coordination with law enforcement. While the standalone SEC Cybersecurity Risk Management Rule was withdrawn in June 2025, cybersecurity remains a core SEC examination focus area and is integral to Reg S-P compliance.

**Recommendation:** Significantly expand the cybersecurity section or reference a standalone Cybersecurity Incident Response Plan, covering: intrusion detection and prevention systems, endpoint protection, MFA requirements, network segmentation, forensic investigation procedures, law enforcement coordination, and cyber insurance coverage.

## 2.3 Medium-Priority Findings -- 90 Day Remediation

These findings represent deficiencies that should be addressed proactively to demonstrate a robust compliance program.

### Finding 9: Alternate Communications -- Customers

**Applicable Rule:** FINRA Rule 4370(c)(4)

**Finding:** Customer communication procedures are vague. The plan states AFS will 'assess which means of communication are still available' but does not provide specific alternate communication channels, customer notification procedures, or website/social media messaging plans for varying disruption scenarios.

**Recommendation:** Define specific alternate communication methods for each disruption scenario (firm-only, building, district, city, regional), including: alternate phone numbers, backup email systems, website notifications, social media communications, and written correspondence procedures.

### Finding 10: Alternate Communications -- Employees

**Applicable Rule:** FINRA Rule 4370(c)(5)

**Finding:** Employee communication relies on a basic 'call tree' but lacks specifics on alternate communication methods beyond phone and email. No mention of mass notification systems, backup communication tools, or procedures when primary channels are down.

**Recommendation:** Expand employee communication section to include: mass notification system details, backup communication tools (e.g., text/SMS, messaging apps), out-of-band communication procedures, and regular testing of the call tree with documented results.

### Finding 11: Critical Business Constituent Impact

**Applicable Rule:** FINRA Rule 4370(c)(7)

**Finding:** No procedures for assessing impact on critical business constituents, banks, and counterparties. The BCP does not identify key counterparty relationships or plans for maintaining those relationships during a disruption.

**Recommendation:** Add a section identifying all critical business constituents (clearing firms, custodians, banks, counterparties) and procedures for: notifying them of disruptions, maintaining operational connectivity, accessing backup systems, and documenting impact assessments.

### Finding 12: Regulatory Reporting

**Applicable Rule:** FINRA Rule 4370(c)(8)

**Finding:** While the BCP mentions communication with regulators generally, it lacks specific procedures for maintaining regulatory reporting obligations (FOCUS reports, trade reporting, etc.) during a disruption.

**Recommendation:** Add specific procedures for maintaining regulatory reporting during disruption, including: list of all regulatory filings and deadlines, alternate methods for submitting reports, designated personnel for regulatory reporting, and procedures for requesting extensions if needed.

### Finding 13: BCP Disclosure to Customers

**Applicable Rule:** FINRA Rule 4370(e)

**Finding:** The BCP contains no provisions for customer disclosure. FINRA requires firms to provide a BCP summary disclosure at account opening, post it on the website, and mail it upon request. The disclosure must address disruptions of varying scope (firm-only, building, district, city, regional).

**Recommendation:** Create a BCP Disclosure Statement and add procedures for: providing disclosure at account opening, posting on firm website, mailing upon request, updating when material changes occur, and addressing varying disruption scenarios.

### Finding 14: FINRA Emergency Contact Reporting

**Applicable Rule:** FINRA Rule 4370(f)

**Finding:** The BCP identifies two emergency contacts but does not reference the FINRA Contact System (FCS) or the requirement to promptly update contact information following material changes and review annually by the 17th business day after year-end.

**Recommendation:** Add procedures for: registering and maintaining emergency contacts in the FINRA Contact System, prompt updates upon material changes, annual review by the 17th business day following year-end, and documenting all updates and reviews.

### Finding 16: Senior Management Approval

**Applicable Rule:** FINRA Rule 4370(b)

**Finding:** The BCP does not reflect approval by a registered principal as required by FINRA Rule 4370(b). There is no signature block, approval date, or evidence of annual review by senior management.

**Recommendation:** Add a formal approval section with: signature block for a registered principal, date of approval, annual review certification, and version control/change log.

### Finding 18: Information Disposal

**Applicable Rule:** SEC Reg S-P

**Finding:** No procedures for proper disposal of customer information and consumer report information. Reg S-P requires covered institutions to properly dispose of consumer information.

**Recommendation:** Add data disposal procedures covering: methods for destroying electronic records (e.g., secure wiping, degaussing), methods for destroying hard copy records (e.g., cross-cut shredding), documentation requirements for disposal activities, and third-party disposal vendor oversight.

### Finding 19: Document Staleness

**Applicable Rule:** FINRA Rule 4370(b)

**Finding:** The document is dated October 2023 (over two years old). Last metadata edit was by 'Joshua Yang' but the emergency contacts list only Fan Feng and Iris Liu. Technology references may be outdated (Synology NAS, specific AT&T services). Annual review documentation is absent.

**Recommendation:** Conduct a comprehensive update including: verifying all personnel, contact information, and titles are current; updating all technology references; documenting the annual review with date and reviewer; and implementing version control.

## 2.4 Low-Priority Findings -- Best Practice Enhancements

### Finding 20: Alternate Site Specifics

**Applicable Rule:** FINRA Rule 4370(c)(6)

**Finding:** The alternate site at '84 Spacial, Irvine, CA 92618' is identified but no details on its capabilities, capacity, connectivity, or readiness are provided. The plan also mentions 'a hotel conference room' as a potential option but provides no pre-arranged agreements.

**Recommendation:** Document alternate site capabilities including: available infrastructure (desks, connectivity, phones), capacity (number of personnel supported), pre-arranged agreements with the location, time required to activate, and regular testing of alternate site readiness.

---

# 3. Findings Matrix

The following matrix provides a consolidated view of all findings for tracking and remediation purposes.

| # | Category | Rule | Severity | Recommendation Summary |
|---|----------|------|----------|----------------------|
| 1 | Incident Response Program | SEC Reg S-P (2024 Amendments) | CRITICAL | Create a standalone Incident Response Plan (IRP) or integrate a comprehensive incident response section into the BCP |
| 2 | Customer Breach Notification | SEC Reg S-P (2024 Amendments) | CRITICAL | Add a Breach Notification section specifying: criteria for determining when notification is required, 30-day notification timeline |
| 3 | Service Provider Oversight | SEC Reg S-P (2024 Amendments) | CRITICAL | Add a Service Provider Management section covering: due diligence procedures for vendor selection, contractual requirements for 72-hour breach notification |
| 4 | Recordkeeping | SEC Reg S-P (2024 Amendments) | HIGH | Add recordkeeping requirements specifying: types of records to be maintained, five-year retention period |
| 5 | Data Backup & Recovery | FINRA Rule 4370(c)(1) | HIGH | Expand data backup section to specify: backup frequency and schedule, RPO and RTO for each data category |
| 6 | Mission Critical Systems | FINRA Rule 4370(c)(2) | HIGH | Create a Mission Critical Systems Inventory that maps each system to its business function |
| 7 | Financial & Operational Assessment | FINRA Rule 4370(c)(3) | HIGH | Add a Financial & Operational Assessment section with procedures for assessing firm operations during disruption |
| 8 | Customer Access to Funds & Securities | FINRA Rule 4370(c)(10) | HIGH | Add detailed procedures for customer account transfer/access and clearing firm arrangements |
| 9 | Alternate Communications -- Customers | FINRA Rule 4370(c)(4) | MEDIUM | Define specific alternate communication methods for each disruption scenario |
| 10 | Alternate Communications -- Employees | FINRA Rule 4370(c)(5) | MEDIUM | Expand employee communication section to include mass notification and backup tools |
| 11 | Critical Business Constituent Impact | FINRA Rule 4370(c)(7) | MEDIUM | Add a section identifying all critical business constituents and disruption procedures |
| 12 | Regulatory Reporting | FINRA Rule 4370(c)(8) | MEDIUM | Add specific procedures for maintaining regulatory reporting during disruption |
| 13 | BCP Disclosure to Customers | FINRA Rule 4370(e) | MEDIUM | Create a BCP Disclosure Statement and add distribution procedures |
| 14 | FINRA Emergency Contact Reporting | FINRA Rule 4370(f) | MEDIUM | Add procedures for FINRA Contact System registration and annual review |
| 15 | Supervisory Continuity | FINRA Rule 3110 | HIGH | Add a Supervisory Continuity section with alternate supervisory personnel and procedures |
| 16 | Senior Management Approval | FINRA Rule 4370(b) | MEDIUM | Add a formal approval section with signature block and version control |
| 17 | Cybersecurity Integration | SEC Reg S-P / FINRA Best Practices | HIGH | Significantly expand the cybersecurity section or reference a standalone CIRP |
| 18 | Information Disposal | SEC Reg S-P | MEDIUM | Add data disposal procedures for electronic and hard copy records |
| 19 | Document Staleness | FINRA Rule 4370(b) | MEDIUM | Conduct comprehensive update of personnel, contacts, technology references |
| 20 | Alternate Site Specifics | FINRA Rule 4370(c)(6) | LOW | Document alternate site capabilities, capacity, and pre-arranged agreements |

---

# 4. Recommended Remediation Roadmap

## Phase 1: Immediate (0-30 Days)

- Draft and implement a written Incident Response Program addressing Reg S-P requirements (Finding 1)
- Create customer breach notification procedures with 30-day timeline (Finding 2)
- Establish service provider oversight framework with 72-hour notification requirements (Finding 3)
- Expand cybersecurity incident response procedures beyond current two bullet points (Finding 17)

## Phase 2: Short-Term (30-60 Days)

- Implement Reg S-P recordkeeping requirements with 5-year retention (Finding 4)
- Create detailed data backup and recovery specifications with RPO/RTO (Finding 5)
- Build Mission Critical Systems Inventory mapped to business functions (Finding 6)
- Develop Financial and Operational Assessment procedures (Finding 7)
- Document specific customer access to funds/securities procedures (Finding 8)
- Add supervisory continuity provisions for FINRA 3110 compliance (Finding 15)

## Phase 3: Medium-Term (60-90 Days)

- Enhance customer and employee alternate communication plans (Findings 9, 10)
- Document critical business constituent relationships and impact procedures (Finding 11)
- Add regulatory reporting continuity procedures (Finding 12)
- Create and distribute BCP Disclosure Statement per FINRA 4370(e) (Finding 13)
- Register/update emergency contacts in FINRA Contact System (Finding 14)
- Obtain registered principal approval and establish version control (Finding 16)
- Add data disposal procedures (Finding 18)
- Conduct comprehensive document refresh and update (Finding 19)
- Document alternate site capabilities and agreements (Finding 20)

---

# 5. Areas of Strength

While significant gaps exist, the current BCP does include several foundational elements:

- General framework for plan activation with three severity levels and defined escalation criteria
- Identification of an alternate office location in Irvine, CA with remote access provisions
- BCP Coordinator and Committee structure with designated authority for declaring an SBD
- Pandemic planning section addressing remote work, staff travel restrictions, and hygiene protocols
- Annual testing and compliance review provisions (though documentation is absent)
- Business Process Criticality Levels with five-tier MAD framework
- Reconstitution phase procedures for returning to normal operations

---

# 6. Disclaimer

This compliance review is provided for informational purposes only and does not constitute legal advice. The analysis reflects the regulatory landscape as of March 2026. Firms should consult with qualified securities counsel to ensure full compliance with all applicable rules and regulations. Regulatory requirements are subject to change, and firms should monitor SEC and FINRA guidance for updates.
