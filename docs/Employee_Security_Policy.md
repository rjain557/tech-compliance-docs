# Technijian, Inc.

# Employee Security Policy

**Version:** 1.0
**Date:** April 6, 2026
**Classification:** Confidential
**Document Owner:** Ravi Jain - CEO/Owner
**Approved By:** Ravi Jain - CEO/Owner
**Next Review Date:** April 6, 2027

---

## 1. Purpose

This policy establishes the security requirements and responsibilities for all personnel throughout the employment lifecycle at Technijian, Inc. ("Technijian"). As a managed IT services provider entrusted with sensitive client data across healthcare, financial services, and other regulated industries, Technijian requires a workforce that is properly vetted, trained, equipped, and governed to protect information assets.

This policy addresses:

- Pre-employment screening and verification
- Security onboarding and account provisioning
- Ongoing security awareness training and compliance
- Role-based training for specialized responsibilities
- Offboarding procedures and access revocation
- Disciplinary actions for policy violations
- Remote work and BYOD security requirements
- Whistleblower protections under federal trade secret law

This policy supplements the Technijian Information Security Program (WISP) and applies to all employees, contractors, subcontractors, and temporary personnel.

### 1.1 Scope

This policy applies to:

- All Technijian employees (full-time, part-time, and temporary)
- All contractors, subcontractors, and consultants performing work for or on behalf of Technijian
- All individuals with access to Technijian or client systems, data, or facilities
- All phases of the employment/engagement lifecycle: pre-employment, onboarding, ongoing employment, and offboarding
- Technijian headquarters at 18 Technology Drive, Suite 141, Irvine, CA 92618, the TPX data center, and all remote work locations

---

## 2. Pre-Employment Screening

### 2.1 Background Checks

All prospective employees and contractors must successfully complete a background screening before being granted access to Technijian or client systems, data, or facilities.

| Screening Component | Applicability | Standard |
|---|---|---|
| **Criminal History Check** | All personnel | Federal and state criminal records, 7-year lookback |
| **Employment Verification** | All personnel | Verification of previous 3 employers or 7 years of employment history |
| **Education Verification** | All personnel where degree is a stated qualification | Verification of highest degree claimed |
| **Professional License Verification** | Where applicable (e.g., CPA, PE) | Verification of current valid license |
| **Credit Check** | Personnel with access to financial data or payment systems | Per FCRA requirements with applicant consent |
| **Identity Verification** | All personnel | Government-issued photo ID; E-Verify or I-9 verification |
| **Sex Offender Registry Check** | All personnel | National sex offender registry |
| **Global Sanctions / Watch List Check** | All personnel | OFAC, BIS, and other applicable sanctions lists |

**Additional Requirements:**

- Background checks are conducted by an approved third-party screening provider in compliance with the Fair Credit Reporting Act (FCRA) and applicable state laws
- Applicants are notified and provide written consent before screening is initiated
- Adverse findings are reviewed by Human Resources and the CEO/Owner before a hiring decision is made
- Rescreening is conducted every 3 years for employees with access to Restricted data or client environments
- Client-specific background check requirements (e.g., HIPAA for healthcare clients, FINRA for financial services) are met before granting access to the client environment

### 2.2 Non-Disclosure Agreement (NDA)

All personnel must execute a Non-Disclosure and Confidentiality Agreement before receiving access to any Technijian or client information. The NDA covers:

- Protection of Technijian proprietary information, trade secrets, and business strategies
- Protection of client data, including NPI, PHI, PII, and all Confidential and Restricted information
- Obligations that survive termination of employment or contract
- Remedies for breach, including injunctive relief and damages
- Compliance with the Defend Trade Secrets Act (DTSA) whistleblower provisions (see Section 12)

---

## 3. Onboarding

### 3.1 Security Awareness Training

All new personnel must complete security awareness training within 30 calendar days of their start date. New personnel are not granted access to client environments until initial security awareness training is complete.

**Training Content:**

