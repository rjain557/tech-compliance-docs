# Technijian, Inc.

# Change Management Policy

**Version:** 1.0
**Date:** April 6, 2026
**Classification:** Confidential
**Document Owner:** Ravi Jain - CEO/Owner
**Approved By:** Ravi Jain - CEO/Owner
**Next Review Date:** April 6, 2027

---

## 1. Purpose

This policy establishes a structured and controlled approach to managing changes to Technijian, Inc.'s ("Technijian") information systems, infrastructure, applications, and configurations. As a managed IT services provider serving clients across healthcare, financial services, and other regulated industries, Technijian must ensure that all changes are planned, tested, approved, and documented to:

- Minimize the risk of service disruptions, security incidents, and unintended consequences
- Maintain the integrity, availability, and security of production systems and client environments
- Ensure compliance with SOC 2, HIPAA, PCI-DSS, and other applicable regulatory frameworks
- Provide full traceability and auditability of all changes to production environments
- Enable effective communication among stakeholders before, during, and after changes

### 1.1 Scope

This policy applies to:

- All changes to Technijian-managed production systems, networks, infrastructure, and applications
- All changes to client environments managed by Technijian under service agreements
- Changes to security controls, firewall rules, access control configurations, and encryption settings
- Changes to cloud service configurations (Microsoft 365, Azure, AWS)
- Changes to monitoring, alerting, and backup configurations
- Software deployments, patches, firmware updates, and configuration modifications
- All Technijian employees, contractors, subcontractors, and temporary personnel who initiate, approve, implement, or verify changes

---

## 2. Definitions

| Term | Definition |
|---|---|
| **Change** | Any addition, modification, or removal of anything that could have a direct or indirect effect on IT services, infrastructure, or configurations |
| **Standard Change** | A pre-authorized, low-risk, routine change that follows an established and documented procedure. Standard changes do not require individual CAB approval. Examples: scheduled patch deployment per approved schedule, user account creation/modification per established process, password resets, adding a printer |
| **Normal Change** | A change that follows the full change management process, including risk assessment, CAB review, and formal approval. Normal changes include infrastructure modifications, firewall rule changes, new system deployments, and application upgrades |
| **Emergency Change** | A change that must be implemented immediately to restore service, resolve a critical security vulnerability, or prevent imminent significant harm. Emergency changes bypass the standard approval process but require retrospective review and documentation within 48 hours |
| **Change Advisory Board (CAB)** | A cross-functional body responsible for reviewing, assessing, and approving or rejecting Normal changes. The CAB evaluates risk, impact, and readiness before authorizing implementation |
| **Change Request (CR)** | A formal document or ticket that records all details of a proposed change, including description, justification, risk assessment, implementation plan, rollback plan, and approvals |
| **Change Window** | A pre-approved timeframe during which changes may be implemented to minimize impact on business operations. Technijian's standard change window is Saturday 10:00 PM - Sunday 6:00 AM PT unless otherwise specified by the client |
| **Rollback Plan** | A documented procedure to reverse a change and restore systems to their pre-change state if the change fails or causes unacceptable issues |
| **Post-Implementation Review (PIR)** | A formal review conducted after change implementation to assess success, identify issues, and capture lessons learned |

---

## 3. Change Classification

### 3.1 Classification Matrix

| Attribute | Standard Change | Normal Change | Emergency Change |
|---|---|---|---|
| **Risk Level** | Low | Low to High | Critical |
| **Pre-Approval** | Pre-authorized via catalog | CAB approval required | Post-implementation approval |
| **Documentation** | Template-based | Full CR required | Abbreviated CR; full documentation within 48 hours |
| **Testing Required** | Per standard procedure | Required before implementation | Best effort; full testing post-implementation |
| **Rollback Plan** | Documented in standard procedure | Required in CR | Required (may be abbreviated) |
| **Implementation Window** | During standard change window or as defined in procedure | Scheduled during change window | Immediate |
| **CAB Review** | Not required (pre-authorized) | Required | Retrospective review within 48 hours |
| **Notification** | Automated notification | Stakeholder notification required | Emergency notification per escalation procedures |
| **Examples** | Routine patching, user provisioning, printer setup | Server migration, firewall rule change, new application deployment | Active security breach remediation, critical outage restoration |

