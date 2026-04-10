# Technijian, Inc.

# Vendor Risk Management Policy

**Version:** 1.0
**Date:** April 6, 2026
**Classification:** Confidential
**Document Owner:** Ravi Jain - CEO/Owner
**Approved By:** Ravi Jain - CEO/Owner
**Next Review Date:** April 6, 2027

---

## 1. Purpose and Scope

### 1.1 Purpose

This Vendor Risk Management Policy establishes the framework for identifying, assessing, monitoring, and mitigating risks associated with third-party vendors, service providers, and sub-processors that support Technijian, Inc.'s operations and managed service delivery. As a managed IT services provider, Technijian relies on a range of technology vendors whose security posture directly impacts the confidentiality, integrity, and availability of Technijian and client data.

This policy ensures that vendor relationships are managed with appropriate due diligence, contractual protections, and ongoing oversight commensurate with the risk each vendor presents.

### 1.2 Scope

This policy applies to:

- All third-party vendors, service providers, suppliers, and sub-processors that provide products or services to Technijian
- All vendor relationships that involve access to, processing of, or storage of Technijian or client data
- All vendor relationships that support critical infrastructure, systems, or service delivery capabilities
- All Technijian personnel responsible for selecting, onboarding, managing, or overseeing vendor relationships
- All vendor relationships regardless of contract value, including free-tier and trial services where Technijian or client data is involved

### 1.3 Exclusions

The following are excluded from the full vendor risk management process but are tracked in the vendor inventory:

- One-time purchases of hardware or physical supplies where no data access or ongoing service relationship exists
- Utility providers (electricity, water) that do not have access to Technijian systems or data

---

## 2. Definitions

| Term | Definition |
|---|---|
| **Vendor** | Any third-party organization that provides products, services, or technology to Technijian in support of its operations or managed service delivery. |
| **Sub-processor** | A vendor engaged by Technijian that processes personal data or regulated data on behalf of Technijian's clients. Sub-processors are subject to the same data protection requirements as Technijian. |
| **Tier 1 Vendor (Critical)** | Vendors that provide services essential to Technijian's core service delivery, have access to Restricted or Confidential data, or whose failure would cause significant operational disruption. Examples: data center provider, EDR platform, RMM platform, backup infrastructure. |
| **Tier 2 Vendor (Significant)** | Vendors that support important business functions, may have access to Internal data, or whose failure would cause moderate operational impact. Examples: collaboration platforms, professional services tools, non-critical SaaS applications. |
| **Tier 3 Vendor (Low Risk)** | Vendors that provide commoditized services, have no access to Sensitive Data, and whose failure would cause minimal operational impact. Examples: office supply vendors, non-data-handling utility services. |
| **BAA** | Business Associate Agreement, required under HIPAA before a vendor processes or stores PHI on behalf of Technijian or its clients. |
| **DPA** | Data Processing Agreement, required under GDPR and other privacy regulations before a vendor processes personal data on behalf of Technijian or its clients. |
| **SOC 2 Report** | Service Organization Control 2 report, an independent audit of a service provider's controls related to security, availability, processing integrity, confidentiality, and privacy. |
| **Vendor Risk Assessment** | A structured evaluation of a vendor's security posture, compliance status, financial stability, and operational capabilities. |
| **SLA** | Service Level Agreement defining the vendor's performance commitments, uptime guarantees, and remedies for service failures. |

---

## 3. Vendor Classification

### 3.1 Classification Criteria

All vendors are classified into one of three tiers based on the following criteria:

| Criterion | Tier 1 (Critical) | Tier 2 (Significant) | Tier 3 (Low Risk) |
|---|---|---|---|
| **Data Access** | Access to Restricted or Confidential data (PHI, PCI, NPI, PII, credentials) | Access to Internal data only | No access to Technijian or client data |
| **Service Criticality** | Essential to core service delivery; failure causes significant client impact | Supports important functions; failure causes moderate impact | Commoditized; failure causes minimal impact |
| **Client Impact** | Direct impact on client environments or client data | Indirect impact on service quality | No client impact |
| **Regulatory Scope** | Subject to HIPAA, PCI-DSS, SOC 2, GDPR, or financial regulations | Subject to general security requirements | Minimal regulatory relevance |
| **Replaceability** | Difficult to replace; long transition period (30+ days) | Moderately replaceable (7-30 days) | Easily replaceable (< 7 days) |

### 3.2 Classification Process