| Topic | Description |
|---|---|
| Information Security Program Overview | Technijian's WISP, policies, and security culture |
| Data Classification and Handling | Classification levels (Public, Internal, Confidential, Restricted), handling requirements, labeling |
| Acceptable Use | Permitted and prohibited use of Technijian and client systems, internet, email, and software |
| Password and Authentication | Password requirements, MFA usage, credential protection, phishing awareness |
| Email Security | Phishing identification, BEC awareness, reporting suspicious emails |
| Social Engineering | Recognition and response to social engineering attempts (phone, in-person, online) |
| Incident Reporting | How to identify and report security incidents, contact information, escalation procedures |
| Data Loss Prevention | DLP controls, restrictions on data transfer, removable media policy |
| Remote Work Security | VPN requirements, home office security, public Wi-Fi risks |
| Client Data Protection | Client data segregation, separate credentials, confidentiality obligations |
| Physical Security | Clean desk policy, visitor management, badge usage, secure areas |
| Regulatory Overview | HIPAA, PCI-DSS, SOC 2, GDPR basics relevant to the employee's role |

### 3.2 Acceptable Use Policy (AUP) Acknowledgment

All new personnel must read and sign the Acceptable Use Policy on or before their first day of work. The AUP covers:

- Authorized use of Technijian systems, networks, email, internet, and cloud services
- Prohibition of personal use that interferes with business operations or security
- Prohibition of installing unauthorized software
- Prohibition of accessing, storing, or transmitting inappropriate, illegal, or unauthorized content
- Prohibition of circumventing security controls
- Acknowledgment that Technijian systems are subject to monitoring
- Acknowledgment that violations may result in disciplinary action up to and including termination

### 3.3 Account Provisioning

Account provisioning for new personnel follows the process defined in the Access Control Policy:

- Standard user account created per role-based template on Day 1
- MFA enrolled and verified on Day 1
- Endpoint provisioned with required security controls (CrowdStrike Falcon EDR, BitLocker/FileVault, MDM enrollment) on Day 1
- Client environment access provisioned upon client assignment with account manager approval
- Privileged access provisioned only after Security Officer approval and PAM onboarding
- All provisioning actions documented in the ticketing system

---

## 4. Ongoing Security Requirements

### 4.1 Annual Security Awareness Training

All personnel must complete security awareness training annually. Annual training refreshes and updates the topics covered in onboarding training and includes:

- Review of current threat landscape and emerging attack techniques
- Lessons learned from actual security incidents (anonymized)
- Policy updates and changes since the last training cycle
- Regulatory updates relevant to Technijian's client base
- Role-specific security topics (see Section 5)

**Training Requirements:**

| Requirement | Standard |
|---|---|
| **Completion Deadline** | Within 30 days of assignment |
| **Passing Score** | 80% or higher on assessment |
| **Remediation** | Personnel who do not pass must retake training within 14 days |
| **Non-Compliance** | Failure to complete training within the deadline may result in access suspension |
| **Record Retention** | Training completion records retained for a minimum of 3 years |

### 4.2 Quarterly Phishing Simulations

Technijian conducts simulated phishing campaigns on a quarterly basis to measure and improve personnel resilience to phishing attacks.

| Element | Standard |
|---|---|
| **Frequency** | Quarterly (minimum 4 campaigns per year) |
| **Scope** | All personnel with email accounts |
| **Scenarios** | Varied and realistic scenarios including credential harvesting, malware delivery, BEC simulation, and spear phishing |
| **Metrics Tracked** | Click rate, credential submission rate, report rate, time to report |
| **Target Click Rate** | Below 5% organization-wide |
| **Immediate Feedback** | Personnel who interact with a simulated phish receive immediate educational feedback |
| **Repeat Offenders** | Personnel who fail 2 or more simulations within a 12-month period are required to complete additional targeted training within 14 days and are flagged for manager notification |
| **Reporting** | Quarterly phishing simulation results are reported to the Security Officer and CEO/Owner |

### 4.3 Policy Acknowledgment

All personnel must acknowledge the following policies annually:

- Information Security Program (WISP)
- Acceptable Use Policy
- Data Classification and Retention Policy
- Access Control Policy
- This Employee Security Policy
- Any additional policies applicable to their role or client assignments

Acknowledgment records are maintained by Human Resources and are available for audit upon request.

---

## 5. Role-Based Training

In addition to general security awareness training, personnel in the following roles must complete specialized training:

| Role | Additional Training Topics | Frequency |
|---|---|---|
| **Engineers with Client Access** | Client data handling, client-specific security requirements, secure remote access procedures, incident escalation for client environments, credential management best practices | Annual + upon new client assignment |
| **Personnel with Privileged Access** | Privileged access management procedures, session recording awareness, JIT access workflows, separation of duties, privileged account attack vectors | Annual + upon PAM onboarding |
| **Personnel Handling PHI** | HIPAA Security Rule requirements, PHI handling and minimum necessary standard, breach notification obligations, HIPAA sanctions | Annual + upon assignment to healthcare client |
| **Personnel Handling Payment Card Data** | PCI-DSS requirements, cardholder data handling, secure payment processing, PCI incident reporting | Annual + upon assignment to PCI-scoped work |
| **Personnel Handling NPI/Financial Data** | GLB Act and FTC Safeguards Rule requirements, SEC/FINRA data handling, NPI classification and protection | Annual + upon assignment to financial services client |
| **IT Operations and System Administrators** | Secure configuration management, patch management procedures, vulnerability management, log review and monitoring, change management | Annual |
| **Incident Responders** | Incident response plan procedures, forensic evidence preservation, communication protocols, tabletop exercise participation | Annual + tabletop exercises quarterly |
| **Human Resources** | Background check procedures, onboarding/offboarding security checklists, personnel file security, FCRA compliance | Annual |

---

## 6. Offboarding

### 6.1 Termination Procedures

Upon termination of employment or contract (voluntary or involuntary), the following actions are executed:

| Step | Action | Timeline | Responsible |
|---|---|---|---|
| 1 | HR notifies IT Operations of termination | Immediately upon decision (before employee is notified for involuntary terminations) | Human Resources |
| 2 | All system access disabled (Active Directory, Azure AD, M365, VPN, RMM, client systems) | **Same day** — within 1 hour for involuntary terminations | IT Operations |
| 3 | Email access revoked; auto-reply or forwarding configured per manager request | **Same day** | IT Operations |
| 4 | Cloud service access revoked (Azure, AWS, SaaS platforms) | **Same day** | IT Operations |
| 5 | Client environment credentials rotated for all clients the individual had access to | **Same day** | IT Operations / Account Managers |
| 6 | MFA registrations removed | **Same day** | IT Operations |
| 7 | Privileged account disabled; privileged credentials rotated | **Same day** | Security Officer / IT Operations |
| 8 | Remote access (VPN, ZTNA) revoked | **Same day** | IT Operations |
| 9 | Physical access revoked (badges, keys, fobs) | **Same day** | Facilities / HR |
| 10 | Company equipment returned (laptop, phone, tokens, external drives, badges) | Within 3 business days; immediate for involuntary terminations | HR / IT Operations |
| 11 | Returned equipment inspected and data securely wiped | Within 5 business days of return | IT Operations |
| 12 | Shared account credentials rotated (if any shared accounts were accessed) | **Same day** | IT Operations |
| 13 | Offboarding checklist completed, signed, and filed | Within 3 business days | HR / IT Operations |
| 14 | Exit interview (security reminder of ongoing NDA obligations) | Last day of employment | Human Resources |

**Same-day deactivation is mandatory and non-negotiable.** IT Operations must maintain the capability to execute emergency access revocation within 1 hour of notification.

### 6.2 Equipment Return

- All company-owned equipment must be returned upon termination, including laptops, mobile devices, monitors, docking stations, hardware security tokens, external storage devices, and printed materials containing Confidential or Restricted information
- Equipment must be returned in person (for on-site employees) or via prepaid tracked shipment (for remote employees) within 3 business days
- Failure to return equipment is reported to HR for further action, including potential legal recourse
- Returned devices are securely wiped per NIST SP 800-88 before reassignment or disposal