### 3.2 Risk Assessment Criteria

Each Normal Change must be assessed for risk using the following criteria:

| Factor | Low | Medium | High |
|---|---|---|---|
| **Impact Scope** | Single system or user | Multiple systems or department | Organization-wide or client-facing |
| **Downtime** | None or < 15 minutes | 15 minutes to 2 hours | > 2 hours |
| **Reversibility** | Easily reversible | Reversible with effort | Difficult or impossible to reverse |
| **Compliance Impact** | None | Minor policy impact | Regulatory or audit impact |
| **Data Risk** | No data impact | Potential data modification | Risk of data loss or corruption |
| **Client Impact** | None | Minor inconvenience | Service disruption or SLA impact |

---

## 4. Change Request Process

### 4.1 Process Flow

All Normal Changes follow this six-step process:

#### Step 1: Request

- The change requester submits a Change Request (CR) through the Technijian ticketing system
- The CR must include:
  - Description of the change and business justification
  - Systems, services, and clients affected
  - Risk assessment using the criteria in Section 3.2
  - Proposed implementation date and change window
  - Detailed implementation plan with step-by-step instructions
  - Rollback plan
  - Testing plan and expected outcomes
  - Communication plan (who needs to be notified before, during, and after)
  - Estimated duration
  - Resource requirements (personnel, tools, vendor involvement)

#### Step 2: Review

- The CR is reviewed by the CAB for completeness, accuracy, and risk
- The CAB evaluates:
  - Technical soundness of the implementation plan
  - Adequacy of the rollback plan
  - Potential conflicts with other scheduled changes
  - Resource availability
  - Client notification requirements
  - Compliance implications
- The CAB may request additional information, modifications to the plan, or deferral to a future change window

#### Step 3: Approve

- Approval authority is determined by change classification and risk level:

| Change Type / Risk | Approval Authority |
|---|---|
| Standard Change | Pre-authorized (no individual approval needed) |
| Normal Change - Low Risk | Change Manager or designated CAB member |
| Normal Change - Medium Risk | CAB majority approval |
| Normal Change - High Risk | CAB unanimous approval + Security Officer |
| Emergency Change | Security Officer or CEO/Owner (retrospective CAB review within 48 hours) |

- Approved CRs are scheduled for implementation during the designated change window
- Rejected CRs are returned to the requester with documented reasons and guidance for resubmission

#### Step 4: Implement

- The change implementer executes the change according to the approved implementation plan
- Deviations from the approved plan must be documented and, if material, approved by the Change Manager before proceeding
- The implementation is performed during the approved change window
- Communication is provided to affected stakeholders per the communication plan
- Real-time status updates are posted to the CR ticket during implementation

#### Step 5: Verify

- Upon completion, the implementer verifies that:
  - The change was implemented as planned
  - Affected systems and services are functioning correctly
  - No unintended side effects are observed
  - Monitoring and alerting are confirming normal operation
- Verification results are documented in the CR ticket
- If verification fails, the rollback plan is executed immediately

#### Step 6: Close

- The CR ticket is updated with:
  - Final implementation status (Successful, Successful with Issues, Failed/Rolled Back)
  - Actual implementation date and time
  - Deviations from the plan (if any)
  - Verification results
  - Lessons learned (if applicable)
- The CR is closed by the Change Manager after confirming all documentation is complete

---

## 5. Change Advisory Board (CAB)

### 5.1 Composition

The CAB consists of the following members:

| Role | Responsibility |
|---|---|
| **Change Manager** (Chair) | Facilitates CAB meetings, manages the change calendar, ensures process compliance |
| **Security Officer** | Evaluates security implications of proposed changes; mandatory reviewer for changes affecting security controls, firewall rules, access management, or client environments |
| **IT Operations Lead** | Assesses operational impact, resource requirements, and implementation feasibility |
| **Client Account Manager** | Represents client interests; ensures client notification and approval requirements are met |
| **Subject Matter Expert(s)** | Invited as needed based on the technical domain of the change (e.g., network, cloud, database) |

### 5.2 CAB Meetings

