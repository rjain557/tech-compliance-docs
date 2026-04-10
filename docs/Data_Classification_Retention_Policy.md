# Technijian, Inc.

# Data Classification and Retention Policy

**Version:** 1.0
**Date:** April 6, 2026
**Classification:** Confidential
**Document Owner:** Ravi Jain - CEO/Owner
**Approved By:** Ravi Jain - CEO/Owner
**Next Review Date:** April 6, 2027

---

## 1. Purpose

This policy establishes the requirements for classifying, handling, retaining, and disposing of all data processed, stored, or transmitted by Technijian, Inc. ("Technijian"). As a managed IT services provider, Technijian handles sensitive data belonging to clients across healthcare, financial services, legal, and other regulated industries. Proper data classification and retention are essential to:

- Protect the confidentiality, integrity, and availability of information assets
- Comply with applicable laws, regulations, and contractual obligations
- Minimize the risk of unauthorized disclosure, data breaches, and regulatory penalties
- Enable consistent and defensible data handling across all operations

This policy supplements the Technijian Information Security Program (WISP) and applies to all employees, contractors, subcontractors, and temporary personnel who access, process, store, or transmit Technijian or client data.

### 1.1 Scope

This policy applies to:

- All data in any form (electronic, paper, verbal) created, received, processed, stored, or transmitted by Technijian
- All information systems, storage media, cloud services, and physical locations where data resides
- All Technijian personnel, including employees, contractors, subcontractors, and temporary staff
- All client data managed by Technijian under service agreements
- Technijian headquarters at 18 Technology Drive, Suite 141, Irvine, CA 92618, the TPX data center, and all remote work locations

---

## 2. Data Classification Levels

All data processed, stored, or transmitted by Technijian must be classified into one of the following four levels. Data owners are responsible for assigning the appropriate classification. When the classification is uncertain, data must be treated at the higher sensitivity level until a formal assessment is completed.

### 2.1 Public

| Attribute | Detail |
|---|---|
| **Definition** | Information approved for public release that would cause no harm if disclosed |
| **Examples** | Marketing materials, published blog posts, public website content, press releases, published whitepapers |
| **Data Owner** | Marketing or designated content owner |
| **Impact of Unauthorized Disclosure** | None or negligible |

### 2.2 Internal

| Attribute | Detail |
|---|---|
| **Definition** | Information intended for internal Technijian use that is not approved for public release |
| **Examples** | Internal procedures, meeting notes, project documentation, training materials, internal communications, organizational charts |
| **Data Owner** | Department head or project lead |
| **Impact of Unauthorized Disclosure** | Minor operational inconvenience; no regulatory or legal consequence |

### 2.3 Confidential

| Attribute | Detail |
|---|---|
| **Definition** | Sensitive business or client information whose unauthorized disclosure would cause significant harm |
| **Examples** | Client infrastructure documentation, Technijian security policies, contracts and agreements, employee PII, financial records, vendor agreements, internal audit reports, business strategies |
| **Data Owner** | Designated business owner or Security Officer |
| **Impact of Unauthorized Disclosure** | Significant financial, legal, or reputational harm; potential contractual breach |

### 2.4 Restricted

| Attribute | Detail |
|---|---|
| **Definition** | Highest sensitivity data. Unauthorized disclosure would cause severe and potentially irreversible harm |
| **Examples** | Client NPI (nonpublic personal information), PHI/ePHI, payment card data (PCI scope), Social Security numbers, credentials and encryption keys, client financial account data, biometric data |
| **Data Owner** | Security Officer or designated compliance owner |
| **Impact of Unauthorized Disclosure** | Severe financial penalties, regulatory action, litigation, loss of client trust, mandatory breach notification |

---

## 3. Handling Requirements

### 3.1 Handling Requirements by Classification Level