### 6.3 Credential Rotation

Upon any personnel departure, the following credential rotation is mandatory:

- All client environment credentials the individual had access to
- All shared or group account credentials the individual may have known
- All service account credentials where the individual had direct password knowledge
- Wi-Fi pre-shared keys for any networks the individual accessed
- API keys, tokens, or secrets the individual managed or had access to

---

## 7. Disciplinary Actions

### 7.1 Violation Categories

| Category | Examples | Potential Consequence |
|---|---|---|
| **Minor Violation** | Failure to lock workstation, late training completion, weak password detected | Verbal warning, mandatory remedial training |
| **Moderate Violation** | Sharing credentials, unauthorized software installation, failure to report a suspected incident, circumventing DLP controls | Written warning, access restriction, mandatory training, performance impact |
| **Serious Violation** | Unauthorized access to data or systems, unauthorized disclosure of Confidential data, deliberate circumvention of security controls, negligent handling of Restricted data | Final written warning, suspension, termination, legal action |
| **Critical Violation** | Theft of data or equipment, deliberate sabotage, aiding unauthorized access, intentional data breach, violation of client trust | Immediate termination, legal action, law enforcement referral |

### 7.2 Disciplinary Process

1. The Security Officer investigates the alleged violation and documents findings
2. HR is notified and participates in the disciplinary process
3. The employee is notified of the findings and given an opportunity to respond
4. The appropriate disciplinary action is determined by the Security Officer, HR, and CEO/Owner based on the severity, intent, impact, and the employee's history
5. Disciplinary action is documented in the employee's personnel file
6. Systemic issues identified through violations are addressed through policy updates and additional training
7. For contractors and subcontractors, violations are addressed per the terms of the contract, which may include immediate termination of the engagement

### 7.3 Mandatory Reporting

All personnel have a duty to report suspected security violations, incidents, or policy breaches immediately to:

- Direct supervisor
- Security Officer (Ravi Jain)
- Anonymous reporting channel (if established)

Retaliation against individuals who report suspected violations in good faith is strictly prohibited and will itself be treated as a serious policy violation.

---

## 8. Remote Work Security

### 8.1 Remote Work Requirements

All personnel working remotely must comply with the following security requirements:

| Requirement | Standard |
|---|---|
| **VPN/ZTNA** | All access to Technijian and client networks must be through the corporate VPN or approved ZTNA solution |
| **Endpoint Security** | Remote devices must have active CrowdStrike Falcon EDR, current patches, full-disk encryption, and active screen lock (5-minute maximum timeout) |
| **Physical Security** | Work area must prevent unauthorized viewing of screens displaying Confidential or Restricted data. Screens must be locked when stepping away |
| **Network Security** | Connection via secured home Wi-Fi with WPA2 or WPA3 encryption. Public Wi-Fi is prohibited for accessing Technijian or client systems unless VPN is active with split tunneling disabled |
| **Printing** | Printing of Confidential or Restricted data at home is prohibited unless explicitly approved. Any approved printed materials must be cross-cut shredded when no longer needed |
| **Voice/Video Calls** | Discussions involving Confidential or Restricted information must be conducted in a private space where conversations cannot be overheard |
| **Shared Spaces** | Technijian work must not be performed on shared or public computers. Family members and other household occupants must not have access to Technijian devices or data |
| **Equipment** | Company-issued equipment is preferred. Personal devices may be used only per the BYOD policy (Section 9) |

### 8.2 Remote Work Environment Assessment

Personnel working remotely are required to self-certify that their remote work environment meets Technijian's security requirements. The self-certification covers:

- Secure and private workspace
- Secured Wi-Fi network
- Ability to secure physical documents and equipment
- No unauthorized individuals have access to work equipment or data

Self-certification is completed upon initial remote work arrangement and annually thereafter.

---

## 9. BYOD (Bring Your Own Device) Policy

### 9.1 BYOD Requirements

Personal devices used to access Technijian or client systems, data, or email must comply with the following requirements:

| Requirement | Standard |
|---|---|
| **MDM Enrollment** | Personal devices must be enrolled in Technijian's Mobile Device Management (MDM) solution before accessing corporate resources |
| **Operating System** | Must run a current, vendor-supported operating system with all security patches applied |
| **Full-Disk Encryption** | Required (BitLocker, FileVault, or native mobile encryption) |
| **Screen Lock** | Automatic screen lock after 5 minutes of inactivity with password/PIN/biometric |
| **EDR Agent** | CrowdStrike Falcon or equivalent endpoint protection must be installed and active |
| **Anti-Malware** | Current anti-malware solution active with automatic updates |
| **Remote Wipe** | Technijian reserves the right to remotely wipe corporate data (containerized wipe where supported) from personal devices upon termination, device loss/theft, or policy violation |
| **Jailbroken/Rooted Devices** | Jailbroken (iOS) or rooted (Android) devices are prohibited from accessing Technijian resources |
| **Prohibited Storage** | Restricted data must not be stored locally on personal devices |
| **Application Restrictions** | Only approved applications may be used to access corporate email, files, and services (e.g., Outlook, OneDrive, Teams via managed apps) |

### 9.2 BYOD Risk Acknowledgment

Personnel using personal devices must sign a BYOD agreement acknowledging:

- Technijian's right to enforce security controls on the device via MDM
- Technijian's right to remotely wipe corporate data from the device
- The employee's responsibility to report device loss or theft immediately
- The employee's responsibility to maintain device security (updates, patches, encryption)
- That the device is subject to monitoring for security compliance
- That Technijian is not responsible for loss of personal data due to security actions on the device

---

## 10. Physical Security

### 10.1 Clean Desk Policy

All personnel must maintain a clean desk at the end of each workday and when leaving their workstation unattended:

- Confidential and Restricted documents must be locked in a desk drawer or filing cabinet
- Screens must be locked (Windows + L / Ctrl + Command + Q) when stepping away
- Removable media containing sensitive data must be secured when not in use
- Whiteboards and shared displays must be erased after meetings involving Confidential information
- Printed materials must be retrieved immediately from shared printers; unclaimed printouts are collected and shredded daily

### 10.2 Visitor Management

- All visitors to Technijian facilities must sign in, present identification, and be escorted at all times
- Visitors are not permitted in secure areas (server rooms, network closets) without Security Officer approval and escort
- Visitor access badges are issued for the duration of the visit and collected upon departure

---

## 11. Intellectual Property and Trade Secret Protection

### 11.1 Ownership

All work product, inventions, discoveries, and developments created by personnel in the course of their employment or engagement with Technijian are the property of Technijian, as specified in the employment agreement or contractor agreement.

### 11.2 Protection of Trade Secrets

Personnel must protect Technijian trade secrets and proprietary information, including but not limited to:

- Client lists and engagement details
- Pricing methodologies and financial data
- Security tools, configurations, and methodologies
- Business strategies and operational procedures
- Software and automation tools developed by Technijian

---

## 12. Defend Trade Secrets Act (DTSA) Whistleblower Notice

### 12.1 Federal Immunity Provision

In accordance with the Defend Trade Secrets Act of 2016 (18 U.S.C. 1833(b)), Technijian provides the following notice to all employees and contractors:

**NOTICE OF IMMUNITY UNDER 18 U.S.C. 1833(b)(1):**

An individual shall not be held criminally or civilly liable under any Federal or State trade secret law for the disclosure of a trade secret that (A) is made (i) in confidence to a Federal, State, or local government official, either directly or indirectly, or to an attorney; and (ii) solely for the purpose of reporting or investigating a suspected violation of law; or (B) is made in a complaint or other document filed in a lawsuit or other proceeding, if such filing is made under seal.

### 12.2 Use in Anti-Retaliation Lawsuits

An individual who files a lawsuit for retaliation by an employer for reporting a suspected violation of law may disclose the trade secret to the attorney of the individual and use the trade secret information in the court proceeding, if the individual (A) files any document containing the trade secret under seal; and (B) does not disclose the trade secret, except pursuant to court order.