- **Scheduled Meetings:** The CAB meets weekly (or as needed) to review pending Normal Change Requests
- **Emergency Meetings:** Convened within 1 hour for Emergency Changes that require immediate discussion
- **Quorum:** A minimum of three CAB members, including the Change Manager and Security Officer, constitutes a quorum for decision-making
- **Meeting Records:** Minutes of CAB meetings, including decisions, attendees, and action items, are documented and retained for a minimum of 3 years

---

## 6. Emergency Change Procedures

### 6.1 Emergency Change Criteria

A change qualifies as an Emergency Change only when:

- A critical production system or client environment is down or severely degraded
- An active security incident requires immediate remediation
- A critical vulnerability with known active exploitation must be patched immediately
- Delay would result in significant financial harm, regulatory non-compliance, or safety risk

### 6.2 Emergency Change Process

1. **Authorization:** The Security Officer or CEO/Owner verbally authorizes the emergency change. If neither is available, the senior-most IT Operations personnel on duty may authorize with mandatory retrospective review
2. **Implementation:** The change is implemented immediately with the best available resources. A rollback plan must be identified before implementation, even if abbreviated
3. **Documentation:** An abbreviated Change Request is created during or immediately after implementation, with full documentation completed within 48 hours
4. **Retrospective Review:** The CAB conducts a retrospective review of all Emergency Changes within 48 hours of implementation. The review assesses appropriateness of the emergency classification, adequacy of the implementation, and any follow-up actions required

### 6.3 Emergency Change Financial Authority

Emergency changes that require unplanned expenditure are subject to the following approval thresholds:

| Expenditure | Approval Authority |
|---|---|
| Up to $2,500 | Security Officer or IT Operations Lead |
| $2,500 - $10,000 | CEO/Owner |
| Over $10,000 | CEO/Owner with documented justification |

The $2,500 threshold aligns with Technijian's standard Statement of Work emergency service provisions. Any emergency work exceeding this cap for client environments requires client authorization before proceeding, unless delay would cause immediate and irreversible harm.

---

## 7. Rollback Procedures

### 7.1 Rollback Requirements

- Every Normal and Emergency Change must have a documented rollback plan before implementation begins
- The rollback plan must include:
  - Step-by-step instructions to restore systems to pre-change state
  - Estimated time to complete rollback
  - Data backup verification (confirm backups are current and accessible before implementing the change)
  - Contact information for escalation during rollback
  - Criteria that trigger rollback (e.g., service unavailable for more than 15 minutes, data integrity issues detected)

### 7.2 Rollback Execution

- Rollback is initiated when:
  - Verification (Step 5) fails and the issue cannot be resolved within the change window
  - Unintended side effects are detected that impact service availability or security
  - The change implementer or Change Manager determines that continuing poses unacceptable risk
- Rollback execution is documented in the CR ticket, including the reason for rollback, steps taken, and final system state
- A Post-Implementation Review is required for all rolled-back changes

---

## 8. Documentation Requirements

### 8.1 Change Request Documentation

All Change Requests must be retained in the Technijian ticketing system with the following minimum documentation:

| Element | Required For |
|---|---|
| Change description and justification | All changes |
| Risk assessment | Normal and Emergency changes |
| Implementation plan | All changes |
| Rollback plan | Normal and Emergency changes |
| Testing evidence | Normal changes |
| Approval records | All changes |
| Implementation log (start time, end time, steps executed) | All changes |
| Verification results | All changes |
| Post-Implementation Review | High-risk Normal, Emergency, and failed changes |

### 8.2 Retention

- Change Request records are retained for a minimum of 3 years
- Records supporting regulatory compliance (SOC 2, HIPAA, PCI-DSS) are retained per the Data Classification and Retention Policy

---

## 9. Change Freeze Periods

### 9.1 Scheduled Freeze Periods

Change freeze periods are designated timeframes during which no Standard or Normal Changes may be implemented unless explicitly approved by the CEO/Owner. Change freezes are imposed during:

- **Holiday Periods:** Thanksgiving week, December 20 through January 2, and other holidays as designated annually by the CEO/Owner
- **Client-Specific Freezes:** As specified in client service agreements (e.g., fiscal year-end, regulatory filing periods, open enrollment periods)
- **Audit Periods:** During active SOC 2, HIPAA, PCI-DSS, or other compliance audits where change activity could affect audit scope

