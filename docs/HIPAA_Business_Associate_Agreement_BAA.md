# HIPAA BUSINESS ASSOCIATE AGREEMENT

**Version:** 1.0
**Date:** [DATE]
**Classification:** Confidential
**Attached to Master Service Agreement:** [MSA-XXXX]

This Business Associate Agreement ("BAA") is entered into by and between:

**[CLIENT NAME]** ("Covered Entity")
[CLIENT ADDRESS]
[CITY, STATE ZIP]

and

**Technijian, Inc.** ("Business Associate")
18 Technology Drive, Suite 141
Irvine, California 92618

This BAA supplements the Master Service Agreement between the Parties (the "MSA") and establishes the Parties' obligations with respect to Protected Health Information under the Health Insurance Portability and Accountability Act of 1996, as amended by the Health Information Technology for Economic and Clinical Health Act ("HITECH Act"), and their implementing regulations at 45 CFR Parts 160 and 164 (collectively, "HIPAA").

---

## 1. DEFINITIONS

Capitalized terms used in this BAA shall have the meanings set forth in 45 CFR Parts 160 and 164, as applicable. The following terms are used in this BAA:

**1.01.** "**Protected Health Information**" or "**PHI**" means individually identifiable health information, as defined in 45 CFR § 160.103, that is created, received, maintained, or transmitted by Business Associate on behalf of Covered Entity.

**1.02.** "**Electronic Protected Health Information**" or "**ePHI**" means PHI that is created, stored, transmitted, or received in electronic form.

**1.03.** "**Breach**" has the meaning set forth in 45 CFR § 164.402.

**1.04.** "**Unsecured PHI**" means PHI that is not rendered unusable, unreadable, or indecipherable to unauthorized persons through the use of a technology or methodology specified by the Secretary in guidance issued under 42 U.S.C. § 17932(h)(2).

**1.05.** "**Security Incident**" has the meaning set forth in 45 CFR § 164.304.

**1.06.** "**Required By Law**" has the meaning set forth in 45 CFR § 164.103.

**1.07.** "**Secretary**" means the Secretary of the United States Department of Health and Human Services.

**1.08.** "**Individual**" means the person who is the subject of the PHI, and includes a person who qualifies as a personal representative under 45 CFR § 164.502(g).

---

## 2. OBLIGATIONS OF BUSINESS ASSOCIATE

**2.01. Use and Disclosure Limitations.** Business Associate shall not use or disclose PHI other than as permitted or required by this BAA, as Required By Law, or as otherwise permitted under HIPAA. Business Associate shall not use or disclose PHI in a manner that would violate Subpart E of 45 CFR Part 164 if done by Covered Entity, except as provided in Section 3.

**2.02. Safeguards.** Business Associate shall implement and maintain administrative, physical, and technical safeguards that reasonably and appropriately protect the confidentiality, integrity, and availability of ePHI that it creates, receives, maintains, or transmits on behalf of Covered Entity, as required by 45 CFR § 164.306, § 164.308, § 164.310, § 164.312, and § 164.316. These safeguards shall be consistent with the Technijian Information Security Program (WISP) and shall include at a minimum:

(a) Encryption of ePHI in transit (TLS 1.2+) and at rest (AES-256);

(b) Multi-factor authentication for all access to systems containing ePHI;

(c) Role-based access controls with quarterly access reviews;

(d) Endpoint Detection and Response (CrowdStrike Falcon) on all endpoints with access to ePHI;

(e) Encrypted backups with tested recovery procedures per the BCP/DR plan;

(f) Audit logging of all access to ePHI with minimum 6-year retention; and

(g) Workforce security training including HIPAA-specific training for personnel with access to PHI.

**2.03. Breach Notification.** Business Associate shall report to Covered Entity any Breach of Unsecured PHI without unreasonable delay and in no event later than **forty-eight (48) hours** after discovery of the Breach, consistent with MSA Section 10.02. Business Associate's notification shall include, to the extent known:

(a) The identification of each Individual whose Unsecured PHI has been, or is reasonably believed to have been, accessed, acquired, used, or disclosed during the Breach;

(b) A description of the nature of the Breach, including the types of PHI involved;

(c) A description of what Business Associate is doing to investigate the Breach, mitigate harm to Individuals, and protect against further Breaches; and

(d) Contact information for Business Associate's designated point of contact for the Breach.

Business Associate shall cooperate with Covered Entity in providing any additional information required for Covered Entity to fulfill its notification obligations under 45 CFR § 164.404 (notification to Individuals), § 164.406 (notification to media), and § 164.408 (notification to the Secretary).

**2.04. Security Incidents.** Business Associate shall report to Covered Entity any Security Incident of which Business Associate becomes aware. For attempted but unsuccessful Security Incidents (such as unsuccessful log-in attempts, pings, port scans, or similar), Business Associate shall provide a summary report upon Covered Entity's written request, no more frequently than quarterly.

**2.05. Sub-contractors.** Business Associate shall ensure that any sub-contractor or agent that creates, receives, maintains, or transmits PHI on behalf of Business Associate agrees in writing to the same restrictions, conditions, and requirements that apply to Business Associate under this BAA. This includes offshore personnel engaged under MSA Section 1.10.

**2.06. Access to PHI.** Business Associate shall, within **fifteen (15) business days** of a request from Covered Entity, make available PHI in a Designated Record Set to Covered Entity (or, at Covered Entity's direction, to an Individual) as necessary for Covered Entity to satisfy its obligations under 45 CFR § 164.524 (Individual's right of access).