| Requirement | Public | Internal | Confidential | Restricted |
|---|---|---|---|---|
| **Encryption at Rest** | Not required | Recommended | Required (AES-256) | Required (AES-256) |
| **Encryption in Transit** | Not required | Required (TLS 1.2+) | Required (TLS 1.2+) | Required (TLS 1.2+) |
| **Access Control** | No restriction | Standard authentication | Role-based, need-to-know | Strict need-to-know, approval required |
| **MFA Required** | No | For remote access | Yes | Yes |
| **Storage on Personal Devices** | Permitted | Permitted with MDM | Prohibited without approval | Prohibited |
| **Removable Media** | Permitted | Permitted | Encrypted media only, with approval | Prohibited |
| **Email Transmission** | Permitted | Permitted internally | Encrypted or via secure portal | Encrypted only, with DLP controls |
| **Cloud Storage** | Permitted | Approved services only | Approved services with encryption | Approved services with encryption and access logging |
| **Printing** | Permitted | Permitted | Minimize; shred when no longer needed | Prohibited unless business-critical; immediate shredding required |
| **Labeling** | Not required | "Internal Use Only" | "Confidential" | "Restricted" |
| **Access Logging** | Not required | Not required | Recommended | Required |
| **Secure Destruction** | Not required | Standard deletion | Secure destruction required | Secure destruction required with certificate |
| **Sharing with Third Parties** | Permitted | NDA required | NDA + data protection agreement | NDA + data protection agreement + Security Officer approval |
| **Backup** | Standard | Standard | Encrypted backups | Encrypted backups with access logging |

### 3.2 Labeling Standards

- **Electronic Documents:** Include the classification level in the document header, footer, or metadata. Confidential and Restricted documents must include the classification label on every page.
- **Email:** Confidential and Restricted information transmitted via email must include the classification level in the subject line prefix (e.g., "[CONFIDENTIAL]" or "[RESTRICTED]").
- **Physical Media:** Physical storage media (USB drives, external hard drives, backup tapes) containing Confidential or Restricted data must be labeled with the classification level and a unique identifier.
- **Paper Documents:** Paper documents containing Confidential or Restricted data must be stamped or printed with the classification level on each page.

### 3.3 Data in Motion

- All Confidential and Restricted data must be encrypted during transmission using TLS 1.2 or higher
- SSL, TLS 1.0, and TLS 1.1 are prohibited
- File transfers of Confidential or Restricted data must use SFTP or SCP; FTP is prohibited
- VPN connections use IPsec or TLS-based tunnels with AES-256 encryption

### 3.4 Data at Rest

- AES-256 is the standard encryption algorithm for data at rest
- Full-disk encryption is required on all endpoints (BitLocker with TPM on Windows, FileVault 2 on macOS)
- SQL Server instances containing Confidential or Restricted data must use Transparent Data Encryption (TDE)
- Backup files must be encrypted using AES-256 before storage
- Encryption keys are stored separately from the data they protect and rotated annually at minimum

---

## 4. Retention Schedule

### 4.1 Retention Periods by Data Type

| Data Type | Retention Period | Regulatory Basis | Classification |
|---|---|---|---|
| Client NPI / financial data | 7 years after end of engagement | SEC Rule 17a-4, FINRA Rule 4511, GLB Act | Restricted |
| PHI / ePHI | 6 years after last use | HIPAA §164.530(j) | Restricted |
| Payment card data (PCI) | Duration of business need only; purge when no longer required | PCI-DSS Req 3.1 | Restricted |
| Employee personnel records | 7 years after termination | Federal/state labor laws, EEOC | Confidential |
| Employee medical records | 7 years after termination (stored separately from personnel files) | ADA, FMLA, OSHA | Restricted |
| Security logs and audit trails | Minimum 1 year online, 3 years archived | SOC 2, PCI-DSS Req 10.7, HIPAA | Confidential |
| Incident response records | 6 years | HIPAA, SOC 2 | Confidential |
| Contracts and agreements | Duration of contract + 7 years | Statute of limitations, legal requirements | Confidential |
| General business records | 7 years | Tax code (IRC §6501), legal requirements | Internal |
| Tax records and financial statements | 7 years | IRC §6501, state tax requirements | Confidential |
| Insurance records | Duration of policy + 7 years | Legal requirements | Confidential |
| Marketing materials | 1 year after last use | Internal policy | Public |
| Internal training materials | 3 years after last use | SOC 2, HIPAA training requirements | Internal |
| Email communications | 7 years | SEC, FINRA (for regulated clients), litigation hold policies | Internal/Confidential |
| Client system documentation | Duration of engagement + 3 years | Contractual, operational continuity | Confidential |
| Vulnerability scan and penetration test reports | 3 years | SOC 2, PCI-DSS, HIPAA | Confidential |
| Access review records | 3 years | SOC 2, HIPAA, PCI-DSS | Confidential |
| Background check records | Duration of employment + 7 years | FCRA, state laws | Restricted |