### 9.2 Freeze Exceptions

- Emergency Changes may be implemented during freeze periods following the Emergency Change Process (Section 6)
- Non-emergency changes during freeze periods require written approval from the CEO/Owner with documented justification
- All freeze period exceptions are reported to the CAB at the next scheduled meeting

---

## 10. Post-Implementation Review (PIR)

### 10.1 PIR Requirements

A Post-Implementation Review is required for:

- All High-Risk Normal Changes
- All Emergency Changes
- All changes that were rolled back
- Any change that caused an unplanned service disruption
- Any change flagged by the CAB for mandatory PIR

### 10.2 PIR Content

The PIR must address the following:

| Element | Description |
|---|---|
| **Change Summary** | Brief description of the change and its business objective |
| **Outcome** | Success, partial success, or failure |
| **Timeline** | Actual vs. planned implementation timeline |
| **Issues Encountered** | Any problems, deviations, or unexpected results |
| **Root Cause (if applicable)** | Root cause analysis for failures or significant issues |
| **Impact** | Actual impact on services, clients, and users |
| **Lessons Learned** | What went well, what could be improved, process improvements |
| **Follow-Up Actions** | Assigned action items with owners and due dates |

### 10.3 PIR Timeline

- PIRs must be completed within 5 business days of change implementation
- PIR findings and action items are reviewed at the next CAB meeting
- Systemic issues identified through PIRs are escalated to the Security Officer for risk register consideration

---

## 11. Compliance Mapping

This policy supports compliance with the following regulatory frameworks and standards:

| Framework / Standard | Relevant Requirements | Policy Section(s) |
|---|---|---|
| **SOC 2 Trust Services Criteria** | CC8.1 (Change Management) — The entity authorizes, designs, develops or acquires, configures, documents, tests, approves, and implements changes to infrastructure, data, software, and procedures to meet its objectives | Sections 3-10 |
| **PCI-DSS v4.0** | Req 6.5 — Changes to all system components in the production environment are managed and documented. Req 6.5.1 — Procedures to manage changes are documented and followed. Req 6.5.2 — Changes are approved by authorized parties. Req 6.5.3 — Changes are tested. Req 6.5.4 — Rollback procedures are in place. Req 6.5.5 — Change documentation includes impact, approval, and testing | Sections 4, 7, 8 |
| **HIPAA Security Rule** | §164.312(e)(2)(ii) — Mechanism to authenticate ePHI integrity. §164.308(a)(5)(ii)(C) — Security reminders. Change management supports overall security management process requirements | Sections 4, 7, 10 |
| **NIST CSF** | PR.IP-3 (Configuration Change Control Processes) — Configuration change control processes are in place | Sections 3-10 |
| **NIST SP 800-53** | CM-3 (Configuration Change Control), CM-4 (Impact Analyses), CM-5 (Access Restrictions for Change) | Sections 3, 4, 5 |
| **GDPR** | Art 32 (Security of Processing) — Ability to ensure ongoing confidentiality, integrity, availability, and resilience of processing systems. Change management supports Art 32 compliance | Sections 4, 7, 10 |
| **ITIL v4** | Change Enablement Practice | Sections 3-10 |

---

## 12. Policy Review

### 12.1 Review Cycle

This policy is reviewed and approved on an annual basis by the Security Officer (Ravi Jain, CEO/Owner). The annual review occurs no later than the anniversary of the last approval date.

### 12.2 Out-of-Cycle Reviews

Out-of-cycle reviews are triggered by:

- Changes in applicable laws, regulations, or contractual requirements
- Significant security incidents resulting from change management failures
- Major changes to Technijian's infrastructure, technology stack, or service offerings
- Audit findings related to change management controls
- Post-Implementation Review trends indicating systemic process issues

### 12.3 Version History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | April 6, 2026 | Ravi Jain | Initial release |

### 12.4 Acknowledgment

All Technijian employees, contractors, and subcontractors with access to production systems must acknowledge receipt and understanding of this policy within 30 days of hire or contract start date, and annually thereafter.

---

**Technijian, Inc.**
18 Technology Drive, Suite 141
Irvine, CA 92618

*This document is the property of Technijian, Inc. and is classified as Confidential. Unauthorized distribution or reproduction is prohibited.*