**2.07. Amendment of PHI.** Business Associate shall, within **fifteen (15) business days** of a request from Covered Entity, make available PHI for amendment and incorporate any amendments to PHI in a Designated Record Set as necessary for Covered Entity to satisfy its obligations under 45 CFR § 164.526.

**2.08. Accounting of Disclosures.** Business Associate shall maintain an accounting of disclosures of PHI as required by 45 CFR § 164.528, and shall make such accounting available to Covered Entity within **thirty (30) days** of a request, to enable Covered Entity to respond to Individual requests for an accounting of disclosures. The accounting shall cover disclosures during the **six (6) year** period preceding the request (or such shorter period as specified in the request).

**2.09. Internal Practices.** Business Associate shall make its internal practices, books, and records relating to the use and disclosure of PHI available to the Secretary for purposes of determining Covered Entity's compliance with HIPAA.

**2.10. Return or Destruction of PHI.** Upon termination of this BAA, or upon Covered Entity's written request, Business Associate shall return or destroy all PHI in its possession, including all copies in any form. Business Associate shall certify destruction in writing upon request. If return or destruction is not feasible, Business Associate shall extend the protections of this BAA to such PHI and limit further uses and disclosures to those purposes that make return or destruction infeasible, for so long as Business Associate retains the PHI.

**2.11. Minimum Necessary.** Business Associate shall use, disclose, or request only the minimum necessary PHI to accomplish the intended purpose of the use, disclosure, or request, as required by 45 CFR § 164.502(b).

**2.12. Record Retention.** Business Associate shall retain all documentation required by this BAA for a minimum of **six (6) years** from the date of creation or the date when the documentation was last in effect, whichever is later, as required by 45 CFR § 164.530(j).

---

## 3. PERMITTED USES AND DISCLOSURES

**3.01.** Business Associate may use or disclose PHI as necessary to perform functions, activities, or services on behalf of Covered Entity as described in the MSA, provided that such use or disclosure does not violate HIPAA.

**3.02.** Business Associate may use or disclose PHI as Required By Law.

**3.03.** Business Associate may use PHI for the proper management and administration of Business Associate, provided that: (a) the disclosures are Required By Law; or (b) Business Associate obtains reasonable assurances from the person to whom the information is disclosed that it will be held confidentially and the person notifies Business Associate of any Breach.

**3.04.** Business Associate may de-identify PHI in accordance with 45 CFR § 164.514(a)-(c). De-identified data is no longer PHI and is not subject to this BAA.

---

## 4. OBLIGATIONS OF COVERED ENTITY

**4.01.** Covered Entity shall notify Business Associate of any limitations in its Notice of Privacy Practices under 45 CFR § 164.520, to the extent that such limitations may affect Business Associate's use or disclosure of PHI.

**4.02.** Covered Entity shall notify Business Associate of any changes in, or revocation of, authorization by an Individual to use or disclose PHI, to the extent that such changes may affect Business Associate's use or disclosure of PHI.

**4.03.** Covered Entity shall notify Business Associate of any restrictions on the use or disclosure of PHI that Covered Entity has agreed to or is required to abide by under 45 CFR § 164.522, to the extent that such restrictions may affect Business Associate's use or disclosure of PHI.

**4.04.** Covered Entity shall not request Business Associate to use or disclose PHI in any manner that would not be permissible under HIPAA if done by Covered Entity.

---

## 5. TERM AND TERMINATION

**5.01. Term.** This BAA shall be effective for the duration of the MSA and shall automatically terminate upon termination of the MSA, subject to Section 5.04.

**5.02. Termination for Material Breach.** If either Party determines that the other Party has committed a material breach of this BAA, the non-breaching Party shall provide written notice specifying the nature of the breach. The breaching Party shall have **thirty (30) days** to cure the breach. If the breach is not cured within such period, the non-breaching Party may terminate this BAA and the MSA.

**5.03. Effect of Termination.** Upon termination of this BAA, Business Associate shall comply with Section 2.10 (Return or Destruction of PHI).

**5.04. Survival.** The obligations of Business Associate under Sections 2.02, 2.03, 2.09, 2.10, 2.11, and 2.12 shall survive termination of this BAA for so long as Business Associate retains any PHI.

---

## 6. MISCELLANEOUS

**6.01. Regulatory References.** The Parties acknowledge that the HITECH Act (Title XIII of the American Recovery and Reinvestment Act of 2009, Pub. L. 111-5) imposes certain obligations on business associates that are independent of the contractual obligations in this BAA. Business Associate shall comply with all applicable HITECH Act provisions.

**6.02. Amendment.** The Parties shall amend this BAA as necessary to comply with changes in HIPAA or other applicable law. Either Party may request amendment by providing written notice to the other Party.

**6.03. Interpretation.** Any ambiguity in this BAA shall be resolved in favor of a meaning that permits the Parties to comply with HIPAA. In the event of a conflict between this BAA and the MSA, this BAA shall prevail with respect to PHI.

**6.04. No Third-Party Beneficiaries.** Nothing in this BAA shall confer upon any person other than the Parties any rights, remedies, obligations, or liabilities.

**6.05. Governing Law.** This BAA shall be governed by the laws of the State of California, consistent with MSA Section 9.08, to the extent not preempted by HIPAA.

**6.06. Liability.** Each Party's liability under this BAA shall be subject to the limitations set forth in MSA Section 5, except that liability for violations of HIPAA that result in regulatory penalties shall not be subject to the Standard Cap.

---

## SIGNATURES

**[CLIENT NAME]** (Covered Entity)

By: ___________________________________

Name: _________________________________

Title: _________________________________

Date: _________________________________

**TECHNIJIAN, INC.** (Business Associate)

By: ___________________________________

Name: _________________________________

Title: _________________________________

Date: _________________________________