### 4.2 Retention Principles

- **Minimum Retention:** Data must be retained for at least the minimum period specified in this schedule
- **Maximum Retention:** Data should not be retained beyond the specified period unless subject to a litigation hold, regulatory investigation, or documented business need approved by the Security Officer
- **Litigation Hold:** When Technijian receives notice of actual or reasonably anticipated litigation, investigation, or audit, all potentially relevant data must be preserved regardless of the retention schedule. Litigation holds are issued by the CEO/Owner or legal counsel and remain in effect until formally released
- **Client-Specific Requirements:** Where client contracts specify retention periods exceeding those in this schedule, the longer period applies. Where client contracts specify shorter periods, the regulatory minimum from this schedule applies
- **Multiple Retention Triggers:** If data is subject to multiple retention requirements, the longest applicable period governs

---

## 5. Disposal and Destruction Methods

### 5.1 Disposal Standards (NIST SP 800-88 Rev. 1)

All disposal of Confidential and Restricted data must follow NIST SP 800-88 Rev. 1 "Guidelines for Media Sanitization." The appropriate sanitization method is determined by the media type and data classification.

| Media Type | Sanitization Method | Standard |
|---|---|---|
| **SSDs / Flash Storage** | Cryptographic erasure (ATA Secure Erase or sanitize command) followed by verification | NIST SP 800-88 Purge |
| **HDDs** | Secure overwrite (3-pass minimum using DoD 5220.22-M pattern) or physical destruction (degaussing + shredding) | NIST SP 800-88 Purge or Destroy |
| **Optical Media (CDs/DVDs)** | Physical shredding using a media-rated shredder | NIST SP 800-88 Destroy |
| **Magnetic Tape** | Degaussing followed by physical destruction | NIST SP 800-88 Destroy |
| **Paper Documents** | Cross-cut shredding (minimum P-4 per DIN 66399) | DIN 66399 Level P-4 |
| **Cloud / Virtual Storage** | Cryptographic erasure with key destruction, followed by platform-specific secure deletion and written confirmation from the cloud provider | NIST SP 800-88 Purge |
| **Mobile Devices** | Factory reset followed by cryptographic erasure verification | NIST SP 800-88 Purge |
| **Network Equipment** | Configuration wipe, factory reset, removal of all storage media | NIST SP 800-88 Clear/Purge |

### 5.2 Disposal by Classification Level

| Classification | Disposal Method |
|---|---|
| **Public** | Standard deletion; no special destruction required |
| **Internal** | Standard deletion; physical media may be recycled after basic wipe |
| **Confidential** | Secure destruction per NIST SP 800-88; certificate of destruction required |
| **Restricted** | Secure destruction per NIST SP 800-88 with witnessed destruction; certificate of destruction required; destruction log entry mandatory |

### 5.3 Destruction Documentation

For all Confidential and Restricted data destruction events, the following must be documented and retained for a minimum of 3 years:

- Date of destruction
- Description of media or data destroyed (type, serial number, asset tag where applicable)
- Sanitization method used
- Name of individual who performed the destruction
- Name of witness (required for Restricted data)
- Certificate of destruction (obtained from vendor for outsourced destruction)
- Verification that destruction was successful

### 5.4 Third-Party Destruction Services

When Technijian engages a third-party vendor for data destruction:

- The vendor must provide a signed certificate of destruction for each destruction event
- The vendor must be vetted through Technijian's vendor risk management process
- The vendor must maintain appropriate insurance coverage
- The vendor must comply with NIST SP 800-88 standards
- Technijian retains the right to audit the vendor's destruction processes

---

## 6. Client Data Provisions

### 6.1 Client Data Segregation

Technijian maintains strict separation of client data to prevent unauthorized cross-client access:

- **Logical Segregation:** Client environments are isolated using dedicated tenancies, separate Active Directory domains or organizational units, and unique access credentials per client
- **Network Segregation:** Client networks are separated using VLANs, firewall rules, and dedicated VPN tunnels. Cross-client network traffic is prohibited
- **Database Segregation:** Client data is stored in separate database instances. Shared databases across clients are prohibited for Restricted or Confidential data
- **Access Controls:** Engineers are granted access only to specific client environments required for their assignments. Cross-client access requires separate authorization

### 6.2 Client Data Ownership

- All client data remains the property of the client at all times
- Technijian acts as a data processor/custodian, not a data owner, for client data
- Upon termination of a service agreement, client data is returned to the client in a mutually agreed-upon format within 30 days, or securely destroyed upon written client request
- Proof of destruction is provided to the client upon request

### 6.3 Client Data Handling

- Client data classification must meet or exceed the classification assigned by the client
- Where client contracts specify data handling requirements stricter than this policy, the client requirements govern
- Client data must not be used for any purpose other than the delivery of contracted services
- Client data must not be shared with other clients, vendors, or third parties without explicit written client authorization
- Access to client data is logged and subject to review per Section 4.3 of the WISP

### 6.4 Client Data Breach Notification

- In the event of a data breach involving client data, Technijian will notify the affected client within 24 hours of confirmation of the breach
- Notification procedures comply with applicable state and federal breach notification laws, including HIPAA, CCPA/CPRA, and state data breach notification statutes
- Technijian cooperates fully with clients in breach investigation and remediation efforts

---

## 7. Compliance Mapping

This policy supports compliance with the following regulatory frameworks and standards:

| Framework / Standard | Relevant Requirements | Policy Section(s) |
|---|---|---|
| **SOC 2 Trust Services Criteria** | CC6.1 (Logical and Physical Access Controls), CC6.5 (Disposal of Data), CC6.7 (Data Classification) | Sections 2, 3, 4, 5 |
| **HIPAA Security Rule** | §164.312(d)(1) (Information Access Management), §164.310(d)(2) (Media Disposal), §164.530(j) (Retention) | Sections 2, 4, 5 |
| **PCI-DSS v4.0** | Req 3 (Protect Stored Account Data), Req 3.1 (Data Retention Policy), Req 9.4 (Media Destruction) | Sections 4, 5 |
| **GDPR** | Art 5(1)(e) (Storage Limitation), Art 17 (Right to Erasure), Art 25 (Data Protection by Design) | Sections 4, 5, 6 |
| **CCPA / CPRA** | §1798.105 (Right to Delete), §1798.100 (Right to Know) | Sections 4, 5, 6 |
| **NIST CSF** | PR.DS (Data Security), PR.IP-6 (Data Destruction) | Sections 2, 3, 4, 5 |
| **NIST SP 800-88 Rev. 1** | Media Sanitization Guidelines | Section 5 |
| **SEC Rule 17a-4** | Record Retention Requirements | Section 4 |
| **FINRA Rule 4511** | Record Retention Requirements | Section 4 |
| **FTC Safeguards Rule** | §314.4(c) (Information Safeguards) | Sections 2, 3, 5 |

---

## 8. Policy Review

### 8.1 Review Cycle

This policy is reviewed and approved on an annual basis by the Security Officer (Ravi Jain, CEO/Owner). The annual review occurs no later than the anniversary of the last approval date.

### 8.2 Out-of-Cycle Reviews

Out-of-cycle reviews are triggered by:

- Changes in applicable laws, regulations, or contractual requirements
- Significant security incidents or data breaches
- Major changes to Technijian's infrastructure, technology stack, or service offerings
- Results of risk assessments or audits that identify policy gaps
- Changes in client regulatory requirements
- New data types or processing activities not covered by the current policy

### 8.3 Version History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | April 6, 2026 | Ravi Jain | Initial release |

### 8.4 Acknowledgment

All Technijian employees, contractors, and subcontractors must acknowledge receipt and understanding of this policy within 30 days of hire or contract start date, and annually thereafter. Acknowledgment records are maintained by Human Resources.

---

**Technijian, Inc.**
18 Technology Drive, Suite 141
Irvine, CA 92618

*This document is the property of Technijian, Inc. and is classified as Confidential. Unauthorized distribution or reproduction is prohibited.*
