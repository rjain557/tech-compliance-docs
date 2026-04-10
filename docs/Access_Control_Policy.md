# Technijian, Inc.

# Access Control Policy

**Version:** 1.0
**Date:** April 6, 2026
**Classification:** Confidential
**Document Owner:** Ravi Jain - CEO/Owner
**Approved By:** Ravi Jain - CEO/Owner
**Next Review Date:** April 6, 2027

---

## 1. Purpose

This policy establishes the requirements for controlling access to Technijian, Inc.'s ("Technijian") information systems, networks, applications, data, and client environments. As a managed IT services provider handling sensitive data for clients in healthcare, financial services, and other regulated industries, Technijian must implement and maintain rigorous access controls to:

- Protect the confidentiality, integrity, and availability of information assets
- Prevent unauthorized access to Technijian and client systems and data
- Comply with SOC 2, HIPAA, PCI-DSS, GDPR, and other applicable regulatory frameworks
- Maintain client trust through demonstrable access governance
- Enable audit traceability for all access to sensitive systems and data

This policy supplements the Technijian Information Security Program (WISP) and provides detailed access control requirements for all personnel.

### 1.1 Scope

This policy applies to:

- All information systems, networks, applications, databases, cloud services, and physical facilities owned or managed by Technijian
- All client systems and environments managed by Technijian under service agreements
- All Technijian employees, contractors, subcontractors, and temporary personnel
- All access methods including on-site, remote, VPN, and cloud-based access
- All account types including user accounts, privileged accounts, service accounts, shared accounts, and guest accounts
- Technijian headquarters at 18 Technology Drive, Suite 141, Irvine, CA 92618, the TPX data center, and all remote work locations

---

## 2. Access Control Principles

### 2.1 Least Privilege

All users are granted only the minimum level of access necessary to perform their assigned job functions. No user receives administrative, elevated, or broad access by default. Access is scoped to specific systems, applications, data sets, and actions required for the user's role.

- Access rights are determined by job function, not by individual request
- Default access for new accounts is restricted; additional access requires formal approval
- Access is reduced or revoked when job functions change or when access is no longer needed
- Temporary elevated access is granted on a time-limited basis with automatic expiration

### 2.2 Separation of Duties

Critical functions are divided among multiple individuals to prevent fraud, error, abuse of privilege, and conflicts of interest.

- No single individual has unchecked control over any critical process
- The individual who requests a change must not be the sole approver of that change
- The individual who develops or configures a system must not be the sole person who deploys it to production
- Financial transactions, system administration, and security monitoring functions are separated where operationally feasible
- Where complete separation is not possible due to organizational size, compensating controls (e.g., enhanced logging, management review) are implemented and documented

### 2.3 Need-to-Know

Access to information is restricted to individuals who have a demonstrated business need to access that information for their current job responsibilities.

- Need-to-know is evaluated at the time of access request and during periodic access reviews
- Access to Restricted and Confidential data (per the Data Classification and Retention Policy) requires explicit justification and approval
- Access to client environments requires assignment to that client engagement
- Curiosity, convenience, or seniority alone do not constitute need-to-know

---

## 3. Account Management

### 3.1 Account Types

| Account Type | Definition | Governance |
|---|---|---|
| **Standard User Account** | Individual account for day-to-day business operations | Assigned to one person; requires manager and system owner approval |
| **Privileged Account** | Account with elevated permissions (domain admin, root, system admin, database admin) | Requires Security Officer approval; subject to PAM controls (Section 6); separate from standard user account |
| **Service Account** | Non-interactive account used by applications, scripts, or automated processes | Requires system owner approval; documented purpose; strong unique password; no interactive login; reviewed quarterly |
| **Shared Account** | Account used by multiple individuals (prohibited except where technically unavoidable) | Requires Security Officer approval with documented justification; all users of the shared account must be identified; usage is logged; reviewed quarterly |
| **Guest / Temporary Account** | Time-limited account for visitors, auditors, or short-term contractors | Maximum 90-day validity with automatic expiration; requires sponsor approval; limited access scope |
| **Emergency / Break-Glass Account** | Account for critical system access when normal access is unavailable | Sealed credentials stored securely; usage triggers immediate alert; requires retrospective review within 24 hours |

### 3.2 Account Naming Standards