- Vendor classification is performed during onboarding and reviewed at each assessment cycle
- The Security Officer assigns the initial classification based on the criteria above
- Classification may be escalated (e.g., Tier 3 to Tier 2) if the vendor's scope of access or criticality changes
- All classification decisions are documented in the vendor inventory

### 3.3 Classification Review

Vendor classifications are reviewed:

- Annually as part of the vendor risk assessment cycle
- When vendor scope of services changes
- When new data types are shared with the vendor
- After a vendor security incident

---

## 4. Vendor Onboarding

### 4.1 Onboarding Process

All new vendors must complete the following onboarding process before being granted access to Technijian systems or data:

| Step | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| **1. Business Justification** | Required | Required | Required |
| **2. Vendor Security Questionnaire** | Full questionnaire (SIG Lite or equivalent) | Abbreviated questionnaire | Not required |
| **3. SOC 2 Type II Report Review** | Required (current, within 12 months) | Requested; ISO 27001 or equivalent accepted | Not required |
| **4. Penetration Test Results** | Requested | Not required | Not required |
| **5. Insurance Verification** | Required (Cyber, E&O, General Liability) | Required (General Liability minimum) | Not required |
| **6. BAA Execution** | Required if PHI is involved | Required if PHI is involved | N/A |
| **7. DPA Execution** | Required if personal data is processed | Required if personal data is processed | N/A |
| **8. NDA Execution** | Required | Required | As needed |
| **9. SLA Review** | Required with defined uptime, RTO, RPO | Required with defined uptime | Not required |
| **10. Security Officer Approval** | Required | Required | IT Operations approval sufficient |

### 4.2 Vendor Security Questionnaire

The vendor security questionnaire covers the following domains:

- Information security program and governance
- Access control and authentication practices
- Data encryption (at rest and in transit)
- Vulnerability management and patching
- Incident response and breach notification
- Business continuity and disaster recovery
- Employee screening and security training
- Sub-processor management
- Data retention and destruction
- Regulatory compliance (HIPAA, PCI-DSS, SOC 2, GDPR as applicable)
- Physical security (for data center and hosting providers)

### 4.3 SOC 2 Report Review

For Tier 1 vendors providing a SOC 2 Type II report:

- The Security Officer reviews the report for the scope of services used by Technijian
- Management assertions, control objectives, and test results are evaluated
- Any qualified opinions, exceptions, or noted deviations are assessed for impact on Technijian
- Complementary User Entity Controls (CUECs) are identified and verified as implemented by Technijian
- The SOC 2 bridge letter is requested if the report period does not cover the current date

### 4.4 Insurance Requirements

| Coverage Type | Tier 1 Minimum | Tier 2 Minimum |
|---|---|---|
| Cyber Liability / Tech E&O | $5,000,000 | N/A (recommended) |
| Commercial General Liability | $1,000,000 per occurrence | $1,000,000 per occurrence |
| Professional Liability (E&O) | $2,000,000 | N/A (recommended) |
| Workers' Compensation | Statutory limits | Statutory limits |

### 4.5 Contractual Requirements

All vendor contracts for Tier 1 and Tier 2 vendors must include:

- Defined scope of services and data handling responsibilities
- Data protection and confidentiality obligations
- Security requirements and standards the vendor must maintain
- Right to audit clause (or equivalent SOC 2 / third-party audit provision)
- Breach notification requirements (notification within 24 hours for Tier 1, 72 hours for Tier 2)
- Data return and destruction obligations upon contract termination
- Indemnification for security breaches caused by vendor negligence
- Compliance with applicable regulations (HIPAA, PCI-DSS, GDPR as relevant)
- Sub-processor disclosure and approval requirements
- Termination provisions, including for-cause termination for material security failures

---

## 5. Ongoing Monitoring

### 5.1 Monitoring Frequency

| Activity | Tier 1 (Critical) | Tier 2 (Significant) | Tier 3 (Low Risk) |
|---|---|---|---|
| **Full Risk Assessment** | Annually | Biennially (every 2 years) | Not required |
| **SOC 2 Report Review** | Annually (upon report issuance) | Biennially | Not required |
| **Security Questionnaire Update** | Annually | Biennially | Not required |
| **Insurance Certificate Renewal** | Annually | Annually | Not required |
| **SLA Performance Review** | Quarterly | Semi-annually | Not required |
| **Security News Monitoring** | Continuous | Continuous | Not required |
| **Sub-processor Change Review** | Upon notification | Upon notification | N/A |

### 5.2 Continuous Monitoring Activities