### 12.3 Acknowledgment Requirement

This notice is included in all Technijian employment agreements, contractor agreements, and Non-Disclosure Agreements. All personnel must acknowledge receipt of this notice at the time of hire or engagement and annually thereafter.

---

## 13. Compliance Mapping

This policy supports compliance with the following regulatory frameworks and standards:

| Framework / Standard | Relevant Requirements | Policy Section(s) |
|---|---|---|
| **SOC 2 Trust Services Criteria** | CC1.4 (Commitment to Competence) — The entity has committed to competence, including the development of the knowledge, skills, and abilities required to achieve the entity's objectives, including information security objectives. CC1.5 (Accountability) — The entity holds individuals accountable for their internal control responsibilities | Sections 2-7 |
| **HIPAA Security Rule** | §164.308(a)(3) (Workforce Security) — Implement policies and procedures to ensure all members of the workforce have appropriate access and to prevent those who do not have access from obtaining access. §164.308(a)(3)(ii)(A) (Authorization/Supervision). §164.308(a)(3)(ii)(B) (Workforce Clearance Procedure). §164.308(a)(3)(ii)(C) (Termination Procedures). §164.308(a)(5) (Security Awareness and Training) | Sections 2, 3, 4, 6 |
| **PCI-DSS v4.0** | Req 12.6 (Security Awareness Education) — Security awareness education is an ongoing activity. 12.6.1 (Formal security awareness program). 12.6.2 (Personnel acknowledge security policies annually). 12.6.3 (Training upon hire and annually). 12.6.3.1 (Training includes awareness of threats and vulnerabilities). 12.6.3.2 (Training includes acceptable use of end-user technologies) | Sections 3, 4, 5 |
| **GDPR** | Art 39(1)(b) (Tasks of the DPO) — Monitoring compliance and awareness-raising and training of staff involved in processing operations. Art 32 (Security of Processing) — Appropriate technical and organizational measures | Sections 3-6, 8, 9 |
| **CCPA / CPRA** | §1798.150 (Reasonable Security) — Implement and maintain reasonable security procedures and practices | Sections 2-9 |
| **NIST CSF** | PR.AT (Awareness and Training) — The organization's personnel and partners are provided cybersecurity awareness education and are trained to perform their information security-related duties. PR.IP-11 (Cybersecurity in Human Resources Practices) | Sections 2-6 |
| **NIST SP 800-53** | AT-1 through AT-4 (Awareness and Training family), PS-1 through PS-8 (Personnel Security family) | Sections 2-7 |
| **Defend Trade Secrets Act** | 18 U.S.C. 1833(b) (Whistleblower Immunity Notice) | Section 12 |
| **FCRA** | Background check requirements and applicant rights | Section 2 |

---

## 14. Policy Review

### 14.1 Review Cycle

This policy is reviewed and approved on an annual basis by the Security Officer (Ravi Jain, CEO/Owner). The annual review occurs no later than the anniversary of the last approval date.

### 14.2 Out-of-Cycle Reviews

Out-of-cycle reviews are triggered by:

- Changes in applicable laws, regulations, or contractual requirements
- Security incidents involving personnel (insider threat, social engineering, credential compromise)
- Audit findings related to personnel security controls
- Changes in Technijian's workforce structure, hiring practices, or remote work policies
- Industry developments in security awareness training or insider threat management
- Changes in client security requirements affecting personnel

### 14.3 Version History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | April 6, 2026 | Ravi Jain | Initial release |

### 14.4 Acknowledgment

All Technijian employees, contractors, and subcontractors must acknowledge receipt and understanding of this policy within 30 days of hire or contract start date, and annually thereafter. Acknowledgment records are maintained by Human Resources.

---

**Technijian, Inc.**
18 Technology Drive, Suite 141
Irvine, CA 92618

*This document is the property of Technijian, Inc. and is classified as Confidential. Unauthorized distribution or reproduction is prohibited.*