- Standard user accounts: firstname.lastname or organizational standard
- Privileged accounts: adm-firstname.lastname or priv-firstname.lastname to distinguish from standard accounts
- Service accounts: svc-applicationname-purpose
- All accounts must be uniquely identifiable and traceable to an individual owner or responsible party

### 3.3 Account Lifecycle

| Event | Action | Timeline |
|---|---|---|
| **New Account Request** | Formal request submitted with business justification | Before access is needed |
| **Account Approval** | Manager approval + system owner approval (+ Security Officer for privileged) | Within 2 business days |
| **Account Provisioning** | IT Operations creates account per approved role template | Within 1 business day of approval |
| **Role Change** | Access adjusted to match new role; previous role access revoked | Within 3 business days of role change |
| **Extended Leave** | Account disabled for leaves exceeding 30 days | Day 1 of leave |
| **Termination** | Account disabled immediately; see Section 9.2 | Same day |
| **Inactivity** | Accounts inactive for 45 days are automatically disabled | Automated |
| **Disabled Account Cleanup** | Disabled accounts deleted after 90 days (unless retention required) | Automated with review |

---

## 4. Authentication Requirements

### 4.1 Multi-Factor Authentication (MFA)

MFA is required for all access to the following systems and services:

- Administrative and privileged access interfaces
- All client environments
- Cloud services (Microsoft 365, Azure, AWS, SaaS platforms)
- VPN connections
- Email (Exchange Online, Outlook)
- Remote desktop and remote management tools
- Security tools and consoles (CrowdStrike, ManageEngine)
- Password vaults and key management systems

**Approved MFA Methods:**

| Method | Permitted Use |
|---|---|
| Authenticator applications (TOTP-based: Microsoft Authenticator, Google Authenticator) | All use cases |
| Hardware security tokens (YubiKey, FIDO2 keys) | All use cases (preferred for privileged accounts) |
| FIDO2/WebAuthn keys | All use cases |
| Push notifications (Microsoft Authenticator) | Standard user accounts |
| SMS-based codes | **Prohibited** for administrative/privileged accounts due to SIM-swap and interception risks. Permitted as a backup method for standard accounts only with documented risk acceptance |
| Phone call verification | **Prohibited** for administrative/privileged accounts |

MFA is enforced via conditional access policies in Microsoft 365/Azure AD and equivalent controls in other platforms.

### 4.2 Password Requirements

| Parameter | Standard Accounts | Privileged Accounts |
|---|---|---|
| **Minimum Length** | 14 characters | 16 characters |
| **Complexity** | Mix of uppercase, lowercase, numbers, and special characters; or a passphrase of 4+ random words | Mix of uppercase, lowercase, numbers, and special characters; or a passphrase of 5+ random words |
| **Maximum Age** | 365 days | 90 days |
| **Password History** | No reuse of last 12 passwords | No reuse of last 24 passwords |
| **Lockout Threshold** | 5 consecutive failed attempts | 3 consecutive failed attempts |
| **Lockout Duration** | 15 minutes | 30 minutes (with Security Officer notification) |
| **Breach Database Check** | Required at creation and rotation | Required at creation and rotation |
| **Storage** | Stored in approved password vault | Stored in PAM solution only |

### 4.3 Session Management

- VPN and remote desktop sessions automatically disconnect after 30 minutes of inactivity
- Web application sessions expire after 60 minutes of inactivity for standard users, 15 minutes for privileged sessions
- Concurrent session limits are enforced where technically feasible
- All sessions to client environments are logged with start time, end time, and source IP

---

## 5. Access Reviews

### 5.1 Review Schedule

| Review Type | Frequency | Scope | Reviewer |
|---|---|---|---|
| **Privileged Access Review** | Quarterly | All privileged accounts, domain admin, root, database admin, cloud admin | Security Officer |
| **Standard User Access Review** | Semi-annually | All standard user accounts and role assignments | Direct managers with Security Officer oversight |
| **Service Account Review** | Quarterly | All service accounts, purpose validation, credential rotation status | System owners with Security Officer review |
| **Shared Account Review** | Quarterly | All shared accounts (if any exist), user lists, justification revalidation | Security Officer |
| **Client Environment Access Review** | Quarterly | All personnel with access to each client environment | Account managers and Security Officer |
| **Guest/Temporary Account Review** | Monthly | All active guest and temporary accounts | Sponsors and IT Operations |
| **Emergency/Break-Glass Account Review** | After each use + quarterly | Break-glass account usage logs and credential integrity | Security Officer |