For all Tier 1 and Tier 2 vendors, the following continuous monitoring activities are performed:

- **Security Advisory Monitoring:** Track vendor security advisories, CVE disclosures, and patch releases. Critical vulnerabilities in vendor products trigger immediate risk assessment
- **Breach and Incident Monitoring:** Monitor news sources, threat intelligence feeds, and vendor communications for reports of vendor breaches or security incidents
- **Service Availability Monitoring:** Track vendor uptime and service availability against SLA commitments
- **Regulatory Action Monitoring:** Monitor for regulatory enforcement actions, lawsuits, or compliance failures involving the vendor
- **Financial Health Monitoring:** Annual review of vendor financial stability indicators for Tier 1 vendors to assess continuity risk

### 5.3 Monitoring Responsibilities

| Responsibility | Owner |
|---|---|
| Overall vendor risk program management | Security Officer (Ravi Jain) |
| Vendor security questionnaire review | Security Officer |
| SOC 2 report review | Security Officer |
| SLA performance tracking | IT Operations |
| Contract and insurance management | CEO/Owner |
| Day-to-day vendor relationship management | Designated account owner per vendor |

---

## 6. Vendor Risk Assessment

### 6.1 Assessment Methodology

Vendor risk assessments evaluate the following risk domains:

| Risk Domain | Assessment Areas |
|---|---|
| **Security Risk** | Information security program maturity, access controls, encryption, vulnerability management, incident response, endpoint security, network security |
| **Compliance Risk** | Regulatory compliance status (HIPAA, PCI-DSS, SOC 2, GDPR), audit findings, certifications |
| **Operational Risk** | Service reliability, uptime history, disaster recovery capabilities, staffing and support quality |
| **Financial Risk** | Financial stability, market position, risk of vendor insolvency or acquisition |
| **Reputational Risk** | Public breach history, regulatory enforcement actions, customer complaints |
| **Concentration Risk** | Degree of Technijian's dependency on the vendor, availability of alternatives |

### 6.2 Risk Scoring

Each risk domain is scored on the following scale:

| Score | Rating | Description |
|---|---|---|
| 1 | Low | Controls are mature and well-documented. Minimal risk identified. |
| 2 | Moderate | Controls are adequate but may have minor gaps. Acceptable risk with monitoring. |
| 3 | High | Significant control gaps identified. Risk requires treatment plan. |
| 4 | Critical | Major control failures or unacceptable risk. Requires immediate remediation or vendor replacement. |

The overall vendor risk rating is the highest individual domain score, weighted toward Security and Compliance risk domains.

### 6.3 Risk Treatment

| Overall Rating | Required Action |
|---|---|
| **Low (1)** | Continue standard monitoring per tier schedule. |
| **Moderate (2)** | Document findings. Request vendor remediation plan within 90 days. Increase monitoring frequency if warranted. |
| **High (3)** | Escalate to CEO/Owner. Require vendor remediation plan within 30 days. Implement compensating controls. Evaluate alternative vendors. |
| **Critical (4)** | Immediate escalation to CEO/Owner. Initiate vendor transition planning. Implement compensating controls immediately. Consider contract termination. |

### 6.4 Assessment Documentation

All vendor risk assessments are documented and retained for a minimum of 3 years. Documentation includes:

- Assessment date and assessor
- Vendor classification tier
- Questionnaire responses and supporting evidence
- SOC 2 or audit report findings
- Risk domain scores and rationale
- Overall risk rating
- Treatment plan and remediation timeline (if applicable)
- Approval by the Security Officer

---

## 7. Sub-processor Management

### 7.1 Sub-processor Requirements