### 5.2 Review Process

1. IT Operations generates access reports for all systems, including user lists, role assignments, and permission levels
2. Designated reviewers evaluate each access grant against current job responsibilities and need-to-know
3. Reviewers confirm access that remains appropriate and flag access that should be revoked or modified
4. Excess or inappropriate permissions are revoked within 5 business days of identification
5. Orphaned accounts (accounts with no active owner) are disabled immediately and investigated
6. Review completion, findings, and remediation actions are documented and retained for a minimum of 3 years

### 5.3 Access Review Evidence

Access review records include:

- Date of review
- Systems and accounts reviewed
- Reviewer identity and sign-off
- Findings (access confirmed, access revoked, access modified)
- Remediation actions taken and completion dates
- Evidence of management approval

---

## 6. Privileged Access Management (PAM)

### 6.1 PAM Requirements

Privileged accounts (domain admin, root, system admin, database admin, cloud admin, and accounts with elevated permissions) are subject to the following additional controls:

| Control | Requirement |
|---|---|
| **Just-in-Time (JIT) Access** | Privileged access is granted on a just-in-time basis where technically feasible. Permanent standing privileged access is minimized. JIT access requests require documented justification, approval, and a defined time window (maximum 8 hours unless extended with re-approval) |
| **Privileged Account Inventory** | All privileged accounts are inventoried with a designated owner, documented purpose, and classification of systems accessible. The inventory is updated in real-time as accounts are created, modified, or decommissioned |
| **Session Recording** | All privileged access sessions to production systems and client environments are recorded (screen capture and/or keystroke logging where technically feasible). Session recordings are retained for a minimum of 1 year and are available for security investigation and audit |
| **Credential Vaulting** | All privileged account credentials are stored in an approved password vault / PAM solution. Direct knowledge of privileged passwords by individuals is minimized. Credentials are checked out from the vault for each session and checked back in upon completion |
| **Automatic Credential Rotation** | Privileged account passwords are rotated automatically after each checkout/use where technically feasible, and at a minimum every 90 days |
| **Privileged Account Separation** | Privileged accounts are separate from standard user accounts. Personnel requiring privileged access must use their standard account for day-to-day activities and their privileged account only when performing administrative tasks |
| **Privileged Action Logging** | All actions performed using privileged accounts are logged, including authentication events, configuration changes, data access, and command execution. Logs are tamper-protected and retained per the Data Classification and Retention Policy |

### 6.2 Privileged Access Log Review

| System Category | Review Frequency |
|---|---|
| High-risk systems (domain controllers, firewalls, client production systems) | Weekly |
| Standard systems | Monthly |
| Service accounts | Monthly |

---

## 7. Remote Access

### 7.1 VPN Access

- All remote access to internal Technijian networks requires connection through the corporate VPN
- VPN connections use IPsec or TLS-based tunnels with AES-256 encryption
- Split tunneling is disabled on VPN connections to ensure all traffic routes through monitored infrastructure
- VPN access requires MFA authentication
- VPN connections are automatically terminated after 30 minutes of inactivity

### 7.2 Endpoint Compliance

Devices connecting remotely must pass endpoint compliance checks before VPN connection is established:

- Current and active EDR agent (CrowdStrike Falcon)
- Operating system and patches within compliance thresholds
- Full-disk encryption enabled (BitLocker/FileVault)
- Active screen lock configured (maximum 5 minutes of inactivity)
- Device registered in Technijian's asset inventory or MDM enrollment

Non-compliant devices are denied VPN access until remediated.

### 7.3 Zero Trust Network Access (ZTNA)

Technijian implements Zero Trust principles for remote access:

- Identity verification is required for every access request regardless of network location
- Device health and compliance are evaluated continuously, not just at connection time
- Access is granted to specific applications and resources, not to entire network segments
- All access is logged and monitored regardless of the user's location or network
- Implicit trust based on network location (e.g., "inside the firewall") is not granted

---

## 8. Client System Access

### 8.1 Client Access Requirements

Access to client environments managed by Technijian is subject to the following additional controls:

| Requirement | Detail |
|---|---|
| **Separate Credentials** | Unique credentials are maintained for each client environment. Technijian personnel must not reuse passwords across client environments or between Technijian and client systems |
| **Client-Specific MFA** | MFA is required for all client environment access, using client-approved MFA methods where specified |
| **Access Authorization** | Access to a client environment requires assignment to that client engagement by the account manager. Access is limited to systems and data necessary for the assigned scope of work |
| **Credential Storage** | All client environment credentials are stored in the approved password vault, segregated by client. Client credentials are never stored in personal password managers, text files, email, or shared documents |
| **Access Logging** | All access to client environments is logged with timestamp, user identity, source IP, systems accessed, and session duration. Logs are retained per the Data Classification and Retention Policy |
| **Cross-Client Isolation** | Access to one client environment does not grant access to any other client environment. Cross-client access requires separate authorization for each client |
| **Client Notification** | Clients are notified of all personnel authorized to access their environments. Changes in authorized personnel are communicated promptly |
| **Credential Rotation** | Client environment credentials are rotated every 90 days, upon personnel change, and immediately upon suspected compromise |

### 8.2 Client Compliance Requirements

Where client contracts or regulatory requirements specify access control standards that exceed those in this policy, the more stringent requirements apply. Common client-specific requirements include:

- Background check requirements (e.g., HIPAA for healthcare clients, FINRA for financial services)
- Specific MFA methods or authentication standards
- Dedicated workstations for client access
- Additional logging or monitoring requirements
- Security awareness training specific to the client's industry

---

## 9. Onboarding and Offboarding

### 9.1 Onboarding (New Hire / New Contractor)

| Step | Action | Timeline | Responsible |
|---|---|---|---|
| 1 | Background check completed and cleared | Before start date | Human Resources |
| 2 | NDA and acceptable use policy signed | Day 1 | Human Resources |
| 3 | Security awareness training completed | Within 30 days | Security Officer / HR |
| 4 | Standard user account created per role template | Day 1 | IT Operations |
| 5 | MFA enrolled and verified | Day 1 | IT Operations / Employee |
| 6 | Endpoint provisioned with required security controls (EDR, encryption, MDM) | Day 1 | IT Operations |
| 7 | Client environment access provisioned (if applicable) | Upon client assignment | Account Manager / IT Operations |
| 8 | Privileged access provisioned (if applicable) | After Security Officer approval and PAM onboarding | Security Officer / IT Operations |
| 9 | Access provisioning documented in ticketing system | Day 1 | IT Operations |

### 9.2 Offboarding (Termination / Contract End)

| Step | Action | Timeline | Responsible |
|---|---|---|---|
| 1 | All system access disabled | **Same day** as termination / last day of contract | IT Operations (triggered by HR notification) |
| 2 | VPN access revoked | **Same day** | IT Operations |
| 3 | Email access revoked; out-of-office or forwarding configured per manager request | **Same day** | IT Operations |
| 4 | Cloud service access revoked (M365, Azure, AWS, SaaS) | **Same day** | IT Operations |
| 5 | Client environment credentials rotated for all clients the individual had access to | **Same day** | IT Operations / Account Managers |
| 6 | MFA tokens/registrations removed | **Same day** | IT Operations |
| 7 | Privileged account disabled and credentials rotated | **Same day** | Security Officer / IT Operations |
| 8 | Company equipment returned (laptop, phone, tokens, badges) | Within 3 business days | HR / IT Operations |
| 9 | Shared credentials rotated for any shared accounts the individual accessed | **Same day** | IT Operations |
| 10 | Remote access to client environments confirmed revoked | Within 24 hours | Account Managers |
| 11 | Offboarding checklist completed and documented | Within 3 business days | HR / IT Operations |

**Same-day revocation is mandatory.** IT Operations must maintain the capability to execute emergency access revocation within 1 hour of notification for involuntary terminations.

### 9.3 Role Changes and Transfers

When an employee changes roles or transfers to a different team:

- Previous role access is reviewed and revoked within 3 business days
- New role access is provisioned per the standard access request process
- Client environment access is adjusted to reflect the new assignment
- The role change is documented in the ticketing system and reflected in the next access review

---

## 10. Monitoring and Enforcement

### 10.1 Access Monitoring

- Authentication events (successful and failed) are logged for all systems
- Privileged account usage is monitored continuously with automated alerting for anomalous activity
- Failed login attempts exceeding lockout thresholds trigger automated alerts
- Access from unusual locations, devices, or at unusual times triggers risk-based authentication challenges
- Dark web monitoring is conducted for Technijian and client credential exposure; exposed credentials trigger immediate forced password reset and incident investigation

### 10.2 Anomaly Detection

The following events trigger automated alerts and investigation:

- Login from a geographic location inconsistent with the user's profile
- Simultaneous sessions from different locations
- Access to systems outside the user's normal scope
- Privilege escalation or role modification outside normal workflow
- Service account interactive login attempts
- Break-glass account usage
- Multiple failed MFA attempts
- Bulk data download or access pattern anomalies

### 10.3 Policy Violations

Violations of this policy are subject to disciplinary action up to and including termination of employment or contract. Confirmed violations are:

- Documented in the employee's personnel record
- Reported to the Security Officer for incident assessment
- Evaluated for potential regulatory notification requirements (e.g., HIPAA breach)
- Used as input for security awareness training improvements

---

## 11. Compliance Mapping

This policy supports compliance with the following regulatory frameworks and standards:

| Framework / Standard | Relevant Requirements | Policy Section(s) |
|---|---|---|
| **SOC 2 Trust Services Criteria** | CC6.1 (Logical and Physical Access Controls) — The entity implements logical access security software, infrastructure, and architectures over protected information assets. CC6.2 (Access Credentials) — The entity manages access credentials for infrastructure and software. CC6.3 (Access Removal) — The entity removes access to protected assets when appropriate | Sections 2-9 |
| **HIPAA Security Rule** | §164.312(a)(1) (Access Control) — Implement technical policies and procedures for systems maintaining ePHI to allow access only to authorized persons. §164.312(a)(2)(i) (Unique User Identification). §164.312(a)(2)(iii) (Automatic Logoff). §164.312(a)(2)(iv) (Encryption and Decryption). §164.312(d) (Person or Entity Authentication) | Sections 3, 4, 6, 7 |
| **PCI-DSS v4.0** | Req 7 (Restrict Access to System Components and Cardholder Data by Business Need to Know) — 7.1 Processes and mechanisms for restricting access are defined and understood. 7.2 Access to system components and data is appropriately defined and assigned. Req 8 (Identify Users and Authenticate Access) — 8.2 User identification and authentication. 8.3 Strong authentication. 8.4 MFA. 8.5 Shared/generic accounts. 8.6 Authentication mechanisms | Sections 2-6, 8 |
| **GDPR** | Art 32 (Security of Processing) — Implement appropriate technical and organizational measures including the ability to ensure the ongoing confidentiality, integrity, availability, and resilience of processing systems and services. Art 25 (Data Protection by Design and by Default) | Sections 2-8, 10 |
| **CCPA / CPRA** | §1798.150 (Reasonable Security) — Implement and maintain reasonable security procedures and practices | Sections 2-8 |
| **NIST CSF** | PR.AC (Identity Management, Authentication, and Access Control) — PR.AC-1 through PR.AC-7 | Sections 2-9 |
| **NIST SP 800-53** | AC-1 through AC-25 (Access Control family) | Sections 2-10 |
| **SEC Regulation S-P** | Rule 30(a) (Safeguard Rule) — Policies and procedures to protect customer records and information | Sections 2-8 |
| **FTC Safeguards Rule** | §314.4(c) (Access Controls) | Sections 2-8 |

---

## 12. Policy Review

### 12.1 Review Cycle

This policy is reviewed and approved on an annual basis by the Security Officer (Ravi Jain, CEO/Owner). The annual review occurs no later than the anniversary of the last approval date.

### 12.2 Out-of-Cycle Reviews

Out-of-cycle reviews are triggered by:

- Changes in applicable laws, regulations, or contractual requirements
- Security incidents involving unauthorized access
- Audit findings related to access controls
- Major changes to Technijian's infrastructure, identity management systems, or service offerings
- New client engagements with access control requirements not addressed by the current policy
- Changes in the threat landscape affecting access control risk

### 12.3 Version History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | April 6, 2026 | Ravi Jain | Initial release |

### 12.4 Acknowledgment

All Technijian employees, contractors, and subcontractors must acknowledge receipt and understanding of this policy within 30 days of hire or contract start date, and annually thereafter. Acknowledgment records are maintained by Human Resources.

---

**Technijian, Inc.**
18 Technology Drive, Suite 141
Irvine, CA 92618

*This document is the property of Technijian, Inc. and is classified as Confidential. Unauthorized distribution or reproduction is prohibited.*