When Technijian engages vendors that act as sub-processors (processing personal data or regulated data on behalf of Technijian's clients):

- **Disclosure:** Technijian maintains a list of all sub-processors and the categories of data they process. This list is made available to clients upon request
- **Client Notification:** Clients are notified of new sub-processors or changes to existing sub-processors before the sub-processor begins processing. Notification includes the sub-processor identity, location, and scope of processing
- **Objection Right:** Where required by contract or regulation (e.g., GDPR Art 28), clients are given a reasonable period (typically 30 days) to object to new sub-processors
- **Due Diligence:** All sub-processors are subject to the same vendor risk assessment and onboarding requirements as Tier 1 or Tier 2 vendors, depending on the data involved
- **Contractual Flow-down:** Sub-processor agreements must include data protection obligations equivalent to those in Technijian's agreements with its clients

### 7.2 Sub-processor Monitoring

- Sub-processors are monitored per the Tier 1 monitoring schedule (Section 5.1)
- Changes in sub-processor security posture or compliance status trigger immediate reassessment
- Sub-processor breaches trigger Technijian's vendor incident response process (Section 9)

---

## 8. Vendor Inventory

### 8.1 Inventory Requirements

Technijian maintains a centralized vendor inventory that includes the following attributes for each vendor:

| Attribute | Description |
|---|---|
| Vendor Name | Legal entity name |
| Vendor Contact | Primary contact and escalation contact |
| Services Provided | Description of products/services provided to Technijian |
| Tier Classification | Tier 1, Tier 2, or Tier 3 |
| Data Access | Types of data the vendor can access or process |
| Sub-processor Status | Whether the vendor acts as a sub-processor |
| Contract Expiration | Contract end date or renewal date |
| BAA/DPA Status | Whether BAA and/or DPA is in place |
| SOC 2 / Certification Status | Current audit report status and expiration |
| Insurance Status | Current insurance certificate status and expiration |
| Last Risk Assessment | Date of most recent risk assessment |
| Risk Rating | Current overall risk rating |
| Vendor Owner | Technijian personnel responsible for the relationship |

### 8.2 Current Vendor Inventory

The following table represents Technijian's current critical and significant vendor relationships:

| Vendor | Tier | Services | Data Access | BAA/DPA | SOC 2 / Cert | Sub-processor |
|---|---|---|---|---|---|---|
| **TPX Communications** | Tier 1 | Data center hosting, colocation, network infrastructure | Restricted (physical access to infrastructure housing client data) | BAA in place | SOC 2 Type II (reviewed annually) | Yes |
| **Microsoft** | Tier 1 | Microsoft 365, Azure, Entra ID, Defender, Intune | Restricted (email, identity, cloud workloads, client data in Azure/M365 tenants) | BAA in place, DPA in place | SOC 2 Type II, ISO 27001, FedRAMP | Yes |
| **CrowdStrike** | Tier 1 | Falcon EDR/XDR, endpoint protection, threat intelligence | Restricted (endpoint telemetry, process data, threat detections across all managed endpoints) | DPA in place | SOC 2 Type II, ISO 27001 | Yes |
| **ManageEngine (Zoho Corp)** | Tier 1 | Endpoint Central Plus (RMM), patch management, software deployment | Restricted (remote access to all managed endpoints, inventory data, configuration data) | DPA in place | SOC 2 Type II, ISO 27001 | Yes |
| **Veeam** | Tier 1 | Backup and disaster recovery, data replication | Restricted (backup data containing client production data, credentials for backup targets) | DPA in place | SOC 2 Type II | Yes |
| **Huntress** | Tier 1 | Managed detection and response, persistent foothold detection, SIEM (planned) | Restricted (endpoint forensic data, threat detections, security event logs) | DPA in place | SOC 2 Type II | Yes |

### 8.3 Inventory Maintenance

- The vendor inventory is updated upon onboarding of new vendors, termination of existing vendors, and whenever vendor attributes change
- A full inventory review is conducted semi-annually
- The Security Officer is responsible for maintaining the accuracy of the inventory

---

## 9. Incident Response for Vendor Breaches

### 9.1 Vendor Breach Notification Requirements

All Tier 1 and Tier 2 vendor contracts require the vendor to notify Technijian of security incidents and data breaches:

| Vendor Tier | Notification Deadline | Notification Method |
|---|---|---|
| Tier 1 (Critical) | Within 24 hours of discovery | Phone call to Security Officer + written notification via email |
| Tier 2 (Significant) | Within 72 hours of discovery | Written notification via email to Security Officer |

### 9.2 Technijian Response Process

Upon receiving notification of a vendor breach or discovering a vendor security incident:

**Phase 1: Initial Response (0-4 hours)**

1. Security Officer assesses the scope and severity of the vendor incident
2. Determine whether Technijian or client data was involved or potentially exposed
3. Activate the Technijian Incident Response Plan if client data is confirmed or suspected to be affected
4. Isolate or restrict vendor access to Technijian and client systems if warranted by the incident scope
5. Notify CEO/Owner

**Phase 2: Investigation and Containment (4-48 hours)**

1. Obtain detailed incident information from the vendor, including timeline, root cause, affected systems, and data involved
2. Conduct internal investigation to determine the impact on Technijian and client data
3. Implement compensating controls (e.g., additional monitoring, access restrictions, credential rotation) as needed
4. Assess whether client notification obligations are triggered under applicable regulations (HIPAA, GDPR, state breach notification laws, contractual requirements)

**Phase 3: Client Notification (as required)**

1. If client data is affected, notify affected clients within the timeframes required by contract and applicable regulation
2. Provide clients with relevant details: nature of the incident, data involved, remediation steps, and Technijian's response actions
3. Coordinate with clients on any joint response activities

**Phase 4: Post-Incident (ongoing)**

1. Obtain the vendor's root cause analysis and remediation plan
2. Verify that the vendor has implemented corrective actions
3. Reassess the vendor's risk rating based on the incident
4. Determine whether to continue, modify, or terminate the vendor relationship
5. Document the incident, response actions, and lessons learned
6. Update vendor risk assessment and monitoring schedule as warranted

### 9.3 Vendor Breach Tracking

All vendor security incidents are tracked in the vendor risk register with the following information:

- Incident date and discovery date
- Vendor name and tier classification
- Incident description and scope
- Data types affected (if any)
- Technijian response actions taken
- Client notifications issued
- Vendor remediation status
- Impact on vendor risk rating
- Lessons learned and policy updates

---

## 10. Termination and Transition

### 10.1 Planned Termination

When a vendor relationship is terminated (either at contract end or by decision):

| Step | Action | Timeline |
|---|---|---|
| 1 | Notify vendor of termination per contract terms | Per contract notice period |
| 2 | Initiate data return process: obtain all Technijian and client data held by the vendor | Begin immediately upon notice |
| 3 | Verify completeness of returned data | Within 15 business days of data receipt |
| 4 | Obtain certification of data destruction from the vendor (all copies, backups, and derived data) | Within 30 days of contract end |
| 5 | Revoke all vendor access to Technijian and client systems (accounts, API keys, VPN, certificates) | On or before contract end date |
| 6 | Transition services to replacement vendor or bring in-house | Per transition plan |
| 7 | Update vendor inventory and notify affected clients | Within 5 business days of transition completion |
| 8 | Archive vendor documentation (contracts, assessments, correspondence) per retention policy | Upon completion |

### 10.2 Emergency Termination

In the event that immediate termination is required (e.g., critical security failure, material breach, unacceptable risk):

1. Security Officer recommends emergency termination to CEO/Owner with documented justification
2. CEO/Owner approves emergency termination
3. All vendor access is revoked immediately (accounts disabled, API keys rotated, VPN tunnels removed, firewall rules updated)
4. Data return and destruction processes are initiated on an expedited basis
5. Transition to alternative vendor or interim manual processes is executed per the contingency plan
6. Affected clients are notified within 24 hours of any service impact

### 10.3 Transition Planning

For Tier 1 vendors, Technijian maintains documented transition plans that include:

- Identification of alternative vendors or in-house capabilities
- Estimated transition timeline and resource requirements
- Data migration procedures
- Service continuity measures during transition
- Client communication plan
- Testing and validation procedures for the replacement solution

---

## 11. Compliance Mapping

This policy supports Technijian's compliance obligations across the following frameworks and regulations:

| Framework / Regulation | Requirement | Policy Section |
|---|---|---|
| **SOC 2 Trust Services Criteria** | **CC9.2** - Risk from vendor and business partner relationships is assessed, managed, and monitored | Sections 3, 4, 5, 6 |
| **HIPAA Security Rule** | **164.308(b)(1)** - Business Associate Contracts: Written contract or arrangement with business associates that create, receive, maintain, or transmit PHI | Sections 4.1, 4.5 |
| **HIPAA Security Rule** | **164.308(b)(4)** - Written contract or other arrangement: Document the satisfactory assurances required by 164.308(b)(1) | Section 4.5 |
| **HIPAA Security Rule** | **164.314(a)** - Business Associate Contracts or Other Arrangements | Section 4 |
| **PCI-DSS v4.0** | **Req 12.8** - Risk to information assets associated with third-party service provider relationships is managed | Sections 3, 4, 5, 6 |
| **PCI-DSS v4.0** | **Req 12.8.1** - List of third-party service providers is maintained | Section 8 |
| **PCI-DSS v4.0** | **Req 12.8.2** - Written agreements with service providers include acknowledgment of responsibility for cardholder data security | Section 4.5 |
| **PCI-DSS v4.0** | **Req 12.8.4** - Program to monitor service providers' PCI-DSS compliance status | Section 5 |
| **PCI-DSS v4.0** | **Req 12.8.5** - Information about which PCI-DSS requirements are managed by each provider | Section 8.2 |
| **GDPR** | **Art 28** - Processor: Binding contract with processors setting out subject-matter, duration, nature and purpose of processing, obligations and rights of the controller | Sections 4.5, 7 |
| **GDPR** | **Art 28(2)** - Sub-processor engagement requires prior authorization of the controller | Section 7.1 |
| **GDPR** | **Art 28(3)(h)** - Processor makes available all information necessary to demonstrate compliance and allow for audits | Section 4.5 |
| **GDPR** | **Art 28(4)** - Sub-processor must be bound by the same data protection obligations | Section 7.1 |
| **NIST CSF** | **ID.SC** - Supply Chain Risk Management | Sections 3, 4, 5, 6 |
| **NIST CSF** | **ID.SC-1** - Supply chain risk management processes are identified, established, assessed, managed, and agreed to | Section 4 |
| **NIST CSF** | **ID.SC-2** - Suppliers and third-party partners are identified, prioritized, and assessed | Sections 3, 6 |
| **NIST CSF** | **ID.SC-4** - Suppliers and third-party partners are routinely assessed using audits, test results, or other forms of evaluation | Section 5 |
| **SEC Regulation S-P** | **Rule 30** - Safeguards Rule: Oversight of service providers | Sections 4, 5 |
| **FTC Safeguards Rule** | **314.4(f)** - Oversee service providers | Sections 4, 5, 6 |

---

## 12. Policy Review

### 12.1 Review Frequency

This policy is reviewed and updated on an annual basis. The next scheduled review is April 6, 2027.

Out-of-cycle reviews are triggered by:

- Significant vendor security incidents affecting Technijian or its clients
- Changes in applicable laws, regulations, or contractual requirements (e.g., new privacy laws, updated PCI-DSS requirements)
- Major changes to Technijian's vendor ecosystem (onboarding of new Tier 1 vendors, termination of critical vendors)
- Audit findings or risk assessment results identifying gaps in vendor risk management
- Industry developments or emerging best practices in third-party risk management

### 12.2 Review Responsibility

The Security Officer (Ravi Jain) is responsible for conducting the annual review. Updated policies are approved by the CEO/Owner before distribution.

### 12.3 Communication

Policy updates are communicated to all Technijian personnel involved in vendor management. Updated versions are published to the controlled document repository.

---

## Appendix A: Version History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | April 6, 2026 | Ravi Jain | Initial release |

---

## Appendix B: Related Documents

| Document | Reference |
|---|---|
| Information Security Program (WISP) | Technijian WISP v1.0 |
| Acceptable Use Policy (AUP) | Technijian AUP v1.0 |
| Incident Response Plan | Technijian IRP |
| Business Continuity / Disaster Recovery Plan | Technijian BCP/DR |
| Data Classification and Handling Guide | WISP Section 5.1 |
| Vendor Security Questionnaire Template | VRM-FORM-001 |
| Vendor Risk Assessment Template | VRM-FORM-002 |

---

## Appendix C: Vendor Security Questionnaire Domains

The following domains are covered in the Technijian Vendor Security Questionnaire (full version for Tier 1, abbreviated for Tier 2):

| # | Domain | Key Topics |
|---|---|---|
| 1 | Governance | Security program, policies, designated security officer, board/management oversight |
| 2 | Access Control | Authentication, MFA, RBAC, privileged access management, access reviews |
| 3 | Data Protection | Encryption at rest/in transit, data classification, DLP, key management |
| 4 | Network Security | Firewalls, segmentation, IDS/IPS, monitoring, wireless security |
| 5 | Endpoint Security | EDR, patching, hardening, mobile device management |
| 6 | Vulnerability Management | Scanning frequency, remediation SLAs, penetration testing |
| 7 | Incident Response | IR plan, breach notification timelines, forensic capabilities |
| 8 | Business Continuity | DR plan, RTO/RPO, backup and recovery testing |
| 9 | Human Resources | Background checks, security training, termination procedures |
| 10 | Physical Security | Data center controls, access logging, environmental controls |
| 11 | Compliance | SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR certifications and audit history |
| 12 | Sub-processors | Sub-processor list, due diligence process, contractual controls |
| 13 | Data Retention | Retention periods, destruction methods, certificates of destruction |
| 14 | Privacy | Privacy program, data subject rights, cross-border transfers |

---

*Technijian, Inc. | 18 Technology Drive, Suite 141, Irvine, CA 92618*
